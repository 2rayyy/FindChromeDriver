import requests
import zipfile
import os




def get_latest_chromedriver_version():
    url = "https://chromedriver.storage.googleapis.com/LATEST_RELEASE"
    response = requests.get(url)
    version = response.text
    return version


def download_latest_chromedriver(version):
    download_url = f"https://chromedriver.storage.googleapis.com/{version}/chromedriver_win32.zip"

    # Download the file
    response = requests.get(download_url, stream=True)
    if response.status_code != 200:
        raise Exception("Failed to download ChromeDriver.")

    # Save the file to the current directory
    with open("chromedriver.zip", "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    print(f"ChromeDriver {version} downloaded successfully.")


def extract_chromedriver(zip_file_path, destination_folder):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extract('chromedriver.exe', path=destination_folder)
