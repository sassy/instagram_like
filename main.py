from selenium import webdriver

URL = "https://www.instagram.com/?hl=ja"

def like_instagram(username, password):
    driver = webdriver.Chrome('./chromedriver')
    driver.get(URL)
    driver.find_element_by_class_name('_b93kq').click()
    driver.find_element_by_name('username').send_keys(username)
    driver.find_element_by_name('password').send_keys(password)
    driver.implicitly_wait(2)
    driver.find_elements_by_tag_name('button')[0].submit()
    tags = driver.find_elements_by_class_name('coreSpriteHeartOpen')
    for tag in tags:
        tag.click()

    driver.quit()


if __name__ == '__main__':
    import fire
    fire.Fire(like_instagram)
