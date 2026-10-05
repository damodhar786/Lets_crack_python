import requests, sys
from datetime import datetime


def get_username():
    if len(sys.argv) == 2:
        userName = sys.argv[1]
        return userName
    else:
        print("Please follow: python github_activity.py <username>")

def api_response(userName):
    
    url = (f"https://api.github.com/users/{userName}/events")

    response = requests.get(url)

    # print(response.headers)
    if response.status_code == 404:
        # data = []
        return None, 404

    if response.status_code == 200:
        data = response.json()
        print("Data retrieved from User's Github")
        # print(data)
        print("*" * 65)
        return data, 200
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None, response.status_code



def process_events(userName):
    events, status_code = api_response(userName)

    if status_code == 200:

        if events:
            # print(event['type'])
            for event in events:

                repository_name = event['repo']['name'].split("/")    
                        
                created_at = event['created_at']
                date_created = datetime.fromisoformat(created_at) # Date when user used github for certain tasks/events
                        
                if event['type'] == "PushEvent":
                    # print(event["payload"])
                                    
                    ref = event["payload"]["ref"].split("/") # Split refs/heads/main to get Main Branch
                        
                    print(f"{event['actor']['login']} Pushed Code to {repository_name[1]} repository in {ref[2]} branch on {date_created.date()}")
                        
                elif event['type'] == "CreateEvent":
                    print(f"{event['actor']['login']} Created a {event['payload']['ref_type']} in {repository_name[1]} Repository on {date_created.date()}")
                        
                # if event['type'] == 'IssuesEvent': # No issues event
        else:
            print("No recent activity...")

    elif status_code == 404:
        print(f"Username {userName} does not exist as a GitHub user")

    else:
        print(f"API Failed")


userName = get_username()