"""Functions to interact with AWS rekognition API."""

import boto3

client = boto3.client("rekognition")
s3 = boto3.client("s3")

response = client.compare_faces(
    SourceImage={
        "S3Object": {
            "Bucket": "lightsail-hackathon",
            "Name": "kate_hudson.jpg",
        }},
    TargetImage={
        "S3Object": {
            "Bucket": "lightsail-hackathon",
            "Name": "goldie_hawn.jpg",
        }
    })

print response
