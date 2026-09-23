from playwright.sync_api import Page, expect


class MenuPage:

    def __init__(self, page: Page):
        self.page = page

        self.menu_button = page.locator(
            "#react-burger-menu-btn"
        )

        self.logout_link = page.locator(
            "[data-test='logout-sidebar-link']"
        )

    def logout(self):
        expect(self.menu_button).to_be_visible()
        self.menu_button.click()

        expect(self.logout_link).to_be_visible()
        self.logout_link.click()