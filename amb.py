import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the path to chromedriver.exe
service = Service(executable_path="C:/Program Files/Google/Chrome/Application/chrome.exe")

# Create a Chrome webdriver instance
driver = webdriver.Chrome(service=service)

# Open Twitter
driver.get("https://twitter.com")

# Wait for the login button to be clickable
wait = WebDriverWait(driver, 10)
login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-testid='loginButton']")))

AMLink = input("Enter the link: ")
if AMLink:
    # Click on the tweet button
    tweet_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Tweet']")))
    tweet_button.click()

    # Wait for the tweet input field to be visible
    tweet_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-testid='tweetTextarea_0']")))
    
    # Input the link
    tweet_input.send_keys(AMLink)

    # Click on the tweet button
    send_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@data-testid='tweetButtonInline']")))
    send_button.click()
else:
    print("No link provided")

# Close the browser
# driver.quit()