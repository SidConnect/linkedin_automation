import time
import pytest
from pages.profile_page import ProfilePage


@pytest.fixture(scope="module")
def profile_page(driver):
    return ProfilePage(driver)


def profile_data(profile_page, home_page, test_logger):

    notification_count = home_page.get_notifications_count()
    print(notification_count)

    home_page.go_to_profile_dashboard()

    followers_count = profile_page.get_followers_count()
    print(followers_count, " Followers")

    connection_count = profile_page.get_connections_count()
    print(connection_count, " Connections")

    profile_page.navigate_to_homepage()
    time.sleep(3)

    test_logger.info("Profile test - SUCCESS")


