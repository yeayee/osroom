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
    "session": {
        "__restart__": "must",
        "SESSION_MONGODB_COLLECT": {
            "sort": 99,
            "info": "Mongodb保存session的collection,当SESSION_TYPE为mongodb时有效",
            "value": "osr_session",
            "type": "string"
        },
        "PERMANENT_SESSION_LIFETIME": {
            "sort": 99,
            "info": "永久会话的有效期.",
            "value": 2592000,
            "type": "int"
        },
        "SESSION_TYPE": {
            "sort": 99,
            "info": "保存Session会话的类型,可选mongodb, redis",
            "value": "mongodb",
            "type": "string"
        },
        "SESSION_KEY_PREFIX": {
            "sort": 99,
            "info": "添加一个前缀,之前所有的会话密钥。这使得它可以为不同的应用程序使用相同的后端存储服务器",
            "value": "osroom",
            "type": "string"
        },
        "SESSION_PERMANENT": {
            "sort": 99,
            "info": "是否使用永久会话",
            "value": True,
            "type": "bool"
        },
        "__sort__": 99,
        "__info__": "Session参数设置（建议技术管理人员使用）"
    },
    "theme_global_conf": {
        "__restart__": "not_must",
        "__info__": "主题的一些全局配置(只对主题有效, 并需要主题支持)",
        "__sort__": 99,
        "TOP_NAV": {
            "sort": 99,
            "info": "最多能同时登录几个使用JWT验证的客户端,超过此数目则会把旧的登录注销",
            "value": {
                "关于": {
                    "next_lev": [
                        {
                            "nav": "关于我们",
                            "link": "/about-us"
                        },
                        {
                            "nav": "联系我们",
                            "link": "/contact"
                        }
                    ],
                    "nav": "关于",
                    "link": ""
                },
                "1": {
                    "next_lev": None,
                    "nav": "首页",
                    "link": "/"
                },
                "2": {
                    "next_lev": None,
                    "nav": "图库",
                    "link": "/photo"
                }
            },
            "type": "dict"
        }
    },
    "py_venv": {
        "VENV_PATH": {
            "sort": 99,
            "info": "python虚拟环境路径",
            "value": "/home/work/project/venv3",
            "type": "string"
        }
    },
    "email": {
        "APP_LOG_URL": {
            "sort": 99,
            "info": "在邮件中显示的LOGO图片URL(1.不填写则不显示.2.如果主题邮件发送html模板不支持，也不显示)",
            "value": "https://avatars1.githubusercontent.com/u/14039952?s=460&v=4",
            "type": "string"
        },
        "MAIL_PASSWORD": {
            "sort": 99,
            "info": "邮箱密码, 是用于发送邮件的密码",
            "value": "<Your password>",
            "type": "password"
        },
        "MAIL_SERVER": {
            "sort": 99,
            "info": "邮箱服务器smtp",
            "value": "smtp.mxhichina.com",
            "type": "string"
        },
        "APP_NAME": {
            "sort": 99,
            "info": "在邮件中显示的APP(WEB)名称(1.不填写则不显示.2.如果主题邮件发送html模板不支持，也不显示)",
            "value": "OSR DEMO",
            "type": "string"
        },
        "MAIL_USE_SSL": {
            "sort": 99,
            "info": "是否使用SSL",
            "value": True,
            "type": "bool"
        },
        "MAIL_DEFAULT_SENDER": {
            "sort": 99,
            "info": "默认发送者邮箱　(显示名称, 邮箱地址)顺序不能调换",
            "value": [
                "OSR DEMO",
                "system@osroom.com"
            ],
            "type": "list"
        },
        "MAIL_USERNAME": {
            "sort": 99,
            "info": "邮箱用户名",
            "value": "system@osroom.com",
            "type": "string"
        },
        "__sort__": 10,
        "__restart__": "must",
        "MAIL_ASCII_ATTACHMENTS": {
            "sort": 99,
            "info": "MAIL ASCII ATTACHMENTS",
            "value": True,
            "type": "bool"
        },
        "MAIL_FOOTER": {
            "sort": 99,
            "info": "发送邮件的页尾",
            "value": "OSROOM开源网站系统",
            "type": "string"
        },
        "MAIL_SUBJECT_SUFFIX": {
            "sort": 99,
            "info": "发送邮件的标题后缀",
            "value": "OSROOM",
            "type": "string"
        },
        "MAIL_PORT": {
            "sort": 99,
            "info": "邮箱服务器端口",
            "value": 465,
            "type": "int"
        },
        "MAIL_USE_TLS": {
            "sort": 99,
            "info": "是否使用TLS",
            "value": False,
            "type": "bool"
        },
        "__info__": "邮件发送参数设置（建议技术管理人员使用）"
    },
    "user_model": {
        "__restart__": "not_must",
        "EDITOR": {
            "sort": 99,
            "info": "新用户默认编辑器类型rich_text或markdown",
            "value": "rich_text",
            "type": "string"
        },
        "__sort__": 99,
        "__info__": "用户Model"
    },
    "babel": {
        "__restart__": "must",
        "BABEL_DEFAULT_LOCALE": {
            "sort": 99,
            "info": "默认语言:可以是zh_CN, en_US等()",
            "value": "zh_CN",
            "type": "string"
        },
        "LANGUAGES": {
            "sort": 99,
            "info": "管理端支持的语言",
            "value": {
                "en_US": {
                    "name": "English",
                    "alias": "En"
                },
                "zh_CN": {
                    "name": "中文",
                    "alias": "中文"
                }
            },
            "type": "dict"
        },
        "__sort__": 9,
        "__info__": "多语言设置"
    },
    "category": {
        "__restart__": "not_must",
        "CATEGORY_TYPE": {
            "sort": 99,
            "info": "分类的品种只能有这几种",
            "value": {
                "主题图片图文": "image_theme",
                "文本内容": "text",
                "主题视频": "video_theme",
                "视频库": "video",
                "主题文本": "text_theme",
                "主题其他": "other_theme",
                "其他": "other",
                "主题音频": "audio_theme",
                "文集": "post",
                "音频库": "audio",
                "图库": "image"
            },
            "type": "dict"
        },
        "CATEGORY_MAX_LEN": {
            "sort": 99,
            "info": "分类名称类型名最多几个字符",
            "value": 15,
            "type": "int"
        },
        "__sort__": 7,
        "__info__": "Web参数设置"
    },
    "post": {
        "__restart__": "not_must",
        "TAG_MAX_LEN": {
            "sort": 99,
            "info": "POST标签最多几个字",
            "value": 10,
            "type": "int"
        },
        "NUM_PAGE": {
            "sort": 99,
            "info": "每个页面获取几篇文章, 如果请求获取文章时指定了指定了per参数, 则此配置无效(此配置也对管理端无效)",
            "value": 10,
            "type": "int"
        },
        "TITLE_MAX_LEN": {
            "sort": 99,
            "info": "文章Title最大长度",
            "value": 50,
            "type": "int"
        },
        "BRIEF_LEN": {
            "sort": 99,
            "info": "获取文章简要的字数",
            "value": 80,
            "type": "int"
        },
        "TAG_MAX_NUM": {
            "sort": 99,
            "info": "POST标签最大个数",
            "value": 5,
            "type": "int"
        },
        "MAX_LEN": {
            "sort": 99,
            "info": "发布文章最多几个字符",
            "value": 5000,
            "type": "int"
        },
        "GET_POST_CACHE_TIME_OUT": {
            "sort": 99,
            "info": "获取多个post数据时, 缓存超时时间(s), 为0表示不缓存数据.<br><span style='color:red;'>只对获取已公开发布的, 并且不是当前用户发布的post有效</span>",
            "value": 60,
            "type": "int"
        },
        "__info__": "文章内容设置",
        "__sort__": 2,
        "NUM_PAGE_MAX": {
            "sort": 99,
            "info": "每个页面最多获取几篇文章(此配置对管理端无效)",
            "value": 30,
            "type": "int"
        }
    },
    "rest_auth_token": {
        "__restart__": "not_must",
        "REST_ACCESS_TOKEN_LIFETIME": {
            "sort": 99,
            "info": "给客户端发补的访问Token AccessToken的有效期",
            "value": 172800,
            "type": "int"
        },
        "LOGIN_LIFETIME": {
            "sort": 99,
            "info": "jwt 登录BearerToken有效期(s)",
            "value": 2592000,
            "type": "int"
        },
        "__info__": "Web参数设置",
        "MAX_SAME_TIME_LOGIN": {
            "sort": 99,
            "info": "最多能同时登录几个使用JWT验证的客户端,超过此数目则会把旧的登录注销",
            "value": 3,
            "type": "int"
        },
        "__sort__": 99
    },
    "login_manager": {
        "__restart__": "not_must",
        "PW_WRONG_NUM_IMG_CODE": {
            "sort": 99,
            "info": "同一用户登录密码错误几次后响应图片验证码, 并且需要验证",
            "value": 5,
            "type": "int"
        },
        "LOGIN_VIEW": {
            "sort": 99,
            "info": "需要登录的页面,未登录时,api会响应401,并带上需要跳转到路由to_url",
            "value": "/sign-in",
            "type": "string"
        },
        "OPEN_REGISTER": {
            "sort": 99,
            "info": "开放注册",
            "value": True,
            "type": "bool"
        },
        "LOGIN_OUT_TO": {
            "sort": 99,
            "info": "退出登录后,api会响应数据会带上需要跳转到路由to_url",
            "value": "/",
            "type": "string"
        },
        "LOGIN_IN_TO": {
            "sort": 99,
            "info": "登录成功后,api会响应数据会带上需要跳转到路由to_url",
            "value": "/",
            "type": "string"
        },
        "__info__": "在线管理（建议技术管理人员使用）",
        "__sort__": 99
    },
    "account": {
        "__restart__": "not_must",
        "USER_AVATAR_MAX_SIZE": {
            "sort": 99,
            "info": "用户头像不能上传超过此值大小(单位Mb)的图片作头像",
            "value": 10.0,
            "type": "float"
        },
        "USERNAME_MAX_LEN": {
            "sort": 99,
            "info": "用户名最大长度",
            "value": 20,
            "type": "int"
        },
        "USER_AVATAR_SIZE": {
            "sort": 99,
            "info": "用户头像保存大小[<width>, <height>]像素",
            "value": [
                "360",
                "360"
            ],
            "type": "list"
        },
        "__info__": "账户设置",
        "__sort__": 6,
        "DEFAULT_AVATAR": {
            "sort": 99,
            "info": "新注册用户默认头像的URL",
            "value": [
                "/static/admin/sys_imgs/avatar_default_1.png",
                "/static/admin/sys_imgs/avatar_default_2.png"
            ],
            "type": "string"
        }
    },
    "name_audit": {
        "AUDIT_PROJECT_KEY": {
            "sort": 99,
            "info": "审核项目的Key(键),审核时会使用一个Key来获取审核规则,正则去匹配用户输入的内容",
            "value": {
                "username": "审核用户名",
                "class_name": "审核一些短的分类名称, 如category, tag"
            },
            "type": "dict"
        },
        "__restart__": "not_must",
        "__sort__": 8,
        "__info__": "名称验证, 如用户名,分类名称"
    },
    "seo": {
        "__restart__": "not_must",
        "__sort__": 4,
        "__info__": "针对网页客户端的简单的SEO配置<br>此模块所有的KEY值, 都可以直接请求全局Api(<br><span style='color:red;'>/api/global</span>)获取.<br>也可以直接在主题中使用Jinjia2模板引擎获取(<br><span style='color:red;'>g.site_global.site_config.XXXX</span>)",
        "DEFAULT_DESCRIPTION": {
            "sort": 99,
            "info": "网站的页面默认简单描述",
            "value": "开源Web系统, 可以作为企业网站, 个人博客网站, 微信小程序Web服务端",
            "type": "string"
        },
        "DEFAULT_KEYWORDS": {
            "sort": 99,
            "info": "网站的页面默认关键词",
            "value": "开源, 企业网站, 博客网站, 微信小程序, Web服务端",
            "type": "string"
        }
    },
    "theme": {
        "__restart__": "not_must",
        "__info__": "主题配置",
        "CURRENT_THEME_NAME": {
            "sort": 99,
            "info": "当前主题名称,需与主题主目录名称相同",
            "value": "osr-style",
            "type": "string"
        },
        "VERSION": {
            "sort": 99,
            "info": "当前主题版本",
            "value": "v0.1",
            "type": "string"
        }
    },
    "content_inspection": {
        "__restart__": "not_must",
        "IMAGE_OPEN": {
            "sort": 99,
            "info": "开启图片检测.需要hook_name为content_inspection_image的图片检测插件",
            "value": False,
            "type": "bool"
        },
        "VEDIO_OPEN": {
            "sort": 99,
            "info": "开启视频检测.需要hook_name为content_inspection_vedio的视频检测插件",
            "value": False,
            "type": "bool"
        },
        "AUDIO_OPEN": {
            "sort": 99,
            "info": "开启音频检测.需要hook_name为content_inspection_audio的音频检测插件",
            "value": False,
            "type": "bool"
        },
        "TEXT_OPEN": {
            "sort": 99,
            "info": "开启text检测.需要hook_name为content_inspection_text的文本检测插件",
            "value": True,
            "type": "bool"
        },
        "ALLEGED_ILLEGAL_SCORE": {
            "sort": 99,
            "info": "内容检测分数高于多少分时属于涉嫌违规(0-100分,对于需要检查的内容有效)",
            "value": 99,
            "type": "float"
        },
        "__info__": "内容检查配置(需要安装相关插件该配置才生效).<br>检测开关:<br>1.如果开启, 并安装有相关的自动检查插件, 则会给发布的内容给出违规评分.如果未安装自动审核插件,则系统会给予评分100分(属涉嫌违规,网站工作人员账户除外).<br>2.如果关闭审核，则系统会给评分0分(不违规)",
        "__sort__": 5
    },
    "weblogger": {
        "__restart__": "not_must",
        "SING_IN_LOG_KEEP_NUM": {
            "sort": 99,
            "info": "登录日志保留个数",
            "value": 30,
            "type": "int"
        },
        "__info__": "操作日志设置",
        "USER_OP_LOG_KEEP_NUM": {
            "sort": 99,
            "info": "用户操作日志保留个数",
            "value": 30,
            "type": "int"
        },
        "__sort__": 99
    },
    "upload": {
        "__restart__": "not_must",
        "UP_ALLOWED_EXTENSIONS": {
            "sort": 99,
            "info": "上传:允许上传的文件后缀(全部小写),每个用英文的','隔开",
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
        "__sort__": 99,
        "SAVE_DIR": {
            "sort": 99,
            "info": "上传:保存目录,如何存在'/'则会自动切分创建子目录",
            "value": "media",
            "type": "string"
        },
        "__info__": "文件上传配置（建议技术管理人员使用）"
    },
    "comment": {
        "INTERVAL": {
            "sort": 99,
            "info": "控制评论频繁度时间(s)",
            "value": 30,
            "type": "int"
        },
        "__restart__": "not_must",
        "NUM_PAGE": {
            "sort": 99,
            "info": "每个页面获取几条评论, 如果请求获取评论时指定了指定了per参数, 则此配置无效(此配置也对管理端无效)",
            "value": 10,
            "type": "int"
        },
        "NUM_OF_INTERVAL": {
            "sort": 99,
            "info": "控制评论频繁度时间内最多评论几次",
            "value": 3,
            "type": "int"
        },
        "TRAVELER_COMMENT": {
            "sort": 99,
            "info": "游客评论开关,是否打开?",
            "value": False,
            "type": "bool"
        },
        "MAX_LEN": {
            "sort": 99,
            "info": "发布评论最多几个字符",
            "value": 300,
            "type": "int"
        },
        "OPEN_COMMENT": {
            "sort": 99,
            "info": "评论开关,是否打开评论功能?",
            "value": False,
            "type": "bool"
        },
        "__info__": "评论内容设置",
        "__sort__": 3,
        "NUM_PAGE_MAX": {
            "sort": 99,
            "info": "每个页面最多获取几条评论(此配置对管理端无效)",
            "value": 30,
            "type": "int"
        }
    },
    "cache": {
        "__restart__": "must",
        "CACHE_KEY_PREFIX": {
            "sort": 99,
            "info": "所有键(key)之前添加的前缀,这使得它可以为不同的应用程序使用相同的memcached(内存)服务器.",
            "value": "osr_cache",
            "type": "string"
        },
        "USE_CACHE": {
            "sort": 99,
            "info": "是否使用缓存功能,建议开启",
            "value": True,
            "type": "bool"
        },
        "CACHE_DEFAULT_TIMEOUT": {
            "sort": 99,
            "info": "(s秒)默认缓存时间,当单个缓存没有设定缓存时间时会使用该时间",
            "value": 600,
            "type": "int"
        },
        "CACHE_TYPE": {
            "sort": 99,
            "info": "缓存使用的类型,可选择redis,mongodb",
            "value": "redis",
            "type": "string"
        },
        "CACHE_MONGODB_COLLECT": {
            "sort": 99,
            "info": "保存cache的collection,当CACHE_TYPE为mongodb时有效",
            "value": "osr_cache",
            "type": "string"
        },
        "__sort__": 99,
        "__info__": "Web缓存参数设置（建议技术管理人员使用）"
    },
    "key": {
        "SECRET_KEY": {
            "sort": 99,
            "info": "安全验证码",
            "value": "ceavewrvwtrhdyjydj",
            "type": "string"
        },
        "__restart__": "must",
        "__info__": "安全Key（建议技术管理人员使用）",
        "SECURITY_PASSWORD_SALT": {
            "sort": 99,
            "info": "安全密码码盐值",
            "value": "ceavewrvwtrhdyjydj",
            "type": "string"
        },
        "__sort__": 99
    },
    "verify_code": {
        "__restart__": "not_must",
        "IMG_CODE_DIR": {
            "sort": 99,
            "info": "图片验证码保存目录",
            "value": "verify_code",
            "type": "string"
        },
        "MAX_NUM_SEND_SAMEIP_PERMIN": {
            "sort": 99,
            "info": "同一IP地址,同一用户(未登录的同属一匿名用户), 允许每分钟调用API发送验证码的最大次数",
            "value": 15,
            "type": "int"
        },
        "SEND_CODE_TYPE": {
            "sort": 99,
            "info": "发送的验证码字符类型，与字符个数",
            "value": {
                "string": 0,
                "int": 6
            },
            "type": "dict"
        },
        "MAX_IMG_CODE_INTERFERENCE": {
            "sort": 99,
            "info": "图片验证码干扰程度的最大值",
            "value": 40,
            "type": "int"
        },
        "MAX_NUM_SEND_SAMEIP_PERMIN_NO_IMGCODE": {
            "sort": 99,
            "info": "同一IP地址,同一用户(未登录的同属同一匿名用户),允许每分钟在不验证[图片验证码]的时候,调用API发送验证码最大次数.<br>超过次数后API会生成[图片验证码]并返回图片url对象(也可以自己调用获取图片验证码API获取).<br>如果你的客户端(包括主题)不支持显示图片验证码,请设置此配置为99999999",
            "value": 1,
            "type": "int"
        },
        "EXPIRATION": {
            "sort": 99,
            "info": "验证码过期时间(s)",
            "value": 600,
            "type": "int"
        },
        "MIN_IMG_CODE_INTERFERENCE": {
            "sort": 99,
            "info": "图片验证码干扰程度的最小值,最小值小于10时无效",
            "value": 10,
            "type": "int"
        },
        "__sort__": 11,
        "__info__": "验证码(建议技术管理员配置)"
    },
    "system": {
        "KEY_HIDING": {
            "sort": 2,
            "info": "开启后,管理端通过/api/admin/xxx获取到的数据中，密钥类型的值，则会以随机字符代替.<br><span style='color:red;'>如某个插件配置中有密码, 不想让它暴露在浏览器, 则可开启.</span>",
            "value": True,
            "type": "bool"
        },
        "TEMPLATES_AUTO_RELOAD": {
            "sort": 3,
            "info": "是否自动加载页面(html)模板.开启后,每次html页面修改都无需重启Web",
            "value": True,
            "type": "bool"
        },
        "MAX_CONTENT_LENGTH": {
            "sort": 1,
            "info": "拒绝内容长度大于此值的请求进入，并返回一个 413 状态码(单位:Mb)",
            "value": 50.0,
            "type": "float"
        },
        "__restart__": "must",
        "__sort__": 99,
        "__info__": "其他web系统参数设置（建议技术管理人员使用）"
    },
    "site_config": {
        "HEAD_CODE": {
            "sort": 13,
            "info": "用于放入html中<br><span style='color:red;'>head标签</span>内的js/css/html代码(如Google分析代码/百度统计代码)",
            "value": "",
            "type": "string"
        },
        "MB_LOGO_DISPLAY": {
            "sort": 4,
            "info": "移动端用App name 还是Logo image 作为APP(Web)的Logo显示, 为空则App name优先<br>可填logo或name(需要主题支持)",
            "value": "name",
            "type": "string"
        },
        "PC_LOGO_DISPLAY": {
            "sort": 3,
            "info": "PC端用App name 还是Logo image 作为APP(Web)的Logo显示, 为空则显示Logo和App name<br>可填logo或name(需要主题支持)",
            "value": "logo",
            "type": "string"
        },
        "STATIC_FILE_VERSION": {
            "sort": 12,
            "info": "静态文件版本(当修改了CSS,JS等静态文件的时候，修改此版本号)",
            "value": 20181024065925,
            "type": "int"
        },
        "APP_NAME": {
            "sort": 1,
            "info": "APP(站点)名称,将作为全局变量使用在平台上",
            "value": "OSR DEMO",
            "type": "string"
        },
        "DOES_NOT_EXIST_URL": {
            "sort": 11,
            "info": "当一个文件或图片不存在的时候, 返回此Image URL",
            "value": "/static/sys_imgs/does_not_exist.png",
            "type": "string"
        },
        "FRIEND_LINK": {
            "sort": 11,
            "info": "友情链接:值(Value)格式为{'url':'友情链接', 'logo_url':'logo链接'}",
            "value": {
                "阿里云": {
                    "aliases": "阿里云",
                    "url": "www.aliyun.com",
                    "icon_url": "",
                    "level": 1
                },
                "七牛云": {
                    "aliases": "七牛云",
                    "url": "www.aliyun.com",
                    "icon_url": "",
                    "level": 1
                },
                "码云": {
                    "aliases": "码云",
                    "url": "www.aliyun.com",
                    "icon_url": "",
                    "level": 1
                },
                "Github": {
                    "aliases": "Github",
                    "url": "www.aliyun.com",
                    "icon_url": "",
                    "level": 1
                }
            },
            "type": "dict"
        },
        "TITLE_SUFFIX": {
            "sort": 8,
            "info": "APP(Web)Title后缀",
            "value": "OSROOM开源Web DEMO",
            "type": "string"
        },
        "__sort__": 1,
        "__restart__": "not_must",
        "LOGO_IMG_URL": {
            "sort": 2,
            "info": "APP(Web)Logo的URL",
            "value": "/static/sys_imgs/osroom-logo.png",
            "type": "string"
        },
        "FAVICON": {
            "sort": 10,
            "info": "APP(Web)favicon图标的URL",
            "value": "/static/sys_imgs/osroom-logo.ico",
            "type": "string"
        },
        "SITE_URL": {
            "sort": 11,
            "info": "Web站点URL(如果没有填写, 则使用默认的当前域名首页地址)",
            "value": "http://www.osroom.com",
            "type": "string"
        },
        "FOOTER_CODE": {
            "sort": 13,
            "info": "用于放入html中<br><span style='color:red;'>body标签</span>内的js/css/html代码(如Google分析代码/百度统计代码)",
            "value": "",
            "type": "string"
        },
        "TITLE_PREFIX": {
            "sort": 6,
            "info": "APP(Web)Title前缀",
            "value": "",
            "type": "string"
        },
        "TITLE_SUFFIX_ADM": {
            "sort": 9,
            "info": "APP(Web)管理端Title后缀",
            "value": "OSROOM管理端",
            "type": "string"
        },
        "__info__": "基础设置: APP(Web)全局数据设置<br>此模块所有的KEY值, 都可以直接请求全局Api(/api/global)获取.也可以直接在主题中使用Jinjia2模板引擎获取(g.site_global.site_config.XXXX)",
        "BACKGROUND_IMG_URL": {
            "sort": 5,
            "info": "网页背景图片(需要主题支持)",
            "value": "/static/sys_imgs/background.jpg",
            "type": "string"
        },
        "TITLE_PREFIX_ADM": {
            "sort": 7,
            "info": "APP(Web)管理端Title前缀",
            "value": "",
            "type": "string"
        }
    }
}