variable "ec2_name" {
  type    = string
  default = "my-ec2-instance"
}

variable "ec2_host" {
  description = "EC2 instance public IP address"
  type        = string
  default     = "123.45.67.89"
}

variable "ec2_user" {
  description = "Username to use when connecting to the EC2 instance"
  type        = string
  default     = "ec2-user"
}