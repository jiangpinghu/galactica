'''
selenium取验证码，暂时不用
'''
#
#
# from PIL import Image  # 用于打开图片和对图片处理
# from selenium import webdriver  # 用于打开网站
# import time  # 代码运行停顿
# import os  # 用于操作文件
# import tesserocr  # 用于识别图片上的验证码
#
#
# class VerificationCode:
#
#     def __init__(self):
#
#         # 指定默认打开网站的浏览器
#         self.driver = webdriver.Chrome()
#         # 变量定位方法
#         self.find_element = self.driver.find_element_by_xpath
#
#     def get_pictures(self):
#
#         # 指定需要删除的文件路径
#         path = 'C:/Users/Administrator/Desktop/png/0001.png'
#         '''# 删除之前截取的图片'''
#         for root, dirs, files in os.walk(path):
#             for name in files:
#                 '''# 填写规则（指定删除信息的格式）'''
#                 if name.endswith("0001.png"):
#                     os.remove(os.path.join(root, name))
#                     print("Delete File: " + os.path.join(root, name))
#         ''' # 打开登陆页面'''
#         self.driver.get('填入你需要打开的http请求')
#         '''# 全屏截图'''
#         self.driver.save_screenshot('pictures.png')
#         page_snap_obj = Image.open('pictures.png')
#         ''' # 定位验证码元素位置'''
#         img = self.find_element('//*[@id="app"]/div/div[2]/form/div[3]/div[2]/div/span/div[1]/img')
#         time.sleep(1)
#         location = img.location
#         '''# 获取验证码的大小参数'''
#         size = img.size
#         left = location['x']
#         top = location['y']
#         right = left + size['width']
#         bottom = top + size['height']
#         '''# 按照验证码的长宽，切割验证码'''
#         image_obj = page_snap_obj.crop((left, top, right, bottom))
#         '''# 保存截取的图片到指定的位置'''
#         image_obj.save(r'C:/Users/Administrator/Desktop/png/0001.png')
#         '''# 处理完验证码后关闭浏览器'''
#         self.driver.close()
#         '''返回处理后的验证码'''
#         return image_obj
#
#     def processing_image(self):
#         self.get_pictures()
#         ''' # 获取指定路径下图片验证码'''
#         image = Image.open("C:/Users/Administrator/Desktop/png/0001.png")
#         ''' # 转灰度'''
#         image = image.convert("L")
#         '''# 该阈值不适合所有验证码，具体阈值请根据验证码情况设置'''
#         the_sho = 112
#         '''table是设定的一个表，下面的for循环可以理解为一个规则，小于阈值的，就设定为0，大于阈值的，就设定为1'''
#         table = []
#         '''# 遍历所有像素，大于阈值的为黑色'''
#         for i in range(256):
#             if i < the_sho:
#                 table.append(0)
#             else:
#                 table.append(1)
#         '''# 对灰度图进行二值化处理，按照table的规则（也就是上面的for循环）'''
#         image = image.point(table, "1")
#         '''# 对去噪后的图片进行识别'''
#         res = tesserocr.image_to_text(image)
#         '''#  打印验证码'''
#         print(res)
#
#
# if __name__ == '__main__':
#     a = VerificationCode()
#     a.processing_image()
#
#
