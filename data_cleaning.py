import pandas as pd

# 1. Load the dataset from the data folder
print("Loading dataset...")
df = pd.read_csv('data/DataCoSupplyChainDataset.csv', encoding='latin-1')

# 2. Select only the columns relevant to Inventory, Supply Chain, and Sales
columns_to_keep = [
    'Type', 'Days for shipping (real)', 'Days for shipment (scheduled)', 
    'Delivery Status', 'Late_delivery_risk', 'Category Name', 
    'Customer Segment', 'Order City', 'Order Country', 
    'Order Item Discount', 'Order Item Product Price', 
    'Order Item Quantity', 'Sales', 'Order Status', 'Shipping Mode','Order Profit Per Order'
]
df_clean = df[columns_to_keep].copy()

# 3. Handle Missing Values & Rename Columns for SQL/Tableau readability
print("Cleaning data...")
df_clean.dropna(inplace=True)
df_clean.columns = df_clean.columns.str.replace(' ', '_').str.lower()

# 4. Feature Engineering: Create a column to flag if an order was delayed
df_clean['is_delayed'] = df_clean.apply(
    lambda row: 1 if row['days_for_shipping_(real)'] > row['days_for_shipment_(scheduled)'] else 0, 
    axis=1
)

# 5. Export the clean dataset back to the data folder
output_path = 'data/cleaned_supply_chain.csv'
df_clean.to_csv(output_path, index=False)
print(f"Data successfully cleaned and saved to {output_path}!")