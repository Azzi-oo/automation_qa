import time
import re
from generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()
    
    def _normalize_address(self, address):
        """Нормализует адрес: заменяет переносы строк и множественные пробелы на одинарные пробелы"""
        if not address:
            return address
        # Заменяем все виды переносов строк на пробел
        normalized = re.sub(r'[\n\r]+', ' ', address)
        # Заменяем множественные пробелы на одинарный
        normalized = re.sub(r'\s+', ' ', normalized)
        return normalized.strip()
    
    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        submit_button = self.element_is_visible(self.locators.SUBMIT)
        self.go_to_element(submit_button)
        time.sleep(1)
        self.click_element_with_js(submit_button)
        time.sleep(5)
        # Нормализуем адреса перед возвратом для корректного сравнения
        current_address_normalized = self._normalize_address(current_address)
        permanent_address_normalized = self._normalize_address(permanent_address)
        return full_name, email, current_address_normalized, permanent_address_normalized
        
    def get_output_result(self):
        full_name = self.element_is_visible(self.locators.CREATED_FULL_NAME).text.split(':')[1].strip()
        email = self.element_is_visible(self.locators.CREATED_EMAIL).text.split(':')[1].strip()
        current_address = self.element_is_visible(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1].strip()
        permanent_address = self.element_is_visible(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1].strip()
        # Нормализуем адреса для корректного сравнения
        current_address_normalized = self._normalize_address(current_address)
        permanent_address_normalized = self._normalize_address(permanent_address)
        return full_name, email, current_address_normalized, permanent_address_normalized
    
    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1].strip()
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1].strip()
        current_address = self.element_is_visible(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1].strip()
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1].strip()
        return full_name == "Test User", email == "test@test.com", current_address == "Test Address", permanent_address == "Test Address"