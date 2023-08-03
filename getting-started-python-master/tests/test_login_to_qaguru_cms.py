from selene import browser, have


def test_valid_login():
    browser.config.hold_driver_at_exit = True


browser.open('https://qa.guru/cms/system/login?required=true')
browser.element('.login-form [name =email]').type('qagurubot@gmail.com').press_tab()
browser.element('[name =email]').type('qagurupassword').press_enter()

browser.element('.login-form.btn-success').click()
browser.element('.logined-form').should(have.text('QA_GURU_BOT'))
test_valid_login()
