from selenium import webdriver
import time

URL = "https://www.instagram.com/?hl=ja"
WAIT_TIME = 1800

class InstagramAgent():
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def like_instagram(self):
        driver = webdriver.Chrome('./chromedriver')
        driver.get(URL)
        driver.find_element_by_class_name('_b93kq').click()
        driver.find_element_by_name('username').send_keys(self.username)
        driver.find_element_by_name('password').send_keys(self.password)
        driver.implicitly_wait(2)
        driver.find_elements_by_tag_name('button')[0].submit()
        tags = driver.find_elements_by_class_name('coreSpriteHeartOpen')
        for tag in tags:
            tag.click()
        driver.quit()

    def like_instagram_loop(self, wait_time=WAIT_TIME):
        while True:
            self.like_instagram()
            time.sleep(wait_time)


if __name__ == '__main__':
    import fire
    fire.Fire(InstagramAgent)
