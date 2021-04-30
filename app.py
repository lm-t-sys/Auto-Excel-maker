#!user/bin/python
#coding : utf-8
from flask import Flask,render_template,request,redirect,url_for
import pandas as pd
import numpy as np
import matplotlib as plt
from IPython.display import HTML

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='GET':

        return render_template("index.html")
    else:
        
        a=request.form.get('indexs')
        b=request.form.get('columns')
        c=request.form.get('values')
        a2=a.split(',')
        b2=b.split(",")
        a3,b3=[],[]
        for aa in a2:
            if a.strip()=="":
                break
            else:
                a3.append(aa)

        for bb in b2:
            b3.append(bb) 
        f=[] 

        d=c.strip().split(",") 
        for i in d:
            f.append(i)    
        f=np.array(f)
        a3_size=len(a3)
        b3_size=len(b3)
        if b3_size>1:
            f=np.array(f).reshape(int(f.size/b3_size),b3_size)     
        else:
            f=np.array(f)                                
        if a3_size<1:
            c2=pd.DataFrame(f,columns=b3,index=None)
        else:
            c2=pd.DataFrame(f,columns=b3,index=a3)              
                    
        ANS=HTML(c2.to_html(classes='table table-striped'))

        c2.to_excel("templates/excelfolder/to_csv.xlsx")

               
        return render_template('index.html',posts=ANS)

if __name__=="__main__":
    app.run(debug=True)    