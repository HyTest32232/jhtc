import pytest

from Web.page_object.index_page import IndexPage


@pytest.fixture()
def get_index():
    index = IndexPage()
    return index