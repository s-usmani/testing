import unittest
import os
import time


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


class MinWebTest(unittest.TestCase):
    # execute the test <x = 0, y = 0, z = 0, submitButton = click> and check the output message is correct
    # Wanted to use chrome instead

    def test0(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(ChromeDriverManager().install(), options = chrome_options)
        cwd = os.getcwd()
        print(cwd)
        # edit the next line to enter the location of "min.html" on your system
        driver.get(r"file:///Users/personalizedmac/Documents/Junior Year/Software Lab/classGitHub/UsmaniSyed/tutorial8/part2/min.html")
        elem = driver.find_element_by_id('x')
        elem.send_keys(0) # enter a representative for x
        elem = driver.find_element_by_id('y')
        elem.send_keys(0) # enter a representative for y
        elem = driver.find_element_by_id('z')
        elem.send_keys(0) # enter a representative for z
        elem = driver.find_element_by_id('computeButton')
        elem.click() #click the button
        result = driver.find_element_by_id('result')
        output = result.text # read the output text
        self.assertEqual("min(0, 0, 0) = 0", output)
        driver.quit() # close the browser window

    def test1(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(ChromeDriverManager().install(), options = chrome_options)
        # edit the next line to enter the location of "min.html" on your system
        driver.get(r"file:///Users/personalizedmac/Documents/Junior Year/Software Lab/classGitHub/UsmaniSyed/tutorial8/part2/min.html")
        elem = driver.find_element_by_id('x')
        elem.send_keys(0) # enter a representative for x
        elem = driver.find_element_by_id('y')
        elem.send_keys(0) # enter a representative for y
        elem = driver.find_element_by_id('z')
        elem.send_keys(1) # enter a representative for z
        elem = driver.find_element_by_id('computeButton')
        elem.click() #click the button
        result = driver.find_element_by_id('result')
        output = result.text # read the output text
        self.assertEqual("min(0, 0, 1) = 0", output)
        driver.quit() # close the browser window

    def test2(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(ChromeDriverManager().install(), options = chrome_options)
        # edit the next line to enter the location of "min.html" on your system
        driver.get(r"file:///Users/personalizedmac/Documents/Junior Year/Software Lab/classGitHub/UsmaniSyed/tutorial8/part2/min.html")
        elem = driver.find_element_by_id('x')
        elem.send_keys(-1) # enter a representative for x
        elem = driver.find_element_by_id('y')
        elem.send_keys(1) # enter a representative for y
        elem = driver.find_element_by_id('z')
        elem.send_keys(1) # enter a representative for z
        elem = driver.find_element_by_id('computeButton')
        result = driver.find_element_by_id('result')
        output = result.text # read the output text
        self.assertEqual("", output)
        driver.quit() # close the browser window

    def test3(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(ChromeDriverManager().install(), options = chrome_options)
        # edit the next line to enter the location of "min.html" on your system
        driver.get(r"file:///Users/personalizedmac/Documents/Junior Year/Software Lab/classGitHub/UsmaniSyed/tutorial8/part2/min.html")
        elem = driver.find_element_by_id('x')
        elem.send_keys(1) # enter a representative for x
        elem = driver.find_element_by_id('y')
        elem.send_keys(1) # enter a representative for y
        elem = driver.find_element_by_id('z')
        elem.send_keys(-1) # enter a representative for z
        elem = driver.find_element_by_id('computeButton')
        elem.click() #click the button
        result = driver.find_element_by_id('result')
        output = result.text # read the output text
        self.assertEqual("min(1, 1, -1) = -1", output)
        driver.quit() # close the browser window

    def test4(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(ChromeDriverManager().install(), options = chrome_options)
        # edit the next line to enter the location of "min.html" on your system
        driver.get(r"file:///Users/personalizedmac/Documents/Junior Year/Software Lab/classGitHub/UsmaniSyed/tutorial8/part2/min.html")
        elem = driver.find_element_by_id('x')
        elem.send_keys(1) # enter a representative for x
        elem = driver.find_element_by_id('y')
        elem.send_keys(0) # enter a representative for y
        elem = driver.find_element_by_id('z')
        elem.send_keys(-1) # enter a representative for z
        elem = driver.find_element_by_id('computeButton')
        result = driver.find_element_by_id('result')
        output = result.text # read the output text
        self.assertEqual("", output)
        driver.quit() # close the browser window

    def test5(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        # edit the next line to enter the location of "min.html" on your system
        driver.get(r"file:///Users/personalizedmac/Documents/Junior Year/Software Lab/classGitHub/UsmaniSyed/tutorial8/part2/min.html")
        elem = driver.find_element_by_id('x')
        elem.send_keys(0) # enter a representative for x
        elem = driver.find_element_by_id('y')
        elem.send_keys(-1) # enter a representative for y
        elem = driver.find_element_by_id('z')
        elem.send_keys(-1) # enter a representative for z
        elem = driver.find_element_by_id('computeButton')
        elem.click() #click the button
        result = driver.find_element_by_id('result')
        output = result.text # read the output text
        self.assertEqual("min(0, -1, -1) = -1", output)
        driver.quit() # close the browser window

if __name__ == '__main__':
    unittest.main()
