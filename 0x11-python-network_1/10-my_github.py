#!/usr/bin/python3
"""
Python script that:
- takes your GitHub credentials (username and password)
- and uses the GitHub API to display your id
"""

from sys import argv
from requests import get
from requests.auth import HTTPBasicAuth

if __name__ == '__main__':
    auth = HTTPBasicAuth(argv[1], argv[2])
    res = get("https://api.github.com/user", auth=auth)
    print(res.json().get('id'))
