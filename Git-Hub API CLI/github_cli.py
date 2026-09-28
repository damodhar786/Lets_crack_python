import requests, json

url = "https://api.github.com/users/damodhar786/events"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Data retrieved")
    # print(data)
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")


event = data[0]
print(event)