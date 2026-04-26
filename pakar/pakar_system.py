GEJALA = [
    {'id': 'G1',  'teks': 'Daun tanaman menguning'},
    {'id': 'G2',  'teks': 'Daun tanaman layu'},
    {'id': 'G3',  'teks': 'Ujung daun mengering'},
    {'id': 'G4',  'teks': 'Tanah terasa terlalu basah'},
    {'id': 'G5',  'teks': 'Tanah terasa terlalu kering'},
    {'id': 'G6',  'teks': 'Tanaman jarang terkena cahaya'},
    {'id': 'G7',  'teks': 'Terkena cahaya matahari langsung terlalu lama'},
    {'id': 'G8',  'teks': 'Muncul bercak pada daun'},
    {'id': 'G9',  'teks': 'Pertumbuhan tanaman terlihat lambat'},
    {'id': 'G10', 'teks': 'Batang atau akar terlihat membusuk'},
]

RULES = [
    {
        'id': 'P1', 'ikon': '💧', 'required': ['G1', 'G4'],
        'diag': 'Tanaman terlalu banyak air',
        'penyebab': 'Frekuensi penyiraman berlebih atau drainase pot yang buruk sehingga akar terendam air.',
        'rek': 'Kurangi frekuensi penyiraman dan pastikan pot memiliki lubang drainase. Biarkan lapisan atas tanah mengering sebelum menyiram kembali.'
    },
    {
        'id': 'P2', 'ikon': '🏜️', 'required': ['G2', 'G5'],
        'diag': 'Tanaman kekurangan air',
        'penyebab': 'Penyiraman terlalu jarang atau tanah mengering terlalu cepat akibat cuaca panas atau pot terlalu kecil.',
        'rek': 'Siram tanaman secukupnya secara teratur. Periksa kelembapan tanah setiap 2–3 hari dengan mencolokkan jari ke tanah sedalam 2 cm.'
    },
    {
        'id': 'P3', 'ikon': '🌵', 'required': ['G3', 'G5'],
        'diag': 'Tanaman mengalami kekeringan',
        'penyebab': 'Kombinasi tanah terlalu kering dan paparan panas berlebih menyebabkan jaringan daun rusak.',
        'rek': 'Tambahkan frekuensi penyiraman secara bertahap, jauhkan dari sumber panas langsung, dan pertimbangkan penggunaan mulsa untuk menahan kelembapan.'
    },
    {
        'id': 'P4', 'ikon': '💡', 'required': ['G1', 'G6'],
        'diag': 'Tanaman kekurangan cahaya',
        'penyebab': 'Intensitas cahaya tidak mencukupi kebutuhan fotosintesis sehingga klorofil daun terdegradasi dan menguning.',
        'rek': 'Pindahkan tanaman ke tempat yang lebih terang. Jika cahaya alami tidak mencukupi, gunakan lampu grow light 12–16 jam per hari.'
    },
    {
        'id': 'P5', 'ikon': '☀️', 'required': ['G7', 'G3'],
        'diag': 'Tanaman terkena cahaya berlebihan',
        'penyebab': 'Paparan sinar matahari langsung terlalu lama menyebabkan dehidrasi dan kerusakan sel daun bagian tepi.',
        'rek': 'Pindahkan ke area dengan cahaya terang tidak langsung (indirect sunlight). Gunakan tirai tipis sebagai filter jika perlu.'
    },
    {
        'id': 'P6', 'ikon': '🍄', 'required': ['G8', 'G4'],
        'diag': 'Risiko infeksi jamur atau penyakit',
        'penyebab': 'Kondisi lembab berlebih menciptakan lingkungan ideal bagi pertumbuhan jamur pada permukaan daun dan batang.',
        'rek': 'Kurangi penyiraman, pangkas daun yang terinfeksi, perbaiki sirkulasi udara di sekitar tanaman, dan pertimbangkan fungisida organik jika perlu.'
    },
    {
        'id': 'P7', 'ikon': '🌱', 'required': ['G2', 'G4', 'G10'],
        'diag': 'Akar kemungkinan membusuk (Root Rot)',
        'penyebab': 'Genangan air di sekitar akar dalam waktu lama menyebabkan bakteri anaerob mengurai jaringan akar hingga membusuk.',
        'rek': 'Cabut tanaman, periksa dan buang bagian akar yang busuk. Ganti media tanam, angin-anginkan akar, lalu tanam kembali. Kurangi penyiraman secara drastis.'
    },
    {
        'id': 'P8', 'ikon': '📏', 'required': ['G9', 'G6'],
        'diag': 'Pertumbuhan terhambat karena cahaya kurang',
        'penyebab': 'Fotosintesis tidak optimal akibat cahaya minim, sehingga tanaman tidak menghasilkan energi yang cukup untuk pertumbuhan.',
        'rek': 'Dekatkan tanaman ke sumber cahaya alami atau gunakan grow light 12–16 jam per hari untuk mendukung pertumbuhan optimal.'
    },
    {
        'id': 'P9', 'ikon': '😟', 'required': ['G1', 'G2', 'G4'],
        'diag': 'Tanaman stres akibat kelebihan air',
        'penyebab': 'Tanah yang terus-menerus jenuh air membuat akar tidak bisa menyerap oksigen, menyebabkan stres fisiologis pada seluruh tanaman.',
        'rek': 'Hentikan penyiraman sementara hingga tanah mengering. Pastikan pot memiliki drainase yang baik dan pertimbangkan media tanam yang lebih porous.'
    },
    {
        'id': 'P10', 'ikon': '🔥', 'required': ['G3', 'G7'],
        'diag': 'Daun terbakar (Leaf Scorch)',
        'penyebab': 'Sinar matahari langsung merusak klorofil dan menyebabkan penguapan air berlebih dari permukaan daun, mengakibatkan tepi daun terbakar.',
        'rek': 'Segera pindahkan ke tempat teduh dengan cahaya tidak langsung. Potong bagian daun yang sudah terbakar agar energi dapat dialihkan ke pertumbuhan baru.'
    },
    {
        'id': 'P11', 'ikon': '🌾', 'required': ['G5', 'G9'],
        'diag': 'Kekurangan nutrisi atau air',
        'penyebab': 'Tanah kering menghambat penyerapan nutrisi oleh akar, sehingga pertumbuhan melambat dan tanaman terlihat lesu.',
        'rek': 'Siram secara teratur dan berikan pupuk cair ringan sesuai kebutuhan. Pastikan media tanam masih subur dan ganti jika sudah terlalu padat.'
    },
]

def default_selections():
    return {g['id']: 'tidak' for g in GEJALA}

def build_selections(form):
    selections = default_selections()
    for g in GEJALA:
        value = form.get(g['id'], 'tidak')
        selections[g['id']] = 'ya' if value == 'ya' else 'tidak'
    return selections

def diagnose(selections):
    active_map = {key: value == 'ya' for key, value in selections.items()}
    active_gejala = [g for g in GEJALA if active_map.get(g['id'])]
    matches = [rule for rule in RULES if all(active_map.get(item, False) for item in rule['required'])]
    return {
        'aktif': active_gejala,
        'matches': matches,
    }
