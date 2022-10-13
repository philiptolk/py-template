locals {
  use_localstack = (terraform.workspace == "localstack")

  aws_settings = (
    local.use_localstack ?
    {
      access_key                  = "test"
      secret_key                  = "test"
      region                      = local.aws_region
      # region                      = "us-east-1"
      s3_use_path_style           = false
      skip_credentials_validation = true
      skip_metadata_api_check     = true
      skip_requesting_account_id  = true

      override_endpoint = "http://localstack:4566"
    } :
    {
      region     = local.aws_region
      access_key = null
      secret_key = null
      
      skip_credentials_validation = null
      skip_metadata_api_check     = null
      skip_requesting_account_id  = null

      override_endpoint = null
    }
  )
}

provider "aws" {
  region     = local.aws_settings.region
  access_key = local.aws_settings.access_key
  secret_key = local.aws_settings.secret_key

  skip_credentials_validation = local.aws_settings.skip_credentials_validation
  skip_metadata_api_check     = local.aws_settings.skip_metadata_api_check
  skip_requesting_account_id  = local.aws_settings.skip_requesting_account_id

  dynamic "endpoints" {
    for_each = local.aws_settings.override_endpoint[*]
    content {
      apigateway     = endpoints.value
      apigatewayv2   = endpoints.value
      cloudformation = endpoints.value
      cloudwatch     = endpoints.value
      dynamodb       = endpoints.value
      ec2            = endpoints.value
      es             = endpoints.value
      elasticache    = endpoints.value
      firehose       = endpoints.value
      iam            = endpoints.value
      kinesis        = endpoints.value
      lambda         = endpoints.value
      rds            = endpoints.value
      redshift       = endpoints.value
      route53        = endpoints.value
      s3             = "http://s3.localstack.localstack.cloud:4566"
      secretsmanager = endpoints.value
      ses            = endpoints.value
      sns            = endpoints.value
      sqs            = endpoints.value
      ssm            = endpoints.value
      stepfunctions  = endpoints.value
      sts            = endpoints.value    
    }
  }
}