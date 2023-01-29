# Use the path {type} = all or single
# Use Querystring id
import json


def lambda_handler(event, context):
    type = event["params"]["path"]["type"]
    res = "error"
    if type.lower() == "all":
        res = "return all users"
    elif type.lower() == "single":
        res = "return only user"
    print(event)
    return {"statusCode": 200, "body": json.dumps("Hello from Lambda!"), "res": res}
