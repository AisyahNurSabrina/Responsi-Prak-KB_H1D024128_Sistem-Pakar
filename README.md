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
