import requests

my_info = {
    "name":"Gregg",
    "lastname": "Hanano",
    "email":"gregg.hanano@gmail.com",
    "message":"sending HTTP POST request to lambdaschool.com/contact-form"
}

results = requests.post("https://lambdaschool.com/contact-form", json = my_info)

print("response: %s status code: %s" % (results.text, results.status_code))
