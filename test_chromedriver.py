from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options # 这个是用来实现无可视化和反检测
import os,sys

if __name__=='__main__':
    # 设置Chromedriver参数,实现让selenium实现无界面和不被检测到的风险
    chrome_options = Options()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging','enable-automation'])
    chrome_options.add_argument('--no-sandbox') # 解决DevToolsActivePort文件不存在的报错
    chrome_options.add_argument('window-size=1920x3000')  # 指定浏览器分辨率
    chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
    #chrome_options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
    chrome_options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
    chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面.
    chrome_options.add_argument('--incognito')  # 隐身模式（无痕模式）
    chrome_options.add_argument('--disable-infobars')  # 禁用浏览器正在被自动化程序控制的提示
    chromedriver = "d:/a/hifini_autologin/hifini_autologin/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(options=chrome_options,executable_path=chromedriver)
    driver.get("https://hifini.com")
    print(sys.stdout.encoding)
    print(sys.getdefaultencoding())
    print(sys.getfilesystemencoding())
    print(driver.title.encode("GB2312"))
    driver.quit()
