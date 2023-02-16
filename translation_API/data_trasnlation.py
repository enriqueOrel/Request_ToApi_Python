if __name__ == "__main__":
	import pandas as pd
	import translation as trs
	import time
	import json

	#Add the Url of the API  here 
	API_URL = " "

	#Include the headers with the unique personal access key token 
	headers = {"Authorization": "Bearer {'INSET KEY HERE'}"}

	#In case is include data add new heades 
	path_json = ""
	path_exel = ""
	
	df = pd.read_excel(path_exel)

	#the number of row where start to read lines
	counter = 0

	for line in range(0, len(df['it-IT'])):
		data = df['{Column_Namehere}'][counter]
		payload = {
		"inputs": data,
		}
		try:
			output = trs.request_tranlation(API_URL, headers, payload, path_json, write_json=False)
			data = json.loads(output)
			translation = str(data[0]['translation_text'])
			print(translation)
			df.at[counter,'column_to_write_tranlations'] = translation
			counter += 1
			time.sleep(0.2)

		except Exception as e:
			pass

