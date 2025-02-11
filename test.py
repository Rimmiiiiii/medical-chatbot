import requests

url = "http://127.0.0.1:5000/translate"
data = {"text": "Hello, how are you?"}
response = requests.post(url, json=data)

print(response.json())  # Expected output: {'translated_text': 'Hallo, wie geht es dir?'}
