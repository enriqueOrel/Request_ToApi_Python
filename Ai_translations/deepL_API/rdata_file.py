if __name__ == "__main__":
	import pandas as pd
	import http_requests as http
	import time
	import json

	API_URL = " "
	headers = {"Authorization": "Bearer {'INSET KEY HERE'}"}

	#PATH of exel file to read data
	path_file = " "
	
	#Pandas create data frame
	df = pd.read_excel(path_file)

	counter = 0
	for line in range(0, len(df['it-IT'])):
		data = df['it-IT'][counter]
		payload = {
		"text": data,
		"source_lang": "IT",
		"target_lang": "ES",
        }

		try:
			output = http.requests_data(API_URL, headers, payload)
			data = json.loads(output)
			translation = str(data[0]['translation_text'])
			print(translation)
			df.at[counter,'es-ES'] = translation
			counter += 1
			time.sleep(0.3)

		except Exception as e:
			print(f"this script has got an exception: {e}")
else:
	print("Please run this script with '-h' for help")
