import time
from pages.base_page import BasePage
from pages.elements_page import TextBoxPage

class TestElements:
    
    class TestTextBox:
        def test_text_box(self, driver):
            page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            page.open()
            full_name, email, current_address, permanent_address = page.fill_all_fields()
            output_name, output_email, output_current_address, output_permanent_address =   page.get_output_result()
            assert output_name == full_name
            assert output_email == email
            assert output_current_address == current_address
            assert output_permanent_address == permanent_address