#wind_prediction_app.py

import streamlit as st
import pandas as pd
import numpy as np
 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
import matplotlib.pyplot as plt
import pickle
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, explained_variance_score

def load_weather_dataset():
    # Load your weather dataset from a CSV file
    df = pd.read_csv('Future_Implementations/new_adilabad.csv')  # Update the path to your dataset
    return df

def get_model(algorithm):
    if algorithm == 'Linear Regression':
        model = LinearRegression()
    elif algorithm == 'Random Forest Regressor':
        model = RandomForestRegressor(n_estimators=100, random_state=42)
    elif algorithm == 'Support Vector Regressor':
        model = SVR()
    return model

def train_model(df, algorithm='Linear Regression'):
    # Function to train a regression model
    X = df[['avg_temp', 'avg_humidity']]
    y = df['avg_wind_speed']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = get_model(algorithm)
    model.fit(X_train, y_train)
    evaluate_model(model, X_test, y_test)

    # Display feature importances for Random Forest Regressor
    if algorithm == 'Random Forest Regressor':
        feature_importances = pd.DataFrame({'Feature': X.columns, 'Importance': model.feature_importances_})
        feature_importances = feature_importances.sort_values(by='Importance', ascending=False)
        st.subheader('Feature Importances:')
        st.write(feature_importances)

    # Save the model to a pickle file
    with open(f'{algorithm.lower().replace(" ", "_")}_model.pkl', 'wb') as model_file:
        pickle.dump(model, model_file)

    return model

def evaluate_model(model, X_test, y_test):
    # Evaluate the model
    y_pred = model.predict(X_test)

    # Calculate metrics
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    explained_var = explained_variance_score(y_test, y_pred)

    # Calculate Adjusted R-squared
    n = len(y_test)
    k = X_test.shape[1]
    adj_r2 = 1 - ((1 - r2) * (n - 1) / (n - k - 1))

    # Display metrics
    st.subheader('Model Evaluation Metrics:')
    st.write(f'Mean Squared Error (MSE): {mse:.2f}')
    st.write(f'Root Mean Squared Error (RMSE): {rmse:.2f}')
    st.write(f'Mean Absolute Error (MAE): {mae:.2f}')
    st.write(f'R-squared (R²): {r2:.4f}')
    st.write(f'Adjusted R-squared: {adj_r2:.4f}')
    st.write(f'Explained Variance Score: {explained_var:.4f}')

    # Display scatter plot and residual plot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
    ax1.scatter(y_test, y_pred, alpha=0.7)
    ax1.set_title('Actual vs. Predicted')
    ax1.set_xlabel('Actual')
    ax1.set_ylabel('Predicted')

    residuals = y_test - y_pred
    ax2.scatter(y_test, residuals, alpha=0.7)
    ax2.set_title('Residuals')
    ax2.set_xlabel('Actual')
    ax2.set_ylabel('Residuals')
    st.pyplot(fig)

# Function to predict wind speed using the trained model
def predict_wind_speed(model, avg_temp, avg_humidity):
    input_data = [[avg_temp, avg_humidity]]
    predicted_wind_speed = model.predict(input_data)
    return predicted_wind_speed[0]

# Main Streamlit app
def main():
    st.title('Wind Speed Prediction App (Weather Data)')

    # Load weather dataset
    df = load_weather_dataset()

    # Select regression algorithm
    algorithm = st.sidebar.selectbox('Select Regression Algorithm',
                                     ['Linear Regression', 'Random Forest Regressor', 'Support Vector Regressor'])

    # Train the model
    model = train_model(df, algorithm)

    # Streamlit UI
    st.sidebar.header('User Input Features')
    avg_temp = st.sidebar.slider('Average Temperature (C)', df['avg_temp'].min(), df['avg_temp'].max(),
                                 df['avg_temp'].mean())
    avg_humidity = st.sidebar.slider('Average Humidity', df['avg_humidity'].min(), df['avg_humidity'].max(),
                                     df['avg_humidity'].mean())

    # Predict wind speed
    if st.sidebar.button('Predict'):
        predicted_wind_speed = predict_wind_speed(model, avg_temp, avg_humidity)
        st.sidebar.success(f'Predicted Wind Speed: {predicted_wind_speed:.2f} km/h')
        print(f'Predicted Wind Speed: {predicted_wind_speed:.2f} km/h')

if __name__ == '__main__':
    main()
