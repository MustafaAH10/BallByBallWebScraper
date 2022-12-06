# Import the necessary modules
from selenium import webdriver
import time

# Create a new Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the website you want to scroll
driver.get("https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2022-23-1298134/england-vs-india-2nd-semi-final-1298178/ball-by-ball-commentary")

# Define the JavaScript code for scrolling the page and loading new content
script = "window.scrollTo(0, document.body.scrollHeight);"

# Set a variable for tracking whether the page is still scrolling
scrolling = True

# Keep scrolling the page until it no longer loads new content
while scrolling:
    # Scroll the page and load new content
    driver.execute_script(script)

    # Calculate the new height of the page
    new_height = driver.execute_script("return document.body.scrollHeight")

    # Check if the new height is the same as the previous height
    if new_height == driver.execute_script("return document.body.scrollTop"):
        # If the new height is the same as the previous height,
        # this means that the page is no longer loading new content,
        # so stop scrolling
        scrolling = False

# Close the webdriver
driver.close()
