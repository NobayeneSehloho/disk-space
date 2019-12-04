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
