import numpy as np
import pandas as pd

# Parameters
base_price = 100  # Base price for the lowest ticket sales
max_price = 500   # Maximum ticket price
num_points = 10000  # Number of data points
min_sales = 10  # Minimum number of tickets sold

# Generate random ticket prices within the specified range
np.random.seed(42)
prices = np.random.uniform(low=base_price, high=max_price, size=num_points)

# Round ticket prices to the nearest cent
prices = np.round(prices, 2)

# Generate ticket sales based on an inverse relationship with some randomness
# Formula: sales = (base_sales * (max_price / price)) * random_factor
base_sales = 1000  # Base number of tickets sold when price is minimum
sales = (base_sales * (max_price / prices)) * np.random.uniform(0.8, 1.2, size=num_points)
sales = np.maximum(sales, min_sales)  # Ensure sales are realistic

# Create a DataFrame
data = pd.DataFrame({
    'ticket_price': prices,
    'number_of_tickets_sold': sales.astype(int)
})

# Save to a CSV file
csv_filename = 'mock_ticket_sales_with_price.csv'
data.to_csv(csv_filename, index=False)

# Print confirmation
print(f'Mock data generated and saved to {csv_filename}')
print(f'Number of rows in the CSV file: {len(data)}')