
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time,os,sys,json

class SeleniamStarter():
    def __init__(self,url):
        self.url=url
        self.BASEDIR=os.path.dirname(__file__)
        # helo
        


        # instantiate a chrome options object so you can set the size and headless preference
        # some of these chrome options might be uncessary but I just used a boilerplate
        # change the <path_to_download_default_directory> to whatever your default download folder is located
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920x1080")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--verbose')
        chrome_options.add_experimental_option("prefs", {
                "download.default_directory": os.path.join(self.BASEDIR,'download'),
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "safebrowsing_for_trusted_sources_enabled": False,
                "safebrowsing.enabled": False
        })
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-software-rasterizer')

        # initialize driver object and change the <path_to_chrome_driver> depending on your directory where your chromedriver should be
        self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="./chromedriver.exe")

        # change the <path_to_place_downloaded_file> to your directory where you would like to place the downloaded file
        download_dir = os.path.join(self.BASEDIR,'download')

        # function to handle setting up headless download
        self.enable_download_headless(self.driver, download_dir)

        # get request to target the site selenium is active on
        self.driver.get(self.url)

    # function to take care of downloading file
    def enable_download_headless(self,browser,download_dir):
        browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
        params = {'cmd':'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
        browser.execute("send_command", params)


# WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="nav-yesterday-tab"]'))).click()
# element=self.driver.find_elements_by_xpath('//*[@id="maincounter-wrap"]')


def main():
    seleniam=SeleniamStarter('https://google.com')
    seleniam.driver.close()


if __name__ == "__main__":
    main()




