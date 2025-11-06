import time
from pages.base_page import BasePage
from pages.elements_page import TextBoxPage

class TestElements:
    
    class TestTextBox:
        def test_text_box(self, driver):
            page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            page.open()
            page.fill_all_fields('Test User', 'test@test.com', 'Test Address', 'Test Address')
            page.get_output_result()
            assert page.check_filled_form()