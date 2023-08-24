from selene import browser


def test_valid_login():
    browser.config.hold_driver_at_exit = True
    browser.open('https://demoqa.com/text-box')
    browser.element('#userName').type('Lina Alekseeva').press_tab()
    browser.element('#userEmail').type('qa@guru.ru').press_tab()
    browser.element('#currentAddress').type('Address').press_tab()
    browser.element('#permanentAddress').type('Permanent Address').press_enter()
    browser.element('#submit').click()
