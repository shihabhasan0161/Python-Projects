from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
import os
from dotenv import load_dotenv
import schedule
import time

load_dotenv()

SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = os.getenv("SMTP_PORT")
SMTP_EMAIL = os.getenv("SMTP_EMAIL")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
SMTP_USERNAME = os.getenv("SMTP_USERNAME")

# initializing the count and max_run
count = 0
max_run = 2


def main(subject="Automated Mail", text="", img=None, attachment=None):

    # build message content
    msg = MIMEMultipart()

    # Subject
    msg["Subject"] = subject

    # from email just for Brevo, other SMTP might require different parameter
    msg["From"] = SMTP_EMAIL

    # text contents
    msg.attach(MIMEText(text))

    # if we have image attachment
    if img is not None:
        if type(img) is not list:
            # make it a list if it's not
            img = [img]

        for i in img:
            # read binary image
            img_data = open(i, "rb").read()
            # attach the image data to msg object
            msg.attach(MIMEImage(img_data, name=os.path.basename(i)))

    # similarly check for attachment
    if attachment is not None:
        if type(attachment) is not list:
            attachment = [attachment]

        for i in attachment:
            # open and read attachment as binary and add the attachment to our msg object
            with open(i, "rb") as f:
                file = MIMEApplication(f.read(), name=os.path.basename(i))

            # here we edit the attached file metadata
            file["Content-Disposition"] = (
                f'attachment; filename="{os.path.basename(i)}"'
            )
            msg.attach(file)

    return msg


def send_mail():
    # connect to the SMTP server
    # I am using Brevo Here, you can use any other SMTP if you wish
    smtp = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    smtp.ehlo()
    smtp.starttls()

    smtp.login(SMTP_USERNAME, SMTP_PASSWORD)

    # Call the main function with the parameter values
    msg = main(
        "This is subject",
        "This is the body text",
        r"C:\Users\Shihab\Downloads\python_logo.jpg",
        r"C:\Users\Shihab\Downloads\Resume.pdf",
    )

    # list of emails to send to
    to = [
        "shihabhasan0161@gmail.com",
    ]

    msg["To"] = ", ".join(to)

    # send the mail
    smtp.sendmail(from_addr=SMTP_EMAIL, to_addrs=to, msg=msg.as_string())
    print("Email sent")

    # Limit the email sending schedule to max_run
    global count
    count += 1
    if count >= max_run:
        print("Max runs reached, closing the program")
        schedule.clear()
        return schedule.CancelJob

    # quit the connection once done!
    smtp.quit()


# We can set a schedule to send email using this -> https://pypi.org/project/schedule/
schedule.every(5).seconds.do(send_mail)
while True:
    schedule.run_pending()
    time.sleep(1)

    # break the loop once job is done!
    if len(schedule.jobs) == 0:
        break
