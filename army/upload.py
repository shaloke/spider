import requests
import io
# import magic

# def get_file_type_by_content(file_path):  
#     mime = magic.Magic(mime=True)  
#     return mime.from_file(file_path)

boundary = '----WebKitFormBoundaryxBi3vAFtUwr5Uw5B'
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Authorization': '45e911ca35b6428e93ddb38146cfd638',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Length': '20493',
    # 'Content-Type': 'multipart/form-data; boundary='+boundary,
    'Host': 'www.gzcdgd.com',
    'Origin': 'https://vant-demo.gzcdgd.com',
    'Pragma': 'no-cache',
    'Referer': 'https://vant-demo.gzcdgd.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "Windows",
}

url = 'https://www.gzcdgd.com/trans/upload'
info='[{"count":"","deptment__dept_parent":"","deptment__full_name":"信息部","deptment__name":"信息部","deptment__oa_id":"78","oa_name":"黄俊康","user_id":"1523"}]'
filelist = ['./addList.json','./changeList.json','./deleteList.json']
for f in filelist:
    with open(f,'rb') as fr:
        data={
            'recv_users':(None,info,None),
            'files':(f,fr.read(),'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'),
            'compression':(None,1,None),
        }
        respone = requests.post(url=url,files=data,headers=headers)
        if respone.status_code == 200:
            print(respone.request.body)
            print('\n')
        else:
            print(respone.text)