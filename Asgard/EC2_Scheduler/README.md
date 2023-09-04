# EC2 Instance Scheduler

This Python script is designed to automate the scheduling of an Amazon EC2 instance based on the specified criteria. It ensures that the EC2 instance runs only on alternate days (Monday, Wednesday, Friday, Sunday) between 9:00 AM GMT and 11:30 AM GMT while keeping the instance stopped during other times to optimize costs.

## Prerequisites

Before using this script, ensure that you have the following prerequisites in place:

- Python installed on your system.
- The Boto3 library installed. You can install it using `pip install boto3`.
- AWS credentials set up with appropriate permissions for EC2.

## Configuration

In the script, you need to configure several parameters:

- `region_name`: The AWS region in which your EC2 instance resides.
- `aws_access_key_id` and `aws_secret_access_key`: Your AWS access key ID and secret access key.
- `ami_id`: The AMI ID of the EC2 instance you want to launch.
- `instance_type`: The EC2 instance type.
- `key_name`: The name of the key pair used for SSH access.
- `is_schedule_active()`: Defines the scheduling logic. It checks if the current day is one of the specified days and if the current time is within the specified time window.

## Usage

1. Ensure that the required configurations are correctly set in the script.

2. Run the script using Python:

   ```bash
   python ec2_scheduler.py
