from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys

# Take the search query as a command line argument
query = ' '.join(sys.argv[1:])

# Start the web driver
driver = webdriver.Firefox()

# Open the Google search page
driver.get("https://www.google.com")

# Find the search box element and enter the query
search_box = driver.find_element_by_name("q")
search_box.send_keys(query)
search_box.send_keys(Keys.RETURN)

# Wait for the results to load
time.sleep(3)

# Find the search results elements
results = driver.find_elements_by_css_selector('.g')

# Print the search results
for result in results:
    title = result.find_element_by_css_selector('h3').text
    link = result.find_element_by_css_selector('a')
    print(title)
    print(link.get_attribute("href"))
    print()

# Close the browser
driver.quit()
