import csv

import plotly.express as px
import numpy as np

def plotfig(data_path):
    with open(data_path)as csv_file:
        df =csv.DictReader(csv_file)
        fig = px.scatter(df, x="Coffee in ml", y="sleep in hours")
        fig.show()

def correaltion(data_path):
    sleep =[]
    Coffee=[]
    with open(data_path)as csv_file:
        ff =csv.DictReader(csv_file)
        for row in ff:
            sleep.append(float(row["sleep in hours"])) 
            Coffee.append(float(row["Coffee in ml"])) 
           
    return {"x":sleep,"y":Coffee}    

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Coffee in ml vs Sleep in hours :-  \n--->",correlation[0,1])

def setup():
    data_path  = "cups of coffee vs hours of sleep.csv"

    datasource = correaltion(data_path)
    findCorrelation(datasource)
    plotfig(data_path)

setup()




