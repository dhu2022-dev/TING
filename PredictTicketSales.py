import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Load the data
data = pd.read_csv('mock_ticket_sales_with_price.csv')

# Prepare the features and target variable
X = data[['ticket_price']].values
y = data['number_of_tickets_sold'].values

# Split the data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize models
models = {
    'Linear Regression': LinearRegression(),
    'Decision Tree': DecisionTreeRegressor(),
    'Random Forest': RandomForestRegressor(),
    'Gradient Boosting': GradientBoostingRegressor(),
    'Neural Network': Sequential([
        Dense(64, activation='relu', input_shape=(1,)),
        Dense(32, activation='relu'),
        Dense(1)
    ])
}

# Compile the neural network model
models['Neural Network'].compile(optimizer='adam', loss='mean_squared_error')

# Train and evaluate models
for name, model in models.items():
    print(f"\nTraining {name}...")
    if name != 'Neural Network':
        model.fit(X_train, y_train)
        y_pred = model.predict(X_val)
        mse = mean_squared_error(y_val, y_pred)
        print(f"{name} Mean Squared Error: {mse:.2f}")
    else:
        # Neural Network needs different handling
        model.fit(X_train, y_train, epochs=10, batch_size=32, verbose=1)
        y_pred = model.predict(X_val)
        mse = mean_squared_error(y_val, y_pred)
        print(f"{name} Mean Squared Error: {mse:.2f}")

print("\nModel training and evaluation completed.")
