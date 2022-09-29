from page_object.HomePage import HomePage


class RegPage(HomePage):
    CSS_REG_DETAILS = '.required.form-group'
    _CSS_BTN_YES = 'label.radio-inline [value="1"]'
    _CSS_BTN_NO = 'label.radio-inline [value="0"]'
    _CSS_SUBCRIBE = '.form-horizontal > fieldset:nth-child(3) > div:nth-child(2) > label:nth-child(1)'
    _CSS_CHECKBOX_POLICY = '[type=checkbox]'
    _CSS_BTN_POLICY = '.agree'
    _CSS_MODAL_POLICY = '.modal-content'
    _CSS_BTN_POLICY_CLOSE = '.close'
    _CSS_BTN_LOGIN_PAGE = '#content > p:nth-child(2) > a'
    _CSS_FIRST_NAME = '#input-firstname'
    _CSS_LAST_NAME = '#input-lastname'
    _CSS_EMAIL = '#input-email'
    _CSS_TELEPHONE = '#input-telephone'
    _CSS_INPUT_CONFIRM = '#input-confirm'
    _PASSWORD = 'password'
    _TEXT_CREATE_ACCOUNT = 'Your Account Has Been Created!'

    def convert_tuple(self, list_elements):
        return tuple([element.text for element in list_elements])

    def click_subscribe_btn_yes(self):
        self.waiting_element(self._CSS_SUBCRIBE)
        self.waiting_element(self._CSS_BTN_YES).click()

    def click_subscribe_btn_no(self):
        self.waiting_element(self._CSS_SUBCRIBE)
        self.waiting_element(self._CSS_BTN_NO).click()

    def click_agree_policy(self):
        self.waiting_element(self._CSS_CHECKBOX_POLICY).click()

    def check_privacy_policy(self):
        self.waiting_element(self._CSS_BTN_POLICY).click()
        self.waiting_element(self._CSS_MODAL_POLICY)
        self.waiting_element(self._CSS_BTN_POLICY_CLOSE).click()

    def input_user_data(self, user_data: dict):
        first_name, last_name, email, telephone = user_data.values()
        self.input_value(self._CSS_FIRST_NAME, first_name)
        self.input_value(self._CSS_LAST_NAME, last_name)
        self.input_value(self._CSS_EMAIL, email)
        self.input_value(self._CSS_TELEPHONE, telephone)

    def input_login_page(self, email: str, password: str):
        self.waiting_element(self._CSS_BTN_LOGIN_PAGE).click()
        self.input_email(email)
        self.input_password(password)

    def input_password_confirm(self, dict_pass: dict):
        password = dict_pass.get(self._PASSWORD)
        self.input_password(password)
        self.input_value(self._CSS_INPUT_CONFIRM, password)

    def check_text_create_account(self):
        self.waiting_title(self._TEXT_CREATE_ACCOUNT)
