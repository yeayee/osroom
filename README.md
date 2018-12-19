
<div align=center><img width="auto" height="50" src="https://raw.githubusercontent.com/osroom/osroom/dev/apps/static/sys_imgs/osroom-logo.png" alt="osroom"/></div>

> Dev开发版(开放更新中,可在Tag中可以选择以往的其他版本)

OSROOM是使用Python3(>=3.4) 语言,基于Flask微型框架 + Mongodb(>=3.4)+ Redis开发的一个Web系统（CMF , Rest Api）.

可用于搭建（开发）个人网站,  企业官网, 也可以作为其他平台的服务端, 比如小程序客户端可以调用OSROOM Api请求操作数据.
功能支持方便,可以自己开发更多的插件或者扩展模块，让功能更全面!
目前只在Ubuntu 14.04, 16.04，18.04和Centos 6测试过，其余Linux发行版还未测试。

### 支持与功能

* 支持开发

- 插件开发，官方插件Github地址: https://github.com/osroom-plugins
- 主题开发，官方主题Github地址:  https://github.com/osroom​​​​​​​/osroom
- 扩展 

* 功能

- 可做Web 服务端Api, Restful api，简单修改即可做微信小程序的Api！

- 管里端和默认主题osr-style都支持富文本和MarkDown编辑器发布文章等!

- 文章与评论功能，可以通过插件自动审核或人工审核用户发布的内容

- 多媒体功能, 图片，文本管理功能

- 权限控制功能，能 设置每一个URL的请求权限，和指定用户拥有的权限

- 网站设置, 大量设置可以在管理端直接修改，无需改动代码

- 支持多语言翻译

更多功能请访问demo网站



### Demo

Demo网站使用默认简单主题，安装了文件存储插件(用于作为图床)，文本内容检查插件，IP识别地址插件

https://demo.osroom.com 

目前Demo安装的属于测试版本，如有BUG请提交

### 文档

> 官网与文档

官网地址: http://osroom.com (由于个人问题，该站可能已下线)

长期可访问文档地址: https://osroom.github.io/osroom-doc


### 为何开发？

那就是基于自己对Web编程的兴趣与学习更多的编程知识.

* 用户端部分功能

![MarkDown](http://osshare.oss-cn-shenzhen.aliyuncs.com/Introduction/markdown.png)
![富文本](http://osshare.oss-cn-shenzhen.aliyuncs.com/Introduction/richtext.png)
![Home](http://osshare.oss-cn-shenzhen.aliyuncs.com/Introduction/home.png)
![用户主页](http://osshare.oss-cn-shenzhen.aliyuncs.com/Introduction/user-home.png)

* Admin部分功能

![Admin主页](http://osshare.oss-cn-shenzhen.aliyuncs.com/Introduction/admin.png)
![Post](http://osshare.oss-cn-shenzhen.aliyuncs.com/Introduction/post.png)
![Media](http://osshare.oss-cn-shenzhen.aliyuncs.com/Introduction/media.png)
![权重管理](http://osshare.oss-cn-shenzhen.aliyuncs.com/Introduction/per1.png)
![API权重管理](http://osshare.oss-cn-shenzhen.aliyuncs.com/Introduction/api-per.png)
![用户角色](http://osshare.oss-cn-shenzhen.aliyuncs.com/Introduction/role.png)
![用户管理](http://osshare.oss-cn-shenzhen.aliyuncs.com/Introduction/userm.png)
![Email](http://osshare.oss-cn-shenzhen.aliyuncs.com/Introduction/emailm.png)
![消息通知](http://osshare.oss-cn-shenzhen.aliyuncs.com/Introduction/send_msg.png)
![可配置](http://osshare.oss-cn-shenzhen.aliyuncs.com/Introduction/config.png)


### License
[BSD2](http://opensource.org/licenses/BSD-2-Clause)
Copyright (c) 2017-present, Allen Woo
