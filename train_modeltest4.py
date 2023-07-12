# -*- coding: utf-8 -*-
"""Train_modeltest4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CdI8ujOU9EsME4Y7NLHKo-vMPs6aIzuS
"""

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

def load_data(file_path):
    """
    Load data from a CSV file into a pandas DataFrame.

    Parameters:
    file_path (str): Path to the CSV file.

    Returns:
    df (pd.DataFrame): Loaded DataFrame.
    """
    df = pd.read_csv(file_path)
    return df

def train_model(df):
    """
    Train a Random Forest Regressor model using the provided DataFrame.

    Parameters:
    df (pd.DataFrame): DataFrame containing the training data.

    Returns:
    model: Trained machine learning model.
    """
    # Assuming the target variable is 'total'
    X = df[['unit_price', 'quantity', 'payment_type']]  # Select relevant columns as features
    y = df['total']  # Set 'total' as the target variable

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = RandomForestRegressor()
    model.fit(X_train, y_train)

    return model

def evaluate_model(model, X_test, y_test):
    """
    Evaluate the trained model on the provided test data and output performance metrics.

    Parameters:
    model: Trained machine learning model.
    X_test (pd.DataFrame): Testing features.
    y_test (pd.Series): Testing target variable.

    Returns:
    None
    """
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    print(f"Mean Absolute Error: {mae}")

def main():
    # Assuming the CSV file is located in the same directory
    file_path = 'data.csv'

    # Load the data
    df = load_data(file_path)

    # Train the model
    model = train_model(df)

    # Evaluate the model
    X_test = df[['unit_price', 'quantity', 'payment_type']]  # Assuming the same features as during training
    y_test = df['total']  # Assuming the same target variable as during training
    evaluate_model(model, X_test, y_test)

if __name__ == '__main__':
    main()