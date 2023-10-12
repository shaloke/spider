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
    # 第一次请求获取数据total
    respone = requests.get(url=url, params=data, headers=headers)
    respone.encoding = 'utf-8'
    total = respone.json()['data']['total']

    # 判断有无该文件，拿到旧数据
    old_data = []
    old_data_id_list = []
    if os.path.isfile('./army/blacklist.json'):
        with open('./army/blacklist.json', 'r', encoding='utf-8') as fr:
            old_data = json.loads(fr.read())
            for i in old_data:
                old_data_id_list.append(i['id'])
    # print(old_data_id_list)

    # 第二次请求,拿到新数据
    new_data_id_list = []
    data['pageSize'] = total
    respone1 = requests.get(url=url, params=data, headers=headers)
    respone1.encoding = 'utf-8'
    new_data = respone1.json()['data']['rows']
    for i in new_data:
        new_data_id_list.append(i['id'])
    # print(new_data_id_list)

    # 对比新旧数据，算出新增和减少项
    add_data = [x for x in new_data if x not in old_data]
    red_data = [x for x in old_data if x not in new_data]
    print(add_data)
    # 新数据写入文件，成为旧数据
    with open('./army/blacklist.json', 'w', encoding='utf-8') as fp:
        # 去重后再写入
        tuple_set = set(tuple(d.items()) for d in new_data)
        result = [dict(t) for t in tuple_set]
        json.dump(result, fp=fp, ensure_ascii=False)
