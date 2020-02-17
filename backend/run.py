from flask import Flask, render_template, jsonify, request
from flask_restful import Resource, Api, reqparse
from translator import get_translation 

app = Flask(__name__,
            static_folder = "./dist/static",
            template_folder = "./dist")
api = Api(app)            

#To be completed
class Translate(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('input', required=True)
        parser.add_argument('inputlanguage', required=False)
        parser.add_argument('outputlanguage', required=False)
        args = parser.parse_args()
        return {'input json' : [args]} 
    def get(self):
        return {"the translation" : "hi"}         

api.add_resource(Translate,'/api/translate' )  

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")
def index():
    return render_template("index.html") 

