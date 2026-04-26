# Sistem Pakar Diagnosa Masalah Tanaman Indoor

Project ini adalah versi Python/Flask dari Sistem Pakar. File `script.js` sudah dihapus dan logika sistem dipindahkan ke `pakar/pakar_system.py`.

## Struktur

```text
plant-pakar-system/
├── app.py
├── requirements.txt
├── vercel.json
├── templates/
│   └── index.html
├── public/
│   └── style.css
└── pakar/
    ├── __init__.py
    └── pakar_system.py
```

## Menjalankan Lokal

```bash
pip install -r requirements.txt
python app.py
```

Buka:

```text
http://127.0.0.1:5000/
```

## Deploy ke Vercel

1. Upload isi folder ini ke repository GitHub khusus Sistem Pakar.
2. Import repository tersebut di Vercel.
3. Deploy.
4. Optional: tambahkan Environment Variable `FUZZY_URL` berisi link hosting Sistem Fuzzy agar tombol menuju Sistem Fuzzy aktif.


Catatan: Logika sistem diproses menggunakan Python Flask. Tidak menggunakan JavaScript untuk perhitungan utama.
