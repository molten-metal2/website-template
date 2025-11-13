variable "bucket_name" {
  description = "Name of the S3 bucket for website hosting"
  type        = string
  default     = "politicnz-website"
}

variable "aws_region" {
  description = "AWS region for resources"
  type        = string
  default     = "ap-southeast-2"
}

