import requests

url = "https://api.github.com/users/damodhar786/events"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Data retrieved")
    print(data)
    print("*" * 65)
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")

events = data
# print(event['type'])
for event in events:
    print(event['type'])
    print(event['actor']['login'])
    print(event['repo']['name'])

    if event['type'] == "PushEvent":
        print(event["payload"])