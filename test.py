from selenium import webdriver
import pandas as pd
import base64
import copy
from contextlib import contextmanager
import pkgutil
import warnings
from selenium.common.exceptions import (InvalidArgumentException,
                                        WebDriverException,
                                        NoSuchCookieException,
                                        UnknownMethodException,
                                        NoSuchElementException,
                                        ElementNotInteractableException)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.html5.application_cache import ApplicationCache
from selenium.webdriver import ActionChains

a = webdriver.Firefox()
a.get('https://www.facebook.com/friends/requests/?fcref=jwl')
a.find_element_by_id('email').send_keys('7871978954')
a.find_element_by_id('pass').send_keys('')
a.find_element_by_id('loginbutton').click()


