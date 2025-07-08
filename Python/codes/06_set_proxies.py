import requests
import username_password

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}

with open('proxy_list.txt', 'r') as p:
    proxy_string = p.read()
    proxy_list = proxy_string.split('\n')

for proxy in proxy_list:
    my_proxy = proxy
    username = username_password.username
    password = username_password.password

    proxy_url = f"http://{username}:{password}@{proxy}"

    proxies = {
        "http": proxy_url,
        "https": proxy_url
    }

    url = "" # set url 
    try:
        response = requests.get(url, proxies=proxies, headers=headers)
        if response.status_code == 200:
            print(f"Request is successful. Proxy: {proxy}")
        else:
            print(f"Request failed. Proxy: {proxy} Status Code: {response.status_code}")
    except Exception as e:
        print(f"Request failed. Proxy: {proxy}. Error: {e}")