from flask import Flask,request,jsonify
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D






#model = pickle.load(open('model2.pkl','rb'))

application=Flask(__name__)

@application.route('/')
def home():
    return "Hello World"

@application.route('/predict/')
def predict():
    '''income = request.form.get('Annual Income (Rs)')
    spending = request.form.get('Spending Score (1-100)')

    input_query=np.array([[income,spending]])'''

    data=pd.read_csv("Mall_Customers2.csv")

    df1=data[["CustomerID","Gender","Age","Annual Income (Rs)","Spending Score (1-100)"]]

    X=df1[["Annual Income (Rs)","Spending Score (1-100)"]]
    X.head()

    from sklearn.cluster import KMeans
    wcss=[]

    for i in range(1,11):
        km=KMeans(n_clusters=i)
        km.fit(X)
        wcss.append(km.inertia_)

    km1=KMeans(n_clusters=5)

    km1.fit(X)

    y=km1.predict(X)

    df1["label"] = y
    df1.head()
    cust1=df1[df1["label"]==1]
    cust2=df1[df1["label"]==2]
    cust3=df1[df1["label"]==0]
    cust4=df1[df1["label"]==3]
    cust5=df1[df1["label"]==4]
    result = {
        
        "Length":len(cust1),
        "Clusters":cust1["CustomerID"].values,
        "Leng":len(cust2),
        "Clust":cust2["CustomerID"].values


    }
    return jsonify(str(result))

if __name__=='__main__':
    application.run(debug=True)
