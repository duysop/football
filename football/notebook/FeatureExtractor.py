import pandas as pd
import numpy as np
def Possesion10Homelater(df,name,id):
    index = list(df[df['team']==name and df['id']<=id].index)
    meanPct=np.mean(list(df.iloc[index][-10:]['homePct(%)']))
def Possesion10Awaylater(df,name,date):
    index = list(df[df['opponent']==name and df['id']<id].index)
    meanPct=np.mean(list(df.iloc[index][-10:]['AwayPct(%)']))
def Form(df,name,date):
    index =list(df[df['team']==name or df['opponent']==name and df['id']<id].index)
    form =0
    for i in range(1,6):
        if df.iloc[index][-i:-i+1]['rerult']==1:form+=1
        else:
            if df.iloc[index][-i:-i+1]['team']==name:form+=df.iloc[index][-i:-i+1]['rerult']
            else:form+=3-df.iloc[index][-i:-i+1]['rerult']


    

    
# mydict = [{'a': 1, 'b': 2, 'c': 3, 'd': 4},
#           {'a': 1, 'b': 200, 'c': 300, 'd': 400},
#           {'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000 }]
# df = pd.DataFrame(mydict)
# index=list(df[df['a']==1].index)
# a=2
# df.iloc[index][-a:]['b']

# np.mean(list(df.iloc[index][-a:]['b']))