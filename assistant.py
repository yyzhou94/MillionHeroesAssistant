# -*- coding:utf-8 -*-

import urllib.request, sys,base64,json,os,time,pyperclip,baiduSearch
from PIL import Image
from aip import AipOcr

start = time.time()
os.system("adb shell /system/bin/screencap -p /sdcard/screenshot.png") 
os.system("adb pull /sdcard/screenshot.png ")  

app_id = '***'                               #百度识别的appID,apikey,secretkey（填你自己的）
api_key= '***'
secret_key= '***'    #每天上限500次，应该也够用了



im = Image.open(r"./screenshot.png")   
img_size = im.size
w = im.size[0]
h = im.size[1]
print("xx:{}".format(img_size))

region = im.crop((70,200, w-70,700))    #裁剪的区域
region.save("./crop_test1.png")

f=open('./crop_test1.png','rb')
image_data=f.read()

client = AipOcr(app_id, api_key, secret_key)                #识别过程
result = client.basicGeneral(image_data)
if "error_code" in result:
    print("baidu api error: ", result["error_msg"])
else:
    keyword="".join([words["words"] for words in result["words_result"]])
keyword = keyword.split(r"．")[-1]
keywords = keyword.split(" ")
keyword = "".join([e.strip("\r\n") for e in keywords if e])
print("keyword: ", keyword)                                 #打印问题

convey = 'n'

if convey == 'y' or convey == 'Y':
    results = baiduSearch.search(keyword, convey=True)
elif convey == 'n' or convey == 'N' or not convey:
    results = baiduSearch.search(keyword)
else:
    print('输入错误')
    exit(0)
count = 0
for result in results:
    #print('{0} {1} {2} {3} {4}'.format(result.index, result.title, result.abstract, result.show_url, result.url))  # 此处应有格式化输出
	print('{0}'.format(result.abstract))  # 此处应有格式化输出
	count=count+1
	if(count == 2):
		break

end = time.time()
print('程序用时：'+str(end-start)+'秒')
