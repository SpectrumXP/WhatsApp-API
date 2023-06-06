from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# List of dangerous links
DANGEROUS_LINKS = [
    "https://youtube.com",
    "http://forbes.com",
    "www.twitter.com",
    # Add more dangerous links here
]

# Path to the ChromeDriver executable on your system
chromedriver_path = r'C:\WINDOWS\System32\chromedriver.exe'

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Start the ChromeDriver service
service = Service(chromedriver_path)

# Create a Chrome WebDriver instance
driver = webdriver.Chrome(service=service, options=chrome_options)

# Prompt the user to enter a link
link = input("Enter a link: ")

# Check if the entered link is in the list of dangerous links
is_dangerous = link in DANGEROUS_LINKS

if is_dangerous:
    print("\nDanger! This link may potentially be harmful or contain explicit content!")
    proceed = input("Do you wish to still proceed to the link? (Yes/No): ")
    if proceed.lower() == 'yes':
        print("Link is now allowed. You may proceed.")
    else:
        print("Link blocked. You cannot proceed.")
else:
    print("Link is safe. You can proceed.")

# Close the Chrome browser
driver.quit()