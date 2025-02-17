from playwright.sync_api import Page


class AddOwnerPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = 'http://localhost:8080/owners/new'
        # Selectors
        self.first_name = '#firstName'
        self.last_name = '#lastName'
        self.address = '#address'
        self.city = '#city'
        self.telephone = '#telephone'
        self.add_new_owner_btn = '.btn'

    def visit_page(self):
        self.page.goto(self.url)
        self.page.wait_for_load_state('load')

    def fill_owner_details(self, owner_data):
        self.page.fill(self.first_name, owner_data['firstName'])
        self.page.fill(self.last_name, owner_data['lastName'])
        self.page.fill(self.address, owner_data['address'])
        self.page.fill(self.city, owner_data['city'])
        self.page.fill(self.telephone, owner_data['telephone'])

    def add_new_owner(self):
        self.page.click(self.add_new_owner_btn)
