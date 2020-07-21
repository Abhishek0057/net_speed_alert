import speedtest
import datetime
import time
import subprocess
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Mbits
MIN_EXPECTED_DOWNLOAD_SPEED = 60
MIN_EXPECTED_UPLOAD_SPEED = 60
TIME_BETWEEN_CONSECUTIVE_SPEEDTEST = 5   #in seconds

def get_new_speeds():
    try:
        get_speedtest_result = subprocess.check_output(['speedtest-cli','--share'])
        decoded_result = get_speedtest_result.decode("utf-8") 
        speedtest_list = decoded_result.split()
        download_speed = speedtest_list[-11]
        upload_speed = speedtest_list[-5]
        result_screen_shot = speedtest_list[-1]
        result = (float(download_speed), float(upload_speed), result_screen_shot)
    except subprocess.CalledProcessError:
        result = None
    return result

def validate_speed(download_speed, upload_speed, result_screen_shot):
    status = True
    if download_speed < MIN_EXPECTED_DOWNLOAD_SPEED or upload_speed < MIN_EXPECTED_UPLOAD_SPEED:
        log_content = f'Date Time: {datetime.datetime.now()} Below min speed Download Speed :{download_speed}, Upload Speed :{upload_speed}, Screen Shot :{result_screen_shot}'
        status = False
    else:
        log_content = f'Date Time: {datetime.datetime.now()} Above min speed, stay clam and enjoy, Download Speed :{download_speed}, Upload Speed :{upload_speed}, Screen Shot :{result_screen_shot}'
    logs(log_content)
    return status
    

def send_alert(validate_speed, download_speed, upload_speed, result_screen_shot):
    if validate_speed==False:
        mail_content = f'''<h3>Hello,
        I am facing low internet speed issue,<br>
        Download speed : {download_speed}<br>
        Upload speed : {upload_speed}<br>
        Speed commitment by your company for both upload and download is : {MIN_EXPECTED_UPLOAD_SPEED, MIN_EXPECTED_DOWNLOAD_SPEED}<br>
        Plesae resolve my issue as soon as possible.<br><br>
        Here is Attachment for the test performed on Ookla</h3> <br> <img src="{result_screen_shot}" alt="img" /> <br>'''

        #The mail addresses and password
        sender_address = 'abhishek07satbhai@gmail.com'
        sender_pass = '****'
        receiver_address = 'abhisheksatbhai@icloud.com'

        #Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = 'Raising Complain for the Internet Speed.'

        #The body and the attachments for the mail
        message.attach(MIMEText(mail_content, 'html', 'utf-8'))

        #Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()                         
        session.login(sender_address, sender_pass)      
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        log_content = f'Date Time: {datetime.datetime.now()} Email Sent, Slow Internet Complain Registered With Your Internet Service Provider'
        logs(log_content)

def logs(content):
    with open("logs.txt", "a") as logs:  
        logs.write(content+'\n')


while True:
    speedtest_result = get_new_speeds()
    if speedtest_result:
        validate = validate_speed(*speedtest_result)
        send_alert(validate, *speedtest_result)
    else:
        log_content = f'Date Time: {datetime.datetime.now()}, Could not connect to server....retrying after {TIME_BETWEEN_CONSECUTIVE_SPEEDTEST} seconds'
        logs(log_content)
    time.sleep(TIME_BETWEEN_CONSECUTIVE_SPEEDTEST)