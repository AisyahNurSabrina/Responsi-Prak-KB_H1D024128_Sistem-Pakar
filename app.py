import os
from flask import Flask, render_template, request, send_from_directory
from pakar.pakar_system import GEJALA, build_selections, default_selections, diagnose

app = Flask(__name__, template_folder="templates")

@app.route('/style.css')
def style_css():
    return send_from_directory('public', 'style.css')

@app.route('/', methods=['GET', 'POST'])
def index():
    selections = default_selections()
    result = None
    if request.method == 'POST':
        selections = build_selections(request.form)
        result = diagnose(selections)

    selected_count = sum(1 for value in selections.values() if value == 'ya')
    progress_width = int(selected_count / len(GEJALA) * 100)
    return render_template(
        'index.html',
        gejala=GEJALA,
        selections=selections,
        selected_count=selected_count,
        progress_width=progress_width,
        result=result,
        fuzzy_url=os.getenv('FUZZY_URL', '#')
    )

if __name__ == '__main__':
    app.run(debug=True)
