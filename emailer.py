import weather
import mailer

def get_emails():
    emails = {}
    emails_file = open('emails.txt','r')
    try:
        for line in emails_file:
            (email, name) = line.split(',')
            emails[email] = name.strip()
    except FileNotFoundError as err:
        print(err)
    return emails


def main():
    emails = get_emails()
    forecast = weather.get_weather_forecast()
    self_email = input('Please input your email address:')
    password = input('Please input your password:')

    for email,name in emails.items():
        mailer.send_email(self_email, password, email, name, forecast)

main()