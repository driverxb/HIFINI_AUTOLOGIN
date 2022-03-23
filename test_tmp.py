from datetime import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options # 这个是用来实现无可视化和反检测

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
    driver = webdriver.Chrome(options=chrome_options)
    #driver = webdriver.Chrome()
    driver.get("https://hifini.com") 
    listcookie = [
        {
            'domain': '.hifini.com', 
            'httpOnly': False, 
            'name': 'Hm_lpvt_4ab5ca5f7f036f4a4747f1836fffe6f2', 
            'path': '/', 
            'secure': False, 
            'value': '1646890264'},
        {
            'domain': '.hifini.com', 
            'expiry': 1678423475, 
            'httpOnly': False, 
            'name': 'Hm_lvt_4ab5ca5f7f036f4a4747f1836fffe6f2', 
            'path': '/', 
            'secure': False, 
            'value': '1646873245,1646881609'}, 
        {
            'domain': 'hifini.com', 
            'expiry': 1655527474, 
            'httpOnly': True, 
            'name': 'bbs_sid', 
            'path': '/', 
            'secure': False, 
            'value': '82dcfke0ceb2ee79bju2sh6v16'},
        {
            'domain': 'hifini.com', 
            'expiry': 1655527474, 
            'httpOnly': True, 
            'name': 'bbs_token', 
            'path': '/', 
            'secure': False, 
            'value': 'dkQ5DtB5F1_2FN_2B7lw0_2F1ogpiLSyPl0mU2foe8vvisqSQEX46vx2xLvcqDM4olHCoQwUIucBO_2BGbklyra9iJBRLQwyFYo_3D'}
     ]
    # 读取cookie并添加cookie
    for Cookie in listcookie:
        driver.add_cookie(Cookie)
    driver.refresh() # 用注入的cookie刷新页面
    sign = driver.find_element(By.ID,"sign") # 找到签到签到标签  
    #M_S_input = input("Please input Minutes: 01:11 ")
    out_file = open('sign_hifini.txt',mode='a+',encoding='UTF-8') # 输出签到记录到文本文件
    time_now = datetime.now().strftime("%H:%M:%S.%f")
    if sign.text == '签到': 
        while True:
            if time_now >= "00:00:00.000000" and time_now <= "00:00:10.000000":
                sign.click() # 对签到标签进行点击操作
                time.sleep(1)
                break # 退出循环 
            print(time_now)
            time_now = datetime.now().strftime("%H:%M:%S.%f")
    out_file.write('恭喜您在 '+datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f ")+'和 '+time_now+' 时刻对 '+driver.title+' 进行了签到!!! \n')
    out_file.close() # 关闭文件并释放内存
    driver.quit() # 关闭Chrome Broswer 并释放内存资源
