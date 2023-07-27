import os
from selenium import webdriver
import streamlit as st
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from functions import get_latest_chromedriver_version, download_latest_chromedriver , extract_chromedriver


if __name__ == "__main__":
    try:
        latest_version = get_latest_chromedriver_version()
        download_latest_chromedriver(latest_version)

        # Replace 'chromedriver.zip' with the actual file path if not in the same directory as the script
        zip_file_path = 'chromedriver.zip'

        # Replace 'extracted_folder' with the destination folder where you want to extract the 'chromedriver.exe' file
        destination_folder = os.getcwd()

        # Create the destination folder if it doesn't exist
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        extract_chromedriver(zip_file_path, destination_folder)
        print("Extraction completed.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Test
path_chrome = "chromedriver.exe"
driver = webdriver.Chrome(path_chrome)
driver.get("https://www.cargonet.no/")


