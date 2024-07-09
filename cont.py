import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(user_name, user_country, user_contact, user_email, user_message):
    # Email configuration
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = 'hardiksachan2@gmail.com'  # Replace with your email
    sender_password = 'hmka elgs roch fyxf'  # Replace with your app password (generated as described above)
    receiver_email = 'hardiksachan70@gmail.com'
    
    # Create the email content
    subject = 'New Feedback from {}'.format(user_name)
    body = f"""
    Name: {user_name}
    Country: {user_country}
    Contact Number: {user_contact}
    Email: {user_email}
    Message/Feedback: {user_message}
    """
    
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        # Connect to the SMTP server and send the email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        print('Email sent successfully.')
    except Exception as e:
        print(f'Failed to send email: {e}')

# Function to take user input and send email
def get_user_input_and_send_email():
    user_name = input('Enter your name: ')
    user_country = input('Enter your country: ')
    user_contact = input('Enter your contact number: ')
    user_email = input('Enter your email: ')
    user_message = input('Enter your message/feedback: ')
    
    send_email(user_name, user_country, user_contact, user_email, user_message)

if __name__ == '__main__':
    get_user_input_and_send_email()
