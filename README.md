# Hospital Triage System

## Cara Menjalankan

1. Aktifkan Virtual Environment
 
`venv\Scripts\activate`

2. Install Dependencies

`pip install -r requirements.txt`

3. Jalankan main.py atau jalankan server dengan `uvicorn main:app --reload --port 8000`
 
4. Server berhasil dijalankan
 
<img width="792" height="309" alt="image" src="https://github.com/user-attachments/assets/31064940-2965-4286-88bb-61ee638ae02c" />


5. Akses API menggunakan Postman
- Pilih method POST
- Masukkan URL `http://localhost:8000/recommend`
- Pada tab Header tambahkan "Content-Type    application/json"
- Pada tab Body, pilih raw dan isi JSON, contoh:
  `{
    "gender": "female",
    "age": 62,
    "symptoms": ["pusing", "mual", "sulit berjalan"]
}`
- Klik Send
 
<img width="1378" height="668" alt="image" src="https://github.com/user-attachments/assets/c0b9e3c0-8330-4dea-9545-0328d06010da" />


6. Opsi lain selain menggunakan Postman, bisa juga dengan menggunakan swagger UI:
- Buka http://localhost:8000/docs
- Cari endpoint POST /recommend, klik Try it out
- Masukkan JSON sesuai format di kolom Request body
 
<img width="1785" height="795" alt="image" src="https://github.com/user-attachments/assets/0ff8c15c-41e4-4f4c-83cc-a98f4e9e3812" />


- Klik Execute
 
<img width="1803" height="776" alt="image" src="https://github.com/user-attachments/assets/2e3dea7c-6396-43f6-9847-3bdf27a956f4" />

 
 
   

  
 
