import requests
import json

test_cases = [
    {
        "gender": "male",
        "age": 22,
        "symptoms": ["batuk", "mual", "sesak napas"]
    },
]

def test_api():
    url = "http://localhost:8000/recommend"
    
    for i, test in enumerate(test_cases, start=1):
        print(f"\n--- Test Case {i} ---")
        print(f"Input: {json.dumps(test, indent=2, ensure_ascii=False)}")  
        
        try:
            response = requests.post(url, json=test)
            print(f"Status Code: {response.status_code}")
            print(f"Result: {response.json()}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    test_api()
