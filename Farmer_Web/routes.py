from flask import render_template,url_for,json,jsonify
from Farmer_Web import app

from Farmer_Web.models import Pais,soda

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
    papo = [{"country_id":cachita.country_id,"country":cachita.country,"last_update": cachita.last_update} for cachita in cacha]
    dumx = json.dumps(papo)
    return jsonify({'data':papo})

@app.route('/Clients')
def clientela():
    return render_template("country.html")

@app.route('/Clients/raws')
def clientss():
    return render_template("country.html")

@app.route('/Clients/paises')
def numero_clientes():
    
    cole = soda()
    kendrick = [{"Pais":c[0],"NumeroC":c[1]} for c in cole]
    dup = json.dumps(kendrick)
    return jsonify({'Data':kendrick})    