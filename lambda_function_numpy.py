import json
import math
import numpy as np


def lambda_handler(event, context):

    start = int(event["queryStringParameters"]["start"])
    stop = int(event["queryStringParameters"]["stop"])
    width = float(event["queryStringParameters"]["width"])
    offsetx = float(event["queryStringParameters"]["offsetx"])
    offsety = float(event["queryStringParameters"]["offsety"])
    panx = float(event["queryStringParameters"]["panx"])
    pany = float(event["queryStringParameters"]["pany"])
    zoom = int(float(event["queryStringParameters"]["zoom"]))
    maxIterations = int(event["queryStringParameters"]["maxIterations"])
    i = np.array(range(start, stop))
    x = np.empty(stop-start)
    x0 = np.empty(stop-start)
    y0 = np.empty(stop-start)
    a = np.zeros(stop-start)
    b = np.zeros(stop-start)
    rx = np.zeros(stop-start)
    ry = np.zeros(stop-start)
    x = i % width
    y = np.floor(i / width)
    x0 = (x + offsetx + panx) / zoom
    y0 = (y + offsety + pany) / zoom
    iterations = np.zeros(stop-start)
    test = np.zeros(stop-start)
    M = np.full((stop-start), True, dtype=bool)
    for i in range(maxIterations):
        test[M] = rx[M] * rx[M] + ry[M] * ry[M]
        rx[M] = a[M] * a[M] - b[M] * b[M] + x0[M]
        ry[M] = 2 * a[M] * b[M] + y0[M]
        a[M] = rx[M]
        b[M] = ry[M]
        iterations[M] = iterations[M] + 1
        M[np.abs(test) > 4] = False

    return {
        "statusCode": 200,
        "body": json.dumps(iterations.tolist()),
        "headers": {"Access-Control-Allow-Origin": "*"}
    }


event = json.loads('{"queryStringParameters": {"start": "0","stop": "1288560","width": "1534","offsetx": "-767","offsety": "-420","panx": "-1084","pany": "-66","zoom": "800","maxIterations": "500"}}')


print(lambda_handler(event, ''))
