"""
Module: inventory.py
Description: Inventory dataset for Configuration Status Accounting (CSA).
Author: Solomon Azowenu (2024/A/SENG/0146)
"""
from typing import List, Dict, Any

# Inventory list containing item_name, quantity, and price
inventory_data: List[Dict[str, Any]] = [
    {"item_name": "Laptop Stand", "quantity": 15, "price": 12000.0},
    {"item_name": "Mechanical Keyboard", "quantity": 8, "price": 35000.0},
    {"item_name": "USB-C Hub", "quantity": 25, "price": 8500.0},
    {"item_name": "27-inch Monitor", "quantity": 5, "price": 145000.0}
]