# -*- coding:utf-8 -*-

import urllib.request,sys,base64,json,os,time
from PIL import Image
from aip import AipOcr
from Search_answer import Search

app_id = '***'                               #百度识别的appID,apikey,secretkey（填你自己的）
api_key= '***'
secret_key= '***'    #每天上限500次，应该也够用了

def main():
  start = time.time()
  os.system("adb shell /system/bin/screencap -p /sdcard/screenshot.png") 
  os.system("adb pull /sdcard/screenshot.png ")  


  im = Image.open(r"./screenshot.png")   
  img_size = im.size
  w = im.size[0]
  h = im.size[1]
  print("xx:{}".format(img_size))

  region = im.crop((70,200, w-70,1200))    #裁剪的区域
  region.save("./crop_test1.png") 

  f=open('./crop_test1.png','rb')
  image_data=f.read()

  client = AipOcr(app_id, api_key, secret_key)                #识别过程
  result = client.basicGeneral(image_data)
  if "error_code" in result:
      print("baidu api error: ", result["error_msg"])
  else:
      words_results = result['words_result']                  #得到识别结果的问题+选项
      #print (result['words_result'])   
  question = ''
  choice = ['','','','','','']
  num = 0
  choice_num = 0
  for words_result in words_results:
        num+=1
        if(num >=len(words_results)-2):
          choice[choice_num] = words_result['words']
          choice_num+=1
        else:
          question = question + words_result['words']

  
  print(question)       #打印问题
  print('  A:'+choice[0]+' B:'+choice[1]+' C:'+choice[2])       #打印选项

  s = Search(question,choice)
  s.search()
  
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
