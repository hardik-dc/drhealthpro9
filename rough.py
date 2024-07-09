from flask import Flask, render_template, request
from mr_healthpro import MrHealthPro
from tracker import analyze_data
import pandas as pd
from researches import get_disease_info
from recom import get_user_location, recommend_hospitals
from cont import send_email

app = Flask(__name__, template_folder='your_custom_templates_folder')
mr_health_pro = MrHealthPro()
hospital_data = pd.read_csv('delhi_hospitals.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/diagnosis', methods=['GET', 'POST'])
def diagnosis():
    predictions = []
    if request.method == 'POST':
        symptoms = request.form['symptoms']
        predictions = mr_health_pro.predict(symptoms)
    return render_template('diagnosis.html', predictions=predictions)

@app.route('/research', methods=['GET', 'POST'])
def research():
    disease_info = {}
    if request.method == 'POST':
        disease_name = request.form['disease']
        summary, content = get_disease_info(disease_name)
        disease_info = {'name': disease_name, 'summary': summary, 'content': content}
    return render_template('research.html', disease_info=disease_info)

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

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        user_name = request.form['name']
        user_country = request.form['country']
        user_contact = request.form['contact']
        user_email = request.form['email']
        user_message = request.form['message']
        send_email(user_name, user_country, user_contact, user_email, user_message)
        return render_template('contact.html', success=True)
    return render_template('contact.html')

@app.route('/track', methods=['GET', 'POST'])
def track():
    recommendations = []
    health_percentage = 0
    fitness_percentage = 0
    if request.method == 'POST':
        age = int(request.form['age'])
        heart_rate = int(request.form['heart_rate'])
        steps = int(request.form['steps'])
        sleep_hours = float(request.form['sleep_hours'])
        calories_burned = int(request.form['calories_burned'])
        recommendations, health_percentage, fitness_percentage = analyze_data(age, heart_rate, steps, sleep_hours, calories_burned)
    return render_template('track.html', recommendations=recommendations, health_percentage=health_percentage, fitness_percentage=fitness_percentage)

if __name__ == '__main__':
    app.run(debug=True)
