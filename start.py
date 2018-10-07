import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import smtplib

def sendEmail(toaddr,subject,body,fileData):
    	msg = MIMEMultipart()
    	if(fileData!=''):
          part = MIMEBase('application', "octet-stream")
          part.set_payload(open(fileData, "rb").read())
          part.add_header('Content-Disposition', 'attachment; filename='+fileData)
          msg.attach(part)
    	fromaddr='agrosense.info@gmail.com'
    	msg['From'] = fromaddr
    	msg['To'] = toaddr
    	msg['Subject'] = subject
    	msg.attach(MIMEText(body, 'plain'))
    	mailer = smtplib.SMTP('smtp.gmail.com', 587)
    	mailer.starttls()
    	mailer.login(fromaddr, "semilleroSI2C")
    	text = msg.as_string()
    	mailer.sendmail(fromaddr, toaddr, text)
    	mailer.quit()


if __name__ == "__main__":
	try:
		sendEmail('2420132006@estudiantesunibague.edu.co','CONECTADO','Listo para piloto','')
	except:
		print "MAIL FAIL"
	sys.exit()
