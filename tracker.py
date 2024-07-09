# Import necessary libraries
import numpy as np
import pandas as pd

# Sample data and thresholds for recommendations
heart_rate_threshold = 100  # beats per minute
steps_threshold = 8000  # steps per day
sleep_hours_threshold = 7  # hours per night
calories_burned_threshold = 1700  # calories per day

# Function to analyze data and make recommendations
def analyze_data(age, heart_rate, steps, sleep_hours, calories_burned):
    recommendations = []
    
    if heart_rate > heart_rate_threshold:
        recommendations.append("Your heart rate is above the normal range. Consider relaxing or consulting a doctor if it persists.")
    elif heart_rate < 60:
        recommendations.append("Your heart rate is below the normal range. Consider exercising more or consulting a doctor")
    else:
        recommendations.append("Your heart rate is within the normal range. Keep up the good work!")
        
    
    if steps < steps_threshold:
        recommendations.append("You have not met your steps goal today. Try to be more active.")
    elif steps > 20000:
        recommendations.append("You have walked too much today. Take some rest!")
    else:
        recommendations.append("Great job meeting your steps goal today!")
        
    
    
    if sleep_hours < sleep_hours_threshold:
        recommendations.append("You didn't get enough sleep last night. Aim for at least 7 hours of sleep.")
    elif sleep_hours > 10:
        recommendations.append("You got too much sleep last night. Try to get back to a healthy routine!")
    else:
        recommendations.append("You had a good amount of sleep last night. Keep it up!")
    
    
    if calories_burned < calories_burned_threshold:
        recommendations.append("You have not burned enough calories today. Consider engaging in more physical activities.")
    elif calories_burned > 2700:
        recommendations.append("You have burned a lot of calories today! Increase your calories consumption accordingly.")
    else:
        recommendations.append("You have burned a good amount of calories today. Well done!")
    
    
    if age >= 50 and heart_rate > 90:
        recommendations.append("As you are above 50 years old, a high heart rate can be concerning. Monitor it closely and consult a doctor if needed.")
    
    # Calculate health and fitness percentage (example logic)
    health_percentage = 100
    fitness_percentage = 100
    
    if heart_rate > heart_rate_threshold:
        health_percentage -= 10
    if heart_rate < 60:
        health_percentage -= 10
    if steps < steps_threshold:
        fitness_percentage -= 20
    if steps > 20000:
        fitness_percentage -= 20
    if sleep_hours < sleep_hours_threshold:
        health_percentage -= 10
    if sleep_hours > 10:
        health_percentage -= 10
    if calories_burned < calories_burned_threshold:
        fitness_percentage -= 20
    if calories_burned > 2700:
        fitness_percentage -= 20
    if age >= 50 and heart_rate > 90:
        health_percentage -= 10

    return recommendations, health_percentage, fitness_percentage
