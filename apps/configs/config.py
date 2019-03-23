#!/usr/bin/env python
# -*-coding:utf-8-*-
__author__ = "Allen Woo"
__readme__='''
################################################################################
1.配置文件
a.除了OVERWRITE_DB外, 其他配置都可以在平台管理端页面修改
b.启动网站/重启网站的时候，系统会自动合并数据库中保存的配置,实现本地配置文件配置与数据库一致.
c.如果你是开发人员,需要手动修改配置文件，请阅读下面说明

2.自动合并过程中:
a.对于本文件新增加的key会添加到数据库(value使用本地的)
b.本文文件没有的,而数据库有保存的key会在数据库删除
c.两边都存在的key, 则value使用数据库的

##如果你不想合并配置, 想用本地配置数据覆盖掉数据库中的配置数据,请修改变量OVERWRITE_DB

变量说明
*OVERWRITE_DB
启动系统时, 配置更新是否来自数据库, 以数据库中的value为主.
如果为True, 则完全以本文件数据上传到数据库中
如果为False, 按照上述[2.自动合并过程中],当次有效, 启动后会自动变为True

*CONFIG　
1.每个配置项中的__sort__作为在管理的显示的时候的排序使用, 如果不存在__sort__,表示该配置不可以在管理端配置
2.配置表,表中没有__restart__的项目将不会出现在管理端的设置中
###############################################################################
'''
# Danger: If True, the database configuration data will be overwritten
# 危险:如果为True, 则会把该文件配置覆盖掉数据库中保存的配置
OVERWRITE_DB = False
CONFIG = {
    "py_venv": {
        "VENV_PATH": {
            "info": "python虚拟环境路径",
            "sort": 99,
            "value": "/home/work/project/venv3",
            "type": "string"
        }
    },
    "email": {
        "MAIL_DEFAULT_SENDER": {
            "info": "默认发送者邮箱　(显示名称, 邮箱地址)顺序不能调换",
            "sort": 99,
            "value": [
                "OSR DEMO",
                "system@osroom.com"
            ],
            "type": "list"
        },
        "APP_LOG_URL": {
            "info": "在邮件中显示的LOGO图片URL(1.不填写则不显示.2.如果主题邮件发送html模板不支持，也不显示)",
            "sort": 99,
            "value": "https://avatars1.githubusercontent.com/u/14039952?s=460&v=4",
            "type": "string"
        },
        "MAIL_ASCII_ATTACHMENTS": {
            "info": "MAIL ASCII ATTACHMENTS",
            "sort": 99,
            "value": True,
            "type": "bool"
        },
        "MAIL_USE_SSL": {
            "info": "是否使用SSL",
            "sort": 99,
            "value": True,
            "type": "bool"
        },
        "MAIL_USERNAME": {
            "info": "邮箱用户名",
            "sort": 99,
            "value": "system@osroom.com",
            "type": "string"
        },
        "MAIL_SERVER": {
            "info": "邮箱服务器smtp",
            "sort": 99,
            "value": "smtp.mxhichina.com",
            "type": "string"
        },
        "MAIL_PASSWORD": {
            "info": "邮箱密码, 是用于发送邮件的密码",
            "sort": 99,
            "value": "<Your password>",
            "type": "password"
        },
        "MAIL_SUBJECT_SUFFIX": {
            "info": "发送邮件的标题后缀",
            "sort": 99,
            "value": "OSROOM",
            "type": "string"
        },
        "__sort__": 10,
        "MAIL_PORT": {
            "info": "邮箱服务器端口",
            "sort": 99,
            "value": 465,
            "type": "int"
        },
        "__restart__": "must",
        "MAIL_USE_TLS": {
            "info": "是否使用TLS",
            "sort": 99,
            "value": False,
            "type": "bool"
        },
        "MAIL_FOOTER": {
            "info": "发送邮件的页尾",
            "sort": 99,
            "value": "OSROOM开源网站系统",
            "type": "string"
        },
        "__info__": "邮件发送参数设置（建议技术管理人员使用）",
        "APP_NAME": {
            "info": "在邮件中显示的APP(WEB)名称(1.不填写则不显示.2.如果主题邮件发送html模板不支持，也不显示)",
            "sort": 99,
            "value": "OSR DEMO",
            "type": "string"
        }
    },
    "system": {
        "__sort__": 99,
        "__restart__": "must",
        "MAX_CONTENT_LENGTH": {
            "info": "拒绝内容长度大于此值的请求进入，并返回一个 413 状态码(单位:Mb)",
            "sort": 1,
            "value": 50.0,
            "type": "float"
        },
        "TEMPLATES_AUTO_RELOAD": {
            "info": "是否自动加载页面(html)模板.开启后,每次html页面修改都无需重启Web",
            "sort": 3,
            "value": True,
            "type": "bool"
        },
        "__info__": "其他web系统参数设置（建议技术管理人员使用）",
        "KEY_HIDING": {
            "info": "开启后,管理端通过/api/admin/xxx获取到的数据中，密钥类型的值，则会以随机字符代替.<br><span style='color:red;'>如某个插件配置中有密码, 不想让它暴露在浏览器, 则可开启.</span>",
            "sort": 2,
            "value": True,
            "type": "bool"
        }
    },
    "theme_global_conf": {
        "__sort__": 99,
        "__info__": "主题的一些全局配置(只对主题有效, 并需要主题支持)",
        "__restart__": "not_must",
        "TOP_NAV": {
            "info": "最多能同时登录几个使用JWT验证的客户端,超过此数目则会把旧的登录注销",
            "sort": 99,
            "value": {
                "关于": {
                    "link": "",
                    "nav": "关于",
                    "next_lev": [
                        {
                            "link": "/about-us",
                            "nav": "关于我们"
                        },
                        {
                            "link": "/contact",
                            "nav": "联系我们"
                        }
                    ]
                },
                "2": {
                    "link": "/photo",
                    "nav": "图库",
                    "next_lev": None
                },
                "1": {
                    "link": "/",
                    "nav": "首页",
                    "next_lev": None
                }
            },
            "type": "dict"
        }
    },
    "theme": {
        "__info__": "主题配置",
        "VERSION": {
            "info": "当前主题版本",
            "sort": 99,
            "value": "v0.1",
            "type": "string"
        },
        "CURRENT_THEME_NAME": {
            "info": "当前主题名称,需与主题主目录名称相同",
            "sort": 99,
            "value": "osr-style",
            "type": "string"
        },
        "__restart__": "not_must"
    },
    "site_config": {
        "STATIC_FILE_VERSION": {
            "info": "静态文件版本(当修改了CSS,JS等静态文件的时候，修改此版本号)",
            "sort": 12,
            "value": 20181024065925,
            "type": "int"
        },
        "FAVICON": {
            "info": "APP(Web)favicon图标的URL",
            "sort": 10,
            "value": "/static/sys_imgs/osroom-logo.ico",
            "type": "string"
        },
        "FOOTER_CODE": {
            "info": "用于放入html中<br><span style='color:red;'>body标签</span>内的js/css/html代码(如Google分析代码/百度统计代码)",
            "sort": 13,
            "value": "",
            "type": "string"
        },
        "TITLE_PREFIX_ADM": {
            "info": "APP(Web)管理端Title前缀",
            "sort": 7,
            "value": "",
            "type": "string"
        },
        "BACKGROUND_IMG_URL": {
            "info": "网页背景图片(需要主题支持)",
            "sort": 5,
            "value": "/static/sys_imgs/background.jpg",
            "type": "string"
        },
        "DOES_NOT_EXIST_URL": {
            "info": "当一个文件或图片不存在的时候, 返回此Image URL",
            "sort": 11,
            "value": "/static/sys_imgs/does_not_exist.png",
            "type": "string"
        },
        "HEAD_CODE": {
            "info": "用于放入html中<br><span style='color:red;'>head标签</span>内的js/css/html代码(如Google分析代码/百度统计代码)",
            "sort": 13,
            "value": "",
            "type": "string"
        },
        "TITLE_PREFIX": {
            "info": "APP(Web)Title前缀",
            "sort": 6,
            "value": "",
            "type": "string"
        },
        "LOGO_IMG_URL": {
            "info": "APP(Web)Logo的URL",
            "sort": 2,
            "value": "/static/sys_imgs/osroom-logo.png",
            "type": "string"
        },
        "__sort__": 1,
        "FRIEND_LINK": {
            "info": "友情链接:值(Value)格式为{'url':'友情链接', 'logo_url':'logo链接'}",
            "sort": 11,
            "value": {
                "Github": {
                    "level": 1,
                    "url": "www.aliyun.com",
                    "icon_url": "",
                    "aliases": "Github"
                },
                "阿里云": {
                    "level": 1,
                    "url": "www.aliyun.com",
                    "icon_url": "",
                    "aliases": "阿里云"
                },
                "码云": {
                    "level": 1,
                    "url": "www.aliyun.com",
                    "icon_url": "",
                    "aliases": "码云"
                },
                "七牛云": {
                    "level": 1,
                    "url": "www.aliyun.com",
                    "icon_url": "",
                    "aliases": "七牛云"
                }
            },
            "type": "dict"
        },
        "TITLE_SUFFIX_ADM": {
            "info": "APP(Web)管理端Title后缀",
            "sort": 9,
            "value": "OSROOM管理端",
            "type": "string"
        },
        "__restart__": "not_must",
        "MB_LOGO_DISPLAY": {
            "info": "移动端用App name 还是Logo image 作为APP(Web)的Logo显示, 为空则App name优先<br>可填logo或name(需要主题支持)",
            "sort": 4,
            "value": "name",
            "type": "string"
        },
        "TITLE_SUFFIX": {
            "info": "APP(Web)Title后缀",
            "sort": 8,
            "value": "OSROOM开源Web DEMO",
            "type": "string"
        },
        "PC_LOGO_DISPLAY": {
            "info": "PC端用App name 还是Logo image 作为APP(Web)的Logo显示, 为空则显示Logo和App name<br>可填logo或name(需要主题支持)",
            "sort": 3,
            "value": "logo",
            "type": "string"
        },
        "__info__": "基础设置: APP(Web)全局数据设置<br>此模块所有的KEY值, 都可以直接请求全局Api(/api/global)获取.也可以直接在主题中使用Jinjia2模板引擎获取(g.site_global.site_config.XXXX)",
        "APP_NAME": {
            "info": "APP(站点)名称,将作为全局变量使用在平台上",
            "sort": 1,
            "value": "OSR DEMO",
            "type": "string"
        },
        "SITE_URL": {
            "info": "Web站点URL(如果没有填写, 则使用默认的当前域名首页地址)",
            "sort": 11,
            "value": "http://www.osroom.com",
            "type": "string"
        }
    },
    "content_inspection": {
        "AUDIO_OPEN": {
            "info": "开启音频检测.需要hook_name为content_inspection_audio的音频检测插件",
            "sort": 99,
            "value": False,
            "type": "bool"
        },
        "ALLEGED_ILLEGAL_SCORE": {
            "info": "内容检测分数高于多少分时属于涉嫌违规(0-100分,对于需要检查的内容有效)",
            "sort": 99,
            "value": 99,
            "type": "float"
        },
        "TEXT_OPEN": {
            "info": "开启text检测.需要hook_name为content_inspection_text的文本检测插件",
            "sort": 99,
            "value": True,
            "type": "bool"
        },
        "IMAGE_OPEN": {
            "info": "开启图片检测.需要hook_name为content_inspection_image的图片检测插件",
            "sort": 99,
            "value": False,
            "type": "bool"
        },
        "__restart__": "not_must",
        "VEDIO_OPEN": {
            "info": "开启视频检测.需要hook_name为content_inspection_vedio的视频检测插件",
            "sort": 99,
            "value": False,
            "type": "bool"
        },
        "__sort__": 5,
        "__info__": "内容检查配置(需要安装相关插件该配置才生效).<br>检测开关:<br>1.如果开启, 并安装有相关的自动检查插件, 则会给发布的内容给出违规评分.如果未安装自动审核插件,则系统会给予评分100分(属涉嫌违规,网站工作人员账户除外).<br>2.如果关闭审核，则系统会给评分0分(不违规)"
    },
    "name_audit": {
        "AUDIT_PROJECT_KEY": {
            "info": "审核项目的Key(键),审核时会使用一个Key来获取审核规则,正则去匹配用户输入的内容",
            "sort": 99,
            "value": {
                "class_name": "审核一些短的分类名称, 如category, tag",
                "username": "审核用户名"
            },
            "type": "dict"
        },
        "__info__": "名称验证, 如用户名,分类名称",
        "__restart__": "not_must",
        "__sort__": 8
    },
    "session": {
        "__sort__": 99,
        "SESSION_PERMANENT": {
            "info": "是否使用永久会话",
            "sort": 99,
            "value": True,
            "type": "bool"
        },
        "PERMANENT_SESSION_LIFETIME": {
            "info": "永久会话的有效期.",
            "sort": 99,
            "value": 2592000,
            "type": "int"
        },
        "SESSION_KEY_PREFIX": {
            "info": "添加一个前缀,之前所有的会话密钥。这使得它可以为不同的应用程序使用相同的后端存储服务器",
            "sort": 99,
            "value": "osroom",
            "type": "string"
        },
        "__restart__": "must",
        "SESSION_TYPE": {
            "info": "保存Session会话的类型,可选mongodb, redis",
            "sort": 99,
            "value": "mongodb",
            "type": "string"
        },
        "SESSION_MONGODB_COLLECT": {
            "info": "Mongodb保存session的collection,当SESSION_TYPE为mongodb时有效",
            "sort": 99,
            "value": "osr_session",
            "type": "string"
        },
        "__info__": "Session参数设置（建议技术管理人员使用）"
    },
    "weblogger": {
        "__sort__": 99,
        "USER_OP_LOG_KEEP_NUM": {
            "info": "用户操作日志保留个数",
            "sort": 99,
            "value": 30,
            "type": "int"
        },
        "__info__": "操作日志设置",
        "SING_IN_LOG_KEEP_NUM": {
            "info": "登录日志保留个数",
            "sort": 99,
            "value": 30,
            "type": "int"
        },
        "__restart__": "not_must"
    },
    "user_model": {
        "__sort__": 99,
        "EDITOR": {
            "info": "新用户默认编辑器类型rich_text或markdown",
            "sort": 99,
            "value": "rich_text",
            "type": "string"
        },
        "__info__": "用户Model",
        "__restart__": "not_must"
    },
    "cache": {
        "CACHE_DEFAULT_TIMEOUT": {
            "info": "(s秒)默认缓存时间,当单个缓存没有设定缓存时间时会使用该时间",
            "sort": 99,
            "value": 600,
            "type": "int"
        },
        "CACHE_TYPE": {
            "info": "缓存使用的类型,可选择redis,mongodb",
            "sort": 99,
            "value": "redis",
            "type": "string"
        },
        "__sort__": 99,
        "__restart__": "must",
        "CACHE_MONGODB_COLLECT": {
            "info": "保存cache的collection,当CACHE_TYPE为mongodb时有效",
            "sort": 99,
            "value": "osr_cache",
            "type": "string"
        },
        "USE_CACHE": {
            "info": "是否使用缓存功能,建议开启",
            "sort": 99,
            "value": True,
            "type": "bool"
        },
        "CACHE_KEY_PREFIX": {
            "info": "所有键(key)之前添加的前缀,这使得它可以为不同的应用程序使用相同的memcached(内存)服务器.",
            "sort": 99,
            "value": "osr_cache",
            "type": "string"
        },
        "__info__": "Web缓存参数设置（建议技术管理人员使用）"
    },
    "login_manager": {
        "__sort__": 99,
        "OPEN_REGISTER": {
            "info": "开放注册",
            "sort": 99,
            "value": True,
            "type": "bool"
        },
        "__restart__": "not_must",
        "PW_WRONG_NUM_IMG_CODE": {
            "info": "同一用户登录密码错误几次后响应图片验证码, 并且需要验证",
            "sort": 99,
            "value": 5,
            "type": "int"
        },
        "LOGIN_IN_TO": {
            "info": "登录成功后,api会响应数据会带上需要跳转到路由to_url",
            "sort": 99,
            "value": "/",
            "type": "string"
        },
        "LOGIN_OUT_TO": {
            "info": "退出登录后,api会响应数据会带上需要跳转到路由to_url",
            "sort": 99,
            "value": "/",
            "type": "string"
        },
        "__info__": "在线管理（建议技术管理人员使用）",
        "LOGIN_VIEW": {
            "info": "需要登录的页面,未登录时,api会响应401,并带上需要跳转到路由to_url",
            "sort": 99,
            "value": "/sign-in",
            "type": "string"
        }
    },
    "post": {
        "BRIEF_LEN": {
            "info": "获取文章简要的字数",
            "sort": 99,
            "value": 80,
            "type": "int"
        },
        "NUM_PAGE": {
            "info": "每个页面获取几篇文章, 如果请求获取文章时指定了指定了per参数, 则此配置无效(此配置也对管理端无效)",
            "sort": 99,
            "value": 10,
            "type": "int"
        },
        "TAG_MAX_NUM": {
            "info": "POST标签最大个数",
            "sort": 99,
            "value": 5,
            "type": "int"
        },
        "NUM_PAGE_MAX": {
            "info": "每个页面最多获取几篇文章(此配置对管理端无效)",
            "sort": 99,
            "value": 30,
            "type": "int"
        },
        "__restart__": "not_must",
        "__sort__": 2,
        "TITLE_MAX_LEN": {
            "info": "文章Title最大长度",
            "sort": 99,
            "value": 50,
            "type": "int"
        },
        "TAG_MAX_LEN": {
            "info": "POST标签最多几个字",
            "sort": 99,
            "value": 10,
            "type": "int"
        },
        "__info__": "文章内容设置",
        "GET_POST_CACHE_TIME_OUT": {
            "info": "获取多个post数据时, 缓存超时时间(s), 为0表示不缓存数据.<br><span style='color:red;'>只对获取已公开发布的, 并且不是当前用户发布的post有效</span>",
            "sort": 99,
            "value": 60,
            "type": "int"
        },
        "MAX_LEN": {
            "info": "发布文章最多几个字符",
            "sort": 99,
            "value": 5000,
            "type": "int"
        }
    },
    "account": {
        "__sort__": 6,
        "__restart__": "not_must",
        "DEFAULT_AVATAR": {
            "info": "新注册用户默认头像的URL",
            "sort": 99,
            "value": [
                "/static/admin/sys_imgs/avatar_default_1.png",
                "/static/admin/sys_imgs/avatar_default_2.png"
            ],
            "type": "string"
        },
        "USER_AVATAR_MAX_SIZE": {
            "info": "用户头像不能上传超过此值大小(单位Mb)的图片作头像",
            "sort": 99,
            "value": 10.0,
            "type": "float"
        },
        "__info__": "账户设置",
        "USER_AVATAR_SIZE": {
            "info": "用户头像保存大小[<width>, <height>]像素",
            "sort": 99,
            "value": [
                "360",
                "360"
            ],
            "type": "list"
        },
        "USERNAME_MAX_LEN": {
            "info": "用户名最大长度",
            "sort": 99,
            "value": 20,
            "type": "int"
        }
    },
    "upload": {
        "__sort__": 99,
        "UP_ALLOWED_EXTENSIONS": {
            "info": "上传:允许上传的文件后缀(全部小写),每个用英文的','隔开",
            "sort": 99,
            "value": [
                "xls",
                "xlxs",
                "excel",
                "txt",
                "pdf",
                "png",
                "jpg",
                "jpeg",
                "gif",
                "ico",
                "mp4",
                "rmvb",
                "avi",
                "mkv",
                "mov",
                "mp3",
                "wav",
                "wma",
                "ogg",
                "zip",
                "gzip",
                "tar"
            ],
            "type": "list"
        },
        "__info__": "文件上传配置（建议技术管理人员使用）",
        "__restart__": "not_must",
        "SAVE_DIR": {
            "info": "上传:保存目录,如何存在'/'则会自动切分创建子目录",
            "sort": 99,
            "value": "media",
            "type": "string"
        }
    },
    "babel": {
        "BABEL_DEFAULT_LOCALE": {
            "info": "默认语言:可以是zh_CN, en_US等()",
            "sort": 99,
            "value": "zh_CN",
            "type": "string"
        },
        "__sort__": 9,
        "__info__": "多语言设置",
        "LANGUAGES": {
            "info": "管理端支持的语言",
            "sort": 99,
            "value": {
                "en_US": {
                    "alias": "En",
                    "name": "English"
                },
                "zh_CN": {
                    "alias": "中文",
                    "name": "中文"
                }
            },
            "type": "dict"
        },
        "__restart__": "must"
    },
    "category": {
        "__sort__": 7,
        "CATEGORY_MAX_LEN": {
            "info": "分类名称类型名最多几个字符",
            "sort": 99,
            "value": 15,
            "type": "int"
        },
        "__info__": "Web参数设置",
        "__restart__": "not_must",
        "CATEGORY_TYPE": {
            "info": "分类的品种只能有这几种",
            "sort": 99,
            "value": {
                "主题音频": "audio_theme",
                "文集": "post",
                "图库": "image",
                "主题其他": "other_theme",
                "音频库": "audio",
                "视频库": "video",
                "主题视频": "video_theme",
                "主题图片图文": "image_theme",
                "文本内容": "text",
                "其他": "other",
                "主题文本": "text_theme"
            },
            "type": "dict"
        }
    },
    "seo": {
        "__info__": "针对网页客户端的简单的SEO配置<br>此模块所有的KEY值, 都可以直接请求全局Api(<br><span style='color:red;'>/api/global</span>)获取.<br>也可以直接在主题中使用Jinjia2模板引擎获取(<br><span style='color:red;'>g.site_global.site_config.XXXX</span>)",
        "DEFAULT_DESCRIPTION": {
            "info": "网站的页面默认简单描述",
            "sort": 99,
            "value": "开源Web系统, 可以作为企业网站, 个人博客网站, 微信小程序Web服务端",
            "type": "string"
        },
        "DEFAULT_KEYWORDS": {
            "info": "网站的页面默认关键词",
            "sort": 99,
            "value": "开源, 企业网站, 博客网站, 微信小程序, Web服务端",
            "type": "string"
        },
        "__restart__": "not_must",
        "__sort__": 4
    },
    "rest_auth_token": {
        "__sort__": 99,
        "REST_ACCESS_TOKEN_LIFETIME": {
            "info": "给客户端发补的访问Token AccessToken的有效期",
            "sort": 99,
            "value": 172800,
            "type": "int"
        },
        "LOGIN_LIFETIME": {
            "info": "jwt 登录BearerToken有效期(s)",
            "sort": 99,
            "value": 2592000,
            "type": "int"
        },
        "__restart__": "not_must",
        "MAX_SAME_TIME_LOGIN": {
            "info": "最多能同时登录几个使用JWT验证的客户端,超过此数目则会把旧的登录注销",
            "sort": 99,
            "value": 3,
            "type": "int"
        },
        "__info__": "Web参数设置"
    },
    "comment": {
        "__sort__": 3,
        "NUM_PAGE_MAX": {
            "info": "每个页面最多获取几条评论(此配置对管理端无效)",
            "sort": 99,
            "value": 30,
            "type": "int"
        },
        "__restart__": "not_must",
        "MAX_LEN": {
            "info": "发布评论最多几个字符",
            "sort": 99,
            "value": 300,
            "type": "int"
        },
        "__info__": "评论内容设置",
        "TRAVELER_COMMENT": {
            "info": "游客评论开关,是否打开?",
            "sort": 99,
            "value": False,
            "type": "bool"
        },
        "INTERVAL": {
            "info": "控制评论频繁度时间(s)",
            "sort": 99,
            "value": 30,
            "type": "int"
        },
        "NUM_PAGE": {
            "info": "每个页面获取几条评论, 如果请求获取评论时指定了指定了per参数, 则此配置无效(此配置也对管理端无效)",
            "sort": 99,
            "value": 10,
            "type": "int"
        },
        "NUM_OF_INTERVAL": {
            "info": "控制评论频繁度时间内最多评论几次",
            "sort": 99,
            "value": 3,
            "type": "int"
        },
        "OPEN_COMMENT": {
            "info": "评论开关,是否打开评论功能?",
            "sort": 99,
            "value": False,
            "type": "bool"
        }
    },
    "key": {
        "SECURITY_PASSWORD_SALT": {
            "info": "安全密码码盐值",
            "sort": 99,
            "value": "ceavewrvwtrhdyjydj",
            "type": "string"
        },
        "SECRET_KEY": {
            "info": "安全验证码",
            "sort": 99,
            "value": "ceavewrvwtrhdyjydj",
            "type": "string"
        },
        "__info__": "安全Key（建议技术管理人员使用）",
        "__restart__": "must",
        "__sort__": 99
    },
    "verify_code": {
        "MAX_NUM_SEND_SAMEIP_PERMIN_NO_IMGCODE": {
            "info": "同一IP地址,同一用户(未登录的同属同一匿名用户),允许每分钟在不验证[图片验证码]的时候,调用API发送验证码最大次数.<br>超过次数后API会生成[图片验证码]并返回图片url对象(也可以自己调用获取图片验证码API获取).<br>如果你的客户端(包括主题)不支持显示图片验证码,请设置此配置为99999999",
            "sort": 99,
            "value": 1,
            "type": "int"
        },
        "EXPIRATION": {
            "info": "验证码过期时间(s)",
            "sort": 99,
            "value": 600,
            "type": "int"
        },
        "IMG_CODE_DIR": {
            "info": "图片验证码保存目录",
            "sort": 99,
            "value": "verify_code",
            "type": "string"
        },
        "__restart__": "not_must",
        "MAX_IMG_CODE_INTERFERENCE": {
            "info": "图片验证码干扰程度的最大值",
            "sort": 99,
            "value": 40,
            "type": "int"
        },
        "__info__": "验证码(建议技术管理员配置)",
        "MAX_NUM_SEND_SAMEIP_PERMIN": {
            "info": "同一IP地址,同一用户(未登录的同属一匿名用户), 允许每分钟调用API发送验证码的最大次数",
            "sort": 99,
            "value": 15,
            "type": "int"
        },
        "MIN_IMG_CODE_INTERFERENCE": {
            "info": "图片验证码干扰程度的最小值,最小值小于10时无效",
            "sort": 99,
            "value": 10,
            "type": "int"
        },
        "SEND_CODE_TYPE": {
            "info": "发送的验证码字符类型，与字符个数",
            "sort": 99,
            "value": {
                "int": 6,
                "string": 0
            },
            "type": "dict"
        },
        "__sort__": 11
    }
}