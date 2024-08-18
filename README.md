# Sales Order Data Processor
```python_tool.py```

This tool processes sales order data, allowing you to calculate total sales by region, filter orders by item type, and identify the top-performing sales representative.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Sakshee5/AIPI510-PythonTool-Assignment.git
```

2. Navigate to the project directory and set up a virtual environment
For Windows:

```bash
py -m venv myenv
myenv\Scripts\activate
```  

For Unix-based systems (Linux/macOS):

```
python3 -m venv myenv
source myenv/bin/activate
```

3. Install Dependencies

```
pip install -r requirements.txt
```

## Usage
Run the tool with the following command:
    
    py python_tool.py --input data/sales_order_data.xlsx --output data/results.xlsx --item Pencil

where

    --input: Path to the input Excel file.
    --output: Path to the output Excel file.
    --item: (Optional) Filter orders by item type.

## Testing
Run the unit tests using:

    pytest

## Troubleshooting
1. Ensure that the input file exists and is in the correct format (.csv or .xlsx).
2. Verify that the paths provided for input and output are correct.