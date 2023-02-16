import requests
from requests.exceptions import HTTPError
import json
import os

def requests_data(url: str, headers: str, payload, **kwargs):
	responce_path: str = kwargs.get('responce_path', None)
	data_path: str = kwargs.get('data_path', None)

	try:
		if data_path != None:
			if os.path.exists(data_path) == True and data_path.endswith('.json') == True:
				with open(data_path,'r') as data_file:
					data = json.load(data_file)
					response = requests.post(url, headers=headers, json=data)
					data = response.json()
					print(data)
				
				if responce_path != None:
					if responce_path.endswith('.json') == True:
						with open(responce_path, 'w', encoding='UTF-8') as f:
							json.dump(data, f, indent=4)

					elif responce_path.endswith('.json') == False:
						return print("The responce file has to be a '.json' file")

				else:
					return print(data)
					
			elif os.path.exists(data_path) == False:
				with open(data_path, 'w', encoding='UTF-8') as f:
					data = {'text': 'Hello World','source_lang':'IT', 'target_lang': 'ES', 'split_sentences': 0}
					json.dump(data, f, indent=4)
					print("The file does not exist, creating it...")
				return print("Run the script again")
		else:
			data = payload
			response = requests.post(url, headers=headers, data=data)
			data = response.json()
			print(data)

			
	except HTTPError as err:
		return print(err.response.json())

	except Exception as e:
		return print(f'the code has returned an error: {e}')

if __name__ == '__main__':
	print("hello world")

