import requests, json

from flask import Flask, request, render_template, jsonify
app = Flask(__name__)


DATA_SOURCE = "http://data.sfgov.org/resource/rqzj-sfat.json"

def pretty(json_str):
    return json.dumps(json_str, sort_keys=True, indent=2, separators=(',', ': ')) 

def sekitar_embarcadero(truck):
    return truck.get('x') > 1 and truck.get('y') > 1 

def applicant_x_y(truck):
    return {
        'Food truck name': truck.get('applicant'),
        'x': truck.get('x'),
        'y': truck.get('y')
    } 

@app.route('/')
def hello_world():    
    return 'Hello World!'


@app.route('/test')
def test():
    d = requests.get(DATA_SOURCE)
    json_data = d.json()

    approved = filter(sekitar_embarcadero, json_data)
    applicants = map(applicant_x_y, approved)
    
    return pretty(applicants)
        

    
    

if __name__ == '__main__':    
    app.run(debug=True)
