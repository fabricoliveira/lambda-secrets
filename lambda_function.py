import json
import boto3


client = boto3.client('ssm')


def lambda_handler(event, context):
    response = ''
    print(event['method'])
    if event['method'] is 'boto3':
        response = client.get_parameter('/IntegracaoDigital/Gateway/Mainframe/credentials')
    else:
        response = {}
    return {
        'statusCode': 200,
        'body': json.dumps({'secrets':response})
    }
