import csv

import plotly.express as px
import numpy as np

def plotfig(data_path):
    with open(data_path)as csv_file:
        df =csv.DictReader(csv_file)
        fig = px.scatter(df, x="Days Present", y="Marks In Percentage")
        fig.show()

def correaltion(data_path):
    Marks =[]
    present=[]
    with open(data_path)as csv_file:
        ff =csv.DictReader(csv_file)
        for row in ff:
            Marks.append(float(row["Marks In Percentage"])) 
            present.append(float(row["Days Present"])) 
           
    return {"x":Marks,"y":present}    

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Student Marks vs Days Present :-  \n--->",correlation[0,1])

def setup():
    data_path  = "Student Marks vs Days Present.csv"

    datasource = correaltion(data_path)
    findCorrelation(datasource)
    plotfig(data_path)

setup()




