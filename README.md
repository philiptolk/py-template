# Reopen in devcontainer
This is meant to be run in the [devcontainer](https://code.visualstudio.com/docs/remote/containers) provided

Uses [localstack](https://docs.localstack.cloud/overview/) and [docker-compose](https://github.com/philiptolk/py-vscode-template/blob/main/.devcontainer/docker-compose.yml)

# Terraform
```
cd terraform
terraform init
terraform plan
terraform apply
```
# Local
create .env file<br>
add is_localstack=true
