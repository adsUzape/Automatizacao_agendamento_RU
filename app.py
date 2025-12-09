from flask import Flask, render_template, request
import subprocess
import os
import sys

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('agendamento.html')

@app.route('/agendar', methods=['POST'])
def agendar():
    usuario = request.form['usuario']
    senha = request.form['senha']
    moradia = request.form.get('moradia', 'nao')  # "sim" | "nao"
    dias = request.form['dias']        # "dd/mm/yyyy,dd/mm/yyyy"
    selecionadas = request.form.getlist('refeicao')
    if moradia == 'nao':
        selecionadas = ['almoco']
    elif not selecionadas:
        selecionadas = ['almoco']

    base_dir = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(base_dir, 'botRu.py')

    args = [
        sys.executable, script_path,
        usuario, senha, moradia, dias, ','.join(selecionadas)
    ]

    result = subprocess.run(args, capture_output=True, text=True, cwd=base_dir)
    out = result.stdout or ''
    err = result.stderr or ''
    return f"<pre>{out}\n{err}</pre>"

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)