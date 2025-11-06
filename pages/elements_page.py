import time
from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()
    
    def fill_all_fields(self, full_name, email, current_address, permanent_address):
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        submit_button = self.element_is_visible(self.locators.SUBMIT)
        self.go_to_element(submit_button)
        time.sleep(1)
        self.click_element_with_js(submit_button)
        time.sleep(5)
        
    def get_output_result(self):
        return self.element_is_visible(self.locators.CREATED_FULL_NAME).text, self.element_is_visible(self.locators.CREATED_EMAIL).text, self.element_is_visible(self.locators.CREATED_CURRENT_ADDRESS).text, self.element_is_visible(self.locators.CREATED_PERMANENT_ADDRESS).text
    
    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1].strip()
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1].strip()
        current_address = self.element_is_visible(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1].strip()
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1].strip()
        return full_name == "Test User", email == "test@test.com", current_address == "Test Address", permanent_address == "Test Address"