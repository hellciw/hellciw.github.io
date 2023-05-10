AUTHOR = 'Alexander'
SITENAME = 'Alexander@blog'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Blogroll
LINKS = (('CSDN', 'https://blog.csdn.net/weixin_47389883?type=blog'),
         ('bilibili', 'https://space.bilibili.com/15219798?spm_id_from=333.1007.0.0'),
         ('LuoGu', 'https://www.luogu.com.cn/blog/LinMax/'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


THEME = 'pelican-alchemy/alchemy'
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['readtime', 'neighbors']