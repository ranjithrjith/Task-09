rom selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Set up the Chrome WebDriver
driver = webdriver.Chrome()

# Open the webpage
driver.get("https://www.saucedemo.com/")

# Fetch and print the title of the webpage
title = driver.title
print("Title of the webpage:", title)

# Get and print the current URL of the webpage
current_url = driver.current_url
print("Current URL of the webpage:", current_url)

# Extract the entire contents of the webpage
page_contents = driver.page_source

# Save the contents in a text file
with open("webpage_task_11.txt", "w", encoding='utf-8') as file:
    file.write(page_contents)

# Close the browser
driver.quit()