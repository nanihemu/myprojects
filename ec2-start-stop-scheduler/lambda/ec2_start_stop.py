import boto3

ec2 = boto3.client("ec2", region_name="ap-south-1")

INSTANCE_IDS = [
    "i-09921011df6d40e19","i-05f451c3e71e6528c", "i-0a4d8a85add1efee9"
]

def lambda_handler(event, context):
    action = event.get("action", "").lower()

    if action == "stop":
        response = ec2.stop_instances(
            InstanceIds=INSTANCE_IDS
        )

    elif action == "start":
        response = ec2.start_instances(
            InstanceIds=INSTANCE_IDS
        )

    else:
        raise ValueError(
            "Invalid action. Use 'stop' or 'start'."
        )

    print(f"Action requested: {action}")
    print(response)

    return {
        "action": action,
        "instance_ids": INSTANCE_IDS,
        "message": "EC2 request submitted successfully"
    }

