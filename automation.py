# from selenium import webdriver
from selenium import webdriver
edge_browser = webdriver.Edge('./msedgedriver.exe')
# by default it searches the driver file in the path of Windows folder in the C drive

# print(edge_browser)
edge_browser.maximize_window()
edge_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

# print('Selenium Easy Demo' in edge_browser.title)
# # we are checking here whether we are on the same page or not, if yes, it will return true

assert 'Selenium Easy Demo' in edge_browser.title
# # if the above is not true, assert will error out, otherwise code will continue

show_message_button = edge_browser.find_element_by_class_name("btn-default")
# the above command basically grabs this
# <button type="button" onclick="showInput();" class="btn btn-default">Show Message</button>

# we can find that button by CSS selector as well, using the below command
# show_message_button = edge_browser.find_element_by_css_selector('#get-input > .btn')


# print(button_text)
# print(show_message_button.get_attribute('innerHTML'))

assert 'Show Message' in edge_browser.page_source

user_message = edge_browser.find_element_by_id("user-message")
user_message.clear()    # to clear any previous message
user_message.send_keys("Hello there!")     # selenium is typing the message

show_message_button.click()     # selenium is clicking the button

output_message = edge_browser.find_element_by_id('display')

print('Hello there!' in output_message.text)
print(output_message.get_attribute('innerHTML'))

assert 'Hello there!' in output_message.text

edge_browser.close()
