import datetime
import os
import smtplib, ssl
from email.mime.text import MIMEText
from dotenv import load_dotenv

EMAIL = {"header": "Bet Notification: A recommended game is occuring in 10 minutes."}


sports_lookup = {
    "nfl": "football", 
    "ncaaf": "football",
    "epl": "football", 
    "nba": "basketball",
    "ncaab": "basketball",
    "wnba": "basketball",
    "mlb": "baseball",
    "nhl": "hockey",
}

def load_env(path):
    if load_dotenv(path):
        return
    raise Exception("Can't load dotenv")

def get_credentials(uname, pword):
    return (os.getenv(uname), os.getenv(pword))

def convert_ann_sport_to_ps_sport(data):
    for entry in data:
        entry["sport"] = sports_lookup[entry["sport"]]

    return data

def start_smtp_server():
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    #server.starttls()
    server.login(os.getenv("MY_EMAIL"), os.getenv("APP_PWD"))
    
    return server


def send_email(server: smtplib.SMTP, sender, receiver, subject, msg):
    mtext = MIMEText(msg)
    mtext['Subject'] = subject
    mtext['From'] = sender
    mtext['To'] = receiver

    server.sendmail(sender, [receiver], mtext.as_string())

def test_email():
    s = start_smtp_server()
    subject = "Automated Test Email"
    msg = "test"
    #send_email(s, os.getenv("MY_EMAIL"), os.getenv("ANN_USERNAME"), subject, msg)
    send_email(s, os.getenv("MY_EMAIL"), os.getenv("MY_EMAIL"), subject, msg)

def test_email2():
    load_dotenv()
    user = os.getenv("MY_EMAIL")
    app_pwd = os.getenv("APP_PWD")
    to = os.getenv("MY_EMAIL")
    port = 465
    print(user, app_pwd)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(user, app_pwd)
        server.sendmail(user, user, "Test email")