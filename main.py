from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<name>')
def user_index(name):
    return render_template('index.html', user_name = name)

@app.route('/Admin')
def Admin():
    return render_template('login_admin.html')


@app.route('/Byling')
def Byl():
    return render_template('Byling.html')


@app.route('/Distan')
def distan():
    return render_template('Distan.html')

@app.route('/Hrchi')
def Harch():
    return render_template('Harch.html')

@app.route('/Kadry')
def Kadr():
    return render_template('Kadr.html')

@app.route('/History')
def History():
    return render_template('History.html')

@app.route('/Kolective')
def Kolective():
    return render_template('Kolektiv.html')

@app.route('/Licens')
def Licens():
    return render_template('Licens.html')

@app.route('/Material')
def Material():
    return render_template('Mater.html')

@app.route('/Mova')
def Mova():
    return render_template('Mova.html')

@app.route('/Nove')
def Nove():
    return render_template('Nove.html')

@app.route('/OsPro')
def Ospro():
    return render_template('OsPro.html')

@app.route('/Perelik')
def Perelik():
    return render_template('Perelik.html')

@app.route('/Plan')
def Plan():
    return render_template('Plan.html')

@app.route('/Poryadok')
def Poryadok():
    return render_template('Poryadok.html')

@app.route('/Potyz')
def Potyz():
    return render_template('Potyz.html')

@app.route('/Pravila')
def Pravila():
    return render_template('Pravila.html')

@app.route('/Proyom')
def Proyom():
    return render_template('Proyom.html')

@app.route('/Psyh')
def Psyh():
    return render_template('Psyh.html')

@app.route('/Publish')
def Publish():
    return render_template('Publish.html')

@app.route('/Rada')
def Rada():
    return render_template('Rada.html')

@app.route('/Regestr')
def Reg():
    return render_template('Regestr.html')

@app.route('/Rekviz')
def Rekviz():
    return render_template('Rekviz.html')

@app.route('/Rezylt')
def Rezylt():
    return render_template('Rezylt.html')

@app.route('/Stat')
def Stat():
    return render_template('Stat.html')

@app.route('/Terit')
def Ter():
    return render_template('Terit.html')

@app.route('/Torg')
def Torg():
    return render_template('Torg.html')

@app.route('/Uprav')
def Uprav():
    return render_template('Uprav.html')

@app.route('/Vakanci')
def Vakan():
    return render_template('Vakan.html')

@app.route('/VSYO')
def VSYO():
    return render_template('VSYO.html')

@app.route('/Ymovi')
def Ymov():
    return render_template('Ymovi.html')

@app.route('/Zvit')
def Zvit():
    return render_template('Zvit.html')

if __name__ == "__main__":
    app.run()