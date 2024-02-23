"""
Main function to perform operations.
"""
from packages.scraping import WebDriver


def main():
    """
    The main function to fetch Instagram post information.

    This function initializes a WebDriver object to fetch post information
    from Instagram and prints all the collected post information.
    """
    print(f"{'*'*25}\nInstagram Post Info Fetcher\n{'*'*25}")

    # Initialize the WebDriver object
    driver = WebDriver()

    # Fetch post information
    driver.post_fetcher()

    # Print all the collected post information
    print(driver.get_all_post_info())


if __name__ == "__main__":
    main()
