from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html', title="Заготовка")


@app.route('/training/<prof>')
def training(prof):
    it = ['инженер', 'строитель']
    return render_template('training.html', title=prof, prof=prof, it=it)


@app.route('/list_prof/<list>')
def list_prof(list):
    profs = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач', 'инженер по терраформированию',
             'климатолог', 'специалист по радиционной защите', 'астрогеолог', 'гляциолог', 'инженер жизнеобеспечения',
             'метеоролог', 'оператор марсохода', 'киберинженер', 'штурман', 'пилот дронов']
    return render_template('list_prof.html', profs=profs, list=list)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    anketa = {'surname': 'Watny', 'name': 'Mark', 'education': 'выше среднего',
              'profession': 'штурман марсохода', 'sex': 'male', 'motivation': 'Всегда мечтал застрять на Марсе!',
              'ready': 'True'}
    return render_template("auto_answer.html", anketa=anketa, title='Анкета')

class EmergencyForm(FlaskForm):
    username = StringField('id астронавта', validators=[DataRequired()])
    password = PasswordField('Пароль астронавта', validators=[DataRequired()])
    username_capitan = StringField('id капитана', validators=[DataRequired()])
    password_capitan = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')

@app.route('/login')
def login():
    form = EmergencyForm()
    return render_template('login.html', title='Аварийный доступ', form=form)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
