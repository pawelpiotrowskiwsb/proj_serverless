import localstack_client.session as boto3

client = boto3.client('s3')

bucket_name = "mybucket"
location = {'LocationConstraint': 'eu-north-1'}

response = client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)

print("Amazon S3 bucket has been created")

response = client.list_buckets()

print("Listing Amazon S3 Buckets:")

for bucket in response['Buckets']:
    print(f"-- {bucket['Name']}")