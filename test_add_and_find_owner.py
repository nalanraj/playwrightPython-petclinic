import pytest
from playwright.sync_api import Playwright

from pageObjects.find_owners_page import FindOwnersPage
from pageObjects.add_owner_page import AddOwnerPage

def test_add_and_find_owner(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    owner_data = {
        "firstName": "John",
        "lastName": "Doe",
        "address": "123 Main St",
        "city": "Springfield",
        "telephone": "1234567890"
    }

    find_owners_page = FindOwnersPage(page)
    add_owner_page = AddOwnerPage(page)

    # Given
    find_owners_page.visit_page()

    # When
    find_owners_page.go_to_add_owner()
    add_owner_page.fill_owner_details(owner_data)
    add_owner_page.add_new_owner()

    # Then
    find_owners_page.verify_owner_information()

    # And
    find_owners_page.visit_page()
    find_owners_page.search_owner(owner_data)
