# coding=utf-8
# Author: Codebat_Raymond
# Email: hofong.chang@gmail.com
# Website: https://codebat.netlify.app/
# Github: https://github.com/hofong428
# date: 3/6/20235:29 PM
import requests
import execjs

acw_sc__v2 = execjs.compile(open('./acw_sc_v2alixi.js', 'r', encoding='utf-8').read()).call('main123')
print(acw_sc__v2)

cookies = {
    'acw_tc': '2760779a16780932483026023ed20bfd7c2b4e3858e97df429c1f9a2de504f',
    'acw_sc__v2': acw_sc__v2
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'acw_tc=2760779a16780932483026023ed20bfd7c2b4e3858e97df429c1f9a2de504f; acw_sc__v2=6405ae5418f78d1539a9dbd942bbabbe25591db8',
    'Pragma': 'no-cache',
    'Referer': 'https://xueqiu.com/today',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://xueqiu.com/today', cookies=cookies, headers=headers).text
print(response)