"""Functions to interact with AWS rekognition API."""

import boto3

client = boto3.client("rekognition")
s3 = boto3.client("s3")

# testing API response from AWS rekognition
# response confirms 2 faces are unmatched
# 99% certainty that both pictures contain faces
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
