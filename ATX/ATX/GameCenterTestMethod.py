import atx


def navigateToMainActivity(driver):
    driver.click_image('./images/wizard-enter.1080x1920.png', timeout=5, safe=True)
    driver.click(266, 1844)


def navigateToWelfareFragment(driver):
    driver.click_image('./images/welfare-channel-enter.1080x1920.png', timeout=5, safe=True)
    driver.click(551, 930)


def initializeAtx(package_name):
    driver = atx.connect()
    driver.start_app(package_name)
    driver.image_path = ['.', './images']
    return driver
