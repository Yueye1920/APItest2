import requests
import json
import yaml


def get_token():
    # 请求行
    login_url = 'http://10.17.8.111/missLogin/sso/v1/userlogin'
    # 请求头
    login_headers = {"Content-Type": "application/x-www-form-urlencoded"}

    login_data = {
        "username": "VzQyMDAwMDAxMA==",
        "password": "ZjY0MmU4NmI3NTg5MDQzYjM0M2U1ZThiYTUxNGNhMDE=",
        "captcha": "MjAyNA=="
    }
    login_res = requests.post(login_url, headers=login_headers, data=login_data)
    print(login_res.text)

    login_res_json = login_res.json()
    # 提取token
    token = login_res_json['tokenid']
    return token


def write_yaml(token):
    t_data = {"token": token}
    with open("../common/token.yml", "w", encoding="utf-8") as f:
        yaml.dump(data=t_data, stream=f, allow_unicode=True)


if __name__ == '__main__':
    token = get_token()
    write_yaml(token)
