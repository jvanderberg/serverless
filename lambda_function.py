import json
import math


def lambda_handler(event, context):

    start = int(event['queryStringParameters']['start'])
    stop = int(event['queryStringParameters']['stop'])
    width = float(event['queryStringParameters']['width'])
    offsetx = float(event['queryStringParameters']['offsetx'])
    offsety = float(event['queryStringParameters']['offsety'])
    panx = float(event['queryStringParameters']["panx"])
    pany = float(event['queryStringParameters']["pany"])
    zoom = int(float(event['queryStringParameters']["zoom"]))
    maxIterations = int(event['queryStringParameters']["maxIterations"])
    iterationsArray = []
    for i in range(start, stop):
        x = i % width
        y = math.floor(i / width)
        x0 = (x + offsetx + panx) / zoom
        y0 = (y + offsety + pany) / zoom

        a = 0
        b = 0
        rx = 0
        ry = 0
        iterations = 0
        while iterations <= maxIterations and rx * rx + ry * ry <= 4:
            rx = a * a - b * b + x0
            ry = 2 * a * b + y0
            a = rx
            b = ry
            iterations = iterations + 1

        iterationsArray.append(iterations)

    return {
        'statusCode': 200,
        'body': json.dumps(iterationsArray),
        'headers': {'Access-Control-Allow-Origin': '*'}
    }


event = json.loads('{"queryStringParameters": {"start": "0","stop": "1288560","width": "1534","offsetx": "-767","offsety": "-420","panx": "-1084","pany": "-66","zoom": "800","maxIterations": "100"}}')


print(lambda_handler(event, ''))
