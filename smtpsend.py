import smtplib
import configemail
import requests
import webbrowser
import json
import jsonpath
import pytest
from selenium import webdriver

#driver = webdriver.Chrome('E:\Webdriver\chromedriver')
randCat = "http://aws.random.cat/meow"
randDog = "https://random.dog/woof.json"
randFox = "https://randomfox.ca/floof/"

otvetCat = requests.get(randCat)
json_response = json.loads(otvetCat.text)
pagesCat = jsonpath.jsonpath(json_response, 'file')



otvetDog = requests.get(randDog)
json_response = json.loads(otvetDog.text)
pagesDog = jsonpath.jsonpath(json_response, 'url')


otvetFox = requests.get(randFox)
json_response = json.loads(otvetFox.text)
pagesFox = jsonpath.jsonpath(json_response, 'image')

def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(configemail.EMAIL_ADDRESS, configemail.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(configemail.EMAIL_ADDRESStest, configemail.EMAIL_ADDRESStest, message)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")


subject = "Test subject"
msg = pagesDog,pagesFox,pagesCat;


send_email(subject,msg)