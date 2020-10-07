
from Farmer_Web import db
from sqlalchemy import text




#sss
class Pais(db.Model):
     __tablename__ = 'country'
     country_id = db.Column(db.Integer,primary_key=True)
     country = db.Column(db.String())
     last_update = db.Column(db.String())
     def __init__(self,country,last_update):
          self.country = country
          self.last_update = last_update
     def __repr__(self):
            return '<country_id{}>'.format(self.country_id)

class Ciudad(db.Model):
     __tablename__ = 'city'
     city_id = db.Column(db.Integer,primary_key=True)
     city = db.Column(db.String())
     country_id = db.Column(db.Integer,db.ForeignKey('country_id'))
     last_update = db.Column(db.String())
     def __init__(self,city,country_id,last_update):
          self.city = city
          self.country_id =country_id
          self.last_update =last_update
     def __repr__(self):
          return 'city_id{}'.format(self.city_id)  


class Address(db.Model):
     __tablename__ = 'address'
     address_id = db.Column(db.Integer,primary_key=True)
     address = db.Column(db.String())
     address2 = db.Column(db.String())
     district = db.Column(db.String())
     city_id = db.Column(db.Integer,db.ForeignKey('city_id'))
     postal_code = db.Column(db.String())
     phone = db.Column(db.String())
     last_update = db.Column(db.String())
     def __init__(self,address,address2,district,city_id,postal_code,phone,last_update):
          self.address = address
          self.address2 = address2
          self.district = district
          self.city_id  = city_id
          self.postal_code = postal_code
          self.phone = phone
          self.last_update = last_update
     def __repr__(self):
         return '<address_id{}>'.format(self.address_id)

class Cliente(db.Model):
     __tablename__ = 'customer'
     customer_id = db.Column(db.Integer,primary_key=True)
     store_id = db.Column(db.Integer)
     first_name = db.Column(db.String())
     last_name = db.Column(db.String())
     email = db.Column(db.String())
     address_id =db.Column(db.Integer,db.ForeignKey('address_id'))
     activebool = db.Column(db.Boolean)
     create_date = db.Column(db.String())
     last_update = db.Column(db.String())
     active = db.Column(db.Integer())
     def __init__(self,store_id,first_name,last_name,email,address_id,activebool,create_date,last_update,active):
          self.store_id = store_id
          self.first_name = first_name
          self.last_name = last_name
          self.email = email
          self.address_id = address_id
          self.activebool = activebool
          self.create_date = create_date
          self.last_update = last_update
          self.active = active
     def __repr__(self):
          return '<customer_id{}>'.format(self.customer_id)

def soda():
    
     sql = text('SELECT public.country.country,COUNT(customer_id) AS clientes FROM public.customer  INNER JOIN public.address ON public.customer.address_id = public.address.address_id INNER JOIN public.city on public.city.city_id =  public.address.city_id INNER JOIN public.country ON public.country.country_id = public.city.country_id GROUP BY public.country.country')
     cole = db.engine.execute(sql)
     return cole


class ClientN():
     def __init__(self,pai,number_client):
          self.pai = pai
          self.number_client = number_client