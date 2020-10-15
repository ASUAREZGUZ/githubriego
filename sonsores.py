from flask import Flask,request,jsonify,abort
import sys

app = Flask(__name__)

invernadero_db={
        "humedad":{
        "h_1" : {
            
            "valor":30,
            "nombre":"aire"
        },
        "h_2" : {
            
            "valor":40,
            "nombre":"aire"
        },
    },
    "temperatura":{
        "t_1" : {
            
            "valor":30,
            "nombre":"aire"
        },
        "t_2" : {
            
            "valor":40,
            "nombre":"aire"
        },
    }
}


@app.route("/RIEGO/<string:nombre>")
def saludo(nombre):
  titulo = request.args.get('titulo', '')
  return f"Hola {titulo} {nombre}"


if __name__ == '__main__':
    app.run(debug=True)
 
