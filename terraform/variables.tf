variable "resource_group_name" {
  description = "Name of the resource group"
  type        = string
  default     = "devops-project001-rg"
}

variable "location" {
  description = "Azure region"
  type        = string
  default     = "eastus"
}

variable "tags" {
  description = "Tags for resources"
  type        = map(string)
  default     = {
    Environment = "Development"
    Project     = "DevOps-Project001"
  }
}

variable "vm_username" {
  description = "Username for the VM"
  type        = string
  default     = "azureuser"
}

variable "vm_password" {
  description = "Password for the VM"
  type        = string
  sensitive   = true
}