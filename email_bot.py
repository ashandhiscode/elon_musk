import sys
sys.path.append('./')
import config
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

class EmailBot() :
    email_address = config.auth_dict['email_address']
    auth = config.auth_dict['password']

    def __init__(self, world_issue, elon) :
        self.world_issue = world_issue
        self.elon = elon

    def return_text(self, elonmusk=False) :
        if elonmusk :
            mail_content = '''You are Elon Musk.'''
        else :
            mail_content = f'''\n\n\n\nThe world issue is: {self.world_issue}'''
        return(mail_content)

    def generate_MIME(self, recipient, name) :
        self.message = MIMEMultipart()
        self.message['From'] = self.email_address
        self.message['Subject'] = "Open this email to find out which world issue you're going to be facing..."
        self.message['To'] = recipient
        self.message.attach(MIMEText(self.return_text(name==self.elon), 'plain'))
    
    def launch_smpt_session(self) :
        self.session = smtplib.SMTP('smtp.gmail.com', 587)
        self.session.starttls()
        self.session.login(self.email_address, self.auth)

    def send_email(self, recipient, name) :
        self.generate_MIME(recipient, name)
        self.launch_smpt_session()
        text = self.message.as_string()
        self.session.sendmail(self.email_address, recipient, text)
        self.session.quit()