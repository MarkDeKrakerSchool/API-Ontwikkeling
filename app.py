from flask import Flask, render_template, url_for
from kentekencheck import KentekenForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '22e6d440e93bc19fe477da8288560673'

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/search_result')
def search_result():
    return render_template('search_result.html')

if __name__ == "__main__":
    app.run(debug=True)

