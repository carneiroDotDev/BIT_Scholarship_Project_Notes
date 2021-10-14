# Project 1 - Deploy Static Website on AWS

**TLDR:** the project is described step by step on Udacity. There are no many todos, its more about following all the steps described on the project page.

The whole project has two major intentions to implement:

- Hosting a static website on S3 and
- Accessing the cached website pages using CloudFront content delivery network (CDN) service. Recall that CloudFront offers low latency and high transfer speeds during website rendering.

## Part 1 - Create S3 Bucket
The page on udacity describe how to proceed step by step, but one more step may be necessary: attach a public policy to the bucket.

```python
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::Bucket-Name/*"
            ]
        }
    ]
}
```

Attention for the substitution of **Bucket-Name** for the name of the bucket you created.
