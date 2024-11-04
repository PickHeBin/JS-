import os
import time
import requests
import json
import time
import base64
import random
import ddddocr
from cv2 import cv2
import numpy as np
from loguru import logger
from PIL import Image, ImageChops
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
# options.add_argument('--ignore-certificate-errors')
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# options.add_experimental_option('useAutomationExtension', False)


def sel_code():
    browser = webdriver.Chrome(chrome_options=options, executable_path='E:/xhs/chromedriver.exe')
    browser.maximize_window()

    # 1.访问网址
    url = 'https://www.douyin.com/'  
    browser.get(url)  # 访问网址

    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="web-login-container"]/article/article/article/div[1]/ul[1]/li[2]')))
    browser.find_element(By.XPATH,'//*[@id="web-login-container"]/article/article/article/div[1]/ul[1]/li[3]').click()
    time.sleep(3)
    # WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="_7hLtYmO"]/button/p')))
    browser.find_element(By.XPATH,'//*[@id="web-login-container"]/article/article/article/form/div[1]/div/input').send_keys('15803795601')
    browser.find_element(By.XPATH,'//*[@id="web-login-container"]/article/article/article/form/div[2]/div/div/input').send_keys('123456')
    browser.find_element(By.XPATH,'//*[@id="web-login-container"]/article/article/article/form/div[5]/button').click()
    time.sleep(2)

    bg_srcs = browser.find_element(By.XPATH,'//*[@id="captcha_container"]/div/div[2]/img[1]')
    bg_src = bg_srcs.get_attribute('src')
    inner_srcs = browser.find_element(By.XPATH,'//*[@id="captcha_container"]/div/div[2]/img[2]')
    inner_src = inner_srcs.get_attribute('src')
    print(bg_src,inner_src)
    time.sleep(1)


    # 获取滑动按钮
    slider = browser.find_element(By.XPATH, '//*[@id="secsdk-captcha-drag-wrapper"]/div[2]/div')  


    def download_jpeg(url, save_path):
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(save_path, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print("图片下载完成")
        else:
            print("图片下载失败")

    # 调用示例
    image_url = bg_src
    save_file = "E:/Dy/pic/dy_yzm.jpeg"

    download_jpeg(image_url, save_file)

    def download_image(url, save_path):
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(save_path, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print("图片下载完成")
        else:
            print("图片下载失败")

    # 调用示例
    image_url = inner_src
    inner_file = "E:/Dy/pic/inner.png"

    download_image(image_url, inner_file)



    """
    背景图排序拼合
    """
    pic_path = 'E:/Dy/pic/dy_yzm.jpeg' # 分割的图片的位置
    pic_target = 'E:/Dy/pic/result/' # 分割后的图片保存的文件夹
    if not os.path.exists(pic_target):  #判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(pic_target)
    #要分割后的尺寸
    cut_width = 344
    cut_length = 92
    # 读取要分割的图片，以及其尺寸等数据
    picture = cv2.imread(pic_path)
    (width, length, depth) = picture.shape
    print(width, length, depth)
    # 预处理生成0矩阵
    pic = np.zeros((cut_width, cut_length, depth))
    # 计算可以划分的横纵的个数
    num_width = int(width / cut_width)
    num_length = int(length / cut_length)
    # for循环迭代生成
    for i in range(0, num_width):
        for j in range(0, num_length):
            pic = picture[i*cut_width : (i+1)*cut_width, j*cut_length : (j+1)*cut_length, :]      
            result_path = pic_target + '{}_{}.jpg'.format(i+1, j+1)
            cv2.imwrite(result_path, pic)
    

    # 原图大小
    original_width = 92
    original_height = 344

    # 文件夹路径和输出文件名
    folder_path = 'E:/Dy/pic/result/'
    output_filename = "E:/Dy/pic/"

    # 拼合顺序
    image_order = ['1_5.jpg', '1_1.jpg', '1_4.jpg', '1_6.jpg', '1_3.jpg', '1_2.jpg']

    # 创建一个空白画布，用于拼合图片
    canvas_height = original_height
    canvas_width = original_width * len(image_order)
    canvas = np.zeros((canvas_height, canvas_width, 3), dtype=np.uint8)

    # 遍历图片拼合
    for i, filename in enumerate(image_order):
        image_path = os.path.join(folder_path, filename)
        image = cv2.imread(image_path)
        
        # 计算当前图片在画布上的位置
        start_x = i * original_width
        end_x = start_x + original_width

        # 将当前图片拷贝到画布上指定的位置
        canvas[0:original_height, start_x:end_x] = image

    # 保存拼合后的图片
    cv2.imwrite(output_filename +'dy_yzm.png', canvas)
    print("图片已还原成功")



    ocr = ddddocr.DdddOcr(det=False, ocr=False)

    with open('E:\Dy\pic\inner.png', 'rb') as f:
        target_bytes = f.read()
    with open('E:\Dy\pic\dy_yzm.png', 'rb') as f:
        background_bytes = f.read()
    res = ocr.slide_match(target_bytes, background_bytes)
    print(res)
    target_x = res.get('target')[0]
    print(target_x)
    # 110 是target图片原始大小
    # 获取滑动百分比
    percentage = target_x / 110
    # distance = percentage * 67.75 + 34
    distance = percentage * 67.75
    print("执行滑动距离 {}".format(distance))

    import pyautogui
    # 设置起始位置
    start_x = 820
    start_y = 690
    # 计算终点位置
    end_x = start_x + distance
    end_y = start_y
    # 移动鼠标到起始位置
    pyautogui.moveTo(start_x, start_y, duration=0.5)
    # 按下鼠标左键
    pyautogui.mouseDown()
    # 往右多拖到20xp
    pyautogui.moveTo(end_x + 20, end_y, duration=0.5)
    #拖回结束位置
    pyautogui.moveTo(end_x, end_y, duration=0.5)
    # 松开鼠标左键
    pyautogui.mouseUp()

    time.sleep(3)
    browser.quit()

sel_code()