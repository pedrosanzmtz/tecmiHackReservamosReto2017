import os, json, reservamosApi
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/places', methods=['POST'])
def places():
	city = request.args.get('city')	
	response_dict = reservamosApi.getPlaces(city)
	response_json = json.dumps(response_dict)
	response = Response(response=response_json, status=200, mimetype="application/json")
	return response

@app.route('/quotes', methods=['POST'])
def quotes():
	data = dict()
	data['origin'] = request.args.get('origin')
	data['destination'] = request.args.get('destination')
	data['start'] = request.args.get('start')
	data['finish'] = request.args.get('finish')
	response_dict = reservamosApi.getQuotes(data)
	response_json = json.dumps(response_dict)
	response = Response(response=response_json, status=200, mimetype="application/json")
	return response

@app.route('/hello', methods=['GET'])
def hello():
	return 'hello'

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)