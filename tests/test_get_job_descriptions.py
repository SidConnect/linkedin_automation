

def get_job_descriptions(home_page):

    search_tag = "automation engineer"
    home_page.search(search_tag)

    home_page.get_job_cards()
