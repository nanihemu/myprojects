# AWS EC2 Auto Scaling with Application Load Balancer — User Data

## Project Overview

This project demonstrates hosting a static website on Amazon EC2 instances behind an Application Load Balancer (ALB), with an Auto Scaling Group (ASG) to manage EC2 instance capacity.

The website is configured using **EC2 Launch Template User Data**. When an instance launches, the User Data script installs Apache, starts the web server, and creates the website's HTML page automatically.

AWS resources are configured through the AWS Management Console.

## Architecture

![AWS EC2 ALB Auto Scaling Architecture](docs/architecture.png)

**Request flow:**

User → Application Load Balancer → Target Group → EC2 Instances

The Auto Scaling Group launches and terminates EC2 instances according to its configured capacity and scaling policies.

## AWS Services Used

- **Amazon EC2:** Runs the website.
- **EC2 Launch Template:** Defines the AMI, instance type, security groups, and User Data.
- **Application Load Balancer:** Distributes incoming website traffic.
- **Target Group:** Registers EC2 instances and performs health checks.
- **Auto Scaling Group:** Manages the EC2 instance fleet.
- **Amazon VPC and Security Groups:** Provide networking and traffic control.

## Implementation Steps

1. Selected an appropriate Amazon Linux AMI and instance configuration.
2. Created an EC2 Launch Template with a User Data script.
3. Used User Data to install Apache and create the HTML website at `/var/www/html/index.html`.
4. Created a target group with an HTTP health check.
5. Configured an Application Load Balancer.
6. Created an Auto Scaling Group using the Launch Template.
7. Attached the Auto Scaling Group to the target group.
8. Accessed the website through the ALB DNS name.
9. Monitored instance health and Auto Scaling behavior.

## User Data Script

Example for Amazon Linux 2023:

```bash
#!/bin/bash
dnf install -y httpd
systemctl enable --now httpd

cat > /var/www/html/index.html <<'EOF'
<!DOCTYPE html>
<html>
<head>
    <title>AWS Auto Scaling Project</title>
</head>
<body>
    <h1>Welcome to My AWS Website</h1>
    <p>Hosted on Amazon EC2.</p>
    <p>Provisioned using Launch Template User Data.</p>
</body>
</html>
EOF
```

The script runs when an EC2 instance initializes. Check the User Data script and cloud-init logs if initialization fails.

## Testing and Validation

- Verified that the website responds through the ALB DNS name.
- Checked target group health status.
- Verified that the Auto Scaling Group uses the intended Launch Template.
- Observed scaling behavior under the test conditions.

**Scaling test note:** Record whether scale-out or scale-in actually occurred. If a test did not meet the configured scaling threshold, document it as not triggered rather than claiming it succeeded.

## Demo Video

Video path in this repository:

`01-ec2-alb-auto-scaling-userdata/videos/auto-scaling-demo.mp4`

[Watch the Auto Scaling Demo](videos/auto-scaling-demo.mp4)

Add the video to this location before using the link. If the recording is too large for GitHub, use an unlisted YouTube video and link to it instead.

## Security Considerations

- Allow public HTTP traffic through the ALB listener as required.
- Allow inbound HTTP traffic to EC2 only from the ALB security group.
- Restrict SSH access to trusted IP addresses when SSH is needed.
- Avoid placing credentials or secrets in User Data.

## Key Learnings

- Automating EC2 initialization with User Data.
- Installing and configuring Apache on Amazon Linux.
- Configuring ALB listeners, target groups, and health checks.
- Integrating a Launch Template with an Auto Scaling Group.
- Monitoring EC2 capacity and scaling policies.

## Project Information

- **Category:** AWS Cloud / Infrastructure
- **Provisioning:** AWS Management Console and Launch Template User Data
- **Web Server:** Apache (`httpd`)
- **Website:** Static HTML
- **Status:** Update based on the features and tests completed.
