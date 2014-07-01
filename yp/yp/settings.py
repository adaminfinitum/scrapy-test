# Scrapy settings for yp project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'yp'

SPIDER_MODULES = ['yp.spiders']
NEWSPIDER_MODULE = 'yp.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
DOWNLOAD_DELAY = 10
USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.97 Safari/537.22 AlexaToolbar/alxg-3.1"