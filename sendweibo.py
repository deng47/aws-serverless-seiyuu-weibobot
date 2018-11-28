import time
import urllib.request
import re
import random

from weibo_login import *
from myTB import *

#登录微博
(session, uid) = wblogin()

Referer = "https://www.weibo.com/u/%s/home?wvr=5" % uid
session.headers["Referer"] = Referer
uploadurl = "https://picupload.weibo.com/interface/pic_upload.php?app=miniblog&s=json&mime=image/jpeg&data=1&wm="


def send(tag, dic, pausetime):

    table = MyTable("weibo")
    posts = table.get_data("source", tag)
    if posts:
        posts = posts[0]['post']
    pre_posts = posts.copy()

    for each in dic:
        if each in posts:
            continue
        message=tag+each
        piclinks = dic[each]
        pids=''

        if len(piclinks)>0:
            for piclink in piclinks:
                f = session.get( piclink, timeout=30 )
                img = f.content
                resp = session.post( uploadurl, data=img )
                upload_json = re.search( '{.*}}', resp.text ).group(0)
                result = json.loads( upload_json )
                code = result["code"]
                if code == "A00006":
                    pid=(result["data"]["pics"]["pic_1"]["pid"])
                    pids += " " + pid
                else:
                    continue
                time.sleep(pausetime)

            pids=pids.strip()

        #写入微博文字内容与上传图片pid
        data = {
                "location": "v6_content_home",
                "appkey": "",
                "style_type": "1",
                "pic_id": pids,
                "text": message,
                "pdetail": "",
                "rank": "0",
                "rankid": "",
                "module": "stissue",
                "pub_type": "dialog",
                "_t": "0",
                }

        #发出微博
        resp = session.post("https://www.weibo.com/aj/mblog/add?ajwvr=6&__rnd=%d" % int( time.time() * 1000),data=data)
        weibo_json = re.search( '{.*}}', resp.text ).group(0)
        result = json.loads( weibo_json )
        
        if result["code"]=='100000':
            print('Posted: ', message)
            if len(posts) == 0:
                posts = [each]
            elif len(posts) > 10:
                posts.append(each)
                posts = posts[1:]
            else:
                posts.append(each)
        
        elif random.randint(0,3) == 0:
            print('Failed: ', message)
            if len(posts) == 0:
                posts = [each]
            elif len(posts) > 10:
                posts.append(each)
                posts = posts[1:]
            else:
                posts.append(each)

    if pre_posts != posts:
        table.update_data('source', tag, 'post', posts)
        print("Table updated")

