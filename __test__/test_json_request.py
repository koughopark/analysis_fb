from analysis_fb.collect.api import web_request as wr

url='http://kickscar.cafe24.com:8080/myapp-api/api/user/list'

def success_fetch_user_list(response):
    print(response)

def error_fetch_user(e):
    print(e)


wr.json_request(url=url, error=error_fetch_user)

'''
json_result = wr.json_request(url)
print(json_result)
'''

# https://graph.facebook.com/v3.0/jtbcnews/posts/?access_token=(토큰을 넣어라 가로도 지우고)&since=20170101&untill=20171231&limit=50