from flask import render_template,url_for,json,jsonify,request,redirect
from Farmer_Web import app

from Farmer_Web.models import Pais,soda,ClientN

@app.route('/',methods = ['POST', 'GET'])
def method_name():
   
    return render_template("home.html")

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
#Muestra la tabla con los  datos
# ss

@app.route('/Clients')
def clientela():
    colera = soda()
    return render_template("customers.html", colera=colera)

@app.route('/Clients/paises')
def numero_clientes():
    
    cole = soda()
    kendrick = [{"Pais":c[0],"Numero":c[1]} for c in cole]
    dup = json.dumps(kendrick)
    return jsonify(kendrick)    

"""""
@app.route('/Clients/paises')
def numero_clientes():
       
    cole = ClientN([{i[0]} for i in soda()],[{ i[1]} for i in soda() ])
    kendrick = [{"Pais":c.pai,"Numero_c":c.number_client} for c in cole()]
    dup = json.dumps(kendrick)
    return jsonify({'Data':kendrick})  
"""""
@app.route('/Clients/raws')
def clientss():
    return render_template("country.html")

