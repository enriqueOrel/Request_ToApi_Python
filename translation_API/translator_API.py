if __name__ == "__main__":
	import pandas as pd
	import translation as trs
	import time
	import json

	API_URL = "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-it-es"
	headers = {"Authorization": "Bearer {your_token}"}

	path_json = ""
	path_exel = ""
	
	df = pd.read_excel(path_exel)
    
	counter = 0
	for line in df['it-IT']:
		counter += 1
		try:
			if str(line) != "nan" and line != " " and line.isnumeric() == False and len(line) >= 5 and line != "<text>Text</text>":
				payload = {
                    "inputs": line,
					}
				output = trs.request_tranlation(API_URL, headers, payload, path_json, write_json=False)
				data = json.loads(output)
				translation = str(data[0]['translation_text'])
				print(translation)
				df.at[counter,'es-ES'] = translation
				time.sleep(0.5)
			else:
				pass
		except Exception as e:
			pass
		
else:
	print("Please run this script with '-h' for help")
