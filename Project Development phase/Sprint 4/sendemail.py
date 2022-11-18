import requests

def sendgridmail(user):
	url = "https://rapidprod-sendgrid-v1.p.rapidapi.com/mail/send"
	payload = {
		"personalizations": [
			{
				"to": [{"email": user}],
				"subject": "Your Monthly expense is exceeded"
			}
		],
		"from": {"email": "persoanlbudget@peta.com"},
		"content": [
			{
				"type": "text/plain",
				"value": "Avoid spending money, your monthly expense is exceeded..."
			}
		]
	}
	headers = {
		"content-type": "application/json",
		"X-RapidAPI-Key": "8dbcdbb4e0msh2ca0fb8c6cfb3b9p13a154jsn1b29565d9fd5",
		"X-RapidAPI-Host": "rapidprod-sendgrid-v1.p.rapidapi.com"
	}
	response = requests.request("POST", url, json=payload, headers=headers)
	print(response.text)