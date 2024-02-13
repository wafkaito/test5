from selenium import webdriver
import datetime

def take_screenshot(driver, name):
    # Generate a timestamp for the screenshot filename
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

    # Define the filename with the timestamp and provided name
    screenshot_file = f"error_sc.png"

    # Take the screenshot using the driver
    driver.save_screenshot(screenshot_file)

    # Print the path of the screenshot for reference
    print(f"Screenshot saved: {screenshot_file}")