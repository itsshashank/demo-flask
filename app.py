from flask import Flask,request,jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Hello(Resource):
    dic ={}
    def get(self):
        if Hello.dic=={}:
            return "Hello World"
        else:
            return jsonify(Hello.dic)
    def post(self):
        data=request.get_json()
        Hello.dic[data["id"]]=data["name"]
        print(Hello.dic)
        return "Added"
    def put(self,id):
        data=request.get_json()
        if id in Hello.dic.keys():
            Hello.dic[id]=data["name"]
            return "Updated"            
        else:
            return "No id found"
    def delete(self,id):
        del Hello.dic[id]
        return "Deleted"


api.add_resource(Hello, '/','/<int:id>')
if __name__ == '__main__':
    print("Started ")
    app.run(host='0.0.0.0',port=5000)
