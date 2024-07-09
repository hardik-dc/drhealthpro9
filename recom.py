from flask import Flask, render_template, request
from geopy.geocoders import Nominatim
from geopy.distance import distance
import pandas as pd

app = Flask(__name__)

# Load hospital data
hospital_data = pd.read_csv('delhi_hospitals.csv')

# Function to get user's location
def get_user_location(address):
    locator = Nominatim(user_agent="hospital_recommendation_app")
    try:
        location = locator.geocode(address)
        return location
    except Exception as e:
        print(f"Error: {e}")
        return None

# Function to recommend hospitals based on user's location
def recommend_hospitals(user_location, hospital_data, num_recommendations=5):
    hospitals = []
    recommended_hospitals = set()  # To keep track of recommended hospitals
    for idx, row in hospital_data.iterrows():
        hospital_location = (row['latitude'], row['longitude'])
        dist = distance(user_location, hospital_location).km
        hospitals.append((row['name'], row['appointment_website'], row['contact_number'], dist))
    
    # Sort hospitals by distance
    hospitals.sort(key=lambda x: x[3])
    
    # Filter unique recommendations
    recommendations = []
    for hospital in hospitals:
        if hospital[0] not in recommended_hospitals:
            recommended_hospitals.add(hospital[0])
            recommendations.append(hospital)
            if len(recommendations) == num_recommendations:
                break
    
    return recommendations

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/appointment', methods=['GET', 'POST'])
def appointment():
    if request.method == 'POST':
        city = request.form['city']
        district = request.form['district']
        address = f"{city}, {district}"
        user_location = get_user_location(address)
        
        if user_location:
            recommendations = recommend_hospitals((user_location.latitude, user_location.longitude), hospital_data)
            return render_template('appointment.html', recommendations=recommendations, user_location=user_location)
        else:
            error_message = f"Unable to find location for {address}. Please try again."
            return render_template('appointment.html', error_message=error_message)
    
    return render_template('appointment.html')

if __name__ == '__main__':
    app.run(debug=True)
