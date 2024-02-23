"""
Module make operations on browser using selenium
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WebDriver:
    """
    Web driver for operations.
    """

    POST_CLASS_NAME = "_aa6e"
    POST_INDEX_CLASS_NAME = "_aamj"
    ACCOUNT_NAME_CLASS_NAME = "_a9zc"
    DESCRIPTION_POST_CLASS_NAME = "_a9zs"
    IMAGE_CLASS_NAME = "_aagv"
    IMAGE_TAG_NAME = "img"
    POST_DATE = "_aaqe"
    WAIT_TIME = 10

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=chrome_options)
        self.post_data = None
        self.urls = []

    def post_fetcher(self, url: str = None):
        """
        Get Post HTML on selenium variable.
        """
        if not url:
            url = input("Provide URL of post:\n> ")

        self.urls.append(url)

        self.driver.get(url)
        wait = WebDriverWait(self.driver, self.WAIT_TIME)
        self.post_data = wait.until(EC.visibility_of_element_located(
            (By.CLASS_NAME, self.POST_CLASS_NAME)))

        return print("Post Fetcher Success")

    def quit(self):
        """
        Close web driver.
        """
        self.driver.quit()

    def get_images_count_index(self):
        """
        Get count of images on post.
        """
        try:
            get_images_index = self.post_data.find_element(
                By.CLASS_NAME, self.POST_INDEX_CLASS_NAME)
            qty_images = get_images_index.find_elements(By.CLASS_NAME, '_acnb')

            return len(qty_images)

        except NoSuchElementException:
            print("No Post Index")
            return 0

    def get_post_text(self):
        """
        Get page_name and description of post.
        """
        return {
            "account_name": self.post_data.find_element(
                By.CLASS_NAME, self.ACCOUNT_NAME_CLASS_NAME).text,
            "description_post": self.post_data.find_element(
                By.CLASS_NAME, self.DESCRIPTION_POST_CLASS_NAME).text
        }

    def get_post_image_url(self):
        """
        Get post image.
        """
        images_post = self.post_data.find_elements(
            By.CLASS_NAME, self.IMAGE_CLASS_NAME)

        if len(images_post) == 0:
            video_post = self.post_data.find_elements(
                By.TAG_NAME, 'video')

            video_urls = {}

            for video_index, video_data in enumerate(video_post):
                video_urls.update(
                    {video_index + 1: video_data.get_attribute('src')}
                )

            return video_urls

        image_urls = {}

        for image_index, image_data in enumerate(images_post):
            image_urls.update(
                {image_index + 1: image_data.find_element(
                    By.TAG_NAME, self.IMAGE_TAG_NAME).get_attribute('src')}
            )

        return image_urls

    def get_post_date(self):
        "Return datetime of post"
        return self.post_data.find_element(
            By.CLASS_NAME, self.POST_DATE).get_attribute('datetime')

    def get_all_post_info(self):
        """
        Return post all info: Image Url, Description and Username Profile 
        """

        post_description_data = self.get_post_text()

        return {
            'account_username': post_description_data['account_name'],
            'image_url': self.get_post_image_url(),
            'description': post_description_data['description_post'],
            'post_date': self.get_post_date()
        }
