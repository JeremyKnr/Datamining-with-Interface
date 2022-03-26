from flask import Flask, render_template, request
import folium
import pandas as pd
import pickle
from SPARQLWrapper import SPARQLWrapper, JSON
import numpy as np

app = Flask(__name__)


def AfficheLesCooCine(liste):
    map = folium.Map(location=[48.8589507, 2.2770205],
                     zoom_start=12
                     )
    for i in range(len(liste)):
        folium.Marker(
            location=[liste[i][4], liste[i][3]],
            popup=liste[i][0] + " Adresse : " + liste[i][1] + " Programmateur : " +
                  liste[i][2],
            icon=folium.Icon(color='red')
        ).add_to(map)
    return map._repr_html_()

def AfficheLesCooLibrairy(liste):
    map = folium.Map(location=[48.8589507, 2.2770205],
                     zoom_start=12
                     )
    for i in range(len(liste)):
        folium.Marker(
            location=[liste[i][5], liste[i][4]],
            popup=liste[i][0] + " Adresse : " + liste[i][1] + liste[i][2] +" Surface : " +
                  liste[i][3],
            icon=folium.Icon(color='red')
        ).add_to(map)
    return map._repr_html_()

def AfficheLesCooMuseum(liste):
    map = folium.Map(location=[48.8589507, 2.2770205],
                     zoom_start=12
                     )
    for i in range(len(liste)):
        folium.Marker(
            location=[liste[i][5], liste[i][4]],
            popup=liste[i][0] + " Adresse : " + liste[i][1] + " Phone : " +
                  liste[i][2]+ " WebSite : " +
                  liste[i][3],
            icon=folium.Icon(color='red')
        ).add_to(map)
    return map._repr_html_()




# All movie theater
def MovieQuery():
    query = SPARQLWrapper("http://localhost:3030/Cinema/query")
    query.setQuery("""
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX j.0: <http://schema.org/>
            SELECT ?nom ?adresse ?programmateur ?lon ?lat
            WHERE {
                ?subject j.0:nom ?nom.
                ?subject j.0:adresse ?adresse.
                ?subject j.0:programmateur ?programmateur.
                ?subject j.0:coordonnees ?lon.
                ?subject j.0:coordonnees ?lat.}
        """)
    query.setReturnFormat(JSON)
    query_results = query.query().convert()
    coordonnee = []

    for i in range(len(query_results["results"]["bindings"])):
        nom = query_results["results"]["bindings"][i]["nom"]["value"]
        adresse = query_results["results"]["bindings"][i]["adresse"]["value"]
        programmateur = query_results["results"]["bindings"][i]["programmateur"]["value"]
        lon_brut = (query_results["results"]["bindings"][i]["lon"]["value"])
        lat_brut = (query_results["results"]["bindings"][i]["lat"]["value"])

        coor = [nom, adresse, programmateur, lon_brut, lat_brut]
        coordonnee.append(coor)

    return (coordonnee)


def MovieQuery2(zpcode1,zpcode2):
    query = SPARQLWrapper("http://localhost:3030/Cinema/query")
    query.setQuery("""
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX j.0: <http://schema.org/>
            SELECT ?nom ?adresse ?programmateur ?lon ?lat ?cp
            WHERE {
                ?subject j.0:nom ?nom.
                ?subject j.0:adresse ?adresse.
                ?subject j.0:programmateur ?programmateur.
                ?subject j.0:coordonnees ?lon.
                ?subject j.0:coordonnees ?lat.
                ?subject j.0:cp ?cp.
                FILTER(""" + zpcode1 + """<?cp && ?cp<""" + zpcode2 + """)}
        """)
    query.setReturnFormat(JSON)
    query_results = query.query().convert()
    coordonnee = []

    for i in range(len(query_results["results"]["bindings"])):
        nom = query_results["results"]["bindings"][i]["nom"]["value"]
        adresse = query_results["results"]["bindings"][i]["adresse"]["value"]
        programmateur = query_results["results"]["bindings"][i]["programmateur"]["value"]
        lon_brut = (query_results["results"]["bindings"][i]["lon"]["value"])
        lat_brut = (query_results["results"]["bindings"][i]["lat"]["value"])

        coor = [nom, adresse, programmateur, lon_brut, lat_brut]
        coordonnee.append(coor)

    return (coordonnee)


def MuseumQuery():
    query = SPARQLWrapper("http://localhost:3030/Museum/query")
    query.setQuery("""
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX j.0: <http://schema.org/>
            SELECT ?nom ?adresse ?phone ?url ?lon ?lat
            WHERE {
                ?subject j.0:nom ?nom.
                ?subject j.0:adresse ?adresse.
                ?subject j.0:phone ?phone.
                ?subject j.0:url ?url.
                ?subject j.0:coordonnees ?lon.
                ?subject j.0:coordonnees ?lat.}
        """)
    query.setReturnFormat(JSON)
    query_results = query.query().convert()
    coordonnee = []

    for i in range(len(query_results["results"]["bindings"])):
        nom = query_results["results"]["bindings"][i]["nom"]["value"]
        adresse = query_results["results"]["bindings"][i]["adresse"]["value"]
        phone = query_results["results"]["bindings"][i]["phone"]["value"]
        url = query_results["results"]["bindings"][i]["url"]["value"]
        lon_brut = (query_results["results"]["bindings"][i]["lon"]["value"])
        lat_brut = (query_results["results"]["bindings"][i]["lat"]["value"])

        coor = [nom, adresse, phone, url, lon_brut, lat_brut]
        coordonnee.append(coor)

    return (coordonnee)

def MuseumQuery2(zpcode):
    query = SPARQLWrapper("http://localhost:3030/Museum/query")
    query.setQuery("""
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX j.0: <http://schema.org/>
            SELECT ?nom ?adresse ?phone ?url ?lon ?lat ?cp
            WHERE {
                ?subject j.0:nom ?nom.
                ?subject j.0:adresse ?adresse.
                ?subject j.0:phone ?phone.
                ?subject j.0:url ?url.
                ?subject j.0:coordonnees ?lon.
                ?subject j.0:coordonnees ?lat.
                ?subject j.0:cp ?cp.
                FILTER regex(?cp,'"""+zpcode+"""')}
        """)
    query.setReturnFormat(JSON)
    query_results = query.query().convert()
    coordonnee = []

    for i in range(len(query_results["results"]["bindings"])):
        nom = query_results["results"]["bindings"][i]["nom"]["value"]
        adresse = query_results["results"]["bindings"][i]["adresse"]["value"]
        phone = query_results["results"]["bindings"][i]["phone"]["value"]
        url = query_results["results"]["bindings"][i]["url"]["value"]
        lon_brut = (query_results["results"]["bindings"][i]["lon"]["value"])
        lat_brut = (query_results["results"]["bindings"][i]["lat"]["value"])

        coor = [nom, adresse, phone, url, lon_brut, lat_brut]
        coordonnee.append(coor)

    return (coordonnee)


def LibrairyQuery():
    query = SPARQLWrapper("http://localhost:3030/Librairy/query")
    query.setQuery("""
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX j.0: <http://schema.org/>
            SELECT ?nom ?surface ?adresse ?ville ?lon ?lat
            WHERE {
                ?subject j.0:nom ?nom.
                ?subject j.0:surface ?surface.
                ?subject j.0:adresse ?adresse.
                ?subject j.0:ville ?ville.
                ?subject j.0:coordonnees ?lon.
                ?subject j.0:coordonnees ?lat.}
        """)
    query.setReturnFormat(JSON)
    query_results = query.query().convert()
    coordonnee = []

    for i in range(len(query_results["results"]["bindings"])):
        nom = query_results["results"]["bindings"][i]["nom"]["value"]
        adresse = query_results["results"]["bindings"][i]["adresse"]["value"]
        ville = query_results["results"]["bindings"][i]["ville"]["value"]
        surface = query_results["results"]["bindings"][i]["surface"]["value"]
        lon_brut = (query_results["results"]["bindings"][i]["lon"]["value"])
        lat_brut = (query_results["results"]["bindings"][i]["lat"]["value"])

        coor = [nom, adresse, ville, surface, lon_brut, lat_brut]
        coordonnee.append(coor)

    return (coordonnee)

def LibrairyQuery2(zipcode):
    query = SPARQLWrapper("http://localhost:3030/Librairy/query")
    query.setQuery("""
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX j.0: <http://schema.org/>
            SELECT ?nom ?surface ?adresse ?ville ?lon ?lat ?cp
            WHERE {
                ?subject j.0:nom ?nom.
                ?subject j.0:surface ?surface.
                ?subject j.0:adresse ?adresse.
                ?subject j.0:ville ?ville.
                ?subject j.0:coordonnees ?lon.
                ?subject j.0:coordonnees ?lat.
                ?subject j.0:cp ?cp.
                FILTER regex(?cp,'"""+zipcode+"""')}
        """)
    query.setReturnFormat(JSON)
    query_results = query.query().convert()
    coordonnee = []

    for i in range(len(query_results["results"]["bindings"])):
        nom = query_results["results"]["bindings"][i]["nom"]["value"]
        adresse = query_results["results"]["bindings"][i]["adresse"]["value"]
        ville = query_results["results"]["bindings"][i]["ville"]["value"]
        surface = query_results["results"]["bindings"][i]["surface"]["value"]
        lon_brut = (query_results["results"]["bindings"][i]["lon"]["value"])
        lat_brut = (query_results["results"]["bindings"][i]["lat"]["value"])

        coor = [nom, adresse, ville, surface, lon_brut, lat_brut]
        coordonnee.append(coor)

    return (coordonnee)

@app.route('/')
def man():
    return render_template('home.html')

@app.route('/Cinema/', methods=['POST'])
def allCinema():
    coordonneeMovie = []
    zipcode = str(request.form['zpcode'])
    if(zipcode==""):
        coordonneeMovie = MovieQuery()
    else:
        coordonneeMovie=MovieQuery2(str(int(zipcode)*1000), str(int(zipcode)*1000+1000))
    print(zipcode)

    return AfficheLesCooCine(coordonneeMovie)


@app.route('/Museum/', methods=['POST'])
def allMuseum():
    coordonneeMuseum = []
    zipcode = str(request.form['zpMus'])
    if(zipcode==""):
        coordonneeMuseum = MuseumQuery()
    else:
        coordonneeMuseum=MuseumQuery2(zipcode)
    print(zipcode)

    return AfficheLesCooMuseum(coordonneeMuseum)


@app.route('/Librairy/', methods=['POST'])
def allLibrairy():
    coordonneeLibrairy = []
    zipcode = str(request.form['zpLb'])
    if(zipcode==""):
        coordonneeLibrairy = LibrairyQuery()
    else:
        coordonneeLibrairy = LibrairyQuery2(zipcode)
    print(zipcode)
    return AfficheLesCooLibrairy(coordonneeLibrairy)

@app.route('/my-link2/')
def OnlyCinema():
    #zipcode=request.form['x1']
    #print(zipcode)
    coordonneeMovie = MovieQueryZipCode(zipcode)
    return AfficheLesCooCine(coordonneeMovie)



if __name__ == "__main__":
    app.run(debug=True)
