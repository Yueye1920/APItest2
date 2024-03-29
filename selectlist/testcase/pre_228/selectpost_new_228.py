import os
import sys
import time
import allure
import pytest
import requests
import json
sys.path.append("E:/pypro/APItest/selectpost/common")
from common.header_token import *

tokenids = YamlHander('../../common/token.yml').read_yaml()
base_url = 'http://10.17.8.228'


@allure.feature('用款计划菜单')
class Testplan:

    @allure.story("用款计划录入（单位）-planbgtbalance")
    def testplanYkjhlrdw(self):
        ykjhlrdw_planbgtbalance_url = base_url + '/payfront/pay-common-service/v3/loadtabledata/planbgtbalance'
        ykjhlrdw_planbgtbalance_headers = {"Content-Type": "application/json",
                                           "tokenid": tokenids}
        ykjhlrdw_planbgtbalance_data = {
            "condition": {},
            "statusCode": "9",
            "menuId": "DDCFF09F6CCDD6BF236BBBE8D8F77C88",
            "appId": "pay_plan_voucher",
            "isHaveZero": "0",
            "params": {
                "accountClsId": "CCBB352E4C7B6BBF4C4AC8F14CC89483",
                "accountType": "63",
                "isFinancial": "0",
                "updateInputAmt": "1"
            },
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "roleId": "201EC9F7611B11B38E60BA5B10633BDB",
            "pageNum": 1,
            "pageSize": 20,
            "sort": "create_time desc"

        }
        # print(type(ykjhlrdw_planbgtbalance_data))
        # 将dict转换为str
        ykjhlrdw_planbgtbalance_data_str = json.dumps(ykjhlrdw_planbgtbalance_data)
        # print(type(ykjhlrdw_planbgtbalance_data_str))
        try:
            ykjhlrdw_planbgtbalance_start = time.time()  # 开始时间
            ykjhlrdw_planbgtbalance_res = requests.post(ykjhlrdw_planbgtbalance_url,
                                                        headers=ykjhlrdw_planbgtbalance_headers,
                                                        data=ykjhlrdw_planbgtbalance_data_str)
            ykjhlrdw_planbgtbalance_res_json = ykjhlrdw_planbgtbalance_res.json()
            ykjhlrdw_planbgtbalance_end = time.time()  # 结束时间
            ykjhlrdw_planbgtbalance_res_time = ykjhlrdw_planbgtbalance_end - ykjhlrdw_planbgtbalance_start
            ykjhlrdw_planbgtbalance_res_time_ms = ykjhlrdw_planbgtbalance_res_time * 1000
            print("\n")
            print(f"响应时间：{ykjhlrdw_planbgtbalance_res_time_ms}毫秒")

            print(ykjhlrdw_planbgtbalance_res.text)

            ###断言
            response_rscode = ykjhlrdw_planbgtbalance_res_json.get('rscode')
            response_result = ykjhlrdw_planbgtbalance_res_json.get('result')

            assert ykjhlrdw_planbgtbalance_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

            ##return ykjhlrdw_planbgtbalance_res_time
        except AssertionError as e:
            print(f"请求失败：{e}")
            raise e  # 主动抛出异常，不写则捕获异常


if __name__ == '__main__':
    pytest.main()

# 执行测试用例
# pytest selectpost.py --alluredir allure-results/
# 生成报告
# allure generate allure-results -o allure-reports/ --clean
# 打开报告
# allure open allure-reports/
