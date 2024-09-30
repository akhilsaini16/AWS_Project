import json

def lambda_handler(event, context):
    print('This was pushed from Local Machine using git and GHA')
    return 100
