import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Ваш API-ключ от 2Captcha
API_KEY = "ваш_api_ключ_2captcha"

# Настройки Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

# Открываем страницу с reCAPTCHA
url = "https://cp.icafecloud.com/"
driver.get(url)

# Ждём появления reCAPTCHA
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "g-recaptcha"))
    )
    print("CAPTCHA найдена.")
except Exception as e:
    print("Ошибка:", e)

# Получаем данные для 2Captcha
SITE_KEY = "6LciUK0UAAAAAAcJNWJTe77O56uqJ34KB39yxh7j"  # Публичный ключ CAPTCHA
PAGE_URL = url

# Отправляем запрос на решение CAPTCHA через 2Captcha
response = requests.post(
    "http://2captcha.com/in.php",
    data={
        "key": API_KEY,
        "method": "userrecaptcha",
        "googlekey": SITE_KEY,
        "pageurl": PAGE_URL,
        "json": 1,
    },
)

result = response.json()
if result["status"] != 1:
    print("Ошибка отправки CAPTCHA:", result["request"])
else:
    captcha_id = result["request"]
    print("ID CAPTCHA:", captcha_id)

    # Ждём, пока CAPTCHA будет решена
    while True:
        time.sleep(5)  # Ждём 5 секунд перед проверкой статуса
        result = requests.get(
            f"http://2captcha.com/res.php?key={API_KEY}&action=get&id={captcha_id}&json=1"
        ).json()
        if result["status"] == 1:
            google_token = result["request"]
            print("CAPTCHA решена, токен:", google_token)
            break
        elif result["request"] != "CAPCHA_NOT_READY":
            print("Ошибка решения CAPTCHA:", result["request"])
            break

# Вставляем решённый токен на страницу
driver.execute_script(
    f"document.getElementById('g-recaptcha-response').value = '{google_token}';"
)

# Отправляем форму с помощью Selenium (эмуляция нажатия кнопки "Отправить")
submit_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
)
submit_button.click()

# Ожидаем завершения авторизации
time.sleep(5)

# Закрываем браузер
driver.quit()
