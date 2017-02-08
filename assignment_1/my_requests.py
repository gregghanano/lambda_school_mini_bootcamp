import requests

results = requests.get("https://www.google.com");

print(results.text);
print(results.status_code);
