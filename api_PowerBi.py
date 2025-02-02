import requests
import time
import random
from datetime import datetime

# Replace this with your Power BI Push URL
PUSH_URL ="https://api.powerbi.com/beta/950737a4-2947-46ce-9c53-4728f01fd598/datasets/51853dc9-0e6e-4705-835e-68cdb7a7d0d3/rows?experience=power-bi&key=ffqvqF5WVx%2ByrRVG1flt2RBxL%2F2jkf05Xtc7ne7KCPbYEo4tLNBm%2FLiP1on0fNXDkUQ3IIbT5KQ%2BnjBW9f5Fsw%3D%3D"


# Function to generate random data
def generate_data():
    regions = ["North", "South", "East", "West"]
    products = ["Product A", "Product B", "Product C", "Product D"]
    return {
        "Region": random.choice(regions),
        "Product": random.choice(products),
        "Sales": round(random.uniform(100, 1000), 2),
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

# Function to send data to Power BI
def send_data():
    headers = {"Content-Type": "application/json"}
    while True:
        data = [generate_data()]  # Power BI expects a list of rows
        response = requests.post(PUSH_URL, json=data, headers=headers)
        if response.status_code == 200:
            print(f"Data sent: {data}")
        else:
            print(f"Failed to send data: {response.status_code}, {response.text}")
        time.sleep(5)  # Wait for 5 seconds before sending the next data point

# Run the script
if __name__ == "__main__":
    print("Starting data feed...")
    send_data()
