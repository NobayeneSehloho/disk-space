# This is a script to read the server hard disk space available on the file systems and the hostnames.
# Centos-Server, Raspbery-Pi1, Mac-Book and LPIC

import subprocess
from subprocess import Popen
import getpass
import string
# All other imports
import smtplib
from smtplib import SMTP
from typing import Union
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pip._vendor.distlib.compat import raw_input
import df_func

# Creating my function to send a email
def send_email():
	"""Please edit the email and password to match the correct details.""" 
    disk_read = subprocess.Popen("df -h", shell=True, stdout=subprocess.PIPE)
    df_output = disk_read.stdout.read()
    # msg: MIMEText = MIMEText("Centos-Server Might be running out of disk space")
    
    #df_func.df_h()
    
    msg = MIMEMultipart()
    msg["Subject"] = "Check disk space on Samba-Server"
    msg["From"] = "<FromEmail>"
    msg["To"] = "<ToEmail>"

    description = "Hi Admnistrator!\n\nSamba-Server might be running out of disk space\n\n"
    body_text = MIMEText(description, 'plain')
    msg.attach(body_text)

    body_df = MIMEText(df_output, 'plain', 'utf-8')
    msg.attach(body_df)

    # msg.as_string()

    # To send a message we need to connect to SMTP server #
    # password = input("please input your password: ")
    pasa = "<MyPassword>"
    server: SMTP = smtplib.SMTP("smtp.<myDomain>", 587)

    server.ehlo()
    # (250, b'smtp.<MyDomain at your service, [XX.XX.XX.XX]\nSIZE 35882577\n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nPIPELINING\nCHUNKING\nSMTPUTF8')

    server.starttls()
    # (220, b'2.0.0 Ready to start TLS')

    server.login("<FromAddress>", pasa)
    # (235, b'2.7.0 Accepted')

    server.sendmail("<FromEmail>", "<ToEmail>", msg.as_string())

    {}
    server.quit()
    # (221, b'2.0.0 closing connection o76sm39310782pfi.119 - gsmtp')

send_email()
