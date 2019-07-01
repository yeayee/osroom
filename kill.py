import os

__author__ = 'Allen Woo'
try:
    shcmd = """ps -ef | grep uwsgi.ini | awk '{print $2}' | xargs kill -9"""
    r = os.system(shcmd)
    print("Kill uwsgi.")
except Exception as e:
    print(e)
