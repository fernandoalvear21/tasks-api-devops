output "resource_group_id" {
  description = "ID of the resource group"
  value       = azurerm_resource_group.rg.id
}

output "public_ip_address" {
  description = "La dirección IP pública de la máquina virtual"
  value       = azurerm_public_ip.pip.ip_address
}

output "vm_name" {
  description = "Nombre de la máquina virtual"
  value       = azurerm_linux_virtual_machine.vm.name
}

output "app_url" {
  description = "URL de la aplicación desplegada"
  value       = "http://${azurerm_public_ip.pip.ip_address}:8000"
}