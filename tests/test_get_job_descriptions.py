import pytest
from pages.jobs_page import JobsPage
import pandas as pd
from utils.excel_utils import write_to_excel


@pytest.fixture(scope="module")
def jobs_page(driver):
    return JobsPage(driver)


@pytest.mark.order(2)
def test_get_job_descriptions(jobs_page):
    search_tag = "SDET"
    jobs_page.search(search_tag)
    for on_page in range(25):
        new_job_details_df = jobs_page.get_job_details()
        write_to_excel(new_job_details_df, "data/post_data.xlsx", "Job Details")
        jobs_page.go_to_page(on_page+2)
