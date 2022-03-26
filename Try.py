from flask import Flask, render_template, request
import folium
import pandas as pd
from SPARQLWrapper import SPARQLWrapper, JSON

app = Flask(__name__)


@app.route('/')
def man():
    print("wsh")
    return render_template('home.html')



if __name__ == "__main__":
    app.run(debug=True)
