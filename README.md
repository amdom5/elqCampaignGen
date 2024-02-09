# Eloqua Campaign Creator Script

This Python script facilitates the creation of Eloqua campaigns in bulk by sending POST requests to the Eloqua API. The script reads campaign data from a CSV file, where each row corresponds to a campaign, and maps CSV columns to API parameters.

## Prerequisites

- Python 3.x
- `requests` library (`pip install requests`)

## Configuration

1. Open the script (`eloqua_campaign_creator.py`) in a text editor.
2. Replace the following placeholders with your actual Eloqua credentials and information:
   - `your_pod_number`: Update with your Eloqua pod number.
   - `your_company_name`: Update with your Eloqua company name.
   - `your_username`: Update with your Eloqua username.
   - `your_password`: Update with your Eloqua password.
   - `path/to/your/csv/file.csv`: Update with the path to your CSV file.

## Usage

1. Ensure the Eloqua account has the necessary permissions access the API and delete syncs.
2. Ensure Python and the `requests` library are installed.
3. Update the script with your Eloqua configuration.
4. Open a terminal and navigate to the script's directory.
5. Run the script by uncommenting the line `# create_bulk_campaigns(csv_file_path)` and executing the script.

Note: Before running the script, make sure to update the 'elqPod', 'elqCompanyName', 'elqUsername', and 'elqPassword' variables with your actual Eloqua credentials.
   
```bash
python eloqua_campaign_creator.py
```

## CSV Format

The CSV file should have the following columns, mapping to Eloqua API parameters:

- `name`: Campaign name
- `description`: Campaign description
- `region`: Campaign region
- `product`: Campaign product
- `budgetedCost`: Budgeted cost for the campaign
