import smtplib

def send_email(from_email, password, to_email, name, forecast):
    server = smtplib.SMTP('smtp.gmail.com', '587')

    server.starttls()

    server.login(from_email, password)

    message = 'Subject: Welcome to the Circus!\n'
    message += 'Hi ' + name + '!\n\n'
    message += forecast + '\n\n'
    message += 'Hope to see you there!'

    server.sendmail(from_email, to_email, message)

    server.quit()