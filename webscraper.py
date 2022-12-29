# Import the necessary modules
from selenium import webdriver
from bs4 import BeautifulSoup
import time

# Create a new Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the website you want to scroll
driver.get("https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2022-23-1298134/england-vs-india-2nd-semi-final-1298178/ball-by-ball-commentary")

# Define the JavaScript code for scrolling the page by a certain amount
script = "window.scrollTo(0, 1000);"

# Set a variable for tracking whether the page is still scrolling
scrolling = True

data = {}

# Keep scrolling the page until it no longer loads new content
while scrolling:
    # Scroll the page and load new content
    driver.execute_script(script)

    # Parse the page HTML using BeautifulSoup
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # Check if the page has any div elements with the specified class name
    if soup.find_all("div", class_="ds-leading-none ds-mb-0.5"):
        # If the page has div elements with the specified class name,
        # stop scrolling and process the data
        scrolling = False

        # Loop through the div elements with the specified class name
        for div in soup.find_all("div", class_="ds-leading-none ds-mb-0.5"):
            # Print the data from each div element
            line = div.text
            # print(line)
            parts = line.split("to")
            bowler = parts[0].strip()
            batsman = parts[1].strip()
            parts = batsman.split(",")
            batsman = parts[0].strip()
            runs = parts[1].strip()

            # If the bowler is already in the dictionary, append the new data to the list of values
            if bowler in data:
                data[bowler].append((batsman, runs))
            # Otherwise, create a new list with the new data
            else:
                data[bowler] = [(batsman, runs)]

            # print(bowler)
            # print(batsman)
            # print(runs)

# Close the webdriver
driver.close()

# print(data)  # ["Shami"])

# Get the name of the batsman
batsmanInput = input("Enter batsman's name:")

# Get the name of the bowler
bowlerInput = input("Enter bowler's name:")

# Initialize a total score variable
total_score = 0
ball_count = 0
num_runs = 0

# Iterate through the data for each bowler
for bowler in data:
    # print(bowler)
    if bowler == bowlerInput:
        for (batsman, runs) in data[bowlerInput]:
            num_runs = 0
            if batsman == batsmanInput:
                ball_count += 1
                if runs == "no run":
                    num_runs = 0
                elif runs == "1 run":
                    num_runs = 1
                elif runs == "2 runs":
                    num_runs = 2
                elif runs == "3 runs":
                    num_runs = 3
                elif runs == "FOUR runs":
                    num_runs = 4
                elif runs == "SIX runs":
                    num_runs = 6
                print(num_runs)
                total_score += num_runs

print(total_score)

# Output the total score
print(f"{batsmanInput} scored {total_score} runs in {ball_count} balls against {bowlerInput}")


    
