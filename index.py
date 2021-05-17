import json
import datetime


def handler(event, context):
    data = {
        'output': 'Helloworld!!! 16-May-21',
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
