import boto3
import os
from botocore.exceptions import ClientError

tag_data = [{'Key':'purpose', 'Value': "updated-testing"}]
s3 = boto3.resource('s3')
buckets = s3.buckets.all()
print (os.environ.get("NUM_SAS_WORKERS"))
for bucket in buckets:
    try:
        bucket_tagging=s3.BucketTagging(bucket.name)
        tags = bucket_tagging.tag_set
        for tag in tags:
            tag_values = list(tag.values())
            if tag_values[0] == 'purpose' and tag_values[1] == 'testing':
                print(bucket.name)
                response = bucket_tagging.put(
                        Tagging={'TagSet': tag_data}
)

    except ClientError as e:
        print ("Error getting tags: ", e)