"""
Inventory Calculation App
"""
from inventory import inventory_data
from utils.helpers import highest_stock_item, lowest_stock_item

def calculate_total_value(items) -> float:
    if not items:
        return 0.0
    return sum(item["quantity"] * item["price"] for item in items)

def main():
    print("--- CSA INVENTORY AUDIT ---")
    total_val = calculate_total_value(inventory_data)
    print(f"Total Stock Valuation: NGN {total_val:,.2f}")
    
    highest = highest_stock_item(inventory_data)
    lowest = lowest_stock_item(inventory_data)
    
    if highest:
        print(f"Max Stock Item: {highest['item_name']} ({highest['quantity']} units)")
    if lowest:
        print(f"Min Stock Item: {lowest['item_name']} ({lowest['quantity']} units)")

if __name__ == "__main__":
    main()