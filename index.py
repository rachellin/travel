from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

DRIVER_PATH = 'C:\chromedriver.exe'
# driver = webdriver.Chrome(executable_path=DRIVER_PATH)

options = webdriver.ChromeOptions()
options.add_argument('--enable-logging')
options.add_argument('--v=1')
driver = webdriver.Chrome(options=options)

# driver = webdriver.Chrome()


# Open the Google Custom Map URL
map_id = "10NXxdOY_DArwWYU3othpTHPzsok2Pjs" # the id is the part before the ampersand 
driver.get('https://www.google.com/maps/d/viewer?mid={}'.format(map_id))

# Allow some time for the page to load
time.sleep(5)

# Find all markers on the map
# markers = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"]')

markers = driver.find_elements(By.CSS_SELECTOR, 'div[class="HzV7m-pbTTYe-ibnC6b pbTTYe-ibnC6b-d6wfac"]')

data = []

for marker in markers:
    # Click on the marker to reveal information
    marker.click()
    time.sleep(2)  # wait for the info window to appear
    
    # Extract information from the info window
    try:
        title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'section-info-window-content-title'))
        ).text
        
        description = driver.find_element(By.CLASS_NAME, 'section-info-window-content-subtitle').text
        address = driver.find_element(By.CLASS_NAME, 'section-info-window-content-address').text

        # Extract longitude and latitude
        coordinates = marker.get_attribute('data-latlng').split(',')
        latitude = coordinates[0]
        longitude = coordinates[1]

        # Extract category (if applicable)
        category = driver.find_element(By.CLASS_NAME, 'section-info-window-content-category').text

        data.append({
            'title': title,
            'description': description,
            'address': address,
            'latitude': latitude,
            'longitude': longitude,
            'category': category
        })

        print("got data for {}".format(title))
    except Exception as e:
        print(f'Error: {e}')
        continue


print(len(data))
print(data[0])
exit()
# Print the extracted data
for entry in data:
    print(entry)

# Close the browser
driver.quit()
