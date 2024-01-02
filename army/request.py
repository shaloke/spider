import requests
import json
import os
if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    }
    url = 'https://www.plap.mil.cn/gateway/gpc-gpcms/rest/v2/punish/public'
    data = {
        'publishType': 'breakFaith',
        'pageNumber': 1,
        'pageSize': 10,
        'creditName': '',
        'handleUnit': '',
        'startDate': '',
        'endDate': ''
    }
    # 获取更改项
    def get_change(old,new):
        if 'change' in old:
            old_change = old['change']
            del old['change']
        change_item = {k: old[k] for k in old if old[k] != new[k]}
        new['change'] = change_item
        if 'change' in old:
            old['change'] = old_change
        return new
    # 判断是否是同一家供应商
    def is_same_com(obj1,obj2):
        if obj1['creditName'] == obj2['creditName'] and obj1['creditCode'] == obj2['creditCode'] and obj1['id'] == obj2['id']:
            return True
        else:
            return False
        
    def compare(olist,nlist):
        change_item_list = []
        for o in olist:
            for n in nlist:
                if is_same_com(o,n):
                    if get_change(o,n)['change'] != {}:
                        change_item_list.append(get_change(o,n))
        return change_item_list
    
    def get_diff(_before,_later):
        add_list = [d for d in _later if not any(d['creditCode'] == old['creditCode'] and d['creditName'] == old['creditName'] and d['id'] == old['id']for old in _before)]
        return add_list
    
    def update_oldlist(path,newlist):
        with open(path,'w',encoding='utf-8') as fp:
            json.dump(newlist,fp=fp,ensure_ascii=False)
    """*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*爬虫-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*"""
    respone = requests.get(url=url, params=data, headers=headers)
    if respone.status_code == 200:
        new_data = []
        old_data = []
        # 第一次请求获取数据total
        respone.encoding = 'utf-8'
        total = respone.json()['data']['total']

        # 第二次请求,拿到新数据
        data['pageSize'] = total
        respone1 = requests.get(url=url, params=data, headers=headers)
        respone1.encoding = 'utf-8'
        new_data = respone1.json()['data']['rows']

        # 对比新旧数据，算出新增和减少项
        # 判断有无该文件，拿到旧数据
        if not os.path.isfile('./oldList.json'):
            print('没有旧文件')
            update_oldlist('./oldList.json',newlist=new_data)
        else:
            with open('./oldList.json', 'r', encoding='utf-8') as fr:
                old_data = json.loads(fr.read())
            with open('./changeList.json','w',encoding='utf-8') as fp:
                json.dump(compare(old_data,new_data),fp=fp,ensure_ascii=False)
            with open('./addList.json','w',encoding='utf-8') as fp:
                json.dump(get_diff(old_data,new_data),fp=fp,ensure_ascii=False)
            with open('./deleteList.json','w',encoding='utf-8') as fp:
                json.dump(get_diff(new_data,old_data),fp=fp,ensure_ascii=False)
            update_oldlist('./oldList.json',newlist=new_data)
            print('结束')
    else:
        print('请求出错')
