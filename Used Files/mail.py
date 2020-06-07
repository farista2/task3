# Import the smtplib module
# The smtplib module defines an SMTP client session object
# that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon.
import smtplib
import urllib.request as urllib
# Senders email
sender_email = "Email"
# Receivers email
rec_email = "Email"

message = (""" Accuracy is Good you can use it """)

# Initialize the server variable
server = smtplib.SMTP('smtp.gmail.com', 587)
# Start the server connection
server.starttls()
# Login
server.login("Email", "Password")
print("Login Success!")
# Send Email
server.sendmail("arpit sironiya", "Email", message)
print(f"Email has been sent successfully to {rec_email}")
