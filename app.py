from flask import Flask,render_template,request,jsonify
import pickle

model  = None

if model == None:
    
    model=pickle.load(open('diabetes.pkl','rb'))
    
app = Flask(__name__)

@app.route('/',methods=['POST'])
def calculate():
    
    data = request.get_json()
    
    preg = float(dict(data)['preg'])
    glu = float(dict(data)['glu'])
    bp = float(dict(data)['bp'])
    st = float(dict(data)['st'])
    ins = float(dict(data)['ins'])
    bmi = float(dict(data)['bmi'])
    dpf = float(dict(data)['dpf'])
    age = float(dict(data)['age'])
    
    output = model.predict([[preg,glu,bp,st,ins,bmi,dpf,age]])
    output = float(output[0])
    
    
    return jsonify(output)



if __name__=='__main__':
    app.run(debug=True)