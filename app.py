"""Flask app for Cupcakes"""
from distutils.log import debug
from flask import Flask, request, render_template, redirect, jsonify, flash, session
from flask_debugtoolbar   import DebugToolbarExtension
from models import db, connect_db, Cupcake 


app = Flask(__name__)

# config DB url (connect to db)

app.config['SQLALCHEMY_DATABASE_URI']  =  'postgresql:///cupcake'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
 

app.config['SECRET_KEY'] = "test@123!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] =False
app.config['SQLALCHEMY_ECHO'] =True
debug = DebugToolbarExtension(app)
connect_db(app)


@app.route('/')
def index_page():
    cupcakes=Cupcake.query.all()
    return render_template('index.html', cupcakes=cupcakes)

@app.route('/api/cupcakes')
def list_cupcakes():
    all_cupcakes = [cupcake.serialize() for cupcake in  Cupcake.query.all()]
    return jsonify(cupcakes=all_cupcakes)


@app.route('/api/cupcakes/<int:id>') 
def get_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)   
    return jsonify(Cupcake=cupcake.serialize())


@app.route('/api/cupcakes',methods=["POST"])    
def create_cupcake():
    #flavor = request.form["flavor"]
    #size = request.form["size"]
    #rating = request.form["rate"]
    #image_url = request.form["url"]
    #new_cupcake = Cupcake(flavor = flavor, size=size,rating=rating, image=image_url)
    new_cupcake =Cupcake(flavor="Margarita", size="Large", rating=9, image="https://www.browneyedbaker.com/wp-content/uploads/2011/05/margarita-cupcakes-22-800-768x1152.jpg")
    db.session.add(new_cupcake)
    db.session.commit()
    response_json=jsonify(new_cupcake.serialize())
    return (response_json,201)

@app.route('/api/cupcakes/<int:id>', methods=["PATCH"])    
def update_cupcake(id):
    cupcake= Cupcake.query.get_or_404(id)
    cupcake.flavor = request.json.get('flavor',cupcake.flavor)
    cupcake.size = request.json.get('size',cupcake.size)
    cupcake.rating = request.json.get('rating',cupcake.rating)
    cupcake.image = request.json.get('image',cupcake.image)
    db.session.commit()
    return jsonify(cupcake.serialize())


@app.route('/api/cupcakes/<int:id>', methods=["DELETE"])    
def delete_cupcake(id):
    cupcake= Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="deleted")      


 