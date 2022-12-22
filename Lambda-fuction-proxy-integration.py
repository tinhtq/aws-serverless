import json


def lambda_handler(event, context):
    type = event["pathParameters"]["type"]
    id = "0"
    res = "error"
    if type.lower() == "all":
        res = "return all users"
    elif type.lower() == "single":
        res = "return only user"
        id = event["queryStringParameters"]["id"]
    print(event)
    return {
        "statusCode": 200,
        "body": json.dumps({"res": res, "id": id, "message": "hello get method"}),
        "headers": {
            "Content-Type": "application/json"
        }
    }
