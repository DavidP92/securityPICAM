import smtplib,ssl  
from picamera import PiCamera  
from time import sleep  
from email.mime.multipart import MIMEMultipart  
from email.mime.base import MIMEBase  
from email.mime.text import MIMEText  
from email.utils import formatdate  
from email import encoders  
  
camera = PiCamera()  

def cheeze_MOFO():
    camera.rotation = 180    
    camera.start_preview()  
    sleep(5)  
    camera.capture('/home/pi/image.jpg')     # image path set
    sleep(5)  
    camera.stop_preview()
    
def send_an_email():  
    toaddr = 'email@gmail.com'      # To id 
    me = 'email@gmail.com'          # your id
    subject = "Picture frm Home!"              # Subject
  
    msg = MIMEMultipart()  
    msg['Subject'] = subject  
    msg['From'] = me  
    msg['To'] = toaddr  
    msg.preamble = "test "   
    #msg.attach(MIMEText(text))  
  
    part = MIMEBase('application', "octet-stream")  
    part.set_payload(open("/home/pi/image.jpg", "rb").read())  
    encoders.encode_base64(part)  
    part.add_header('Content-Disposition', 'attachment; filename="image.jpg"')   # File name and format name
    msg.attach(part)  
  
    try:  
       s = smtplib.SMTP('smtp.gmail.com', 587)  # Protocol
       s.ehlo()  
       s.starttls()  
       s.ehlo()  
       s.login(user = me, password = '**********')  # User id & password
       #s.send_message(msg)  
       s.sendmail(me, toaddr, msg.as_string())  
       s.quit()  
    #except:  
    #   print ("Error: unable to send email")    
    except SMTPException as error:  
          print ("Error")                # Exception
cheeze_MOFO()  
send_an_email()  
