from appium import webdriver
import time

# server 启动参数
desired_caps = dict()
# 设备信息
# 大小写无所谓
desired_caps['platformName'] = 'Android'
# desired_caps['platformName'] = 'iOS'
# 比如版本号5.2.3，可以写成 "5.2.3"，"5.2"，"5"
desired_caps['platformVersion'] = '5.1'
# android随便写，但是不能不写，也不能为空字符串
# IOS不能随便写，写成"Iphone 8"，后面规定就都写
desired_caps['deviceName'] = '192.168.56.101:5555'
# app信息
desired_caps['appPackage'] = 'com.android.browser'
desired_caps['appActivity'] = '.BrowserActivity'
# 解决输入中文的问题  **加入Uiautomator2框架,输入中文问题也可以解决
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
# 这里运用 press_keycode 按回车有点问题,不启用这方法
# desired_caps['automationName'] = 'Uiautomator2'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 获取app包名和启动名
# Windows: adb shell dumpsys window windows | findstr mFocusedApp
# Mac/Linux: adb shell dumpsys window windows | grep mFocusedApp

print(driver.contexts)

print(driver.current_context)

driver.find_element_by_id("com.android.browser:id/url").send_keys("www.baidu.com")

time.sleep(1)

driver.press_keycode(66)

time.sleep(1)

# 切换webview环境,以后再find_element就去找网页的
driver.switch_to.context("WEBVIEW_com.android.browser")

print(driver.current_context)

time.sleep(1)

driver.find_element_by_id("index-kw").send_keys("10086")

driver.find_element_by_id("index-bn").click()

# 切换APP环境,以后再find_element就去找原生的
driver.switch_to.context("NATIVE_APP")

driver.find_element_by_id("com.android.browser:id/url").send_keys("www.zhihu.com")

time.sleep(1)

driver.press_keycode(66)
