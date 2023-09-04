import boto3
from params import *
import datetime
import time

# Initialize the EC2 client
ec2 = boto3.client('ec2', region_name=region_name, aws_access_key_id=region_name,
                   aws_secret_access_key=aws_secret_access_key)

# Specify the AMI ID, instance type, and key pair
ami_id = 'ami-0261755bbcb8c4a84'  # Use the appropriate AMI ID
instance_type = 't2.micro'
key_name = 'sample_ec2'

# Create the instance
response = ec2.run_instances(
    ImageId=ami_id,
    InstanceType=instance_type,
    MinCount=1,
    MaxCount=1
)

instance_id = response['Instances'][0]['InstanceId']

print(f'Instance created with ID: {instance_id}')


def start_instance(instance_id):
    ec2.start_instances(InstanceIds=[instance_id])
    print(f'Starting instance {instance_id}')


def stop_instance(instance_id):
    ec2.stop_instances(InstanceIds=[instance_id])
    print(f'Stopping instance {instance_id}')


def get_existing_instances():
    response = ec2.describe_instances()
    # Extract instance IDs using list comprehension
    instance_ids = [instance['InstanceId'] for reservation in response['Reservations'] for instance in
                    reservation['Instances']]
    return instance_ids

# Define the schedule
def is_schedule_active():
    current_time = datetime.datetime.now(datetime.timezone.utc)
    current_day = current_time.strftime("%A")

    # Check if it's an alternate day
    if current_day in ["Monday", "Wednesday", "Friday", "Sunday"]:
        # Check if it's within the time window (9:00 AM to 11:30 AM GMT)
        if (current_time.hour == 9 and current_time.minute >= 0) or \
                (current_time.hour == 10) or \
                (current_time.hour == 11 and current_time.minute <= 30):
            return True

    return False


# Main function
def main():
    while True:
        if is_schedule_active():
            start_instance()
        else:
            stop_instance()
        # Sleep for a minute before checking the schedule again
        time.sleep(60)


if __name__ == '__main__':
    main()
