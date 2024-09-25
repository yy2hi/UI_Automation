import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# webdriver 생성
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--disable-web-security")
chrome_options.add_argument("--remote-allow-origins=*")
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

wait = WebDriverWait(driver, 10)

# Finds element by XPath
def admin_url():
    return "http://172.21.5.8/admin/#/login"

def tenant_url():
    return "http://172.21.5.8/tenant/#/login"

# 어드민 페이지 열기
driver.get(url=admin_url())

# 사용할 ID와 비밀번호를 지정합니다.
admin_id = "admin"
admin_pw = "tmax@23"

# ID 입력란을 찾아서 클릭하고 ID를 입력합니다.
id_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/form/div[3]/div[1]/div[2]/input')
ActionChains(driver).click(id_input).perform()
id_input.clear()
id_input.send_keys(admin_id)

# 비밀번호 입력란을 찾아서 클릭하고 비밀번호를 입력합니다.
pw_input = driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/form/div[3]/div[2]/div[2]/input")
ActionChains(driver).click(pw_input).perform()
pw_input.clear()
pw_input.send_keys(admin_pw)

# 로그인 버튼 클릭
login_btn = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/form/span/button')
ActionChains(driver).click(login_btn).perform()
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="호스트 OS"]/span[1]')))
time.sleep(0.5)

# lnb 호스트 os 클릭
lnb_host_os_btn = driver.find_element(By.XPATH, '//*[@id="호스트 OS"]/span[1]')
ActionChains(driver).click(lnb_host_os_btn).perform()

# lnb 호스트 os > 인스턴스 클릭
lnb_host_os_instance_btn = driver.find_element(By.XPATH, '//*[@id="호스트 OS"]/div/div/div/ul/a[1]/li/button/span/span')
ActionChains(driver).click(lnb_host_os_instance_btn).perform()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//Your/Expected/XPath')))
# # 인스턴스 추가 클릭
# add_instance = driver.find_element(By.XPATH, '//*[@id="toggle-basic"]')
# ActionChains(driver).click(add_instance).perform()

# # 인스턴스 추가 > 인스턴스 등록 클릭
# regi_instance = driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/div/div/div[2]/div[1]/div/ul/li[2]/a')
# ActionChains(driver).click(regi_instance).perform()
# wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="input"]')))

# # [인스턴스 등록 모달창] 인스턴스 이름 기입
# host_os_instance1 = "bcde"
# instance_input = driver.find_element(By.XPATH, '//*[@id="input"]')
# ActionChains(driver).click(instance_input).perform()
# instance_input.send_keys(host_os_instance1)
#
# # [인스턴스 등록 모달창] 등록 클릭
# click_regi_instance = driver.find_element(By.XPATH, '//*[@id="pf-modal-part-3"]/footer/button[2]')
# ActionChains(driver).click(click_regi_instance).perform()
# wait.until(EC.invisibility_of_element_located((By.XPATH, '//*[@id="pf-modal-part-3"]')))

# 인스턴스 이름 클릭 -> 상세 페이지 접근
detail_host_os = driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/div/div/div[3]/div/div/table/tbody/tr[1]/td[2]/a')
ActionChains(driver).click(detail_host_os).perform()

# master8 상세 페이지에서 eno2 행 찾기
text_to_find_PNIC = "eno2"
row_xpath = f'//td[@data-label="이름" and contains(text(), "{text_to_find_PNIC}")]/../td[@class="pf-c-table__check"]/label/input'

# 해당 행의 체크박스 클릭
checkbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, row_xpath)))
checkbox.click()

# 편집 버튼이 포함된 div 요소의 일부 속성을 사용하여 XPath를 작성
edit_button_xpath = '//button[contains(text(), "편집")]'
edit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, edit_button_xpath)))

# 편집 버튼 클릭
ActionChains(driver).click(edit_button).perform()

# eno2 편집 버튼 클릭
edit_PNIC = driver.find_element(By.XPATH, '//*[@id="pf-tab-section-0-pf-1710479651199fy45htzaa"]/div/div[1]/div/button')
ActionChains(driver).click(edit_PNIC).perform()

# 인터페이스 편집 모달창에서 용도 목록 열기
edit_button_xpath = '//*[@id="pf-tab-section-0-pf-1710479651199fy45htzaa"]/div/div[1]/div/button'
edit_PNIC = driver.find_element(By.XPATH, '//*[@id="pf-select-toggle-id-12"]')
ActionChains(driver).click(edit_PNIC).perform()

# 용도 목록에서 data-isp 행 찾기
text_to_find_usage = "data-isp"
ow_xpath = f'//td[@data-label="용도" and contains(text(), "{text_to_find_usage}")]/../td[@class="pf-c-table__check"]/label/input'

# 해당 행의 체크박스를 클릭
checkbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, row_xpath)))
checkbox.click()






# # 인스턴스 등록 후 체크박스가 나타날 때까지 대기합니다.
# checkbox_parent_xpath = '//*[@id="root"]/div[3]/div/div[1]/div/div/div[3]/div/div/table/tbody'
# checkbox_index = 1  # 이 숫자를 등록 후 나타나는 체크박스의 인덱스로 설정합니다.
# checkbox_xpath = f'{checkbox_parent_xpath}/tr[{checkbox_index}]/td[1]/label/input'
# checkbox = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, checkbox_xpath)))
# checkbox.click()

# 브라우저를 종료합니다.
#driver.close()