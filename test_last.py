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
    listcookie = [
        {
            'name': 'Hm_lvt_4ab5ca5f7f036f4a4747f1836fffe6f2',
            'value': '1647767150,1647770028,1647770511,1647822281'}, 
        {
            'name': 'bbs_sid', 
            'value': 't8k2ummrfs6e6ldd3j4l76qcn8'},
        {
            'name': 'bbs_token', 
            'value': 'NIggccPbSZlrwG4soWASP10R8q8TqwbwqB0VFSFu7v_2Ffxun_2Frm71Rx_2B5eFMFhn7U83qldqJZI7ozUOhn0reZ6ZDrzBQ_3D'}
     ]
    # 读取cookie并添加cookie
    for Cookie in listcookie:
        driver.add_cookie(Cookie)
    driver.refresh() # 用注入的cookie刷新页面
    sg_sign = driver.find_element(By.ID,"sg_sign") # 找到签到签到标签  
    while True:
        time_now = time.strftime("%H:%M:%S",time.localtime())
        if time_now == "09:30:00" :
            sg_sign.click() # 对签到标签进行点击操作
            break # 退出循环 
    sleep(1)
    driver.save_screenshot(datetime.now().strftime("%Y-%m-%d-%H-%M-%S")+'.png') #屏幕截图保存       
    driver.get('https://sctapi.ftqq.com/SCT130527TxL3yQVPGSag7mZ8b6XJ68Kz2.send?title=Hifini_web_Sign&desp='+'Localtime  恭喜您在 '+datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f ")+'和 '+time_now+' 时刻对 '+driver.title+' 进行了签到!!! \n')  
    driver.quit() # 关闭Chrome Broswer 并释放内存资源
