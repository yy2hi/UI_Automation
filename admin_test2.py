from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class WebDriver:
    def __init__(self):
        self.driver = self._initialize_driver()
        self.wait = WebDriverWait(self.driver, 10)  # WebDriverWait 객체 생성

    def _initialize_driver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--disable-web-security")
        chrome_options.add_argument("--remote-allow-origins=*")
        chrome_options.add_experimental_option("detach", True)
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    def click(self, element):
        ActionChains(self.driver).click(element).perform()

    def find_element(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)

    def admin_login(self, url, username, password):
        self.driver.get(url)
        id_input = self.find_element('//*[@id="root"]/div/div[2]/form/div[3]/div[1]/div[2]/input')
        pw_input = self.find_element("//*[@id='root']/div/div[2]/form/div[3]/div[2]/div[2]/input")

        id_input.clear()
        id_input.send_keys(username)

        pw_input.clear()
        pw_input.send_keys(password)

        login_btn = self.find_element('//*[@id="root"]/div/div[2]/form/span/button')
        self.click(login_btn)
        self.wait.until(EC.url_contains("admin"))  # admin 페이지가 로드될 때까지 대기

    def navigate_to_instance_registration(self):
        lnb_host_os_btn = self.find_element('//*[@id="호스트 OS"]/span[1]')
        self.click(lnb_host_os_btn)

        lnb_host_os_instance_btn = self.find_element('//*[@id="호스트 OS"]/div/div/div/ul/a[1]/li/button/span/span')
        self.click(lnb_host_os_instance_btn)

        add_instance = self.find_element('//*[@id="toggle-basic"]')
        self.click(add_instance)

        regi_instance = self.find_element('//*[@id="root"]/div[3]/div/div[1]/div/div/div[2]/div[1]/div/ul/li[2]/a')
        self.click(regi_instance)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="input"]')))  # 입력란이 나타날 때까지 대기


    def register_instance(self, instance_name):
        instance_input = self.find_element('//*[@id="input"]')
        instance_input.clear()
        instance_input.send_keys(instance_name)

        click_regi_instance = self.find_element('//*[@id="pf-modal-part-3"]/footer/button[2]')
        self.click(click_regi_instance)
        self.wait.until(EC.invisibility_of_element_located((By.XPATH, '//*[@id="pf-modal-part-3"]')))  # 모달이 사라질 때까지 대기


    def close(self):
        self.driver.close()

def main():
    # WebDriver 인스턴스 생성
    driver = WebDriver()

    # 어드민 로그인
    driver.admin_login(url="http://172.21.5.8/admin/#/login",
                       username="admin",
                       password="tmax@23")

    # 인스턴스 등록 페이지로 이동
    driver.navigate_to_instance_registration()

    # 인스턴스 등록
    driver.register_instance(instance_name="abcde")

    # WebDriver 종료
    driver.close()

if __name__ == "__main__":
    main()