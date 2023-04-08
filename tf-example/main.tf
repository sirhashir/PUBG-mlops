provider "aws" {
  region = "eu-north-1a"
}

resource "aws_instance" "example" {
  ami           = "ami-0fb653ca2d3203ac1"
  instance_type = "t2.micro"

  tags = {
    Name = "var.ec2_name"
  }
}
