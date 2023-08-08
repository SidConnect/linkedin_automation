import pytest
from datetime import datetime
from utils.excel_utils import read_excel_data, write_to_excel
import configparser
import pandas as pd
from pages.new_post_page import NewPostPage
import time

config = configparser.ConfigParser(interpolation=None)
config.read(r"C:\Users\thaku\PycharmProjects\linkedin_automation\pytest.ini")


@pytest.fixture(scope='module')
def new_post_page(driver):
    return NewPostPage(driver)


def post_creation(new_post_page, home_page, test_logger):
    home_page.start_a_new_post()
    post_data_file_path = config.get("FileLocations", "post_data_file_path")
    df = read_excel_data(post_data_file_path, "post_data")
    test_logger.info("Get Excel Data - SUCCESS")

    for index, row in df.iterrows():
        if pd.isna(row["Date Posted"]):
            post_content = row["Content"]
            post_idea = row["Post Ideas"]
            post_attachment_path = row["Attachments"]

            test_logger.info(f"Creating a new post: {post_idea}")
            new_post_page.enter_post_content(post_content)
            new_post_page.enter_attachment(post_attachment_path, post_idea)

            new_post_page.create_post()
            df.at[index, 'date_posted'] = datetime.now().strftime("%Y-%m-%d")

            write_to_excel(df, post_data_file_path)
            break

        else:
            continue
