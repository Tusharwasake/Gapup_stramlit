

import pandas as pd 
import numpy as np
from pymongo import MongoClient,DESCENDING
import matplotlib as math   
import matplotlib.pyplot as plt
import streamlit as st


#title of the app
st.title("Gapup Strategy")




mongo = MongoClient("mongodb+srv://my_algo_user:uN3VJWO5WDPYhYA9@cluster0.otr8r.mongodb.net/?retryWrites=true&w=majority")
mydb = mongo['Test1']
coll = mydb["Pnl_Gap"]
data_table= (coll.find({},{'_id': 0, 'Date': 1,'PNL': 1}))
table =list(coll.find({},{'_id': 0, 'Date': 1,'PNL': 1}))




date=[]
pnl=[]

for i in table:
    date.append(list(i.values())[0])
    pnl.append(list(i.values())[1])


Sum_pnl=[]
pl= 0
for new in pnl:
    
    pl =  pl + new
    Sum_pnl.append(pl)
    

chart_data = pd.DataFrame(
    Sum_pnl,date
)
st.line_chart(chart_data)

st.table(table)


st.table(["Total PNL",Sum_pnl[-1]])


