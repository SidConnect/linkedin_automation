import pytest
from pages.jobs_page import JobsPage


@pytest.fixture(scope="module")
def jobs_page(driver):
    return JobsPage(driver)

@pytest.mark.order(2)
def test_get_job_descriptions(jobs_page):
    search_tag = "automation engineer"
    jobs_page.search(search_tag)
    jobs_page.get_job_cards()
