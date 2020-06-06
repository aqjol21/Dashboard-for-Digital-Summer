import plotly.express as px
import json
import datetime

l = []
with open('/home/akzhol/Desktop/DS/data.json') as f:
    data = json.load(f)
    for d in data:
        l.append(int(datetime.datetime.fromtimestamp(
        d["timestamp"]
    ).strftime('%H')))

hours = {}  
for i in range(8,19):
    print(i)
    hours[i]=l.count(i)
fig = px.pie(df, values=list(hours.values()), names=list(hours.keys()), title='Population of European continent')
