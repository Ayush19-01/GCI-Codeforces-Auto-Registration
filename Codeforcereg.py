#Made for the sole purpose of GCI 2019
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
a=input('Handle(must be unique): ')
b=input('Email-id(Must be unused before): ')
c=input('Password(strong and difficult to crack): ')
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://codeforces.com/register')
h1=driver.find_element_by_name('handle')
h1.send_keys(a)
e1=driver.find_element_by_name('email')
e1.send_keys(b)
p1= driver.find_element_by_name('password')
p1.send_keys(c)
p2= driver.find_element_by_name('passwordConfirmation')
p2.send_keys(c)
register=driver.find_element_by_class_name('submit')
register.click()
