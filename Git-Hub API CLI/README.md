# GitHub User Activity CLI

A simple Python command-line application that fetches and displays a user's recent public GitHub activity using the GitHub Events API.

## Features

- Accepts a GitHub username through the command line.
- Fetches the user's recent public GitHub events.
- Displays `PushEvent` activity.
- Displays `CreateEvent` activity.
- Shows the repository, branch/type, and event date.
- Handles invalid usernames and API errors.
- Handles users with no recent activity.
- Uses HTTP status codes to handle different API responses.

## Requirements

- Python 3.x
- `requests` library
- Internet connection

## Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd Lets_crack_python
```

Install the required dependency:

```bash
pip install requests
```

## Usage

Run the program from the command line:

```bash
python github_activity.py <username>
```

Example:

```bash
python github_activity.py johnDoe
```

The program will fetch the user's recent GitHub activity and display supported events.

Example output:

```text
Data retrieved from User's Github
*****************************************************************
damodhar786 Pushed Code to Lets_crack_python repository in main branch on 2026-09-26
damodhar786 Created a branch in Lets_crack_python Repository on 2026-09-25
```

## Error Handling

The application handles different situations based on the GitHub API response:

- **200** — Successfully retrieved activity.
- **404** — GitHub user does not exist.
- **Other status codes** — API request failed.
- **No recent activity** — Displays a message when the user has no available events.
- **Invalid command-line arguments** — Displays the correct usage format.

## Project Structure

```text
Lets_crack_python/
│
├── github_activity.py
└── README.md
```

## How It Works

The application follows this flow:

```text
Command-line username
        ↓
   get_username()
        ↓
   api_response()
        ↓
 GitHub Events API
        ↓
    JSON response
        ↓
   process_events()
        ↓
 PushEvent / CreateEvent
        ↓
    Formatted output
```

## Technologies Used

- Python
- Requests
- GitHub REST API
- `sys.argv`
- `datetime`

## What I Practiced

This project helped me practice:

- Python functions
- Command-line arguments
- Working with REST APIs
- HTTP status codes
- JSON data handling
- Dictionaries and nested data
- Conditional statements
- Loops
- String manipulation
- Date/time conversion
- Basic error handling
- Structuring a small Python CLI application

## Scope

Currently, the application processes:

- `PushEvent`
- `CreateEvent`

Other GitHub event types are currently ignored.

## Future Improvements

Possible improvements for a future version:

- Support more GitHub event types.
- Improve CLI argument parsing.
- Add automated tests.
- Add optional authentication for higher API rate limits.
- Improve output formatting.

## License

This project is created for learning and practice purposes.