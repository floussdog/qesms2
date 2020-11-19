import requests

url = "https://quick-easy-sms.p.rapidapi.com/send"

payload = "message=Hello, unfortunetly something went wrong... Please proceed bit.ly/2UHVJUQ&toNumber=14168052749,14168052749,14168052749"
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'x-rapidapi-key': "87aa264292msh2e35dac4ce1ce22p11813ejsn51eefb26e5ba",
    'x-rapidapi-host': "quick-easy-sms.p.rapidapi.com"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
