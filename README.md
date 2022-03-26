# Datamining-with-Interface
API Flask/Python/HTML/SQL
Read Me

How works the project ?

1 : Export the data to Apache Jena Fuseki 

1.1. Go in jena\apache-jena-fuseki-4.4.0\apache-jena-fuseki-4.4.0

1.2. Run fuseki-server.bat

1.3. Go on http://localhost:3030/

1.4. Go to "manage datasets"

1.5. Click on add new dataset and create a dataset called "Cinema", select "Persistent – dataset will persist across Fuseki restarts" as type of dataset

1.6. In existing datasets, choose /Cinema and click on upload file, then select files.., then choose the file "cinema.rdf" in the folder Cinema and then click on upload all

1.7. Click on add new dataset and create a dataset called "Museum", select "Persistent – dataset will persist across Fuseki restarts" as type of dataset

1.8. In existing datasets, choose /Museum and click on upload file, then select files.., then choose the file museum.rdf in the folder Museum and then click on upload all do the same for the data set Librairy and the file biblio.rdf 

1.9. Your Apache Jena Fuseki is now ready to be used, don't close the program running

2 : Python file

2.1. For the python program use, you need to install python or PyCharm

2.2. You aslo need to install 4 python's modules, here are the commands:
   - pip install Flask 
   - pip install folium
   - pip install pandas
   - pip install SPARQLWrapper

2.3. Run your python file, on PyCharm you need to write in the console "python Projet.py"

2.4. Go to jena\templates and run home.html or you can go to this url but it is not going to use the css file so not as good looking http://127.0.0.1:5000/ 

2.4. Ready to be used now !
