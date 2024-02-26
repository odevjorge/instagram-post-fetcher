"""
Main function to perform operations.
"""
from core.management.data.post import DataManage


def main():
    """
    The main function to fetch Instagram post information.

    This function initializes a WebDriver object to fetch post information
    from Instagram and prints all the collected post information.
    """
    print(f"{'*'*25}\nInstagram Post Data Fetcher\n{'*'*25}")

    data = DataManage()

    info = data.get_all_post_info()

    print(info)


if __name__ == "__main__":
    main()
