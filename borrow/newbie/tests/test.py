from borrow.newbie.tests.runFullPositiveTest import *
from PIL import Image, ImageChops
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By



def difference_images(img1, img2):
    image_1 = Image.open(img1)
    image_2 = Image.open(img2)
    result = ImageChops.difference(image_1, image_2).getbbox()
    print(result)
    if result == None:
        print(img1, img2, 'matches')
    else:
        print(img1, img2, 'no_matches')
    return

wait = WebDriverWait(web_driver, 20)
element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'loan__description')))
web_driver.save_screenshot('active_loan_fact.png')
difference_images('Expected/active_loan.png', 'active_loan_fact.png')
web_driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div/span[2]/a').click()
time.sleep(5)
web_driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[2]/div/div/div/div[2]').click()
time.sleep(5)
web_driver.save_screenshot('item_fact.png')
difference_images('Expected/active_loan.png', 'item_fact.png')



# result = ImageChops.difference(image_1, image_2)
# print(result.getbbox())
