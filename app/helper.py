import json
from bson import json_util

def serialize_data(data):
    return json.loads(json_util.dumps(data))

def collection_to_list(collection):
    empty_list = []
    for data in collection:
        empty_list.append(serialize_data(data))
    return empty_list

def request_success(body):
    return {"statusCode": 200, "body": body}

def request_error(body):
    return {"statusCode": 400, "body": body}

def youtube_to_id(link):
    regex = ["https", ":", "/", "www", ".", "youtube", "com", "watch?v=", "youtu.be"]
    for reg in regex:
        link = link.replace(reg, "")
    return link