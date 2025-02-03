output "storage_account_primary_access_key" {
  value = data.azurerm_storage_account.example.primary_connection_string
  sensitive = true
}