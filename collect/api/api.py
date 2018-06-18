# facebook API Wrapper Functions
from urllib.parse import urlencode
from .web_request import json_request

# ACCESS_TOKEN : 접근할떄 필요한 키값
ACCESS_TOKEN = "EAACEdEose0cBADkYZAGRzYIrNZClZCebGV9YgZBY5M9YokeRQkD6vuVPUT6BSSVv7lmliiMgs1fAPYzQ1FVM2RZAuZB5TUSY7O9lbU1NsHbLb0AcylombA5dYJfikU349u4onTfwzYHFqfIMSm3LZCtJD7J1kamwXWxYjOgyabnO3YwaNCahLaO2JGimI716NJzTgZBvxmK7ggZDZD"
BASE_URL_FB_API = "https://graph.facebook.com/v3.0"  # 고정된 값이고 주소 외우삼


def fb_gen_url(
        base=BASE_URL_FB_API,
        node='',  # 안넣을수도있으니까 기본값으로
        **params):  # 페이스북 url을 generatic을 한다.
    url = '%s/%s/?%s' % (base, node, urlencode(params)) # 노드 없고 바로 params
    return url


# return '%s/%s/posts/?%s' % (base,node, urlencode(params))
#     이 방법도 가능

def fb_name_to_id(pagename):
    url = fb_gen_url(node=pagename, access_token=ACCESS_TOKEN) # 노드 자리에 access_token 넣는다
    json_result = json_request(url=url)
    return json_result.get("id") #id 태그를 가져온다


def fb_fetch_posts(pagename, since, until): # fetch 가져오다 구현하다
    url = fb_gen_url(
        node=fb_name_to_id(pagename) + "/posts/",
        fields='id, message, link, name, type, shares, reactions, created_time, comments.limit(0).summary('
               'true).limit(0).summary(true)',
        since=since,
        until=until,
        limit=50,
        access_token=ACCESS_TOKEN)

    print(url)
    # json_result = json_request(url=url)
    # print(json_result)
    # 리스트로 N개를 받기위한 함수

    # results = []
    isnext = True  # true냐 false에 따라서 달라고하기
    while isnext is True:  # isnext가 true면 루프돌기
        json_result = json_request(url=url)
        # 페이징 정보 가져오기 왜? json result가 null일수 있어서
        paging = None
        if json_result is None:
            paging = None
        else:
            paging = json_result.get('paging')  # none이 아니면 paging을 가져오자
        # 위 코드는 단순 코드임
        # 삼항연산자 쓰면 더 간결함
        # isnext = True
        # while isnext is True:
        #     json_result = json_request(url=url)
        #     paging = None if json_result is None else json_result.get('paging')
        posts = None if json_result is None else json_result.get('data')

        # results += posts #posts의 새로운 50개 리스트를 추가 하는 과정 append는 업데이트됨 ㅎㅎ
        url = None if paging is None else paging.get("next")  # 마지막 posts의 경우 null로 나타남
        # roop돌때 url을 다시 쓰려고 url로 잡아줌
        isnext = url is not None

        # return results  #roop가 끝난다음에 결과를 출력하기 위해 바깥에 씀
        yield posts  # 얘는 for문 안에 넣어야 된다
