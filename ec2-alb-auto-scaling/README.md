# AWS EC2 Web Servers with Application Load Balancer and Auto Scaling

## 📌 Project Overview

This project demonstrates how to host a static website on Amazon EC2 instances and distribute incoming web traffic using an **Application Load Balancer (ALB)**. An **EC2 Auto Scaling Group (ASG)** manages the number of instances based on its configured capacity and scaling policies.

The infrastructure is configured using the AWS Management Console and demonstrates load balancing, health checks, high availability, and automatic instance management.

## 🏗️ Architecture

**Request Flow:**

User / Internet → Internet Gateway → Application Load Balancer → Target Group → EC2 Instances

The EC2 instances run a static website using Nginx or Apache HTTP Server.

The Auto Scaling Group manages EC2 instances across the configured Availability Zones.

![AWS EC2 ALB Auto Scaling Architecture](docs/architecture.png)

## ☁️ AWS Services Used

| AWS Service | Purpose |
|---|---|
| Amazon EC2 | Hosts the static website |
| EC2 Launch Template | Defines the configuration for launching EC2 instances |
| Application Load Balancer | Distributes incoming HTTP/HTTPS requests |
| Target Group | Registers EC2 instances and performs health checks |
| EC2 Auto Scaling Group | Maintains the desired EC2 capacity and manages instance replacement |
| Amazon VPC | Provides the networking environment |
| Subnets | Provide network placement for AWS resources |
| Internet Gateway | Enables internet connectivity for eligible resources |
| Route Tables | Control network traffic routing |
| Security Groups | Control inbound and outbound traffic |

## ⚙️ Implementation Steps

### 1. Create a Launch Template

Created an EC2 Launch Template specifying the required Amazon Machine Image (AMI), instance type, security group, and other launch settings.

### 2. Create a Target Group

Created a target group to register the EC2 instances and configure health checks for the website.

### 3. Create an Application Load Balancer

Configured an internet-facing Application Load Balancer and listener to receive incoming requests and forward them to the target group.

### 4. Configure an Auto Scaling Group

Created an Auto Scaling Group using the launch template and configured the required subnets and desired capacity.

### 5. Deploy the Static Website

Configured the EC2 instances to serve static HTML and CSS content using Nginx or Apache HTTP Server.

### 6. Test the Application

Accessed the website through the ALB DNS name and checked target health and Auto Scaling behavior.

## 🧪 Testing and Validation

The following tests can be documented with screenshots after verification:

- [ ] Access the static website using the ALB DNS name.
- [ ] Verify that the registered EC2 instances are healthy.
- [ ] Confirm that the ALB forwards requests to the target group.
- [ ] Verify that the Auto Scaling Group maintains the configured desired capacity.
- [ ] Terminate a test instance and verify whether the ASG launches a replacement.
- [ ] Test scale-out and scale-in if a scaling policy is configured.

## 📸 Project Screenshots

Add screenshots from your AWS environment in the `docs/screenshots/` directory.

Suggested screenshots:

1. Launch Template configuration
2. Target Group and healthy targets
3. Application Load Balancer configuration
4. Auto Scaling Group configuration
5. Static website opened through the ALB DNS name
6. Auto Scaling activity history and scaling results, if tested

## 🔐 Security Considerations

- Restrict inbound access using Security Groups.
- Allow web traffic to EC2 instances from the ALB security group where possible.
- Avoid exposing SSH access to the entire internet.
- Do not commit AWS credentials, private keys, or other secrets to GitHub.

## 📚 Learning Outcomes

- Understanding EC2 instance provisioning and launch templates
- Configuring Application Load Balancers and target groups
- Understanding health checks and traffic distribution
- Configuring Auto Scaling Groups
- Learning AWS networking and security fundamentals
- Documenting cloud projects using GitHub

## 👨‍💻 Project Information

**Project Category:** AWS Cloud / Infrastructure

**Deployment Method:** AWS Management Console

**Website Type:** Static Website

**Web Server:** Nginx Server, depending on the deployed configuration
