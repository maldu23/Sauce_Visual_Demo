from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib3
from os import environ
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.remote.webelement import WebElement
from saucelabs_visual.client import SauceLabsVisual
from saucelabs_visual.typing import FullPageConfig, IgnoreRegion, IgnoreElementRegion

#instantiates the visual client
client = SauceLabsVisual()

urllib3.disable_warnings()

options = ChromeOptions()

options.browser_version = 'latest'

options.platform_name = 'Windows 10'
sauce_options = {}
sauce_options['username'] = environ['SAUCE_USERNAME']
sauce_options['accessKey'] = environ['SAUCE_ACCESS_KEY']
sauce_options['build'] = 'Visual Test'
sauce_options['name'] = 'Visual Test'
#sauce_options['extendedDebugging'] = 'true'
#sauce_options['capturePerformance'] = 'true'
options.set_capability('sauce:options', sauce_options)

url = "https://ondemand.us-west-1.saucelabs.com:443/wd/hub"
driver = webdriver.Remote(command_executor=url, options=options)


def test_website():

    #creates the visual build
    client.create_build(name='Test woot')
    
    #point to customer website
    driver.get("https://www.insertCustomerWebsiteHere.com/")

    # Get your Selenium session ID
    session_id = driver.session_id  

    #creates snapshot on the first page
    client.create_snapshot_from_webdriver(
        name="First Page",
        session_id=driver.session_id,
        capture_dom=True
    )

    #Here are some ways to find elements. You will likely use Class Name and ID the most and should definitely start there. 
    #You should only use the others if these 2 don't work.
    driver.find_elements(By.CLASS_NAME, 'xxx')
    driver.find_element(By.ID, '')
    driver.find_element(By.XPATH, '')
    driver.find_element(By.CSS_SELECTOR, '')

    #Partial link text is especially useful when trying to click something that isn't a button. 
    #Often websites have href link elements that cannot be found and clicked the same way buttons can be.
    driver.find_element(By.PARTIAL_LINK_TEXT, '')

    #Especially if you intend to use an element in multiple ways, I would set it to a variable
    #this might mean making an assertion on an expected value, then afterwards clicking it for example

    element1 = driver.find_elements(By.CLASS_NAME, 'xxx')

    #I personally recommend finding an element to click that can take you to a new page. This allows you to show multiple screenshots in your visual build.
    element1.click()

    element2 = driver.find_elements(By.CLASS_NAME, 'xxx')

    #creates snapshot on the second page
    client.create_snapshot_from_webdriver(
        name="Deals Page",
        session_id=driver.session_id,
        capture_dom=True,

        #allows you to ignore an element you saved earlier
        ignore_elements = [
            IgnoreElementRegion(element = element2)
        ]

    )


    if 1 == 1:
        driver.execute_script('sauce:job-result=passed')
    else:
        driver.execute_script('sauce:job-result=failed')

    #Finishes the visual build. This is a necessary step the same way quitting the driver is.
    client.finish_build()

    driver.quit()


test_website()
