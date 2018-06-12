from analysis_fb.collect.api import api

'''
url = api.fb_genurl(node='jtbcnews', a=10, b=20, s='kickscar')
print(url)
'''
'''
id = api.fb_name_to_id('jtbcnews')
print(id)
'''

# api.fb_fetch_posts('jtbcnews', '20170101', '20171231')

# results = api.fb_fetch_posts('jtbcnews', '2017-01-01', '2017-12-31')
# print(len(results))

for posts in api.fb_fetch_posts('jtbcnews', '2017-01-01', '2017-12-31'):
    print(posts)

# for posts in api.fb_fetch_posts('jtbcnews', '2018-06-11', '2018-06-12'):
#     print(posts)