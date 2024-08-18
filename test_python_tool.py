import pytest
import pandas as pd
from python_tool import calculate_total_sales_by_region, filter_orders_by_item, top_sales_rep, process_sales_data

@pytest.fixture
def sample_data():
    """Fixture to provide sample data for testing."""
    data = {
        'OrderDate': ['1-6-21', '1-23-21', '2-9-21'],
        'Region': ['East', 'Central', 'Central'],
        'Rep': ['Jones', 'Kivell', 'Jardine'],
        'Item': ['Pencil', 'Binder', 'Pencil'],
        'Units': [95, 50, 36],
        'Unit Cost': [1.99, 19.99, 4.99],
        'Total': [189.05, 999.50, 179.64]
    }
    return pd.DataFrame(data)

def test_calculate_total_sales_by_region(sample_data):
    """Test the calculation of total sales by region."""
    result = calculate_total_sales_by_region(sample_data)
    expected = pd.DataFrame({
        'Region': ['Central', 'East'],
        'Total': [1179.14, 189.05]
    })
    pd.testing.assert_frame_equal(result, expected)

def test_filter_orders_by_item(sample_data):
    """Test filtering orders by a specific item."""
    result = filter_orders_by_item(sample_data, 'Pencil')
    assert len(result) == 2
    assert result.iloc[0]['Rep'] == 'Jones'

def test_top_sales_rep(sample_data):
    """Test finding the top sales representative by total sales."""
    result = top_sales_rep(sample_data)
    assert result == 'Kivell'

def test_invalid_file_format(tmp_path):
    """Test handling an invalid file format."""
    invalid_file = tmp_path / "invalid_file.txt"
    invalid_file.write_text("This is not a valid file format.")
    
    with pytest.raises(ValueError, match="Unsupported file format. Please provide a .csv or .xlsx file."):
        process_sales_data(invalid_file, tmp_path / "output.xlsx")


def test_csv_format(sample_data, tmp_path):
    """Test processing a CSV file format."""
    csv_file = tmp_path / "data.csv"
    sample_data.to_csv(csv_file, index=False)
    
    output_file = tmp_path / "output.xlsx"
    process_sales_data(csv_file, output_file)
    
    # Check that the output file has been created and contains expected sheets
    with pd.ExcelFile(output_file) as xls:
        assert 'Total Sales by Region' in xls.sheet_names
        assert 'Filtered Orders' in xls.sheet_names
        assert 'Top Sales Representative' in xls.sheet_names

def test_xlsx_format(sample_data, tmp_path):
    """Test processing an Excel file format."""
    xlsx_file = tmp_path / "data.xlsx"
    sample_data.to_excel(xlsx_file, index=False)
    
    output_file = tmp_path / "output.xlsx"
    process_sales_data(xlsx_file, output_file)
    
    # Check that the output file has been created and contains expected sheets
    with pd.ExcelFile(output_file) as xls:
        assert 'Total Sales by Region' in xls.sheet_names
        assert 'Filtered Orders' in xls.sheet_names
        assert 'Top Sales Representative' in xls.sheet_names
