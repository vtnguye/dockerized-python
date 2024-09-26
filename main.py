import requests

response = requests.get("https://api.github.com")
print(f"GitHub API Status: {response.status_code}")
