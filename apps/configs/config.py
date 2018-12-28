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
    "content_inspection": {
        "ALLEGED_ILLEGAL_SCORE": {
            "type": "float",
            "value": 99,
            "sort": 99,
            "info": "内容检测分数高于多少分时属于涉嫌违规(0-100分,对于需要检查的内容有效)"
        },
        "__restart__": "not_must",
        "IMAGE_OPEN": {
            "type": "bool",
            "value": False,
            "sort": 99,
            "info": "开启图片检测.需要hook_name为content_inspection_image的图片检测插件"
        },
        "__info__": "内容检查配置(需要安装相关插件该配置才生效).<br>检测开关:<br>1.如果开启, 并安装有相关的自动检查插件, 则会给发布的内容给出违规评分.如果未安装自动审核插件,则系统会给予评分100分(属涉嫌违规,网站工作人员账户除外).<br>2.如果关闭审核，则系统会给评分0分(不违规)",
        "TEXT_OPEN": {
            "type": "bool",
            "value": True,
            "sort": 99,
            "info": "开启text检测.需要hook_name为content_inspection_text的文本检测插件"
        },
        "__sort__": 5,
        "VEDIO_OPEN": {
            "type": "bool",
            "value": False,
            "sort": 99,
            "info": "开启视频检测.需要hook_name为content_inspection_vedio的视频检测插件"
        },
        "AUDIO_OPEN": {
            "type": "bool",
            "value": False,
            "sort": 99,
            "info": "开启音频检测.需要hook_name为content_inspection_audio的音频检测插件"
        }
    },
    "comment": {
        "MAX_LEN": {
            "type": "int",
            "value": 300,
            "sort": 99,
            "info": "发布评论最多几个字符"
        },
        "NUM_OF_INTERVAL": {
            "type": "int",
            "value": 3,
            "sort": 99,
            "info": "控制评论频繁度时间内最多评论几次"
        },
        "__info__": "评论内容设置",
        "NUM_PAGE_MAX": {
            "type": "int",
            "value": 30,
            "sort": 99,
            "info": "每个页面最多获取几条评论(此配置对管理端无效)"
        },
        "__sort__": 3,
        "NUM_PAGE": {
            "type": "int",
            "value": 10,
            "sort": 99,
            "info": "每个页面获取几条评论, 如果请求获取评论时指定了指定了per参数, 则此配置无效(此配置也对管理端无效)"
        },
        "OPEN_COMMENT": {
            "type": "bool",
            "value": True,
            "sort": 99,
            "info": "评论开关,是否打开评论功能?"
        },
        "TRAVELER_COMMENT": {
            "type": "bool",
            "value": True,
            "sort": 99,
            "info": "游客评论开关,是否打开?"
        },
        "INTERVAL": {
            "type": "int",
            "value": 30,
            "sort": 99,
            "info": "控制评论频繁度时间(s)"
        },
        "__restart__": "not_must"
    },
    "theme": {
        "CURRENT_THEME_NAME": {
            "type": "string",
            "value": "osr-style",
            "sort": 99,
            "info": "当前主题名称,需与主题主目录名称相同"
        },
        "__restart__": "not_must",
        "__info__": "主题配置"
    },
    "py_venv": {
        "VENV_PATH": {
            "type": "string",
            "value": "/home/work/project/venv3",
            "sort": 99,
            "info": "python虚拟环境路径"
        }
    },
    "seo": {
        "__sort__": 4,
        "DEFAULT_KEYWORDS": {
            "type": "string",
            "value": "开源, 企业网站, 博客网站, 微信小程序, Web服务端",
            "sort": 99,
            "info": "网站的页面默认关键词"
        },
        "__restart__": "not_must",
        "__info__": "针对网页客户端的简单的SEO配置<br>此模块所有的KEY值, 都可以直接请求全局Api(<br><span style='color:red;'>/api/global</span>)获取.<br>也可以直接在主题中使用Jinjia2模板引擎获取(<br><span style='color:red;'>g.site_global.site_config.XXXX</span>)",
        "DEFAULT_DESCRIPTION": {
            "type": "string",
            "value": "开源Web系统, 可以作为企业网站, 个人博客网站, 微信小程序Web服务端",
            "sort": 99,
            "info": "网站的页面默认简单描述"
        }
    },
    "login_manager": {
        "__restart__": "not_must",
        "__info__": "在线管理（建议技术管理人员使用）",
        "__sort__": 99,
        "LOGIN_VIEW": {
            "type": "string",
            "value": "/sign-in",
            "sort": 99,
            "info": "需要登录的页面,未登录时,api会响应401,并带上需要跳转到路由to_url"
        },
        "OPEN_REGISTER": {
            "type": "bool",
            "value": True,
            "sort": 99,
            "info": "开放注册"
        },
        "LOGIN_IN_TO": {
            "type": "string",
            "value": "/",
            "sort": 99,
            "info": "登录成功后,api会响应数据会带上需要跳转到路由to_url"
        },
        "PW_WRONG_NUM_IMG_CODE": {
            "type": "int",
            "value": 5,
            "sort": 99,
            "info": "同一用户登录密码错误几次后响应图片验证码, 并且需要验证"
        },
        "LOGIN_OUT_TO": {
            "type": "string",
            "value": "/",
            "sort": 99,
            "info": "退出登录后,api会响应数据会带上需要跳转到路由to_url"
        }
    },
    "category": {
        "__sort__": 7,
        "CATEGORY_MAX_LEN": {
            "type": "int",
            "value": 30,
            "sort": 99,
            "info": "分类名称类型名最多几个字符"
        },
        "__restart__": "not_must",
        "__info__": "Web参数设置",
        "CATEGORY_TYPE": {
            "type": "dict",
            "value": {
                "主题-文本": "text_theme",
                "主题-图文": "image_theme",
                "主题-视频": "video_theme",
                "主题-其他": "other_theme",
                "主题-音频": "audio_theme",
                "其他类型库": "other",
                "图文|图库": "image",
                "文本内容": "text",
                "文集": "post",
                "视频库": "video",
                "音频库": "audio"
            },
            "sort": 99,
            "info": "分类的品种只能有这几种"
        }
    },
    "theme_global_conf": {
        "__restart__": "not_must",
        "__info__": "主题的一些全局配置(只对主题有效, 并需要主题支持)",
        "__sort__": 99,
        "TOP_NAV": {
            "type": "dict",
            "value": {
                "1": {
                    "link": "/",
                    "nav": "首页",
                    "next_lev": None
                },
                "2": {
                    "link": "/photo",
                    "nav": "图库",
                    "next_lev": None
                },
                "3": "{\"link\":\"\",\"nav\":\"关于\",\"next_lev\":[{\"link\":\"post?id=5c25ebac38ab5579004b3f21\",\"nav\":\"时间轴\"}，{\"link\":\"/about-us\",\"nav\":\"关于我们\"},{\"link\":\"/contact\",\"nav\":\"联系我们\"}]}",
                "4": {
                    "link": "/post?id=5aede042c8980538592c3b7b",
                    "nav": "留言板",
                    "next_lev": None
                }
            },
            "sort": 99,
            "info": "最多能同时登录几个使用JWT验证的客户端,超过此数目则会把旧的登录注销"
        }
    },
    "rest_auth_token": {
        "LOGIN_LIFETIME": {
            "type": "int",
            "value": 2592000,
            "sort": 99,
            "info": "jwt 登录BearerToken有效期(s)"
        },
        "__restart__": "not_must",
        "__info__": "Web参数设置",
        "__sort__": 99,
        "MAX_SAME_TIME_LOGIN": {
            "type": "int",
            "value": 3,
            "sort": 99,
            "info": "最多能同时登录几个使用JWT验证的客户端,超过此数目则会把旧的登录注销"
        },
        "REST_ACCESS_TOKEN_LIFETIME": {
            "type": "int",
            "value": 172800,
            "sort": 99,
            "info": "给客户端发补的访问Token AccessToken的有效期"
        }
    },
    "site_config": {
        "BACKGROUND_IMG_URL": {
            "type": "string",
            "value": "/static/sys_imgs/background.jpg",
            "sort": 5,
            "info": "网页背景图片(需要主题支持)"
        },
        "SITE_URL": {
            "type": "string",
            "value": "http://www.osroom.com",
            "sort": 11,
            "info": "Web站点URL(如果没有填写, 则使用默认的当前域名首页地址)"
        },
        "DOES_NOT_EXIST_URL": {
            "type": "string",
            "value": "/static/sys_imgs/does_not_exist.png",
            "sort": 11,
            "info": "当一个文件或图片不存在的时候, 返回此Image URL"
        },
        "TITLE_PREFIX_ADM": {
            "type": "string",
            "value": "",
            "sort": 7,
            "info": "APP(Web)管理端Title前缀"
        },
        "__info__": "基础设置: APP(Web)全局数据设置<br>此模块所有的KEY值, 都可以直接请求全局Api(/api/global)获取.也可以直接在主题中使用Jinjia2模板引擎获取(g.site_global.site_config.XXXX)",
        "FOOTER_CODE": {
            "type": "string",
            "value": "",
            "sort": 13,
            "info": "用于放入html中<br><span style='color:red;'>body标签</span>内的js/css/html代码(如Google分析代码/百度统计代码)"
        },
        "__sort__": 1,
        "TITLE_SUFFIX_ADM": {
            "type": "string",
            "value": "OSROOM管理端",
            "sort": 9,
            "info": "APP(Web)管理端Title后缀"
        },
        "APP_NAME": {
            "type": "string",
            "value": "OSR DEMO",
            "sort": 1,
            "info": "APP(站点)名称,将作为全局变量使用在平台上"
        },
        "FAVICON": {
            "type": "string",
            "value": "/static/sys_imgs/osroom-logo.ico",
            "sort": 10,
            "info": "APP(Web)favicon图标的URL"
        },
        "TITLE_SUFFIX": {
            "type": "string",
            "value": "OSROOM开源Web DEMO",
            "sort": 8,
            "info": "APP(Web)Title后缀"
        },
        "FRIEND_LINK": {
            "type": "dict",
            "value": {
                "Github": {
                    "logo_url": "http://osr.local.com:5000/static/admin/sys_imgs/osroom-logo-1.png?w=240&h=240",
                    "url": "https://github.com/osroom/osroom"
                }
            },
            "sort": 11,
            "info": "友情链接:值(Value)格式为{'url':'友情链接', 'logo_url':'logo链接'}"
        },
        "PC_LOGO_DISPLAY": {
            "type": "string",
            "value": "logo",
            "sort": 3,
            "info": "PC端用App name 还是Logo image 作为APP(Web)的Logo显示, 为空则显示Logo和App name<br>可填logo或name(需要主题支持)"
        },
        "__restart__": "not_must",
        "MB_LOGO_DISPLAY": {
            "type": "string",
            "value": "logo",
            "sort": 4,
            "info": "移动端用App name 还是Logo image 作为APP(Web)的Logo显示, 为空则App name优先<br>可填logo或name(需要主题支持)"
        },
        "TITLE_PREFIX": {
            "type": "string",
            "value": "",
            "sort": 6,
            "info": "APP(Web)Title前缀"
        },
        "STATIC_FILE_VERSION": {
            "type": "int",
            "value": 20181208125734,
            "sort": 12,
            "info": "静态文件版本(当修改了CSS,JS等静态文件的时候，修改此版本号)"
        },
        "LOGO_IMG_URL": {
            "type": "string",
            "value": "/static/sys_imgs/osroom-logo.png",
            "sort": 2,
            "info": "APP(Web)Logo的URL"
        },
        "HEAD_CODE": {
            "type": "string",
            "value": "",
            "sort": 13,
            "info": "用于放入html中<br><span style='color:red;'>head标签</span>内的js/css/html代码(如Google分析代码/百度统计代码)"
        }
    },
    "system": {
        "TEMPLATES_AUTO_RELOAD": {
            "type": "bool",
            "value": True,
            "sort": 3,
            "info": "是否自动加载页面(html)模板.开启后,每次html页面修改都无需重启Web"
        },
        "__restart__": "must",
        "MAX_CONTENT_LENGTH": {
            "type": "float",
            "value": 50.0,
            "sort": 1,
            "info": "拒绝内容长度大于此值的请求进入，并返回一个 413 状态码(单位:Mb)"
        },
        "__info__": "其他web系统参数设置（建议技术管理人员使用）",
        "__sort__": 99,
        "KEY_HIDING": {
            "type": "bool",
            "value": True,
            "sort": 2,
            "info": "开启后,管理端通过/api/admin/xxx获取到的数据中，密钥类型的值，则会以随机字符代替.<br><span style='color:red;'>如某个插件配置中有密码, 不想让它暴露在浏览器, 则可开启.</span>"
        }
    },
    "session": {
        "__restart__": "must",
        "SESSION_MONGODB_COLLECT": {
            "type": "string",
            "value": "osr_session",
            "sort": 99,
            "info": "Mongodb保存session的collection,当SESSION_TYPE为mongodb时有效"
        },
        "__info__": "Session参数设置（建议技术管理人员使用）",
        "SESSION_PERMANENT": {
            "type": "bool",
            "value": True,
            "sort": 99,
            "info": "是否使用永久会话"
        },
        "__sort__": 99,
        "SESSION_TYPE": {
            "type": "string",
            "value": "redis",
            "sort": 99,
            "info": "保存Session会话的类型,可选mongodb, redis"
        },
        "SESSION_KEY_PREFIX": {
            "type": "string",
            "value": "osr-session:",
            "sort": 99,
            "info": "添加一个前缀,之前所有的会话密钥。这使得它可以为不同的应用程序使用相同的后端存储服务器"
        },
        "PERMANENT_SESSION_LIFETIME": {
            "type": "int",
            "value": 2592000,
            "sort": 99,
            "info": "永久会话的有效期."
        }
    },
    "weblogger": {
        "__sort__": 99,
        "__restart__": "not_must",
        "SING_IN_LOG_KEEP_NUM": {
            "type": "int",
            "value": 30,
            "sort": 99,
            "info": "登录日志保留个数"
        },
        "__info__": "操作日志设置",
        "USER_OP_LOG_KEEP_NUM": {
            "type": "int",
            "value": 30,
            "sort": 99,
            "info": "用户操作日志保留个数"
        }
    },
    "user_model": {
        "__sort__": 99,
        "__restart__": "not_must",
        "__info__": "用户Model",
        "EDITOR": {
            "type": "string",
            "value": "rich_text",
            "sort": 99,
            "info": "新用户默认编辑器类型rich_text或markdown"
        }
    },
    "verify_code": {
        "MAX_NUM_SEND_SAMEIP_PERMIN_NO_IMGCODE": {
            "type": "int",
            "value": 1,
            "sort": 99,
            "info": "同一IP地址,同一用户(未登录的同属同一匿名用户),允许每分钟在不验证[图片验证码]的时候,调用API发送验证码最大次数.<br>超过次数后API会生成[图片验证码]并返回图片url对象(也可以自己调用获取图片验证码API获取).<br>如果你的客户端(包括主题)不支持显示图片验证码,请设置此配置为99999999"
        },
        "__restart__": "not_must",
        "__info__": "验证码(建议技术管理员配置)",
        "IMG_CODE_DIR": {
            "type": "string",
            "value": "admin/verify_code",
            "sort": 99,
            "info": "图片验证码保存目录"
        },
        "__sort__": 11,
        "EXPIRATION": {
            "type": "int",
            "value": 600,
            "sort": 99,
            "info": "验证码过期时间(s)"
        },
        "MIN_IMG_CODE_INTERFERENCE": {
            "type": "int",
            "value": 10,
            "sort": 99,
            "info": "图片验证码干扰程度的最小值,最小值小于10时无效"
        },
        "MAX_NUM_SEND_SAMEIP_PERMIN": {
            "type": "int",
            "value": 15,
            "sort": 99,
            "info": "同一IP地址,同一用户(未登录的同属一匿名用户), 允许每分钟调用API发送验证码的最大次数"
        },
        "SEND_CODE_TYPE": {
            "type": "dict",
            "value": {
                "int": 6,
                "string": 0
            },
            "sort": 99,
            "info": "发送的验证码字符类型，与字符个数"
        },
        "MAX_IMG_CODE_INTERFERENCE": {
            "type": "int",
            "value": 40,
            "sort": 99,
            "info": "图片验证码干扰程度的最大值"
        }
    },
    "upload": {
        "__sort__": 99,
        "SAVE_DIR": {
            "type": "string",
            "value": "media",
            "sort": 99,
            "info": "上传:保存目录,如何存在'/'则会自动切分创建子目录"
        },
        "UP_ALLOWED_EXTENSIONS": {
            "type": "list",
            "value": [
                "txt",
                "xlxs",
                "excel",
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
            "sort": 99,
            "info": "上传:允许上传的文件后缀(全部小写),每个用英文的','隔开"
        },
        "__restart__": "not_must",
        "__info__": "文件上传配置（建议技术管理人员使用）"
    },
    "key": {
        "SECURITY_PASSWORD_SALT": {
            "type": "string",
            "value": "12343erfegrg",
            "sort": 99,
            "info": "安全密码码盐值"
        },
        "__sort__": 99,
        "__restart__": "must",
        "SECRET_KEY": {
            "type": "string",
            "value": "12333r32fddvve",
            "sort": 99,
            "info": "安全验证码"
        },
        "__info__": "安全Key（建议技术管理人员使用）"
    },
    "babel": {
        "__sort__": 9,
        "BABEL_DEFAULT_LOCALE": {
            "type": "string",
            "value": "zh_CN",
            "sort": 99,
            "info": "默认语言:可以是zh_CN, en_US等()"
        },
        "LANGUAGES": {
            "type": "dict",
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
            "sort": 99,
            "info": "管理端支持的语言"
        },
        "__restart__": "must",
        "__info__": "多语言设置"
    },
    "name_audit": {
        "__sort__": 8,
        "__restart__": "not_must",
        "AUDIT_PROJECT_KEY": {
            "type": "dict",
            "value": {
                "class_name": "审核一些短的分类名称, 如category, tag",
                "username": "审核用户名"
            },
            "sort": 99,
            "info": "审核项目的Key(键),审核时会使用一个Key来获取审核规则,正则去匹配用户输入的内容"
        },
        "__info__": "名称验证, 如用户名,分类名称"
    },
    "post": {
        "MAX_LEN": {
            "type": "int",
            "value": 5000,
            "sort": 99,
            "info": "发布文章最多几个字符"
        },
        "__sort__": 2,
        "__restart__": "not_must",
        "TAG_MAX_NUM": {
            "type": "int",
            "value": 5,
            "sort": 99,
            "info": "POST标签最大个数"
        },
        "TITLE_MAX_LEN": {
            "type": "int",
            "value": 50,
            "sort": 99,
            "info": "文章Title最大长度"
        },
        "NUM_PAGE_MAX": {
            "type": "int",
            "value": 30,
            "sort": 99,
            "info": "每个页面最多获取几篇文章(此配置对管理端无效)"
        },
        "__info__": "文章内容设置",
        "NUM_PAGE": {
            "type": "int",
            "value": 15,
            "sort": 99,
            "info": "每个页面获取几篇文章, 如果请求获取文章时指定了指定了per参数, 则此配置无效(此配置也对管理端无效)"
        },
        "TAG_MAX_LEN": {
            "type": "int",
            "value": 10,
            "sort": 99,
            "info": "POST标签最多几个字"
        },
        "BRIEF_LEN": {
            "type": "int",
            "value": 80,
            "sort": 99,
            "info": "获取文章简要的字数"
        },
        "GET_POST_CACHE_TIME_OUT": {
            "type": "int",
            "value": 60,
            "sort": 99,
            "info": "获取多个post数据时, 缓存超时时间(s), 为0表示不缓存数据.<br><span style='color:red;'>只对获取已公开发布的, 并且不是当前用户发布的post有效</span>"
        }
    },
    "account": {
        "USER_AVATAR_MAX_SIZE": {
            "type": "float",
            "value": 10.0,
            "sort": 99,
            "info": "用户头像不能上传超过此值大小(单位Mb)的图片作头像"
        },
        "DEFAULT_AVATAR": {
            "type": "string",
            "value": "/static/sys_imgs/avatar_default.png",
            "sort": 99,
            "info": "新注册用户默认头像的URL"
        },
        "USERNAME_MAX_LEN": {
            "type": "int",
            "value": 20,
            "sort": 99,
            "info": "用户名最大长度"
        },
        "__info__": "账户设置",
        "__sort__": 6,
        "USER_AVATAR_SIZE": {
            "type": "list",
            "value": [
                "360",
                "360"
            ],
            "sort": 99,
            "info": "用户头像保存大小[<width>, <height>]像素"
        },
        "__restart__": "not_must"
    },
    "email": {
        "MAIL_FOOTER": {
            "type": "string",
            "value": "OSROOM开源网站系统",
            "sort": 99,
            "info": "发送邮件的页尾"
        },
        "MAIL_PASSWORD": {
            "type": "password",
            "value": "<Your password>",
            "sort": 99,
            "info": "邮箱密码, 是用于发送邮件的密码"
        },
        "MAIL_SERVER": {
            "type": "string",
            "value": "smtp.mxhichina.com",
            "sort": 99,
            "info": "邮箱服务器smtp"
        },
        "__sort__": 10,
        "APP_NAME": {
            "type": "string",
            "value": "",
            "sort": 99,
            "info": "在邮件中显示的APP(WEB)名称(1.不填写则不显示.2.如果主题邮件发送html模板不支持，也不显示)"
        },
        "MAIL_ASCII_ATTACHMENTS": {
            "type": "bool",
            "value": True,
            "sort": 99,
            "info": "MAIL ASCII ATTACHMENTS"
        },
        "MAIL_SUBJECT_SUFFIX": {
            "type": "string",
            "value": "OSROOM",
            "sort": 99,
            "info": "发送邮件的标题后缀"
        },
        "MAIL_USE_TLS": {
            "type": "bool",
            "value": False,
            "sort": 99,
            "info": "是否使用TLS"
        },
        "__restart__": "must",
        "MAIL_DEFAULT_SENDER": {
            "type": "list",
            "value": [
                "OSR DEMO",
                "system@osroom.com"
            ],
            "sort": 99,
            "info": "默认发送者邮箱　(显示名称, 邮箱地址)顺序不能调换"
        },
        "MAIL_PORT": {
            "type": "int",
            "value": 465,
            "sort": 99,
            "info": "邮箱服务器端口"
        },
        "__info__": "邮件发送参数设置（建议技术管理人员使用）",
        "APP_LOG_URL": {
            "type": "string",
            "value": "/static/sys_imgs/osroom-logo.png",
            "sort": 99,
            "info": "在邮件中显示的LOGO图片URL(1.不填写则不显示.2.如果主题邮件发送html模板不支持，也不显示)"
        },
        "MAIL_USE_SSL": {
            "type": "bool",
            "value": True,
            "sort": 99,
            "info": "是否使用SSL"
        },
        "MAIL_USERNAME": {
            "type": "string",
            "value": "system@osroom.com",
            "sort": 99,
            "info": "邮箱用户名"
        }
    },
    "cache": {
        "CACHE_KEY_PREFIX": {
            "type": "string",
            "value": "osr_cache",
            "sort": 99,
            "info": "所有键(key)之前添加的前缀,这使得它可以为不同的应用程序使用相同的memcached(内存)服务器."
        },
        "__restart__": "must",
        "__info__": "Web缓存参数设置（建议技术管理人员使用）",
        "__sort__": 99,
        "USE_CACHE": {
            "type": "bool",
            "value": True,
            "sort": 99,
            "info": "是否使用缓存功能,建议开启"
        },
        "CACHE_TYPE": {
            "type": "string",
            "value": "redis",
            "sort": 99,
            "info": "缓存使用的类型,可选择redis,mongodb"
        },
        "CACHE_MONGODB_COLLECT": {
            "type": "string",
            "value": "osr_cache",
            "sort": 99,
            "info": "保存cache的collection,当CACHE_TYPE为mongodb时有效"
        },
        "CACHE_DEFAULT_TIMEOUT": {
            "type": "int",
            "value": 600,
            "sort": 99,
            "info": "(s秒)默认缓存时间,当单个缓存没有设定缓存时间时会使用该时间"
        }
    }
}