from tbselenium.tbdriver import TorBrowserDriver
from tbselenium.utils import start_xvfb, stop_xvfb
from time import sleep
import os

directorio = os.getcwd()
link = input("Adfly link : ")
def mi_link():
        try:
            driver = TorBrowserDriver(directorio)
            driver.get('http://fumacrom.com/vVsD/')
            sleep(5)
            adnext = driver.find_element_by_id("skip_bu2tton")
            adnext.click()
            sleep(50)
            driver.quit()
            return
        except:
            print("Error")
            return
def tu_link():
        try:
            driver = TorBrowserDriver(directorio)
            driver.get(link)
            sleep(5)
            adnext = driver.find_element_by_id("skip_bu2tton")
            adnext.click()
            sleep(50)
            driver.quit()
            return
        except:
            print("Error")
            return
while True:
    xvfb_display = start_xvfb()
    tu_link()
    mi_link()
