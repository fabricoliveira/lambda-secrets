import json
import boto3

from aws_lambda_powertools.utilities import parameters

client = boto3.client('ssm')

def lambda_handler(event, context):
    response = ''
    print(event['method'])
    if event['method'] == 'boto3':
        print('************ executando boto3 ***************')
        response = client.get_parameter(Name='/IntegracaoDigital/Gateway/Mainframe/credentials')
        response = response['Parameter']['Value']
    else:
        print('************ executando AWS lambda powertools ***************')
        response = parameters.get_parameter('/IntegracaoDigital/Gateway/Mainframe/credentials')

    return response
