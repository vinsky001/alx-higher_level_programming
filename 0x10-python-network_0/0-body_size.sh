#!/bin/bash
# a Bash script that takes in a URL, sends a request, and displays the size
curl -s "${1}" | wc -c
