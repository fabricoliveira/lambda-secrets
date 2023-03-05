import json
import boto3


def lambda_handler(event, context):
    response = ''
    print(event['method'])
    if event['method'] == 'boto3':
        print('************ executando boto3 ***************')
        client = boto3.client('ssm')
        response = client.get_parameter(Name='/IntegracaoDigital/Gateway/Mainframe/credentials')
    else:
        response = {}
    return {
        'statusCode': 200,
        'body': json.dumps({'secrets':response.items()})
    }
