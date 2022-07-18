from mytest.utils import create_chrome_driver, add_cookies

browser_driver = create_chrome_driver()
browser_driver.get('https://www.jd.com/')
add_cookies(browser_driver, 'jd.json')  # 添加用户信息cookies,模拟登录
print('this is master modify demo by')
print('this is a modify conflict demo by hot-fix')
print('push test')
print('push test')
