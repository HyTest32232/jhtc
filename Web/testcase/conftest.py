import pytest
# from selenium import webdriver

from Web.page_object.index_page import IndexPage

@pytest.fixture()
def get_index():
    index = IndexPage()
    return index

# @pytest.fixture(scope="function",autouse=True)
# def load_test():
#     driver = webdriver.Chrome()
#     yield
#     driver.quit()
