# MillionHeroesAssistant

# 百万英雄/冲顶大会/芝士超人 辅助小工具
# 分支版本（限安卓手机）

## 运行环境
Python 3.6<br/>
android-platform-tools（访问[google](https://developer.android.google.cn/studio/releases/platform-tools.html)下载，默认 mac，windows， linux 均支持，同时将adb工具所在路径添加到系统环境变量下）


## 基本思路
思路没啥本质区别
## 百度ocr
百度ocr：https://cloud.baidu.com/product/ocr.html<br/>
注册登录后进入右上角控制台，再左侧找到文字识别，创建一个应用，默认设置即可。<br/>
重点来了，找到AppID、API Key、Secret Key，后面需要在程序中填入自己的ID和密钥。<br/>
第二个重点：api接口需要的是另一个access_token，计算方法如下：访问<br/>
https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=【官网获取的ApiKey】&client_secret=【官网获取的SecretKey】<br/>
第一段出现的就是access_token，保存好填入assistant.py中。<br/>
（没错，就是我偷懒了，然而这个token有效期是一个月，我个人认为算好放进去就行了。。。）

## 部署与使用
1. 手机打开开发者模式，连接电脑，信任后，使用`adb devices`来检查是否有自己的设备，确认已经连接
2. 在assistant.py中填入自己的百度ocr的access_token
3. 打开手机上的答题app，等待有题目的时候运行`python assistant.py`
4. 等待几秒后，将根据识别出的问题进行百度搜索，并返回两个搜索结果
5. 答案仅供参考，辅助锦上添花，奖金不论多少，知识才是无价之宝

## 测试结果
屏幕所示问题如下：<br/>
![image](https://github.com/yyzhou94/MillionHeroesAssistant/blob/master/screenshot.png?raw=true)<br/>
截取部分如下：<br/>
![image](https://github.com/yyzhou94/MillionHeroesAssistant/blob/master/crop_test1.png?raw=true)<br/>
返回答案：<br/>
![image](https://github.com/yyzhou94/MillionHeroesAssistant/blob/master/1.PNG)<br/>

## 参考项目
- [wuditken/MillionHeroes](https://github.com/wuditken/MillionHeroes)
- [smileboywtu/MillionHeroAssistant](https://github.com/smileboywtu/MillionHeroAssistant)
