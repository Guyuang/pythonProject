import requests

#执行api调用并存储响应
url="https://api.github.com/search/repositories?q=language:python&sort=stars"
headers={'Accept':'application/vnd.github.v3+json'}
r=requests.get(url,headers=headers)
print(f"status code:{r.status_code}")

#将api响应赋给一个变量
response_dict=r.json()
print(f"Total repositories:{response_dict['total_count']}")

#探索有关仓库信息
repo_dicts=response_dict['items']
print(f"repositories returned:{len(repo_dicts)}")

#研究第一个仓库
repo_dicts =repo_dicts[0]
print(f"\nKeys:{len(repo_dicts)}")
for key in sorted(repo_dicts.keys()):
    print(key)

