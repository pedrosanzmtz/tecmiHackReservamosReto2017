import requests

def getPlaces(city, size=10):
	url = 'https://www.reservamos.mx/api/v2/places.json?from=' + city + '&prefetch=true'
	r = requests.get(url)
	json = r.json()
	final = json[:size]
	return final

def getQuotes(data, size=5):
	url = 'https://www.reservamos.mx/api/v2/quotes?origin='+data['origin']+ '&' \
			'&destination='+data['destination']+'&start='+data['start']+'&finish='+data['finish']
	
	r = requests.get(url)
	json = r.json()
	json = [json[key] for key in json.keys() if len(json[key]) != 0]
	lo = len(json)
	results = list()
	for i in json:
		for j in i:
			result = dict()
			j["score"] = (p * j["duration"]) * j["price"]
			result["score"] = j["score"]
			result["price"] = j["price"]
			result["duration"] = j["duration"]
			result["transportation"] = j["transportation"]
			result["date"] = j["date"]
			results.append(result)
	results = sorted(results, key=lambda x: x['score'])
	results = results[:size]
	return results

def getPopularity(city, to):
	url = 'https://www.reservamos.mx/api/v2/places.json?from=' + city + '&prefetch=true'
	r = requests.get(url)
	json = r.json()
	p = 0.1
	for i in json:
		if to == i['slug']:
			p = float(i['popularity'])
			break
	return p