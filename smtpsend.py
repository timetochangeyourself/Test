import smtplib
import configemail
import requests
import webbrowser
import json
import jsonpath
import pytest
import time
from selenium import webdriver

#1 Step
#Open getnada and save email

driver = webdriver.Chrome('E:\Webdriver\chromedriver')  # Optional argument, if not specified will search path.
driver.get('https://getnada.com');
driver.maximize_window()
try:
    content = driver.find_element_by_class_name('address.what_to_copy')
    EMAIL_ADDRESStest = content.text
    print("Email address saved")
except:
    print("Email address dont`t saved, check search elements")

#2 Step
#request random links
randCat = "http://aws.random.cat/meow"
randDog = "https://random.dog/woof.json"
randFox = "https://randomfox.ca/floof/"

otvetCat = requests.get(randCat)
json_response = json.loads(otvetCat.text)
pagesCat = jsonpath.jsonpath(json_response, 'file')[0]

otvetDog = requests.get(randDog)
json_response = json.loads(otvetDog.text)
pagesDog = jsonpath.jsonpath(json_response, 'url')[0]

otvetFox = requests.get(randFox)
json_response = json.loads(otvetFox.text)
pagesFox = jsonpath.jsonpath(json_response, 'image')[0]

# 3 Step
#connecting gmail and send links
def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(configemail.EMAIL_ADDRESS, configemail.PASSWORD)

        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(EMAIL_ADDRESStest, EMAIL_ADDRESStest, message)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")

#link transfer through HTML letters
subject = "Test subject"

msg = """\
<html>
  <head></head>
  <body>
       <a href={pagesCat}>{pagesCat}</a><br>
       <a href={pagesDog}>{pagesDog}</a><br>
       <a href={pagesFox}>{pagesFox}</a>
  </body>
</html>
""".format(pagesCat=pagesCat, pagesDog=pagesDog, pagesFox=pagesFox)

send_email(subject, msg)


#Step 4
#open lettwrs
time.sleep(8)
open = driver.find_element_by_class_name('msg_item')
open.click()
time.sleep(2)



fraim = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/iframe')
test = driver.switch_to.frame(fraim)
test = driver.find_element_by_xpath('/html/body/a[1]')
test = test.text
assert pagesCat == test
print("links in letter match links in pages")

test1 = driver.find_element_by_xpath('/html/body/a[2]')
test1 = test1.text
assert pagesDog == test1
print("links in letter match links in pages")

test2 = driver.find_element_by_xpath('/html/body/a[3]')
test2 = test2.text
assert pagesFox == test2
print("links in letter match links in pages")


#Step 5
#open links and make screenshot
driverscreen = webdriver.Chrome('E:\Webdriver\chromedriver')  # Optional argument, if not specified will search path.
driverscreen.get(pagesCat);
driver.maximize_window()
driverscreen.save_screenshot('Cat.png')
driverscreen.quit()
#Cat

driverscreen = webdriver.Chrome('E:\Webdriver\chromedriver')
driverscreen.get(pagesDog);
driver.maximize_window()
driverscreen.save_screenshot('Dog.png')
driverscreen.quit()
#Dog

driverscreen = webdriver.Chrome('E:\Webdriver\chromedriver')
driverscreen.get(pagesFox);
driver.maximize_window()
driverscreen.save_screenshot('Fox.png')
driverscreen.quit()
#Fox