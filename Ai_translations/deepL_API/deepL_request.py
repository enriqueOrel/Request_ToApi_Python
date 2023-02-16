import http_requests as http
        
url = 'https://api-free.deepl.com/v2/translate'
headers = {'Authorization': 'DeepL-Auth-Key {your_key}'}

#include path of JSON file in case the request include data, 
data = ""

#add the argumet write_jason and provide the path 
file = ""

#make the request 
response = http.requests_data(url, headers, data, file, write_json=True) 

print(response)