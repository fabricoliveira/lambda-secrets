import json
import boto3

from aws_lambda_powertools.utilities import parameters

client = boto3.client('ssm')

def lambda_handler(event, context):
    response = {}
    arn   = ''
    url   = ''
    user  = ''
    token = ''

    if event['method'] == 'boto3':
        print('************ executando boto3 ***************')
        arn = client.get_parameter(Name='/IntegracaoDigital/Gateway/Mainframe/credentials')['Parameter']['Value']
        url = client.get_parameter(Name='/IntegracaoDigital/Gateway/Mainframe/url')['Parameter']['Value']
    else:
        print('************ executando AWS lambda powertools ***************')
        arn = parameters.get_parameter('/IntegracaoDigital/Gateway/Mainframe/credentials')
        url = parameters.get_parameter('/IntegracaoDigital/Gateway/Mainframe/url')
        #user = parameters.get_parameter(arn)

    response = {
        'arn':arn,
        'url': url,
        'user': user,
        'token': token
    }

    return response
