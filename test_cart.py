from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_add_to_cart(driver, wait):
    driver.get("https://demoblaze.com/")

    # Находим первую карточку товара и кликаем по названию
    first_product_link = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".card-title a"))
    )

    product_name = first_product_link.text
    first_product_link.click()

    # Ждём кнопку «Add to cart» и нажимаем
    add_to_cart_btn = wait.until(
       EC.element_to_be_clickable((By.CSS_SELECTOR,"a.btn.btn-success.btn-lg"))
    )
    add_to_cart_btn.click()

    # Ждём появления модального окна
    wait.until(EC.alert_is_present())

    alert = driver.switch_to.alert
    alert.accept()

    # Переходим в корзину, чтобы проверить товар
    cart_link = driver.find_element(By.ID, "cartur")
    cart_link.click()

    # Проверяем наличие товара

    cart_item = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, f"//tr[contains(@class, 'success')][.//td[contains(text(), '{product_name}')]]")
        )
    )

    place_order_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Place Order']"))
    )
    place_order_btn.click()

