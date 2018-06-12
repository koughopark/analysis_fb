# test json

from urllib.request import Request, urlopen              #모듈 가져오기
# from datetime import *
import datetime
import sys
import json

try:
    url = 'http://kickscar.cafe24.com:8080/myapp-api/api/user/list'
    request = Request(url)                              #리퀘스트 객체 생성

    urlopen(request)
    resp = urlopen(request)                             #응답 받기
    resp_body = resp.read().decode("utf-8")             #응답 읽기 (바디 내용)  - 바이트로 통신    인코딩 했으면 디코딩도 해야함
    print('print(resp_body) : ')
    print('type : ', type(resp_body))
    print(resp_body)                                    #네이버 바디(코드)를 가져옴

    json_result = json.loads(resp_body)

    print('')
    print('print(json_result) : ')
    print('type : ', type(json_result))
    print(json_result)
    print('')
    data = json_result['data']
    print(type(data), " : ", data)

except Exception as e:
    print('%s %s' % (e, datetime.now()), file=sys.stderr)

'''
System.out.println("HelloWorld");

'''
#html 받앗음