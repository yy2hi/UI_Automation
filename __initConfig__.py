def webdriver():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--disable-web-security")
    chrome_options.add_argument("--remote-allow-origins=*")
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

# def driver_path():
#     return r"C:\Users\tmax\Desktop\pythonProject\driver\chromedriver.exe"

def admin_url():
    return "http://172.21.5.8/admin/#/login"

def tenant_url():
    return "http://172.21.5.8/tenant/#/login"

def admin_info():
    return {"id": "admin", "pw": "tmax@23"}