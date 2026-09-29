import requests
from datetime import datetime

def api_response():
    url = "https://api.github.com/users/damodhar786/events"

    response = requests.get(url)

    # print(response.headers)

    if response.status_code == 200:
        data = response.json()
        print("Data retrieved from User's Github")
        # print(data)
        print("*" * 65)
        return data
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")



def event_created():
    events = api_response()

    # print(event['type'])
    for event in events:

        repository_name = event['repo']['name'].split("/")    

        created_at = event['created_at']
        date_created = datetime.fromisoformat(created_at) # Date when user used github for certain tasks/events

        if event['type'] == "PushEvent":
            # print(event["payload"])
        
            ref = event["payload"]["ref"].split("/") # Split refs/heads/main to get Main Branch

            print(f"{event['actor']['login']} Pushed Code to {repository_name[1]} repository in {ref[2]} branch on {date_created.date()}")

        if event['type'] == "CreateEvent":
            
            print(f"{event['actor']['login']} Created a {event['payload']['ref_type']} in {repository_name[1]} Repository on {date_created.date()}")

        # if event['type'] == 'IssuesEvent': # No issues event

event_created()