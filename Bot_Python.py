from webbot import Browser 
from dotenv import load_dotenv
import time
import schedule



def schule():
    web = Browser()
    #Enter school link
    web.go_to('') 
    web.click(id='page-login-index')
    #Enter name
    web.type('' , into='Email')
    print('name')
    web.click('NEXT' , tag='span')
    #Enter Password
    web.type('' , into='password' , id='passwordFieldId')
    print("Password")
    web.click(id='loginbtn')
    print("login")
    web.click(xpath='//*[@id="single_button6098c554ee0ad20"]')
    #Enter scentence
    web.type('', into='textbox', id='id_onlinetext_editoreditable')
    web.click(id='id_submitbutton') 
    print("Done")

# Uhrzeit            Enter time
schedule.every().day.at(" ").do(schule)

while True:
    schedule.run_pending()
    time.sleep(1)

