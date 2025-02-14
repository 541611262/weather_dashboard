# weather_plots.py

import matplotlib.pyplot as plt
import pandas as pd

# Function to create the forecast card (the panel showing max/min temperature and weather)
def create_forecast_card(ax, date, max_temp, min_temp, weather):
    # Set axis properties
    ax.axis('off')  # Hide the axis
    ax.text(0.5, 0.9, f"Weather for {date}", ha='center', va='center', fontsize=14, fontweight='bold')
    ax.text(0.5, 0.7, f"Max Temp: {max_temp}°C", ha='center', va='center', fontsize=12)
    ax.text(0.5, 0.5, f"Min Temp: {min_temp}°C", ha='center', va='center', fontsize=12)
    ax.text(0.5, 0.3, f"Weather: {weather}", ha='center', va='center', fontsize=12)
    
    # Adjust text positions if needed
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

# Function to plot the scatter plot of temperature vs wind speed
def plot_scatter(df, x_column, y_column, ax, title):
    # Scatter plot of temperature vs wind speed
    ax.scatter(df[x_column], df[y_column], c='b', alpha=0.5)
    ax.set_title(title)
    ax.set_xlabel(f"{x_column}")
    ax.set_ylabel(f"{y_column}")
    
    # Display the grid
    ax.grid(True)

# Function to plot the min/max temperature for the entire period
def plot_min_max(df, date_column, min_column, max_column, ax, title):
    # Plot min/max temperature
    ax.plot(df[date_column], df[min_column], label="Min Temp (°C)", color='blue', marker='o')
    ax.plot(df[date_column], df[max_column], label="Max Temp (°C)", color='red', marker='o')
    
    ax.set_title(title)
    ax.set_xlabel("Date")
    ax.set_ylabel("Temperature (°C)")
    
    # Rotate the x-axis labels for better visibility
    ax.tick_params(axis='x', rotation=45)
    
    # Display the legend
    ax.legend()
    
    # Show grid lines
    ax.grid(True)

# Function to plot the hourly temperature change
def plot_hourly_temp(df, ax, title="Hourly Temperature Variation"):
    # Plot the temperature variation across hours
    ax.plot(df['Hour'], df['Temperature (C)'], label="Temperature (°C)", color='orange')
    ax.set_title(title)
    ax.set_xlabel("Hour")
    ax.set_ylabel("Temperature (°C)")
    
    # Display grid and legend
    ax.grid(True)
    ax.legend()

# Function to plot hourly wind speed variation
def plot_hourly_wind(df, ax, title="Hourly Wind Speed Variation"):
    # Plot wind speed variation across hours
    ax.plot(df['Hour'], df['Wind Speed (m/s)'], label="Wind Speed (m/s)", color='green')
    ax.set_title(title)
    ax.set_xlabel("Hour")
    ax.set_ylabel("Wind Speed (m/s)")
    
    # Display grid and legend
    ax.grid(True)
    ax.legend()

# Function to plot the daily temperature variation
def plot_daily_temp(df, ax, title="Daily Temperature Variation"):
    # Plot the daily temperature variation
    ax.plot(df['Date'], df['Temperature (C)'], label="Temperature (°C)", color='purple')
    ax.set_title(title)
    ax.set_xlabel("Date")
    ax.set_ylabel("Temperature (°C)")
    
    # Rotate the x-axis labels for better visibility
    ax.tick_params(axis='x', rotation=45)
    
    # Display grid and legend
    ax.grid(True)
    ax.legend()
