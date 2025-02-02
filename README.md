# Real-Time Dashboard (Power BI)

## Overview
This project demonstrates the implementation of a real-time Power BI dashboard that updates dynamically using streaming data. The dashboard is connected to a simulated API feed to visualize sales data, including regional breakdowns and time-series trends.

## Problem Statement
In modern business environments, real-time data visualization is critical for informed decision-making. Traditional dashboards rely on batch processing, which introduces latency. This project aims to create a real-time dashboard in Power BI using a streaming dataset, ensuring up-to-the-minute analytics and insights.

## Components
The solution consists of the following key components:
- **Power BI Service:** Used for creating and hosting the real-time dashboard.
- **Streaming Dataset:** A live data feed simulating real-time sales updates.
- **API Integration:** A simulated API source generating sales transactions.
- **Power BI Visualizations:** Includes key performance indicators (KPIs), bar charts by region, and a time-series line chart.

## Features
- **Real-Time Data Updates:** Dashboard refreshes dynamically as new data arrives.
- **Interactive Visuals:** Users can explore sales performance by region and over time.
- **KPI Metrics:** Displays aggregated sales figures in real time.
- **Scalability:** Can integrate with actual streaming APIs for production use.

## Setup Instructions
### 1. Create a Streaming Dataset in Power BI
1. Navigate to **Power BI Service**.
2. Click on **Workspaces** > **My Workspace**.
3. Select **Create** > **Streaming Dataset**.
4. Choose **API** as the data source and define the schema (e.g., Timestamp, Region, Sales).
5. Enable **Historic Data Analysis** for better visualization.

### 2. Connect to a Streaming Data Source
- Use a Python script to generate simulated sales data.
- Example Python script using REST API:
  ```python
  import requests
  import time
  import random
  from datetime import datetime

  PUSH_URL ="https://api.powerbi.com/beta/950737a4-2947-46ce-9c53-4728f01fd598/datasets/51853dc9-0e6e-4705-835e-68cdb7a7d0d3/rows?experience=power-bi&key=ffqvqF5WVx%2ByrRVG1flt2RBxL%2F2jkf05Xtc7ne7KCPbYEo4tLNBm%2FLiP1on0fNXDkUQ3IIbT5KQ%2BnjBW9f5Fsw%3D%3D"


  def generate_data():
    regions = ["North", "South", "East", "West"]
    products = ["Product A", "Product B", "Product C", "Product D"]
    return {
        "Region": random.choice(regions),
        "Product": random.choice(products),
        "Sales": round(random.uniform(100, 1000), 2),
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

  def send_data():
    headers = {"Content-Type": "application/json"}
    while True:
        data = [generate_data()]  
        response = requests.post(PUSH_URL, json=data, headers=headers)
        if response.status_code == 200:
            print(f"Data sent: {data}")
        else:
            print(f"Failed to send data: {response.status_code}, {response.text}")
        time.sleep(5)

  if __name__ == "__main__":
    print("Starting data feed...")
    send_data()


### 3. Build the Power BI Dashboard
1. Open **Power BI Service** and create a new dashboard.
2. Click **Add Tile** > **Custom Streaming Data**.
3. Select the previously created streaming dataset.
4. Add **KPI**, **Bar Chart**, and **Line Chart** visuals.
5. Arrange and format visuals for clarity.

### 4. Deploy and Monitor
- Share the dashboard with stakeholders.
- Subscribe to alerts for anomalies in real-time sales.


## Conclusion
This project successfully sets up a real-time Power BI dashboard using streaming data. The approach ensures businesses can monitor live sales metrics, enabling data-driven decision-making.

