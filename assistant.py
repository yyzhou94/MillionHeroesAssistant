# -*- coding:utf-8 -*-


import urllib,sys,base64,json,os,time,baiduSearch
from PIL import Image
from aip import AipOcr
start = time.time()
os.system("adb shell /system/bin/screencap -p /sdcard/screenshot.png") 
os.system("adb pull /sdcard/screenshot.png ")  
access_token = '***'                         #填入自己的即可 

im = Image.open(r"./screenshot.png")   
img_size = im.size
w = im.size[0]
h = im.size[1]
print("xx:{}".format(img_size))

region = im.crop((70,200, w-70,700))    #裁剪的区域
region.save("./crop_test1.png")

url2 = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token='+access_token
f = open(r'./crop_test1.png', 'rb')             # 二进制方式打开图文件
img = base64.b64encode(f.read())
f.close()
params = {"image": img}
params = urllib.parse.urlencode(params)
data = bytes(params, encoding='utf8') 
req = urllib.request.Request(url2,data,method="POST")
req.add_header('Content-Type', 'application/x-www-form-urlencoded')
response = urllib.request.urlopen(req)
content = response.read().decode('utf-8')

if (content):
    content = json.loads(content)
    
    keyword="".join([words["words"] for words in list(content['words_result'])])
    print (keyword)

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

while True:
    print("""
请在题目出现时按Enter搜索答案
         """)

    enter = input("按Enter键开始，按q键后Enter退出...")
    if enter == 'q':
        break
    try:
        main()
    except Exception as e:
        print(str(e))
        
print("欢迎下次使用,帮忙Git右上角点个star哦！")   
