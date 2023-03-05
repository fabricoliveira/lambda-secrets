import json
import boto3

from aws_lambda_powertools.utilities import parameters


def lambda_handler(event, context):
    response = {}


    url = parameters.get_parameter('/IntegracaoDigital/Gateway/Mainframe/url')
    


    credentials = parameters.get_parameter('/IntegracaoDigital/Gateway/Mainframe/credentials')
    credentials = json.loads(parameters.get_secret(credentials))
    user = credentials['gateway-mainframe-ims-user']
    token = credentials['gateway-mainframe-ims-token']

    response = {
        'credentials': credentials,
        'url': url,
        'user': user,
        'token': token
    }
    return response
