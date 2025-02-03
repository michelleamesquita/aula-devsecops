terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = "=3.97.1"
    }
  }
}

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "example" {
  name     = "mi-test3"
  location = "East US"
}

resource "azurerm_storage_account" "example" {
  name                     = "michelleamesquita2"
  resource_group_name      = azurerm_resource_group.example.name
  location                 = azurerm_resource_group.example.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_storage_container" "example" {
  name                  = "content"
  storage_account_name  = azurerm_storage_account.example.name
  container_access_type = "container"
}

data "azurerm_storage_account" "example" {
  name                = azurerm_storage_account.example.name
  resource_group_name = azurerm_resource_group.example.name
}


resource "azurerm_storage_blob" "image" {
  name                   = "pituco.jpeg"
  storage_account_name   = azurerm_storage_account.example.name
  storage_container_name = azurerm_storage_container.example.name
  type                   = "Block"
  source                 = "puppy.jpeg"
  content_type           = "image/jpeg"
}


