import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager

class TestCombinedTestCases():
    def setup_method(self, method):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--disable-web-security")
        chrome_options.add_argument("--remote-allow-origins=*")
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def update_spreadsheet(self, result):
        # Google 스프레드시트 페이지 업데이트
        self.driver.get("https://docs.google.com/spreadsheets/d/1Vfnx48r25tpUp9xLCUXgmtGgcKvyzugY8rbYkT-0Sys/edit#gid=1323494429")
        self.driver.maximize_window()

        # 테스트 결과 반영
        cell_selector = "#mN98wd > .grid4-inner-container:nth-child(12)"
        self.driver.find_element(By.CSS_SELECTOR, cell_selector).click()
        self.driver.find_element(By.CSS_SELECTOR, ".docsCommonGMDCDialog").click()
        self.driver.find_element(By.CSS_SELECTOR, ".waffle-ac-highlighted").click()
        self.driver.find_element(By.ID, "waffle-rich-text-editor").send_keys(result)

    def update_spreadsheet(self):
        # Google 스프레드시트 페이지 업데이트
        self.driver.execute_script(
            "window.open('https://docs.google.com/spreadsheets/d/1Vfnx48r25tpUp9xLCUXgmtGgcKvyzugY8rbYkT-0Sys/edit#gid=1323494429','_blank');")
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.get("https://docs.google.com/spreadsheets/d/1Vfnx48r25tpUp9xLCUXgmtGgcKvyzugY8rbYkT-0Sys/edit#gid=1323494429")

        # JavaScript를 사용하여 두 번째 시트로 이동
        js_script = """
            var sheetsTab = document.querySelectorAll('.docs-sheet-tab');
            sheetsTab[1].click();
        """
        self.driver.execute_script(js_script)

        # 테스트 결과 반영
        for i, result in enumerate(self.test_results):
            cell_selector = f"G{i + 12}"  # 예시: G12, G13...
            cell = self.driver.find_element(By.CSS_SELECTOR,
                                            f".grid-container [data-row-index='{i + 11}'] [data-col-index='6']")
            cell.click()
            cell.send_keys(result)

    def test_admin_page(self):
        # Test name: admin_page_test
        self.driver.get("https://iqa.tmax-superapp.com/admin/")
        self.driver.maximize_window()
        result = 'PASS'  # 테스트 결과 기본값
        # 테스트 케이스 수행
        try:
            self.driver.find_element(By.CSS_SELECTOR, ".login-FormGroup-wrapper").click()
            self.driver.find_element(By.NAME, "horizontal-form-name").click()
            self.driver.find_element(By.NAME, "horizontal-form-name").send_keys("admin")
            self.driver.find_element(By.NAME, "horizontal-form-email").click()
            self.driver.find_element(By.NAME, "horizontal-form-email").send_keys("tmax@23")
            password_icon = self.driver.find_element(By.CSS_SELECTOR, ".passwordIcon > path:nth-child(2)")
            ActionChains(self.driver).click(password_icon).perform()
            self.driver.find_element(By.CSS_SELECTOR, ".pf-c-form").click()
            login_button = self.driver.find_element(By.CSS_SELECTOR, ".pf-c-button")
            ActionChains(self.driver).click(login_button).perform()
            self.driver.find_element(By.CSS_SELECTOR, ".select-main-menu > .pf-c-menu__item-main > .pf-c-menu__item-text").click()
        except Exception as e:
            print(f"Test failed: {e}")
            result = 'FAIL'  # 테스트 실패 시 결과 업데이트

        # 스프레드시트 업데이트
        self.update_spreadsheet(result)

    def test_some_other_feature(self):
        # Test name: some_other_feature_test
        self.driver.get("https://example.com")
        # 테스트 케이스 수행
        # 테스트 결과 업데이트
        result = 'PASS'  # 또는 'FAIL'
        # 스프레드시트 업데이트
        self.update_spreadsheet(result)