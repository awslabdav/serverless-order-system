import boto3, uuid

client = boto3.resource('dynamodb')
table = client.Table("Orders")

def lambda_handler(event, context):
    for record in event['Records']:
        print("test")
        payload = record["body"]
        print(str(payload))
        table.put_item(Item= {'OrderID': str(uuid.uuid4()),'order':  payload})
        #print(OrderID)