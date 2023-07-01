#!/usr/bin/python3
"""
Python script that:
- fetches https://alx-intranet.hbtn.io/status
- must use the package urllib
- not allowed to import any packages other than urllib
- The body of the response must be displayed
- like the following example (tabulation before -)
- must use a with statement
"""

if __name__ == "__main__":
    from urllib.request import urlopen, Request

    url = "https://alx-intranet.hbtn.io/status"
    req = Request(url)
    with urlopen(req) as res:
        content = res.read()

    print("Body response:")
    print(f"\t- type:", type(content))
    print(f"\t- content:", (content))
    print(f"\t- utf8 content:", content.decode('utf-8'))
