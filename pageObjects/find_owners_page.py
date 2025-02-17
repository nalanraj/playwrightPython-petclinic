from playwright.sync_api import Page, expect


class FindOwnersPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = 'http://localhost:8080/owners/find'
        # Selectors
        self.add_owner_btn = 'a.btn'
        self.owner_information_class = '.container-fluid'
        self.owner_information_txt = 'Owner Information'
        self.last_name_input = '#lastName'
        self.find_owner_btn = '.col-sm-offset-2 > .btn'
        self.owner_result_txt = 'Owners'

    def visit_page(self):
        self.page.goto(self.url)

    def go_to_add_owner(self):
        self.page.click(self.add_owner_btn)

    def verify_owner_information(self):
        # expect(self.page).to_(self.owner_information_txt) --> assertion in playwright
        assert self.owner_information_txt in self.page.content()

    def search_owner(self, owner_data):
        self.page.fill(self.last_name_input, owner_data['lastName'])
        self.page.click(self.find_owner_btn)
        # expect(self.page).to_have_text(self.owner_result_txt) --> assertion in playwright
        assert self.owner_result_txt in self.page.content()
