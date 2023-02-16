import requests
from requests.exceptions import HTTPError
import json

def request_tranlation(url: str, headers: str, payload, file_directory: str, write_json: bool):
	try:
		response = requests.post(url, headers=headers, json=payload)
		data = response.json()
		json_dump = json.dumps(data, indent=4)
		if file_directory.endswith('.json') and write_json == True:
			with open(file_directory, 'a') as f:
				json.dump(data, f)
		elif file_directory.endswith('.json') == False:
			return print("The file has to be a '.json' file")
		else:
			return json_dump

	except HTTPError as err:
		return print(err.response.json())

	except Exception as e:
		return print(f'the code has returned an error: {e}')

if __name__ == '__main__':
	print("this is a module bro")

