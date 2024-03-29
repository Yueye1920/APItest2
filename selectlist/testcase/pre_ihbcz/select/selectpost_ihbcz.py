# coding=utf-8
import time
import allure
import pytest
import requests
import json
import sys
import os


sys.path.append("E:/pypro/APItest2/selectpost/common")
from common.header_token import *
from logs.loggerController import logs


logss = logs()
tokenids = YamlHander().read_yaml()
base_url ='http://www.ihbcz.gov.cn'


@allure.feature('左侧树')
class Testazcs:
    @allure.story("预算单位")
    @allure.title("预算单位：agency")
    def testagency(self):
        agency_url= base_url + '/pay-common-service/v3/apifront/lefttree'
        agency_headers = {"Content-Type": "application/json",
                                           "tokenid": tokenids}
        agency_data = {"elementCode": "AGENCY"}
        agency_data_str = json.dumps(agency_data)
        try:
            agency_start=time.time()   #开始时间
            agency_res = requests.get(agency_url,
                                                        headers=agency_headers,
                                                        params=agency_data)
            agency_res_json = agency_res.json()
            agency_end =time.time()   #结束时间
            agency_res_time= agency_end -agency_start
            agency_res_time_ms=  agency_res_time * 1000
            print("\n")
            print(f"响应时间：{agency_res_time_ms}毫秒")

            # print(agency_res.text)
            logss.logger.info("请求参数：{}，{}，{}".format(agency_url,agency_data,agency_headers))
            logss.logger.info("返回结果：{}".format(agency_res.text))

            ###断言
            response_rscode = agency_res_json.get('rscode')
            response_result = agency_res_json.get('result')

            ###使用pytest.assume进行断言，失败一个后，可用正常允许其它用例
            # pytest.assume(agency_res.status_code == 200)
            # pytest.assume(response_rscode == 200 )
            # pytest.assume(response_result == "请求成功")

            assert agency_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"
        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("左侧树断言失败：%s",e)
            raise e  # 主动抛出异常，不写则捕获异常



@allure.feature('用款计划模块')
class Testplan:

    @allure.story("用款计划录入（单位）")
    @allure.title("额度列表：planbgtbalance")
    def testplanYkjhlrdwPlanbgtbalance(self):
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
            ykjhlrdw_planbgtbalance_start=time.time()   #开始时间
            ykjhlrdw_planbgtbalance_res = requests.post(ykjhlrdw_planbgtbalance_url,
                                                        headers=ykjhlrdw_planbgtbalance_headers,
                                                        data=ykjhlrdw_planbgtbalance_data_str)
            ykjhlrdw_planbgtbalance_res_json = ykjhlrdw_planbgtbalance_res.json()
            ykjhlrdw_planbgtbalance_end =time.time()   #结束时间
            ykjhlrdw_planbgtbalance_res_time= ykjhlrdw_planbgtbalance_end -ykjhlrdw_planbgtbalance_start
            ykjhlrdw_planbgtbalance_res_time_ms=  ykjhlrdw_planbgtbalance_res_time * 1000
            print("\n")
            print(f"响应时间：{ykjhlrdw_planbgtbalance_res_time_ms}毫秒")

            # print(ykjhlrdw_planbgtbalance_res.text)
            logss.logger.info("请求参数：{}，{}，{}".format(ykjhlrdw_planbgtbalance_url,ykjhlrdw_planbgtbalance_data_str,ykjhlrdw_planbgtbalance_headers))
            logss.logger.info("返回结果：{}".format(ykjhlrdw_planbgtbalance_res.text))
            ###断言
            response_rscode = ykjhlrdw_planbgtbalance_res_json.get('rscode')
            response_result = ykjhlrdw_planbgtbalance_res_json.get('result')

            # pytest.assume(ykjhlrdw_planbgtbalance_res.status_code == 200)
            # pytest.assume(response_rscode == 200 )
            # pytest.assume(response_result == "请求成功")

            assert ykjhlrdw_planbgtbalance_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

            ##return ykjhlrdw_planbgtbalance_res_time
        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("用款计划录入（单位）-额度列表 断言失败：%s",e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("用款计划录入（单位）")
    @allure.title("TAB页签数量：datastatuscount")
    def testplanYkjhlrdwDatastatuscount(self):
        ykjhlrdw_datastatuscount_url = base_url + '/payfront/plan-service/v3/payplanvoucher/front/datastatuscount'
        ykjhlrdw_datastatuscount_headers = {"Content-Type": "application/json",
                                           "tokenid": tokenids}
        ykjhlrdw_datastatuscount_data = {
            "statusCodeArr": [
                "1",
                "2",
                "4",
                "5",
                "0"
            ],
            "menuId": "DDCFF09F6CCDD6BF236BBBE8D8F77C88",
            "isHaveZero": "0",
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "appId": "pay_plan_voucher",
            "roleId": "201EC9F7611B11B38E60BA5B10633BDB",
            "params": {
                "accountClsId": "CCBB352E4C7B6BBF4C4AC8F14CC89483",
                "accountType": "63",
                "isFinancial": "0",
                "updateInputAmt": "1"
            }

        }

        # 将dict转换为str
        ykjhlrdw_datastatuscount_data_str = json.dumps(ykjhlrdw_datastatuscount_data)
        try:
            ykjhlrdw_datastatuscount_start = time.time()  # 开始时间
            ykjhlrdw_datastatuscount_res = requests.post(ykjhlrdw_datastatuscount_url,
                                                        headers=ykjhlrdw_datastatuscount_headers,
                                                        data=ykjhlrdw_datastatuscount_data_str)
            ykjhlrdw_datastatuscount_res_json = ykjhlrdw_datastatuscount_res.json()
            ykjhlrdw_datastatuscount_end = time.time()  # 结束时间
            ykjhlrdw_datastatuscount_res_time = ykjhlrdw_datastatuscount_end - ykjhlrdw_datastatuscount_start
            ykjhlrdw_datastatuscount_res_time_ms = ykjhlrdw_datastatuscount_res_time * 1000
            print("\n")
            print(f"响应时间：{ykjhlrdw_datastatuscount_res_time_ms}毫秒")

            # print(ykjhlrdw_datastatuscount_res.text)
            logss.logger.info("请求参数：{}，{}，{}".format(ykjhlrdw_datastatuscount_url,ykjhlrdw_datastatuscount_data_str,ykjhlrdw_datastatuscount_headers))
            logss.logger.info("返回结果：{}".format(ykjhlrdw_datastatuscount_res.text))
            ###断言
            response_rscode = ykjhlrdw_datastatuscount_res_json.get('rscode')
            response_result = ykjhlrdw_datastatuscount_res_json.get('result')

            pytest.assume(ykjhlrdw_datastatuscount_res.status_code == 200)
            pytest.assume(response_rscode == 200 )
            pytest.assume(response_result == "请求成功")

            assert ykjhlrdw_datastatuscount_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("用款计划录入（单位）-TAB页签数量 断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常











if __name__ == '__main__':

    pytest.main()


# 切换路径
# cd E:\pypro\APItest2\selectlist\testcase\pre_111
# 执行测试用例
# pytest selectpost_new_111.py --alluredir ./allure-results/
# 生成报告
# allure generate allure-results -o allure-reports/ --clean
# 打开报告
# allure open allure-reports/