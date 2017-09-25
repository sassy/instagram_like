from selenium import webdriver
import time

URL = "https://www.instagram.com/?hl=ja"
WAIT_TIME = 1800
WAIT_LOADING_TIME = 5

class InstagramAgent(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def like_instagram(self):
        driver = webdriver.Chrome('./chromedriver')
        driver.get(URL)
        driver.find_element_by_class_name('_b93kq').click()
        send_key = lambda x, y: driver.find_element_by_name(x).send_keys(y)
        send_key('username', self.username)
        send_key('password', self.password)
        driver.implicitly_wait(2)
        driver.find_elements_by_tag_name('button')[0].submit()
        for i in range(5):
            tags = driver.find_elements_by_class_name('coreSpriteHeartOpen')
            for tag in tags:
                tag.click()
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(WAIT_LOADING_TIME)
        driver.quit()

    def like_instagram_loop(self, wait_time=WAIT_TIME):
        while True:
            self.like_instagram()
            time.sleep(wait_time)


if __name__ == '__main__':
    import fire
    fire.Fire(InstagramAgent)
