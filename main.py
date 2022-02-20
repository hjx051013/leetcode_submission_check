 # -*- coding: utf-8 -*-  
import json
import logging
from urllib import request
import requests

import schedule

PROTOCOL = "https" 
LEETCODE_CN_DOMAIN = "leetcode-cn.com"
LEETCODE_DOMAIN = "leetcode.com"
PATH = "/graphql/"

headers = {
  'Content-Type': 'application/json',
  'Cookie': 'aliyungf_tc=f3423b016aafee50df9ee34edacded9c41f243b1f55f2425c428b6e154b0c2e6; csrftoken=45oxOwuhTj3rd7il2CfrdnJzHLTDRxz1YUMgB8WR3asLJcD5M4cvScoQbaD5aEHl'
}

submission_query_template = '''
{ 
    recentSubmissionList(username: "%s", limit: %d) {
        title
        titleSlug
        timestamp
        statusDisplay
        lang
        __typename
    }
}
'''


logging.captureWarnings(True)

class Conf(object):
    def __init__(self, file_path) -> None:
        file = open(file_path)
        try:
            data = json.load(file) 
        finally:
            file.close()
        self.conf = data
        
    def get_user_infos(self):
        return self.conf.get("users", [])

    def get_notify_emails(self):
        return self.conf.get("notify_emails", [])
    
class ContestCheck(object):
    def  __init__(self, user_infos, observers) -> None:
        self.user_infos = user_infos
        self.observers = observers
        self.leetcodeid_to_nickname = {}
        for user_info in self.user_infos:
            self.leetcodeid_to_nickname[user_info.leetcode_id] = user_info.wechat_nickname
    
    def run(self):
        pass   
                
                
        
        

class DailyCheck(object):
    def  __init__(self, user_infos, observers) -> None:
        self.user_infos = user_infos
        self.observers = observers
        self.leetcodeid_to_nickname = {}
        for user_info in self.user_infos:
            self.leetcodeid_to_nickname[user_info.leetcode_id] = user_info.wechat_nickname
            
    def run(self):
        for user_info in self.user_infos:
            leetcode_id = user_info.leetcode_id
            nick_name = ""
            if leetcode_id[-1] == "/":
                nick_name = leetcode_id[leetcode_id[:-1].rindex("/")+1:-1]
            else:
                nick_name = leetcode_id[leetcode_id.rindex("-1")+1:]
            if "leetcode-cn.com" in leetcode_id:
                url = PROTOCOL + "://" + LEETCODE_CN_DOMAIN + PATH
            else:
                url = PROTOCOL + "://" + LEETCODE_DOMAIN + PATH
            payload = submission_query_template % (nick_name, 1)
            response = requests.request("POST", url, headers=headers, data=payload, verify=False)
            if response.status_code != 200:
                logging.error("error reason: %s", response.text)
            else:
                res = response.json()
                
        
        

def read_conf():
    pass

def check_daily():
    pass
     
def check_week_contest():
    pass
 
def main():
    # read config
    conf = read_conf()
    
    # daily check leetcode
    check_daily(conf)
    
    # check leetcode week contest
    check_week_contest(conf)
    
     
if __name__ == "__main__":
     main()