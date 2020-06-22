from flask import Flask, render_template, url_for, flash, redirect
from kentekencheck import KentekenForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '22e6d440e93bc19fe477da8288560673'


@app.route('/search_result')
def search_result():
    return render_template('search_result.html')


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = KentekenForm()
    if form.validate_on_submit():
        return redirect(url_for('search_result'))
    return render_template('index.html', title='Register', form=form)


if __name__ == "__main__":
    app.run(debug=True)
