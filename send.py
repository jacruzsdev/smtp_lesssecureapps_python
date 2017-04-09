# -*- coding: utf-8 -*-
import smtplib
import email
import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class SMTPManager(object):
    """DEEP KERNEL -> SMTP_MANAGER.

    Set up email using an smtp server
    """
    def __init__(self, sender, password, to, subject,
            smtp_server_name = "smtp.gmail.com", smtp_server_port = 587):
        """Send emails.

        Params:
        *sender             -   email
        *password           -   sender's password
        *to                 -   final email
        *subject            -   title of the email
        *msg                -   email's message
        *smtp_server_name   -   smtp server name used by sender's email - default:smtp.gmail.com
        *smtp_server_port   -   smtp server port used by sender's email - default:587"""

        #VARIABLES
        self.sender = sender
        self.password = password
        self.to = to
        self.subject = u'{}'.format(subject)
        self.smtp_server = None
        self.smtp_server_name = smtp_server_name
        self.smtp_server_port = smtp_server_port

    def init_smtp(self):
        """Set up smtp server.
        """
        #CONFIG SMTP SERVER
        self.smtp_server = smtplib.SMTP(self.smtp_server_name, self.smtp_server_port)

        #STARTING TLS
        self.smtp_server.starttls()
        #LOGIN SESSION
        self.smtp_server.login(self.sender, self.password)

    def send(self, msg):
        """Send email.
        Params:
        *msg    - email message to send
        """
        #INIT STMP SERVER
        msg = u'{}'.format(msg)
        self.init_smtp()

        #SEND EMAIL
        self.smtp_server.sendmail(self.sender, self.to, msg.encode('utf-8'))
        self.smtp_server.close()


def send_message(sender, pwsd, to, subject, msg):
    msg         = u"To: {}\nFrom: {}\nSubject: {}\n{}\n\n".format(to, sender, subject, msg)
    #SMTP_MANAGER OBJECT
    smtp_manager_object = smtp_send.smtp_manager(sender, password, to, subject)
    #SEND EMAIL
    smtp_manager_object.send(msg)
    return
