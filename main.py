from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, PrivateAttr
from typing import List
import os
import google.generativeai as genai
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms.base import LLM
from dotenv import load_dotenv

load_dotenv()

class GoogleAI(LLM):
    _model: any = PrivateAttr()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY not found in environment variables")
        genai.configure(api_key=api_key)
        self._model = genai.GenerativeModel('gemini-1.5-flash')
    
    def _call(self, prompt: str, stop=None) -> str:
        response = self._model.generate_content(prompt)
        return response.text
    
    @property
    def _llm_type(self) -> str:
        return "google_ai"

app = FastAPI(title="Hospital Triage System")

llm = GoogleAI()

prompt_template = PromptTemplate(
    input_variables=["gender", "age", "symptoms"],
    template="""
    Seorang pasien dengan data:
    - Jenis kelamin: {gender}
    - Umur: {age} tahun  
    - Gejala: {symptoms}
    Pilih departemen rumah sakit yang paling tepat dari: Cardiology, Neurology, Orthopedics, Internal Medicine, Emergency, Gastroenterology, Pulmonology, Dermatology, Ophthalmology, ENT, Urology, Gynecology, Pediatrics, Psychiatry, General Surgery.    
    Jawab hanya dengan nama departemen saja.
    """
)

chain = LLMChain(llm=llm, prompt=prompt_template)

class PatientInfo(BaseModel):
    gender: str
    age: int
    symptoms: List[str]

class RecommendationResponse(BaseModel):
    recommended_department: str

@app.post("/recommend", response_model=RecommendationResponse)
async def recommend_department(patient: PatientInfo):
    try:
        symptoms_text = ", ".join(patient.symptoms)
        result = chain.run(
            gender=patient.gender,
            age=patient.age,
            symptoms=symptoms_text
        )
        department = result.strip()
        return RecommendationResponse(recommended_department=department)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"message": "Hospital Triage System API with LangChain"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
