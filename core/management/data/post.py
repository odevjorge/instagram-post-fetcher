"Interface for Post Data Management and Information Handling."

from core.scraping.post import WebScraper


class DataManage:
    """
    Class to manage post information
    """

    ACCOUNT_USERNAME_KEY = 'account_username'
    DESCRIPTION_KEY = 'description'
    TAGS_KEY = 'tags'
    IMAGES_URL_KEY = 'images_url'
    POST_DATE_KEY = 'post_date'

    def __init__(self, post_url: str = None) -> None:
        self.scraper = WebScraper()

        self.post_url(post_url)

    def post_url(self, post_url: str = None):
        self.scraper.post_fetcher(post_url)

    def description_normalized(self):
        """
        Return normalized post description
        """
        post_description_data = self.scraper.get_post_text()

        description = post_description_data['description_post'].split("#")

        description_dict = {
            self.ACCOUNT_USERNAME_KEY: post_description_data['account_name'],
            self.DESCRIPTION_KEY: description.pop(0),
            self.TAGS_KEY: [f"#{i}" for i in description]
        }

        return description_dict

    def get_all_post_info(self):
        """
        Return all post information: Image URL, Description, and
        Username Profile
        """
        post_description_data = self.description_normalized()

        post_description_data.update({
            self.IMAGES_URL_KEY: self.scraper.get_post_image_url(),
            self.POST_DATE_KEY: self.scraper.get_post_date()
        })

        return post_description_data
