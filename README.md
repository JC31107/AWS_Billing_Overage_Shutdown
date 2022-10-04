# AWS_Billing_Overage_Shutdown
Scripts for automatically shutting down EC2 instances on billing alerts

This is an overview on steps required to create a billing alert, create an SNS topic, and have a Lambda function iterate through all EC2 instances with a particular name

The steps are performed in reverse for ease of configuration

Create a Lambda function with a name of your choice, and deploy the lambda_function.py Python code

Modify the permission group on the Lambda function to match the JSON file provided.
  Alternativly you can add the permissions of ec2.describeinstances, ec2.stopinstances, and sns.subscribe to an existing permission
  
Create an SNS topic as a standard type, not FIFO

Create a subscription and map the Lambra function through

Edit the access policy on the SNS topic and allow permission for billing to send messages.   Formatting on this can be a touch wonky, there is an example JSON provided that can probably be copied and pasted after updating the account ID and the resource names

Go into the Billing console and create a new budget
In the budget create a threshold to fire the Lambda function, I chose 105% of actual budget cost
In the alert expand "Amazon SNS Alerts" and paste in the ARN of the SNS topic previously created

To test you can go into the SNS and send a message to the tpoic, content isn't importand as the Lambda function doesn't care who or what calls it, so make sure security is locked down!
