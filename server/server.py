from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html', title="Заготовка")


@app.route('/training/<prof>')
def training(prof):
    ns = ['врач', 'доктор', 'учёный']
    it = ['инженер', 'строитель']
    return render_template('training.html', title=prof, prof=prof, ns=ns, it=it)


@app.route('/list_prof/<list>')
def list_prof(list):
    profs = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач', 'инженер по терраформированию',
             'климатолог', 'специалист по радиционной защите', 'астрогеолог', 'гляциолог', 'инженер жизнеобеспечения',
             'метеоролог', 'оператор марсохода', 'киберинженер', 'штурман', 'пилот дронов']
    return render_template('list_prof.html', profs=profs, list=list)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
