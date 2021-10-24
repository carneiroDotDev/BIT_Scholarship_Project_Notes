# BIT_Scholarship_Council_Notes
Repository to create notes regarding the projects and lessons of all the three different tracks
This project majors on Deploying Infrastructure as Code


- Creating a Launch Configuration for the four servers
  The cloud formation output has a Load Balancer having the public url to be displayed.
- Downloading application from S3 Bucket and creating IAM role that allows instances to use this service.

## Example of a Cloud formation Template.



.......




## Point to note
- While creating your template file remember to use AMI image that matches your correct aws location to avoid running into Rollback errors.

- 502 error could easily emerges while deploying the loadbalancer created from the Stack,one way to approach this is by reloading your browser might take some time to refresh.

- Indetation is a major concern that must be observered while creating both the yaml files.
