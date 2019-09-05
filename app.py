from flask import Flask, request, render_template
import csv
import pandas as pd

#Definicion de la app flask
app = Flask(__name__)


@app.route('/log/temp=<temp>hum=<hum>time=<time>',methods=['GET'])
def saludo(temp,hum,time):
    
    data = {'Temperatura': [temp],
        'Humedad': [hum],
        'age': [time]}
    df = pd.DataFrame(data, columns = ['Temperatura', 'Humedad', 'Tiempo'])
    df.to_csv('09052019.csv')

    return ('Temperatura: ' + temp + ' // Humedad: '+ hum + ' // Tiempo'+ time)

#@app.route('/index')
#def index():

if __name__ == "__main__":
	app.run()
