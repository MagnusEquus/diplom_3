main_url = "https://stellarburgers.nomoreparties.site/"
login_url = "https://stellarburgers.nomoreparties.site/login"
forgot_password_url = "https://stellarburgers.nomoreparties.site/forgot-password"
reset_password_url = "https://stellarburgers.nomoreparties.site/reset-password"
profile_url = "https://stellarburgers.nomoreparties.site/account/profile"
order_history_url = "https://stellarburgers.nomoreparties.site/account/order-history"
feed_url = "https://stellarburgers.nomoreparties.site/feed"

restore_pass_xpath = "//a[@href='/forgot-password']"
restore_pass_button_xpath = "//button[text()='Восстановить']"
reset_mail_input_xpath = "//input[@type='text']"
input_new_pass_xpath = "//input[@name='Введите новый пароль']"
new_pass_show_xpath = "//div[@class='input__icon input__icon-action']"
new_pass_input_parent_xpath = "//input[@name='Введите новый пароль']/parent::*"
account_link_xpath = "//a[@href='/account']"
input_login_email_xpath = "//input[@type='text']"
input_login_pass_xpath = "//input[@type='password']"
login_button_xpath = "//button[text()='Войти']"
order_history_button_xpath = "//a[text()='История заказов']"
logout_button_xpath = "//button[text()='Выход']"
constructor_button_xpath = "//p[text()='Конструктор']"
feed_link_button_xpath = "//p[text()='Лента Заказов']"
ingredient_popup_xpath = "//h2[text()='Детали ингредиента']"
first_ingredient_xpath = "//ul[contains(@class,'BurgerIngredients_ingredients__list')][1]/a[1]"
ingredient_popup_close_xpath = "//section[contains(@class,'Modal_modal_opened')]/div[contains(@class,'Modal_modal__container')]/button"
ingredient_counter_value_xpath = "//ul[contains(@class,'BurgerIngredients_ingredients__list')][1]/a[1]/div[1]/p"
constructor_bun_first_dragndrop_xpath = "//span[text()='Перетяните булочку сюда (верх)']"
order_button_xpath = "//button[text()='Оформить заказ']"
feed_first_order_xpath = "//ul[contains(@class,'OrderFeed_list')][1]"
feed_close_order_popup_xpath = "//section[contains(@class,'Modal_modal_opened')]/div[contains(@class,'Modal_modal__container')]/button"
order_close_new_order_popup_xpath = "//section[contains(@class,'Modal_modal_opened')]/div[contains(@class,'Modal_modal__container')]/button"
order_history_first_order_number_xpath = "//ul[contains(@class,'OrderHistory_profileList__')]/li[1]/a/div[1]/p[1]"
feed_order_list_xpath = "//ul[contains(@class,'OrderFeed_list')]"
feed_order_number_xpath = "//ul[contains(@class,'OrderFeed_list')]/li[ELEMENTNUMBER]/a/div[1]/p[1]"
feed_orders_today_xpath = "//div[contains(@class,'OrderFeed_ordersData')]/div[3]/p[2]"
feed_orders_overall_xpath = "//div[contains(@class,'OrderFeed_ordersData')]/div[2]/p[2]"
feed_ordernumber_in_progress_xpath = "//ul[contains(@class, 'OrderFeed_orderListReady')]/li[text()='ORDERNUMBER']"
