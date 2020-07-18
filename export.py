from generate import *
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders
import datetime 



generate_questions(mult = 10, sq = 6, cube = 6, rev_mult = 10)



fromaddr = "sahilmathpractice@gmail.com"
toaddr = "riyapahooja@gmail.com"

msg = MIMEMultipart() 
msg['From'] = fromaddr 
  
# storing the receivers email address  
msg['To'] = toaddr 
  
# storing the subject  

d = datetime.datetime.now()

da =d.strftime("%d %b")
msg['Subject'] = "Math practice for " + da

db = d.strftime("%I:%M %p %d %b '%y")
body = "Math Practice Problems (generated at " + db + ")\n\n:By Sahil Pahooja"
msg.attach(MIMEText(body, 'plain')) 

filename = "Math_Practice_" + d.strftime("%d%b") + ".txt"
attachment = open(filename, "rb") 

# instance of MIMEBase and named as p 
p = MIMEBase('application', 'octet-stream') 
  
# To change the payload into encoded form 
p.set_payload((attachment).read()) 
  
# encode into base64 
encoders.encode_base64(p) 
   
p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
  
# attach the instance 'p' to instance 'msg' 
msg.attach(p) 
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login(fromaddr, "MATH1234") 
  
# Converts the Multipart msg into a string 
text = msg.as_string() 
  
# sending the mail 
s.sendmail(fromaddr, toaddr, text) 
  
# terminating the session 
s.quit() 