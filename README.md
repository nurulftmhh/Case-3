# Hospital Triage System

## Cara Menjalankan

1. Aktifkan Virtual Environment
 
`venv\Scripts\activate`

2. Install Dependencies

`pip install -r requirements.txt`

3. Jalankan main.py atau jalankan server dengan `uvicorn main:app --reload --port 8000`
 
5. Server berhasil dijalankan
6. 
<img width="741" height="289" alt="image" src="https://github.com/user-attachments/assets/ef626ceb-b044-4226-aa0f-8f1b006e52ad" />

7. Akses API menggunakan Postman
- Pilih method POST
- Masukkan URL `http://localhost:8000/recommend`
- Pada tab Header tambahkan "Content-Type    application/json"
- Pada tab Body, pilih raw dan isi JSON, contoh:
  `{
  "gender": "male",
  "age": 22,
  "symptoms": ["batuk", "mual", "sesak napas"]
}`
- Klik Send
 
<img width="1367" height="656" alt="image" src="https://github.com/user-attachments/assets/92c39eb2-5a5e-4195-a22f-64e646734d9f" />

7. Opsi lain selain menggunakan Postman, bisa juga dengan menjalankan test.py jika server sudah dijalankan. Atau bisa menggunakan swagger UI:
- Buka http://localhost:8000/docs
- Cari endpoint POST /recommend, klik Try it out
- Masukkan JSON sesuai format di kolom Request body
 
<img width="1801" height="792" alt="image" src="https://github.com/user-attachments/assets/e9836487-e8f9-4a68-b599-2723ea785a12" />

- Klik Execute
 
<img width="1800" height="768" alt="image" src="https://github.com/user-attachments/assets/88062bda-cfd0-475b-a53d-09998295ca12" />
 
 
   

  
 
