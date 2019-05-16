import smtplib,ssl
import RPi.GPIO as GPIO
from picamera import PiCamera  
from time import sleep  
from email.mime.multipart import MIMEMultipart  
from email.mime.base import MIMEBase  
from email.mime.text import MIMEText  
from email.utils import formatdate  
from email import encoders  
  
camera = PiCamera()  
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)

def cheeze_MOFO():
    camera.rotation = 180    
    camera.start_preview()  
    sleep(5)  
    camera.capture('/home/pi/image.jpg')     # image path set
    sleep(5)  
    camera.stop_preview()
    
def send_an_email():  
    toaddr = 'Davidpaez1006@gmail.com'      # To id 
    me = 'Davidpaez1006@gmail.com'          # your id
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
       s.login(user = me, password = 'November29!')  # User id & password
       #s.send_message(msg)  
       s.sendmail(me, toaddr, msg.as_string())  
       s.quit()  
    #except:  
    #   print ("Error: unable to send email")    
    except SMTPException as error:  
          print ("Error")                # Exception

while True:
    i = GPIO.input(11)
    if i == 0:  # When output from motion sensor is LOW
        print "No intruders", i
        sleep(0.3)
    elif i == 1:  # When output from motion sensor is HIGH
        print "Intruder detected", i
        cheeze_MOFO()  
        send_an_email() 
 
