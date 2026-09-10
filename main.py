from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/temperatura', methods=['POST'])
def temperatura():
    valor = float(request.form['valor'])

    conversao = (valor * 9 / 5) + 32

    return render_template('index.html', conversao=conversao, valor=valor)
if __name__ == '__main__':
    app.run(debug=True)