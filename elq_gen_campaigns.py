import requests
import csv
import base64

# Placeholder for the Pod Number
elqPod = "your_pod_number"  # Update this with the actual pod number

# Eloqua API credentials and base URL
elqUrl = f"https://secure.p{elqPod}.eloqua.com/api/REST/2.0/assets/campaign"
elqCompanyName = "your_company_name"
elqUsername = "your_username"
elqPassword = "your_password"

# Function to create a campaign
def create_campaign(name, description, region, product, budgeted_cost):
    url = elqUrl
    headers = {
        "Authorization": f"Basic {base64.b64encode(f'{elqCompanyName}\\{elqUsername}:{elqPassword}'.encode()).decode()}",
        "Content-Type": "application/json",
    }

    # Build the campaign data payload
    campaign_data = {
        "name": name,
        "description": description,
        "region": region,
        "product": product,
        "budgetedCost": budgeted_cost,
    }

    response = requests.post(url, headers=headers, json=campaign_data)

    if response.status_code == 201:
        print(f"Campaign '{name}' created successfully.")
    else:
        print(f"Error creating campaign '{name}'. Status code: {response.status_code}, Response: {response.text}")

# Function to read campaign data from CSV and create each campaign
def create_bulk_campaigns(csv_file_path):
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            create_campaign(
                row['name'],
                row['description'],
                row['region'],
                row['product'],
                row['budgetedCost']
            )

# Example usage
if __name__ == "__main__":
    # Update the path to your CSV file
    csv_file_path = "path/to/your/csv/file.csv"
    
    # Update the pod number before running the script
    print("Before running the script, please update the 'elqPod' variable with your actual pod number.")
    
    # Update the Eloqua API credentials before running the script
    print("Please update the 'elqCompanyName', 'elqUsername', and 'elqPassword' variables with your actual Eloqua credentials.")
    
    # Uncomment the line below to execute the script
    # elq_gen_campaigns(csv_file_path)
