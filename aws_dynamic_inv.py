#!/bin/python
import sys
try:
  import boto3
except Exception as e:
    print(e)
    print("Please rectify above exception and then try again")
    sys.exit(1)
