from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager


class InstaBot:
    def __init__(self, username, pw):
        self.username = username
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")
        time.sleep(2)
        # facebook login
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[6]/button/span[2]').click()
        time.sleep(2)
        #  username
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[1]/input').send_keys(username)
        # password
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[2]/input').send_keys(pw)
        # click on login
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[3]/button').click()
        # click on not now for a pop up
        time.sleep(10)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click()

        time.sleep(5)

    def get_unfollowers(self):
        # go to my profile
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a').click()
        time.sleep(2)
        # click on following
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]").click()
        following = self.get_names()
        # click on followers
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]").click()
        followers = self.get_names()
        # Generate list for not following
        not_following_back = [user for user in following if user not in followers]
        #print(followers)
        print(not_following_back)

    def get_names(self):
        time.sleep(2)
        # click on followers
        #self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a').click()
        #time.sleep(1)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            time.sleep(2)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        # close button
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/button').click()
        return names


my_bot = InstaBot('vaishrk98@gmail.com', '.')
my_bot.get_unfollowers()
