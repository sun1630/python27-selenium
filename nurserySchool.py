#-*-coding=utf-8-*-

from selenium import webdriver
from selenium.webdriver.support.select import Select
import os
import win32api,win32con

'''
import requests
from StringIO import StringIO
from PIL import Image,ImageEnhance,ImageFilter
import pytesseract
import numpy as np

## 识别验证码
def ocr(img_path):
    # 二值化  
    threshold = 140  
    table = []  
    for i in range(256):  
        if i < threshold:  
            table.append(0)  
        else:  
            table.append(1) 
    
    image = requests.get(img_path)
    img = None
    if image.status_code == requests.codes.ok:
       img = Image.open(StringIO(image.content))
       img.save('a_code.png')
       #new_img=img.resize((300,50), Image.ANTIALIAS) 

       enh_col = ImageEnhance.Color(img)
       color = 1.5
       new_img = enh_col.enhance(color)

       new_img = new_img.convert('L') 
       #对比度增强
       enh_con = ImageEnhance.Contrast(new_img)
       contrast = 9
       image_contrasted = enh_con.enhance(contrast)
       image_contrasted.save('b.png')
       image_contrasted.load()
       text = pytesseract.image_to_string(image_contrasted, lang='eng')
       #print text.strip().replace(' ', '')
       return text.strip().replace(' ', '')
    return ''
'''
'''
## 修改注册表
def setReg():
    reg_root = win32con.HKEY_LOCAL_MACHINE
    reg_path = r"SOFTWARE\Google\Chrome\MachineLevelUserCloudPolicyEnrollmen"
    reg_flags = win32con.WRITE_OWNER|win32con.KEY_WOW64_64KEY|win32con.KEY_ALL_ACCESS
 
    #直接创建（若存在，则为获取）
    key, _ = win32api.RegCreateKeyEx(reg_root, reg_path, reg_flags)
     
    #设置项
    win32api.RegSetValueEx(key, "", 0, win32con.REG_SZ, 'This is a test item')
     
    #关闭
    win32api.RegCloseKey(key)
    
    
    #reg_path = r'HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Google\Chrome'
    #reg_flags = win32con.WRITE_OWNER|win32con.KEY_WOW64_64KEY|win32con.KEY_ALL_ACCESS

    #直接创建
    #win32api.RegCreateKey(r'HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Google\Chrome','MachineLevelUserCloudPolicyEnrollmen')
    #设置项
    #win32api.RegSetValueEx(r'HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Google\Chrome\MachineLevelUserCloudPolicyEnrollmen', '', 0, win32con.REG_SZ, 'python selenium')
 
    #关闭
    #win32api.RegCloseKey(r'HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Google\Chrome\MachineLevelUserCloudPolicyEnrollmen')
'''
## 录入信息
def addInfo():
    driver = webdriver.Chrome('./webBrowser/chromedriver')  # Optional argument, if not specified will search path.
    driver.maximize_window()
    
    driver.get("http://2018.dm2y.com:8082/")
    
    name = driver.find_element_by_id('Options_0').send_keys(u'张三')
    sex = driver.find_element_by_xpath('//*/input[@name="Options_1"][1]')
    sex.click()

    brithday = driver.find_element_by_name('Options_2')
    brithday.click()
    tbSelYear = driver.find_element_by_id('tbSelYear')
    Select(tbSelYear).select_by_value('2015')
    tbSelMonth = driver.find_element_by_id('tbSelMonth')
    Select(tbSelMonth).select_by_value('2')
    tbSelDay = driver.find_element_by_xpath('//div[@id="calendardiv"]/table/tbody/tr[2]/td[1]/div[1]/table/tbody/tr[4]/td[3]')
    tbSelDay.click()

    idCard = driver.find_element_by_id('Options_3').send_keys('130425201502177280')
    phone = driver.find_element_by_id('Options_4').send_keys('18201111111')
    addr = driver.find_element_by_id('Options_5').send_keys(u'河北省邯郸市大名县名城首府7号楼2单元1102')

    file_path = os.path.abspath('recent.jpg')
    driver.switch_to_frame(driver.find_element_by_xpath('//span[@id="Qs_Imgs_32"]/div[1]/iframe'))
    recentPhotos = driver.find_element_by_id('fileField')
    recentPhotos.send_keys(file_path.decode('gbk'))

    driver.switch_to.default_content()
    file_path1 = os.path.abspath('hukou.jpg')
    driver.switch_to_frame(driver.find_element_by_xpath('//span[@id="Qs_Imgs_17"]/div[1]/iframe'))
    hukouPhoto = driver.find_element_by_id('fileField')
    hukouPhoto.send_keys(file_path1.decode('gbk'))

    driver.switch_to.default_content()
    img_path = driver.find_element_by_xpath('//form[@id="Ss_Form_list"]/div[2]/img[1]')
    '''
    #识别率低
    code = ocr(img_path.get_attribute('src')) ## 识别验证码图片
    print code
    validationCode = driver.find_element_by_name('Web_Code').send_keys(code)
    '''
    
    validationCode = driver.find_element_by_name('Web_Code')
    driver.execute_script("arguments[0].focus();", validationCode)

    os.system('pause')  # 阻止关闭 
    #driver.quit()


if __name__ == '__main__':
    #setReg()
    addInfo()
    #ocr('http://2018.dm2y.com:8082/Code.asp?')


