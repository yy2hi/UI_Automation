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
    @classmethod
    def setup_class(cls):
        cls.chrome_options = webdriver.ChromeOptions()
        cls.chrome_options.add_argument("--ignore-certificate-errors")
        cls.chrome_options.add_argument("--disable-web-security")
        cls.chrome_options.add_argument("--remote-allow-origins=*")
        cls.chrome_options.add_experimental_option("detach", True)

        # 웹 드라이버 생성
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=cls.chrome_options)
        cls.vars = {}
        cls.admin_tab_opened = False

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    @classmethod
    def switch_to_admin_page_tab(cls):
        if not cls.admin_tab_opened:
            cls.driver.switch_to.window(cls.driver.window_handles[0])
            cls.driver.get("https://iqa.tmax-superapp.com/admin/")
            cls.driver.maximize_window()
            cls.admin_tab_opened = True

    @classmethod
    def switch_to_spreadsheet_tab(cls):
        # 새로운 탭 열기
        cls.driver.execute_script("window.open('');")
        # 열린 탭으로 전환
        cls.driver.switch_to.window(cls.driver.window_handles[-1])
        cls.driver.get("https://docs.google.com/spreadsheets/d/1Vfnx48r25tpUp9xLCUXgmtGgcKvyzugY8rbYkT-0Sys/edit#gid=1323494429")
        cls.driver.maximize_window()

    def update_spreadsheet(self, result):
        # 테스트 결과 반영
        cell_selector = f".grid-container [data-row-index='{11 + len(self.test_results)}'] [data-col-index='6']"
        cell = self.driver.find_element(By.CSS_SELECTOR, cell_selector)
        cell.click()
        cell.send_keys(result)

    def test_admin_page(self):
        # Test name: admin_page_test
        self.switch_to_admin_page_tab()
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
        finally:
            self.switch_to_spreadsheet_tab()  # 테스트가 완료된 후에 스프레드시트 탭으로 전환
            self.update_spreadsheet(result)

    def test_some_other_feature(self):
        # Test name: some_other_feature_test
        self.switch_to_admin_page_tab()
        result = 'PASS'  # 또는 'FAIL'
        self.update_spreadsheet(result)
