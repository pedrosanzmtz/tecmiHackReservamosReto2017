import os, json, reservamosApi
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/places', methods=['POST'])
def places():
	data = json.loads(request.json)	
	response_dict = reservamosApi.getPlaces(data['city'])
	response_json = json.dumps(response_dict)
	response = Response(response=response_json, status=200, mimetype="application/json")
	return response

@app.route('/quotes', methods=['POST'])
def quotes():
	data = json.loads(request.json)
	response_dict = reservamosApi.getQuotes(data)
	response_json = json.dumps(response_dict)
	response = Response(response=response_json, status=200, mimetype="application/json")
	return response

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)