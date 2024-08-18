# Required Imports
import pandas as pd   # library for csv manipulation
import argparse       # library to run the script as a Command Line Tool
import os

# Helper Methods
def calculate_total_sales_by_region(df):
    """To calculate total sales by region."""
    return df.groupby('Region')['Total'].sum().reset_index()

def filter_orders_by_item(df, item):
    """Filter orders by item type."""
    return df[df['Item'] == item]

def top_sales_rep(df):
    """Function to find the top-performing sales representative by total sales."""
    return df.groupby('Rep')['Total'].sum().idxmax()

# Main Method
def process_sales_data(input_file_path, output_file_path, item=None):
    """Function to read, process and save a sample excel file"""
    # Read the CSV/Excel file based on the extension
    ext = os.path.splitext(input_file_path)[1].lower()

    # handle exceptions that might occur during file reading
    # For example, catching FileNotFoundError or PermissionError.
    try:
        if ext == '.xlsx':
            df = pd.read_excel(input_file_path)
        elif ext == '.csv':
            df = pd.read_csv(input_file_path)
        else:
            raise ValueError("Unsupported file format. Please provide a .csv or .xlsx file.")
    except ValueError as e:
        raise ValueError(f"Error reading file: {e}")

    # Calculate total sales by region
    total_sales_by_region = calculate_total_sales_by_region(df)
    
    # Filter by item if specified
    if item:
        df = filter_orders_by_item(df, item)
    
    # Find top sales representative
    top_rep = top_sales_rep(df)
    
    # Write the results to a new CSV file
    with pd.ExcelWriter(output_file_path) as writer:
        total_sales_by_region.to_excel(writer, sheet_name='Total Sales by Region', index=False)
        df.to_excel(writer, sheet_name='Filtered Orders', index=False)
        pd.DataFrame({'Top Sales Rep': [top_rep]}).to_excel(writer, sheet_name='Top Sales Representative', index=False)

    print(f"Processed data saved to {output_file_path}")

def main():
    # using argparse library to run script as a Command Line Tool
    parser = argparse.ArgumentParser(description="Process sales order data.")
    parser.add_argument('--input', required=True, help="Relative path to excel or csv file")
    parser.add_argument('--output', required=True, help="Relative path to output excel file")
    parser.add_argument('--item', help="Filter orders by item type")
    args = parser.parse_args()
    
    process_sales_data(args.input, args.output, args.item)

if __name__ == "__main__":
    main()
