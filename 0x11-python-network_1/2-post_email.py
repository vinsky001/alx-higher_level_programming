#!/usr/bin/python3
"""
Python script that:
- sends a POST request to the passed URL with the email as a parameter,
- and displays the body of the response (decoded in utf-8)
"""

from sys import argv
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    values = {"email" = sys.argv[2]}

    data = url.parse.urllencode(values).encode("ascii")
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
