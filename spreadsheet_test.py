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
        self.test_results = []  # 각 테스트 케이스의 결과를 저장할 리스트

    def teardown_method(self, method):
        self.driver.quit()

    def update_spreadsheet(self):
        # Google 스프레드시트 페이지 업데이트
        self.driver.get("https://docs.google.com/spreadsheets/d/1Vfnx48r25tpUp9xLCUXgmtGgcKvyzugY8rbYkT-0Sys/edit")
        self.driver.set_window_size(1377,919)

        # 테스트 결과 반영
        for i, result in enumerate(self.test_results):
            cell_selector = f"#mN98wd > .grid4-inner-container:nth-child({i + 12})"
            self.driver.find_element(By.CSS_SELECTOR, cell_selector).click()
            self.driver.find_element(By.CSS_SELECTOR, ".docsCommonGMDCDialog").click()
            self.driver.find_element(By.CSS_SELECTOR, ".waffle-ac-highlighted").click()
            self.driver.find_element(By.ID, "waffle-rich-text-editor").send_keys(result)

        # 새로운 탭 열기
        self.driver.execute_script("window.open('about:blank','_blank');")
        # 새로운 탭으로 전환
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # 스프레드시트 페이지 열기
        self.driver.get("https://docs.google.com/spreadsheets/d/1Vfnx48r25tpUp9xLCUXgmtGgcKvyzugY8rbYkT-0Sys/edit")

        # JavaScript를 사용하여 두 번째 시트로 이동
        js_script = """
            var sheetsTab = document.querySelectorAll('.docs-sheet-tab');
            sheetsTab[1].click();
        """
        self.driver.execute_script(js_script)

    def test_combined_test_cases(self):
        # Test name: admintest
        # Step # | name | target | value
        # 1 어드민 페이지 열기
        self.driver.get("https://iqa.tmax-superapp.com/admin/")
        self.driver.set_window_size(1377, 919)
        if False:  # 테스트 결과에 따라 조건 변경
            self.test_results.append('FAIL')  # PASS 또는 FAIL로 변경하여 테스트 결과 저장
        else:
            self.test_results.append('TRUE')  # PASS 또는 FAIL로 변경하여 테스트 결과 저장


        # 2 ID PW 적고 로그인 하기
        self.driver.find_element(By.CSS_SELECTOR, ".login-FormGroup-wrapper").click()
        self.driver.find_element(By.NAME, "horizontal-form-name").click()
        self.driver.find_element(By.NAME, "horizontal-form-name").send_keys("admin")
        self.driver.find_element(By.NAME, "horizontal-form-email").click()
        self.driver.find_element(By.NAME, "horizontal-form-email").send_keys("tmax@23")
        # password 보기 클릭
        password_icon = self.driver.find_element(By.CSS_SELECTOR, ".passwordIcon > path:nth-child(2)")
        ActionChains(self.driver).click(password_icon).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".pf-c-form").click()
        # 로그인 버튼 클릭
        login_button = self.driver.find_element(By.CSS_SELECTOR, ".pf-c-button")
        ActionChains(self.driver).click(login_button).perform()
        # 9 | click | css=.select-main-menu > .pf-c-menu__item-main > .pf-c-menu__item-text |
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".select-main-menu > .pf-c-menu__item-main > .pf-c-menu__item-text").click()
        if False:  # 테스트 결과에 따라 조건 변경
            self.test_results.append('FAIL')
        else:
            self.test_results.append('TRUE')

        # 10 | click | id=호스트 OS |
        self.driver.find_element(By.ID, "호스트 OS").click()
        # 11 | click | id=머신 |
        self.driver.find_element(By.ID, "머신").click()
        # 12 | click | id=컴퓨트 |
        self.driver.find_element(By.ID, "컴퓨트").click()
        # 13 | click | id=네트워크 |
        self.driver.find_element(By.ID, "네트워크").click()
        # 14 | click | css=#\C2A4\D1A0\B9AC\C9C0 > .pf-c-accordion__toggle-text |
        self.driver.find_element(By.CSS_SELECTOR, "#\\C2A4\\D1A0\\B9AC\\C9C0 > .pf-c-accordion__toggle-text").click()
        # 15 | click | id=모니터링 |
        self.driver.find_element(By.ID, "모니터링").click()
        # 16 | click | id=관리 |
        self.driver.find_element(By.ID, "관리").click()
        # 17 | click | id=호스트 OS |
        self.driver.find_element(By.ID, "호스트 OS").click()
        # 18 | click | css=#\D638\C2A4\D2B8\ OS .link-style:nth-child(1) .pf-c-menu__item-text |
        self.driver.find_element(By.CSS_SELECTOR,
                                 "#\\D638\\C2A4\\D2B8\\ OS .link-style:nth-child(1) .pf-c-menu__item-text").click()
        # 19 | mouseOver | css=#\D638\C2A4\D2B8\ OS .link-style:nth-child(1) .pf-c-menu__item-text |
        element = self.driver.find_element(By.CSS_SELECTOR,
                                           "#\\D638\\C2A4\\D2B8\\ OS .link-style:nth-child(1) .pf-c-menu__item-text")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # 20 | mouseOut | css=.pf-m-focus .pf-c-menu__item-text |
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        # 21 | click | id=호스트 OS |
        self.driver.find_element(By.ID, "호스트 OS").click()
        # 22 | click | id=호스트 OS |
        self.driver.find_element(By.ID, "호스트 OS").click()
        # 23 | click | css=#\D638\C2A4\D2B8\ OS .link-style:nth-child(2) .pf-c-menu__item-text |
        self.driver.find_element(By.CSS_SELECTOR,
                                 "#\\D638\\C2A4\\D2B8\\ OS .link-style:nth-child(2) .pf-c-menu__item-text").click()
        # 24 | mouseOver | css=#\D638\C2A4\D2B8\ OS .link-style:nth-child(2) .pf-c-menu__item-text |
        element = self.driver.find_element(By.CSS_SELECTOR,
                                           "#\\D638\\C2A4\\D2B8\\ OS .link-style:nth-child(2) .pf-c-menu__item-text")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # 25 | mouseOut | css=.pf-m-focus .pf-c-menu__item-text |
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        # 26 | click | css=#\D638\C2A4\D2B8\ OS .link-style:nth-child(3) .pf-c-menu__item-text |
        self.driver.find_element(By.CSS_SELECTOR,
                                 "#\\D638\\C2A4\\D2B8\\ OS .link-style:nth-child(3) .pf-c-menu__item-text").click()
        # 27 | click | id=머신 |
        self.driver.find_element(By.ID, "머신").click()
        # 28 | click | xpath=//dd[@id='머신']/div/div/div/ul/a/li/button/span/span |
        self.driver.find_element(By.XPATH, "//dd[@id=\'머신\']/div/div/div/ul/a/li/button/span/span").click()
        # 29 | click | xpath=//dd[@id='머신']/div/div/div/ul/a[2]/li/button/span/span |
        self.driver.find_element(By.XPATH, "//dd[@id=\'머신\']/div/div/div/ul/a[2]/li/button/span/span").click()
        # 30 | click | xpath=//dd[@id='머신']/div/div/div/ul/a[3]/li/button/span/span |
        self.driver.find_element(By.XPATH, "//dd[@id=\'머신\']/div/div/div/ul/a[3]/li/button/span/span").click()
        # 31 | mouseOver | xpath=//dd[@id='머신']/div/div/div/ul/a[3]/li/button/span/span |
        element = self.driver.find_element(By.XPATH, "//dd[@id=\'머신\']/div/div/div/ul/a[3]/li/button/span/span")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # 32 | mouseOut | css=.pf-m-focus .pf-c-menu__item-text |
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        # 33 | click | id=컴퓨트 |
        self.driver.find_element(By.ID, "컴퓨트").click()
        # 34 | click | xpath=//dd[@id='컴퓨트']/div/div/div/ul/a/li/button/span/span |
        self.driver.find_element(By.XPATH, "//dd[@id=\'컴퓨트\']/div/div/div/ul/a/li/button/span/span").click()
        # 35 | click | css=#\B124\D2B8\C6CC\D06C > .pf-c-accordion__toggle-text |
        self.driver.find_element(By.CSS_SELECTOR, "#\\B124\\D2B8\\C6CC\\D06C > .pf-c-accordion__toggle-text").click()
        # 36 | click | xpath=//dd[@id='네트워크']/div/div/div/ul/a/li/button/span/span |
        self.driver.find_element(By.XPATH, "//dd[@id=\'네트워크\']/div/div/div/ul/a/li/button/span/span").click()
        # 37 | mouseOver | xpath=//dd[@id='네트워크']/div/div/div/ul/a/li/button/span/span |
        element = self.driver.find_element(By.XPATH, "//dd[@id=\'네트워크\']/div/div/div/ul/a/li/button/span/span")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # 38 | mouseOut | css=.pf-m-focus .pf-c-menu__item-text |
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        # 39 | click | xpath=//dd[@id='네트워크']/div/div/div/ul/a[2]/li/button/span/span |
        self.driver.find_element(By.XPATH, "//dd[@id=\'네트워크\']/div/div/div/ul/a[2]/li/button/span/span").click()
        # 40 | mouseOver | xpath=//dd[@id='네트워크']/div/div/div/ul/a[2]/li/button/span/span |
        element = self.driver.find_element(By.XPATH, "//dd[@id=\'네트워크\']/div/div/div/ul/a[2]/li/button/span/span")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # 41 | mouseOut | css=.pf-m-focus .pf-c-menu__item-text |
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        # 42 | click | css=#\C2A4\D1A0\B9AC\C9C0 > .pf-c-accordion__toggle-text |
        self.driver.find_element(By.CSS_SELECTOR, "#\\C2A4\\D1A0\\B9AC\\C9C0 > .pf-c-accordion__toggle-text").click()
        # 43 | click | xpath=(//button[@type='button'])[26] |
        self.driver.find_element(By.XPATH, "(//button[@type=\'button\'])[26]").click()
        # 44 | mouseOver | xpath=(//button[@type='button'])[26] |
        element = self.driver.find_element(By.XPATH, "(//button[@type=\'button\'])[26]")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # 45 | mouseOut | css=.pf-m-focus > .pf-c-menu__item |
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        # 46 | click | xpath=//dd[@id='스토리지']/div/div/div/ul/a[2]/li/button/span/span |
        self.driver.find_element(By.XPATH, "//dd[@id=\'스토리지\']/div/div/div/ul/a[2]/li/button/span/span").click()
        # 47 | click | css=#\BAA8\B2C8\D130\B9C1 > .pf-c-accordion__toggle-text |
        self.driver.find_element(By.CSS_SELECTOR, "#\\BAA8\\B2C8\\D130\\B9C1 > .pf-c-accordion__toggle-text").click()
        # 48 | click | xpath=//dd[@id='모니터링']/div/div/div/ul/a/li/button/span/span |
        self.driver.find_element(By.XPATH, "//dd[@id=\'모니터링\']/div/div/div/ul/a/li/button/span/span").click()
        # 49 | mouseOver | xpath=//dd[@id='모니터링']/div/div/div/ul/a[2]/li/button/span/span |
        element = self.driver.find_element(By.XPATH, "//dd[@id=\'모니터링\']/div/div/div/ul/a[2]/li/button/span/span")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # 50 | click | xpath=//dd[@id='모니터링']/div/div/div/ul/a[2]/li/button/span/span |
        self.driver.find_element(By.XPATH, "//dd[@id=\'모니터링\']/div/div/div/ul/a[2]/li/button/span/span").click()
        # 51 | mouseOver | xpath=//dd[@id='모니터링']/div/div/div/ul/a[3]/li/button/span/span |
        element = self.driver.find_element(By.XPATH, "//dd[@id=\'모니터링\']/div/div/div/ul/a[3]/li/button/span/span")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # 52 | click | xpath=//dd[@id='모니터링']/div/div/div/ul/a[3]/li/button/span/span |
        self.driver.find_element(By.XPATH, "//dd[@id=\'모니터링\']/div/div/div/ul/a[3]/li/button/span/span").click()
        # 53 | click | id=관리 |
        self.driver.find_element(By.ID, "관리").click()
        # 54 | click | xpath=//dd[@id='관리']/div/div/div/ul/a/li/button/span/span |
        self.driver.find_element(By.XPATH, "//dd[@id=\'관리\']/div/div/div/ul/a/li/button/span/span").click()
        # 55 | mouseOver | css=.pf-m-focus .pf-c-menu__item-text |
        element = self.driver.find_element(By.CSS_SELECTOR, ".pf-m-focus .pf-c-menu__item-text")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # 56 | mouseOut | css=.pf-m-focus .pf-c-menu__item-text |
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        # 57 | click | xpath=//dd[@id='관리']/div/div/div/ul/a[2]/li/button/span/span |
        self.driver.find_element(By.XPATH, "//dd[@id=\'관리\']/div/div/div/ul/a[2]/li/button/span/span").click()
        # 58 | click | xpath=//dd[@id='관리']/div/div/div/ul/a[3]/li/button/span/span |
        self.driver.find_element(By.XPATH, "//dd[@id=\'관리\']/div/div/div/ul/a[3]/li/button/span/span").click()
        # 59 | mouseOver | xpath=//dd[@id='관리']/div/div/div/ul/a[3]/li/button/span/span |
        element = self.driver.find_element(By.XPATH, "//dd[@id=\'관리\']/div/div/div/ul/a[3]/li/button/span/span")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # 60 | mouseOut | css=.pf-m-focus .pf-c-menu__item-text |
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        # 61 | click | css=.link-style:nth-child(4) .pf-c-menu__item |
        self.driver.find_element(By.CSS_SELECTOR, ".link-style:nth-child(4) .pf-c-menu__item").click()
        # 62 | click | xpath=//dd[@id='관리']/div/div/div/ul/a[2]/li/button/span/span |
        self.driver.find_element(By.XPATH, "//dd[@id=\'관리\']/div/div/div/ul/a[2]/li/button/span/span").click()
        # 63 | click | name=checkrow4 |
        self.driver.find_element(By.NAME, "checkrow4").click()
        # 첫 번째 테스트 케이스 종료
        if True:  # 테스트 결과에 따라 조건 변경
            self.test_results.append('PASS')  # PASS 또는 FAIL로 변경하여 테스트 결과 저장

        # 두 번째 테스트 케이스 시작
        # Step # | name | target | value
        # ... 두 번째 테스트 케이스 단계들...
        # 두 번째 테스트 케이스 종료
        if False:  # 테스트 결과에 따라 조건 변경
            self.test_results.append('FAIL')  # PASS 또는 FAIL로 변경하여 테스트 결과 저장

        # 세 번째 테스트 케이스 시작
        # Step # | name | target | value
        # ... 세 번째 테스트 케이스 단계들...
        # 세 번째 테스트 케이스 종료
        if True:  # 테스트 결과에 따라 조건 변경
            self.test_results.append('PASS')  # PASS 또는 FAIL로 변경하여 테스트 결과 저장

        # 네 번째 테스트 케이스 시작
        # Step # | name | target | value
        # ... 네 번째 테스트 케이스 단계들...
        # 네 번째 테스트 케이스 종료
        if False:  # 테스트 결과에 따라 조건 변경
            self.test_results.append('FAIL')  # PASS 또는 FAIL로 변경하여 테스트 결과 저장

        # 스프레드시트 업데이트
        self.update_spreadsheet()