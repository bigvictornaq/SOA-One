from flask import Flask,render_template,url_for,json,jsonify
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://ifxvfpua:4552V0r2IkVujztnh3F5puUE79kTmuQM@lallah.db.elephantsql.com:5432/ifxvfpua"
db = SQLAlchemy(app)

from models import Pais

@app.route('/')
def method_name():
   return render_template("login.html")

@app.route('/casa')
def home():
    return render_template("home.html")

    
@app.route('/Countries')
def paiss():
    return render_template("country.html")

@app.route('/Countries/raws')
def dtoke():
    cacha = Pais.query.order_by(Pais.country_id).all()
    papo = [{"ID":cachita.country_id,"Nombre":cachita.country,"Ultima Actualizacion": cachita.last_update} for cachita in cacha]
    dumx = json.dumps(papo)
    return jsonify({"data":papo})



if __name__ == '__main__':
    app.run(debug=True)