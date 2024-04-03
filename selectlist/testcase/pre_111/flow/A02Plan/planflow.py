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
base_url ='http://10.17.8.111'


@allure.feature('(case01)用款计划(单位)')
class Testplandw:
    @allure.story("(step01)用款计划录入(单位)")
    @allure.title("用款计划录入(单位)：保存")
    def testYkjhlrdwInsert(self):
        ykjhlrdw_insert_url= base_url + '/payfront/plan-service/v3/payplanvoucher/front/action/insert'
        ykjhlrdw_insert_headers = {"Content-Type": "application/json",
                                           "tokenid": tokenids}
        ykjhlrdw_insert_data = {
            "actionName": "新增",
            "appId": "pay_plan_voucher",
            "menuId": "DDCFF09F6CCDD6BF236BBBE8D8F77C88",
            "actionType": "1",
            "glType": 1,
            "isBudget": 'true',
            "list": [
                {
                    "id": "d90f49adb78db8343547023025efcf4d",
                    "use_des": "测试计划",
                    "month": "4",
                    "plan_app_amt": "100",
                    "fileList": []
                }
            ]

        }
        ykjhlrdw_insert_data_str = json.dumps(ykjhlrdw_insert_data)
        try:
            ykjhlrdw_insert_start=time.time()   #开始时间
            ykjhlrdw_insert_res = requests.post(ykjhlrdw_insert_url,
                                                        headers=ykjhlrdw_insert_headers,
                                                        data=ykjhlrdw_insert_data_str)
            ykjhlrdw_insert_res_json = ykjhlrdw_insert_res.json()
            ykjhlrdw_insert_end =time.time()   #结束时间
            ykjhlrdw_insert_res_time= ykjhlrdw_insert_end -ykjhlrdw_insert_start
            ykjhlrdw_insert_res_time_ms=  ykjhlrdw_insert_res_time * 1000
            print("\n")
            print(f"响应时间：{ykjhlrdw_insert_res_time_ms}毫秒")

            # print(ykjhlrdw_insert_res.text)
            logss.logger.info("请求参数：{}，{}，{}".format(ykjhlrdw_insert_url,ykjhlrdw_insert_data_str,ykjhlrdw_insert_headers))
            logss.logger.info("返回结果：{}".format(ykjhlrdw_insert_res.text))

            ###断言
            response_rscode = ykjhlrdw_insert_res_json.get('rscode')
            response_result = ykjhlrdw_insert_res_json.get('result')

            ###使用pytest.assume进行断言，失败一个后，可用正常允许其它用例
            # pytest.assume(agency_res.status_code == 200)
            # pytest.assume(response_rscode == 200 )
            # pytest.assume(response_result == "请求成功")

            assert ykjhlrdw_insert_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"
        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s",e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step01)用款计划录入(单位)")
    @allure.title("用款计划录入(单位)：未送审列表")
    def testYkjhlrdwLoadTableDatas(self):
        ykjhlrdw_loadTableDatas_url = base_url + '/payfront/plan-service/v3/payplanvoucher/front/loadtabledatas'
        ykjhlrdw_loadTableDatas_headers = {"Content-Type": "application/json",
                                            "tokenid": tokenids}
        ykjhlrdw_loadTableDatas_data = {
            "condition": {},
            "statusCode": "1",
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

        # 将dict转换为str
        ykjhlrdw_loadTableDatas_data_str = json.dumps(ykjhlrdw_loadTableDatas_data)
        try:
            ykjhlrdw_loadTableDatas_start = time.time()  # 开始时间
            ykjhlrdw_loadTableDatas_res = requests.post(ykjhlrdw_loadTableDatas_url,
                                                         headers=ykjhlrdw_loadTableDatas_headers,
                                                         data=ykjhlrdw_loadTableDatas_data_str)
            ykjhlrdw_loadTableDatas_res_json = ykjhlrdw_loadTableDatas_res.json()
            ykjhlrdw_loadTableDatas_end = time.time()  # 结束时间
            ykjhlrdw_loadTableDatas_res_time = ykjhlrdw_loadTableDatas_end - ykjhlrdw_loadTableDatas_start
            ykjhlrdw_loadTableDatas_res_time_ms = ykjhlrdw_loadTableDatas_res_time * 1000
            print("\n")
            print(f"响应时间：{ykjhlrdw_loadTableDatas_res_time_ms}毫秒")
            # print(ykjhlrdw_loadTableDatas_res.text)

            global ykjhlrdw_plan_id
            ykjhlrdw_plan_id = ykjhlrdw_loadTableDatas_res_json.get("data").get("rows")[0]["id"]
            print("计划id：",ykjhlrdw_plan_id)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(ykjhlrdw_loadTableDatas_url, ykjhlrdw_loadTableDatas_data_str,
                                       ykjhlrdw_loadTableDatas_headers))
            logss.logger.info("返回结果：{}".format(ykjhlrdw_loadTableDatas_res.text))
            ###断言
            response_rscode = ykjhlrdw_loadTableDatas_res_json.get('rscode')
            response_result = ykjhlrdw_loadTableDatas_res_json.get('result')

            # pytest.assume(ykjhlrdw_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert ykjhlrdw_loadTableDatas_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step01)用款计划录入(单位)")
    @allure.title("用款计划录入(单位)：送审")
    def testYkjhlrdwAudit(self):
        ykjhlrdw_audit_url = base_url + '/payfront/plan-service/v3/payplanvoucher/action/audit'
        ykjhlrdw_audit_headers = {"Content-Type": "application/json",
                                       "tokenid": tokenids}
        ykjhlrdw_audit_data = {
            "actionName": "送审",
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "appId": "pay_plan_voucher",
            "menuId": "DDCFF09F6CCDD6BF236BBBE8D8F77C88",
            "actionType": "2",
            "glType": 0,
            "ids": [
                ykjhlrdw_plan_id
            ]
        }

        # 将dict转换为str
        ykjhlrdw_audit_data_str = json.dumps(ykjhlrdw_audit_data)
        try:
            ykjhlrdw_audit_start = time.time()  # 开始时间
            ykjhlrdw_audit_res = requests.post(ykjhlrdw_audit_url,
                                                    headers=ykjhlrdw_audit_headers,
                                                    data=ykjhlrdw_audit_data_str)
            ykjhlrdw_audit_res_json = ykjhlrdw_audit_res.json()
            ykjhlrdw_audit_end = time.time()  # 结束时间
            ykjhlrdw_audit_res_time = ykjhlrdw_audit_end - ykjhlrdw_audit_start
            ykjhlrdw_audit_res_time_ms = ykjhlrdw_audit_res_time * 1000
            print("\n")
            print(f"响应时间：{ykjhlrdw_audit_res_time_ms}毫秒")
            # print(ykjhlrdw_audit_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(ykjhlrdw_audit_url, ykjhlrdw_audit_data_str,
                                       ykjhlrdw_audit_headers))
            logss.logger.info("返回结果：{}".format(ykjhlrdw_audit_res.text))
            ###断言
            response_rscode = ykjhlrdw_audit_res_json.get('rscode')
            response_result = ykjhlrdw_audit_res_json.get('result')

            # pytest.assume(ykjhlrdw_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert ykjhlrdw_audit_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step02)用款计划审核(单位)")
    @allure.title("用款计划审核(单位)：审核")
    def testYkjhshdwAudit(self):
        ykjhshdw_audit_url = base_url + '/payfront/plan-service/v3/payplanvoucher/action/audit'
        ykjhshdw_audit_headers = {"Content-Type": "application/json",
                                       "tokenid": tokenids}
        ykjhshdw_audit_data = {
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "actionName": "审核",
            "appId": "pay_plan_voucher",
            "menuId": "47CFF09F6CCDD6BF236BBBE8D8F25C14",
            "actionType": "2",
            "glType": 0,
            "ids": [
                ykjhlrdw_plan_id
            ]
        }

        # 将dict转换为str
        ykjhshdw_audit_data_str = json.dumps(ykjhshdw_audit_data)
        try:
            ykjhshdw_audit_start = time.time()  # 开始时间
            ykjhshdw_audit_res = requests.post(ykjhshdw_audit_url,
                                                    headers=ykjhshdw_audit_headers,
                                                    data=ykjhshdw_audit_data_str)
            ykjhshdw_audit_res_json = ykjhshdw_audit_res.json()
            ykjhshdw_audit_end = time.time()  # 结束时间
            ykjhshdw_audit_res_time = ykjhshdw_audit_end - ykjhshdw_audit_start
            ykjhshdw_audit_res_time_ms = ykjhshdw_audit_res_time * 1000
            print("\n")
            print(f"响应时间：{ykjhshdw_audit_res_time_ms}毫秒")
            # print(ykjhshdw_audit_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(ykjhshdw_audit_url, ykjhshdw_audit_data_str,
                                       ykjhshdw_audit_headers))
            logss.logger.info("返回结果：{}".format(ykjhshdw_audit_res.text))
            ###断言
            response_rscode = ykjhshdw_audit_res_json.get('rscode')
            response_result = ykjhshdw_audit_res_json.get('result')

            # pytest.assume(ykjhlrdw_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert ykjhshdw_audit_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step03)用款计划审核(部门)")
    @allure.title("用款计划审核(部门)：审核")
    def testYkjhshbmAudit(self):
        ykjhshbm_audit_url = base_url + '/payfront/plan-service/v3/payplanvoucher/action/audit'
        ykjhshbm_audit_headers = {"Content-Type": "application/json",
                                          "tokenid": tokenids}
        ykjhshbm_audit_data = {
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "actionName": "审核",
            "appId": "pay_plan_voucher",
            "menuId": "182B5660A9F3CE6F4CB4728E5F6A2A32",
            "actionType": "2",
            "glType": 0,
            "ids": [
                ykjhlrdw_plan_id
            ]
        }

        # 将dict转换为str
        ykjhshbm_audit_data_str = json.dumps(ykjhshbm_audit_data)
        try:
            ykjhshbm_audit_start = time.time()  # 开始时间
            ykjhshbm_audit_res = requests.post(ykjhshbm_audit_url,
                                                       headers=ykjhshbm_audit_headers,
                                                       data=ykjhshbm_audit_data_str)
            ykjhshbm_audit_res_json = ykjhshbm_audit_res.json()
            ykjhshbm_audit_end = time.time()  # 结束时间
            ykjhshbm_audit_res_time = ykjhshbm_audit_end - ykjhshbm_audit_start
            ykjhshbm_audit_res_time_ms = ykjhshbm_audit_res_time * 1000
            print("\n")
            print(f"响应时间：{ykjhshbm_audit_res_time_ms}毫秒")
            # print(ykjhshbm_audit_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(ykjhshbm_audit_url, ykjhshbm_audit_data_str,
                                       ykjhshbm_audit_headers))
            logss.logger.info("返回结果：{}".format(ykjhshbm_audit_res.text))
            ###断言
            response_rscode = ykjhshbm_audit_res_json.get('rscode')
            response_result = ykjhshbm_audit_res_json.get('result')

            # pytest.assume(ykjhlrdw_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert ykjhshbm_audit_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step04)用款计划审核(复审)")
    @allure.title("用款计划审核(复审)：审核")
    def testYkjhshfsAudit(self):
        ykjhshfs_audit_url = base_url + '/payfront/plan-service/v3/payplanvoucher/action/audit'
        ykjhshfs_audit_headers = {"Content-Type": "application/json",
                                          "tokenid": tokenids}
        ykjhshfs_audit_data = {
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "actionName": "审核",
            "appId": "pay_plan_voucher",
            "menuId": "47CFF09F6ADCB6BF236CDAE8D8F33C73",
            "actionType": "2",
            "glType": 0,
            "ids": [
                ykjhlrdw_plan_id
            ]
        }

        # 将dict转换为str
        ykjhshfs_audit_data_str = json.dumps(ykjhshfs_audit_data)
        try:
            ykjhshfs_audit_start = time.time()  # 开始时间
            ykjhshfs_audit_res = requests.post(ykjhshfs_audit_url,
                                                       headers=ykjhshfs_audit_headers,
                                                       data=ykjhshfs_audit_data_str)
            ykjhshfs_audit_res_json = ykjhshfs_audit_res.json()
            ykjhshfs_audit_end = time.time()  # 结束时间
            ykjhshfs_audit_res_time = ykjhshfs_audit_end - ykjhshfs_audit_start
            ykjhshfs_audit_res_time_ms = ykjhshfs_audit_res_time * 1000
            print("\n")
            print(f"响应时间：{ykjhshfs_audit_res_time_ms}毫秒")
            # print(ykjhshfs_audit_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(ykjhshfs_audit_url, ykjhshfs_audit_data_str,
                                       ykjhshfs_audit_headers))
            logss.logger.info("返回结果：{}".format(ykjhshfs_audit_res.text))
            ###断言
            response_rscode = ykjhshfs_audit_res_json.get('rscode')
            response_result = ykjhshfs_audit_res_json.get('result')

            # pytest.assume(ykjhlrdw_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert ykjhshfs_audit_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step05)用款计划批复")
    @allure.title("用款计划批复：批复")
    def testYkjhpfReplyplan(self):
        ykjhpf_replyplan_url = base_url + '/payfront/plan-service/v3/payplanvoucher/front/action/replyplan'
        ykjhpf_replyplan_headers = {"Content-Type": "application/json",
                                          "tokenid": tokenids}
        ykjhpf_replyplan_data = {
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "actionName": "批复",
            "appId": "pay_plan_voucher",
            "menuId": "6CF559B30C55449DB03F5067F88AE2E7",
            "actionType": "2",
            "glType": 3,
            "advice": "ces",
            "ids": [
                ykjhlrdw_plan_id
            ]
        }

        # 将dict转换为str
        ykjhpf_replyplan_data_str = json.dumps(ykjhpf_replyplan_data)
        try:
            ykjhpf_replyplan_start = time.time()  # 开始时间
            ykjhpf_replyplan_res = requests.post(ykjhpf_replyplan_url,
                                                       headers=ykjhpf_replyplan_headers,
                                                       data=ykjhpf_replyplan_data_str)
            ykjhpf_replyplan_res_json = ykjhpf_replyplan_res.json()
            ykjhpf_replyplan_end = time.time()  # 结束时间
            ykjhpf_replyplan_res_time = ykjhpf_replyplan_end - ykjhpf_replyplan_start
            ykjhpf_replyplan_res_time_ms = ykjhpf_replyplan_res_time * 1000
            print("\n")
            print(f"响应时间：{ykjhpf_replyplan_res_time_ms}毫秒")
            # print(ykjhpf_replyplan_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(ykjhpf_replyplan_url, ykjhpf_replyplan_data_str,
                                       ykjhpf_replyplan_headers))
            logss.logger.info("返回结果：{}".format(ykjhpf_replyplan_res.text))
            ###断言
            response_rscode = ykjhpf_replyplan_res_json.get('rscode')
            response_result = ykjhpf_replyplan_res_json.get('result')

            # pytest.assume(ykjhlrdw_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert ykjhpf_replyplan_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常


@allure.feature('(case02)用款计划(财政)')
class Testplandb:
    @allure.story("(step01)用款计划录入(代编)")
    @allure.title("用款计划录入(代编)：保存")
    def testYkjhlrdbInsert(self):
        ykjhlrdb_insert_url= base_url + '/payfront/plan-service/v3/payplanvoucher/front/action/insert'
        ykjhlrdb_insert_headers = {"Content-Type": "application/json",
                                           "tokenid": tokenids}
        ykjhlrdb_insert_data = {
            "actionName": "新增",
            "appId": "pay_plan_voucher",
            "menuId": "6BC83CEA77C447F7ADB65F964CF314EF",
            "actionType": "1",
            "glType": 1,
            "isBudget": 'true',
            "list": [
                {
                    "id": "d90f49adb78db8343547023025efcf4d",
                    "use_des": "代编计划",
                    "month": "4",
                    "plan_app_amt": "150",
                    "fileList": [],
                    "attachment_id": ""
                }
            ]

        }
        ykjhlrdb_insert_data_str = json.dumps(ykjhlrdb_insert_data)
        try:
            ykjhlrdb_insert_start=time.time()   #开始时间
            ykjhlrdb_insert_res = requests.post(ykjhlrdb_insert_url,
                                                        headers=ykjhlrdb_insert_headers,
                                                        data=ykjhlrdb_insert_data_str)
            ykjhlrdb_insert_res_json = ykjhlrdb_insert_res.json()
            ykjhlrdb_insert_end =time.time()   #结束时间
            ykjhlrdb_insert_res_time= ykjhlrdb_insert_end -ykjhlrdb_insert_start
            ykjhlrdb_insert_res_time_ms=  ykjhlrdb_insert_res_time * 1000
            print("\n")
            print(f"响应时间：{ykjhlrdb_insert_res_time_ms}毫秒")

            # print(ykjhlrdb_insert_res.text)
            logss.logger.info("请求参数：{}，{}，{}".format(ykjhlrdb_insert_url,ykjhlrdb_insert_data_str,ykjhlrdb_insert_headers))
            logss.logger.info("返回结果：{}".format(ykjhlrdb_insert_res.text))

            ###断言
            response_rscode = ykjhlrdb_insert_res_json.get('rscode')
            response_result = ykjhlrdb_insert_res_json.get('result')

            ###使用pytest.assume进行断言，失败一个后，可用正常允许其它用例
            # pytest.assume(agency_res.status_code == 200)
            # pytest.assume(response_rscode == 200 )
            # pytest.assume(response_result == "请求成功")

            assert ykjhlrdb_insert_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"
        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s",e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step01)用款计划录入(代编)")
    @allure.title("用款计划录入(代编)：未送审列表")
    def testYkjhlrdbLoadTableDatas(self):
        ykjhlrdb_loadTableDatas_url = base_url + '/payfront/plan-service/v3/payplanvoucher/front/loadtabledatas'
        ykjhlrdb_loadTableDatas_headers = {"Content-Type": "application/json",
                                            "tokenid": tokenids}
        ykjhlrdb_loadTableDatas_data = {
            "condition": {},
            "statusCode": "1",
            "menuId": "6BC83CEA77C447F7ADB65F964CF314EF",
            "leftTreeCode": "",
            "isHaveZero": "0",
            "classname": "com.boss.payplan.ui.page.PayPlanVoucherPage",
            "appId": "pay_plan_voucher",
            "roleId": "201EC9F7611B11B38E60BA5B10633BDB",
            "params": {
                "accountClsId": "CCBB352E4C7B6BBF4C4AC8F14CC89483",
                "accountType": "63",
                "isFinancial": "0",
                "updateInputAmt": "1"
            },
            "pageNum": 1,
            "pageSize": 20,
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "sort": "create_time desc"
        }

        # 将dict转换为str
        ykjhlrdb_loadTableDatas_data_str = json.dumps(ykjhlrdb_loadTableDatas_data)
        try:
            ykjhlrdb_loadTableDatas_start = time.time()  # 开始时间
            ykjhlrdb_loadTableDatas_res = requests.post(ykjhlrdb_loadTableDatas_url,
                                                         headers=ykjhlrdb_loadTableDatas_headers,
                                                         data=ykjhlrdb_loadTableDatas_data_str)
            ykjhlrdb_loadTableDatas_res_json = ykjhlrdb_loadTableDatas_res.json()
            ykjhlrdb_loadTableDatas_end = time.time()  # 结束时间
            ykjhlrdb_loadTableDatas_res_time = ykjhlrdb_loadTableDatas_end - ykjhlrdb_loadTableDatas_start
            ykjhlrdb_loadTableDatas_res_time_ms = ykjhlrdb_loadTableDatas_res_time * 1000
            print("\n")
            print(f"响应时间：{ykjhlrdb_loadTableDatas_res_time_ms}毫秒")
            # print(ykjhlrdb_loadTableDatas_res.text)

            global ykjhlrdb_plan_id
            ykjhlrdb_plan_id = ykjhlrdb_loadTableDatas_res_json.get("data").get("rows")[0]["id"]
            print("计划id：",ykjhlrdb_plan_id)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(ykjhlrdb_loadTableDatas_url, ykjhlrdb_loadTableDatas_data_str,
                                       ykjhlrdb_loadTableDatas_headers))
            logss.logger.info("返回结果：{}".format(ykjhlrdb_loadTableDatas_res.text))
            ###断言
            response_rscode = ykjhlrdb_loadTableDatas_res_json.get('rscode')
            response_result = ykjhlrdb_loadTableDatas_res_json.get('result')

            # pytest.assume(ykjhlrdb_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert ykjhlrdb_loadTableDatas_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step01)用款计划录入(代编)")
    @allure.title("用款计划录入(代编)：送审")
    def testYkjhlrdbAudit(self):
        ykjhlrdb_audit_url = base_url + '/payfront/plan-service/v3/payplanvoucher/action/audit'
        ykjhlrdb_audit_headers = {"Content-Type": "application/json",
                                       "tokenid": tokenids}
        ykjhlrdb_audit_data = {
            "actionName": "送审",
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "appId": "pay_plan_voucher",
            "menuId": "6BC83CEA77C447F7ADB65F964CF314EF",
            "actionType": "2",
            "glType": 0,
            "ids": [
                ykjhlrdb_plan_id
            ]
        }

        # 将dict转换为str
        ykjhlrdb_audit_data_str = json.dumps(ykjhlrdb_audit_data)
        try:
            ykjhlrdb_audit_start = time.time()  # 开始时间
            ykjhlrdb_audit_res = requests.post(ykjhlrdb_audit_url,
                                                    headers=ykjhlrdb_audit_headers,
                                                    data=ykjhlrdb_audit_data_str)
            ykjhlrdb_audit_res_json = ykjhlrdb_audit_res.json()
            ykjhlrdb_audit_end = time.time()  # 结束时间
            ykjhlrdb_audit_res_time = ykjhlrdb_audit_end - ykjhlrdb_audit_start
            ykjhlrdb_audit_res_time_ms = ykjhlrdb_audit_res_time * 1000
            print("\n")
            print(f"响应时间：{ykjhlrdb_audit_res_time_ms}毫秒")
            # print(ykjhlrdb_audit_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(ykjhlrdb_audit_url, ykjhlrdb_audit_data_str,
                                       ykjhlrdb_audit_headers))
            logss.logger.info("返回结果：{}".format(ykjhlrdb_audit_res.text))
            ###断言
            response_rscode = ykjhlrdb_audit_res_json.get('rscode')
            response_result = ykjhlrdb_audit_res_json.get('result')

            # pytest.assume(ykjhlrdb_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert ykjhlrdb_audit_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step02)用款计划审核(代编)")
    @allure.title("用款计划审核(代编)：审核")
    def testykjhshdbAudit(self):
        ykjhshdb_audit_url = base_url + '/payfront/plan-service/v3/payplanvoucher/action/audit'
        ykjhshdb_audit_headers = {"Content-Type": "application/json",
                                       "tokenid": tokenids}
        ykjhshdb_audit_data = {
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "actionName": "审核",
            "appId": "pay_plan_voucher",
            "menuId": "F5D5BF1E7C84450BBEAC45463605263A",
            "actionType": "2",
            "glType": 0,
            "ids": [
                ykjhlrdb_plan_id
            ]
        }

        # 将dict转换为str
        ykjhshdb_audit_data_str = json.dumps(ykjhshdb_audit_data)
        try:
            ykjhshdb_audit_start = time.time()  # 开始时间
            ykjhshdb_audit_res = requests.post(ykjhshdb_audit_url,
                                                    headers=ykjhshdb_audit_headers,
                                                    data=ykjhshdb_audit_data_str)
            ykjhshdb_audit_res_json = ykjhshdb_audit_res.json()
            ykjhshdb_audit_end = time.time()  # 结束时间
            ykjhshdb_audit_res_time = ykjhshdb_audit_end - ykjhshdb_audit_start
            ykjhshdb_audit_res_time_ms = ykjhshdb_audit_res_time * 1000
            print("\n")
            print(f"响应时间：{ykjhshdb_audit_res_time_ms}毫秒")
            # print(ykjhshdb_audit_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(ykjhshdb_audit_url, ykjhshdb_audit_data_str,
                                       ykjhshdb_audit_headers))
            logss.logger.info("返回结果：{}".format(ykjhshdb_audit_res.text))
            ###断言
            response_rscode = ykjhshdb_audit_res_json.get('rscode')
            response_result = ykjhshdb_audit_res_json.get('result')

            # pytest.assume(ykjhlrdw_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert ykjhshdb_audit_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step03)用款计划审核(复审)")
    @allure.title("用款计划审核(复审)：审核")
    def testYkjhshfsAudit(self):
        ykjhshfs_audit_url = base_url + '/payfront/plan-service/v3/payplanvoucher/action/audit'
        ykjhshfs_audit_headers = {"Content-Type": "application/json",
                                          "tokenid": tokenids}
        ykjhshfs_audit_data = {
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "actionName": "审核",
            "appId": "pay_plan_voucher",
            "menuId": "47CFF09F6ADCB6BF236CDAE8D8F33C73",
            "actionType": "2",
            "glType": 0,
            "ids": [
                ykjhlrdb_plan_id
            ]
        }

        # 将dict转换为str
        ykjhshfs_audit_data_str = json.dumps(ykjhshfs_audit_data)
        try:
            ykjhshfs_audit_start = time.time()  # 开始时间
            ykjhshfs_audit_res = requests.post(ykjhshfs_audit_url,
                                                       headers=ykjhshfs_audit_headers,
                                                       data=ykjhshfs_audit_data_str)
            ykjhshfs_audit_res_json = ykjhshfs_audit_res.json()
            ykjhshfs_audit_end = time.time()  # 结束时间
            ykjhshfs_audit_res_time = ykjhshfs_audit_end - ykjhshfs_audit_start
            ykjhshfs_audit_res_time_ms = ykjhshfs_audit_res_time * 1000
            print("\n")
            print(f"响应时间：{ykjhshfs_audit_res_time_ms}毫秒")
            # print(ykjhshfs_audit_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(ykjhshfs_audit_url, ykjhshfs_audit_data_str,
                                       ykjhshfs_audit_headers))
            logss.logger.info("返回结果：{}".format(ykjhshfs_audit_res.text))
            ###断言
            response_rscode = ykjhshfs_audit_res_json.get('rscode')
            response_result = ykjhshfs_audit_res_json.get('result')

            # pytest.assume(ykjhlrdw_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert ykjhshfs_audit_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step04)用款计划批复")
    @allure.title("用款计划批复：批复")
    def testYkjhpfReplyplan(self):
        ykjhpf_replyplan_url = base_url + '/payfront/plan-service/v3/payplanvoucher/front/action/replyplan'
        ykjhpf_replyplan_headers = {"Content-Type": "application/json",
                                          "tokenid": tokenids}
        ykjhpf_replyplan_data = {
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "actionName": "批复",
            "appId": "pay_plan_voucher",
            "menuId": "6CF559B30C55449DB03F5067F88AE2E7",
            "actionType": "2",
            "glType": 3,
            "advice": "ces",
            "ids": [
                ykjhlrdb_plan_id
            ]
        }

        # 将dict转换为str
        ykjhpf_replyplan_data_str = json.dumps(ykjhpf_replyplan_data)
        try:
            ykjhpf_replyplan_start = time.time()  # 开始时间
            ykjhpf_replyplan_res = requests.post(ykjhpf_replyplan_url,
                                                       headers=ykjhpf_replyplan_headers,
                                                       data=ykjhpf_replyplan_data_str)
            ykjhpf_replyplan_res_json = ykjhpf_replyplan_res.json()
            ykjhpf_replyplan_end = time.time()  # 结束时间
            ykjhpf_replyplan_res_time = ykjhpf_replyplan_end - ykjhpf_replyplan_start
            ykjhpf_replyplan_res_time_ms = ykjhpf_replyplan_res_time * 1000
            print("\n")
            print(f"响应时间：{ykjhpf_replyplan_res_time_ms}毫秒")
            # print(ykjhpf_replyplan_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(ykjhpf_replyplan_url, ykjhpf_replyplan_data_str,
                                       ykjhpf_replyplan_headers))
            logss.logger.info("返回结果：{}".format(ykjhpf_replyplan_res.text))
            ###断言
            response_rscode = ykjhpf_replyplan_res_json.get('rscode')
            response_result = ykjhpf_replyplan_res_json.get('result')

            # pytest.assume(ykjhlrdw_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert ykjhpf_replyplan_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常


@allure.feature('(case03)用款计划(交投)')
class Testplanjt:
    @allure.story("(step01)单位用款计划录入")
    @allure.title("单位用款计划录入：保存")
    def testDwykjhlrInsert(self):
        dwykjhlr_insert_url= base_url + '/payfront/plan-service/v3/payplanvoucher/front/action/insert'
        dwykjhlr_insert_headers = {"Content-Type": "application/json",
                                           "tokenid": tokenids}
        dwykjhlr_insert_data = {
            "isFinancial": "1",
            "actionName": "新增",
            "bookkeepingType": "1",
            "appId": "pay_plan_voucher",
            "menuId": "47CFF09F6CCDD6BF236BBBE8D8F77C88",
            "actionType": "1",
            "glType": 1,
            "isBudget": 'true',
            "list": [
                {
                    "id": "d90f49adb78db8343547023025efcf4d",
                    "use_des": "交投计划",
                    "month": "4",
                    "plan_app_amt": "170",
                    "fileList": []
                }
            ]

        }
        dwykjhlr_insert_data_str = json.dumps(dwykjhlr_insert_data)
        try:
            dwykjhlr_insert_start=time.time()   #开始时间
            dwykjhlr_insert_res = requests.post(dwykjhlr_insert_url,
                                                        headers=dwykjhlr_insert_headers,
                                                        data=dwykjhlr_insert_data_str)
            dwykjhlr_insert_res_json = dwykjhlr_insert_res.json()
            dwykjhlr_insert_end =time.time()   #结束时间
            dwykjhlr_insert_res_time= dwykjhlr_insert_end -dwykjhlr_insert_start
            dwykjhlr_insert_res_time_ms=  dwykjhlr_insert_res_time * 1000
            print("\n")
            print(f"响应时间：{dwykjhlr_insert_res_time_ms}毫秒")

            # print(dwykjhlr_insert_res.text)
            logss.logger.info("请求参数：{}，{}，{}".format(dwykjhlr_insert_url,dwykjhlr_insert_data_str,dwykjhlr_insert_headers))
            logss.logger.info("返回结果：{}".format(dwykjhlr_insert_res.text))

            ###断言
            response_rscode = dwykjhlr_insert_res_json.get('rscode')
            response_result = dwykjhlr_insert_res_json.get('result')

            ###使用pytest.assume进行断言，失败一个后，可用正常允许其它用例
            # pytest.assume(agency_res.status_code == 200)
            # pytest.assume(response_rscode == 200 )
            # pytest.assume(response_result == "请求成功")

            assert dwykjhlr_insert_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"
        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s",e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step01)单位用款计划录入")
    @allure.title("单位用款计划录入：未送审列表")
    def testDwykjhlrLoadTableDatas(self):
        dwykjhlr_loadTableDatas_url = base_url + '/payfront/plan-service/v3/payplanvoucher/front/loadtabledatas'
        dwykjhlr_loadTableDatas_headers = {"Content-Type": "application/json",
                                            "tokenid": tokenids}
        dwykjhlr_loadTableDatas_data = {
            "statusCode": "1",
            "menuId": "47CFF09F6CCDD6BF236BBBE8D8F77C88",
            "leftTreeCode": "",
            "isHaveZero": "0",
            "classname": "com.boss.payplan.ui.page.PayPlanVoucherPage",
            "appId": "pay_plan_voucher",
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "roleId": "201EC9F7611B11B38E60BA5B10633BDB",
            "params": {
                "accountClsId": "CCBB352E4C7B6BBF4C4AC8F14CC89483",
                "accountType": "63",
                "isFinancial": "0"
            },
            "pageNum": 1,
            "pageSize": 20,
            "sort": "create_time desc",
            "condition": {
                "agency_code": [],
                "fund_type_code": [],
                "manage_mof_dep_code": [],
                "pay_type_code": []
            }
        }

        # 将dict转换为str
        dwykjhlr_loadTableDatas_data_str = json.dumps(dwykjhlr_loadTableDatas_data)
        try:
            dwykjhlr_loadTableDatas_start = time.time()  # 开始时间
            dwykjhlr_loadTableDatas_res = requests.post(dwykjhlr_loadTableDatas_url,
                                                         headers=dwykjhlr_loadTableDatas_headers,
                                                         data=dwykjhlr_loadTableDatas_data_str)
            dwykjhlr_loadTableDatas_res_json = dwykjhlr_loadTableDatas_res.json()
            dwykjhlr_loadTableDatas_end = time.time()  # 结束时间
            dwykjhlr_loadTableDatas_res_time = dwykjhlr_loadTableDatas_end - dwykjhlr_loadTableDatas_start
            dwykjhlr_loadTableDatas_res_time_ms = dwykjhlr_loadTableDatas_res_time * 1000
            print("\n")
            print(f"响应时间：{dwykjhlr_loadTableDatas_res_time_ms}毫秒")
            # print(dwykjhlr_loadTableDatas_res.text)

            global dwykjhlr_plan_id
            dwykjhlr_plan_id = dwykjhlr_loadTableDatas_res_json.get("data").get("rows")[0]["id"]
            print("计划id：",dwykjhlr_plan_id)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(dwykjhlr_loadTableDatas_url, dwykjhlr_loadTableDatas_data_str,
                                       dwykjhlr_loadTableDatas_headers))
            logss.logger.info("返回结果：{}".format(dwykjhlr_loadTableDatas_res.text))
            ###断言
            response_rscode = dwykjhlr_loadTableDatas_res_json.get('rscode')
            response_result = dwykjhlr_loadTableDatas_res_json.get('result')

            # pytest.assume(dwykjhlr_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert dwykjhlr_loadTableDatas_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step01)单位用款计划录入")
    @allure.title("单位用款计划录入：送审")
    def testDwykjhlrAudit(self):
        dwykjhlr_audit_url = base_url + '/payfront/plan-service/v3/payplanvoucher/action/audit'
        dwykjhlr_audit_headers = {"Content-Type": "application/json",
                                       "tokenid": tokenids}
        dwykjhlr_audit_data = {
            "actionName": "送审",
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "appId": "pay_plan_voucher",
            "menuId": "47CFF09F6CCDD6BF236BBBE8D8F77C88",
            "actionType": "2",
            "glType": 0,
            "ids": [
                dwykjhlr_plan_id
            ]
        }

        # 将dict转换为str
        dwykjhlr_audit_data_str = json.dumps(dwykjhlr_audit_data)
        try:
            dwykjhlr_audit_start = time.time()  # 开始时间
            dwykjhlr_audit_res = requests.post(dwykjhlr_audit_url,
                                                    headers=dwykjhlr_audit_headers,
                                                    data=dwykjhlr_audit_data_str)
            dwykjhlr_audit_res_json = dwykjhlr_audit_res.json()
            dwykjhlr_audit_end = time.time()  # 结束时间
            dwykjhlr_audit_res_time = dwykjhlr_audit_end - dwykjhlr_audit_start
            dwykjhlr_audit_res_time_ms = dwykjhlr_audit_res_time * 1000
            print("\n")
            print(f"响应时间：{dwykjhlr_audit_res_time_ms}毫秒")
            # print(dwykjhlr_audit_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(dwykjhlr_audit_url, dwykjhlr_audit_data_str,
                                       dwykjhlr_audit_headers))
            logss.logger.info("返回结果：{}".format(dwykjhlr_audit_res.text))
            ###断言
            response_rscode = dwykjhlr_audit_res_json.get('rscode')
            response_result = dwykjhlr_audit_res_json.get('result')

            # pytest.assume(dwykjhlr_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert dwykjhlr_audit_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step02)用款计划审核")
    @allure.title("用款计划审核：审核")
    def testYkjhshAudit(self):
        ykjhsh_audit_url = base_url + '/payfront/plan-service/v3/payplanvoucher/action/audit'
        ykjhsh_audit_headers = {"Content-Type": "application/json",
                                       "tokenid": tokenids}
        ykjhsh_audit_data = {
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "actionName": "审核",
            "appId": "pay_plan_voucher",
            "menuId": "9E2203AEA2CB11EBB9E28C3DBE542F37",
            "actionType": "2",
            "glType": 0,
            "ids": [
                dwykjhlr_plan_id
            ]
        }

        # 将dict转换为str
        ykjhsh_audit_data_str = json.dumps(ykjhsh_audit_data)
        try:
            ykjhsh_audit_start = time.time()  # 开始时间
            ykjhsh_audit_res = requests.post(ykjhsh_audit_url,
                                                    headers=ykjhsh_audit_headers,
                                                    data=ykjhsh_audit_data_str)
            ykjhsh_audit_res_json = ykjhsh_audit_res.json()
            ykjhsh_audit_end = time.time()  # 结束时间
            ykjhsh_audit_res_time = ykjhsh_audit_end - ykjhsh_audit_start
            ykjhsh_audit_res_time_ms = ykjhsh_audit_res_time * 1000
            print("\n")
            print(f"响应时间：{ykjhsh_audit_res_time_ms}毫秒")
            # print(ykjhsh_audit_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(ykjhsh_audit_url, ykjhsh_audit_data_str,
                                       ykjhsh_audit_headers))
            logss.logger.info("返回结果：{}".format(ykjhsh_audit_res.text))
            ###断言
            response_rscode = ykjhsh_audit_res_json.get('rscode')
            response_result = ykjhsh_audit_res_json.get('result')

            # pytest.assume(ykjhlrdw_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert ykjhsh_audit_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step03)用款计划审核(复审)")
    @allure.title("用款计划审核(复审)：审核")
    def testYkjhshfsAudit(self):
        ykjhshfs_audit_url = base_url + '/payfront/plan-service/v3/payplanvoucher/action/audit'
        ykjhshfs_audit_headers = {"Content-Type": "application/json",
                                          "tokenid": tokenids}
        ykjhshfs_audit_data = {
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "actionName": "审核",
            "appId": "pay_plan_voucher",
            "menuId": "47CFF09F6ADCB6BF236CDAE8D8F33C73",
            "actionType": "2",
            "glType": 0,
            "ids": [
                dwykjhlr_plan_id
            ]
        }

        # 将dict转换为str
        ykjhshfs_audit_data_str = json.dumps(ykjhshfs_audit_data)
        try:
            ykjhshfs_audit_start = time.time()  # 开始时间
            ykjhshfs_audit_res = requests.post(ykjhshfs_audit_url,
                                                       headers=ykjhshfs_audit_headers,
                                                       data=ykjhshfs_audit_data_str)
            ykjhshfs_audit_res_json = ykjhshfs_audit_res.json()
            ykjhshfs_audit_end = time.time()  # 结束时间
            ykjhshfs_audit_res_time = ykjhshfs_audit_end - ykjhshfs_audit_start
            ykjhshfs_audit_res_time_ms = ykjhshfs_audit_res_time * 1000
            print("\n")
            print(f"响应时间：{ykjhshfs_audit_res_time_ms}毫秒")
            # print(ykjhshfs_audit_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(ykjhshfs_audit_url, ykjhshfs_audit_data_str,
                                       ykjhshfs_audit_headers))
            logss.logger.info("返回结果：{}".format(ykjhshfs_audit_res.text))
            ###断言
            response_rscode = ykjhshfs_audit_res_json.get('rscode')
            response_result = ykjhshfs_audit_res_json.get('result')

            # pytest.assume(ykjhlrdw_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert ykjhshfs_audit_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step04)用款计划批复")
    @allure.title("用款计划批复：批复")
    def testYkjhpfReplyplan(self):
        ykjhpf_replyplan_url = base_url + '/payfront/plan-service/v3/payplanvoucher/front/action/replyplan'
        ykjhpf_replyplan_headers = {"Content-Type": "application/json",
                                          "tokenid": tokenids}
        ykjhpf_replyplan_data = {
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "actionName": "批复",
            "appId": "pay_plan_voucher",
            "menuId": "6CF559B30C55449DB03F5067F88AE2E7",
            "actionType": "2",
            "glType": 3,
            "advice": "ces",
            "ids": [
                dwykjhlr_plan_id
            ]
        }

        # 将dict转换为str
        ykjhpf_replyplan_data_str = json.dumps(ykjhpf_replyplan_data)
        try:
            ykjhpf_replyplan_start = time.time()  # 开始时间
            ykjhpf_replyplan_res = requests.post(ykjhpf_replyplan_url,
                                                       headers=ykjhpf_replyplan_headers,
                                                       data=ykjhpf_replyplan_data_str)
            ykjhpf_replyplan_res_json = ykjhpf_replyplan_res.json()
            ykjhpf_replyplan_end = time.time()  # 结束时间
            ykjhpf_replyplan_res_time = ykjhpf_replyplan_end - ykjhpf_replyplan_start
            ykjhpf_replyplan_res_time_ms = ykjhpf_replyplan_res_time * 1000
            print("\n")
            print(f"响应时间：{ykjhpf_replyplan_res_time_ms}毫秒")
            # print(ykjhpf_replyplan_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(ykjhpf_replyplan_url, ykjhpf_replyplan_data_str,
                                       ykjhpf_replyplan_headers))
            logss.logger.info("返回结果：{}".format(ykjhpf_replyplan_res.text))
            ###断言
            response_rscode = ykjhpf_replyplan_res_json.get('rscode')
            response_result = ykjhpf_replyplan_res_json.get('result')

            # pytest.assume(ykjhlrdw_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert ykjhpf_replyplan_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常
        

@allure.feature('(case04)调减计划(单位)')
class Testplanless:
    @allure.story("(step01)调减计划录入(单位)")
    @allure.title("调减计划录入(单位)：保存")
    def testtjjhlrdwNewinsert(self):
        tjjhlrdw_newinsert_url= base_url + '/payfront/plan-service/v3/payplanvoucher/front/action/newinsert'
        tjjhlrdw_newinsert_headers = {"Content-Type": "application/json",
                                           "tokenid": tokenids}
        tjjhlrdw_newinsert_data = {
            "appId": "pay_plan_voucher",
            "menuId": "490E0A13B01FC073F77F47B392022AC4",
            "actionType": "1",
            "glType": 1,
            "isBudget": 'false',
            "list": [
                {
                    "id": "1775326015709990912",
                    "use_des": "调减计划",
                    "month": "4",
                    "plan_app_amt": "-50",
                    "fileList": [],
                    "attachment_id": ""
                }
            ]
        }
        tjjhlrdw_newinsert_data_str = json.dumps(tjjhlrdw_newinsert_data)
        try:
            tjjhlrdw_newinsert_start=time.time()   #开始时间
            tjjhlrdw_newinsert_res = requests.post(tjjhlrdw_newinsert_url,
                                                        headers=tjjhlrdw_newinsert_headers,
                                                        data=tjjhlrdw_newinsert_data_str)
            tjjhlrdw_newinsert_res_json = tjjhlrdw_newinsert_res.json()
            tjjhlrdw_newinsert_end =time.time()   #结束时间
            tjjhlrdw_newinsert_res_time= tjjhlrdw_newinsert_end -tjjhlrdw_newinsert_start
            tjjhlrdw_newinsert_res_time_ms=  tjjhlrdw_newinsert_res_time * 1000
            print("\n")
            print(f"响应时间：{tjjhlrdw_newinsert_res_time_ms}毫秒")

            # print(tjjhlrdw_newinsert_res.text)
            logss.logger.info("请求参数：{}，{}，{}".format(tjjhlrdw_newinsert_url,tjjhlrdw_newinsert_data_str,tjjhlrdw_newinsert_headers))
            logss.logger.info("返回结果：{}".format(tjjhlrdw_newinsert_res.text))

            ###断言
            response_rscode = tjjhlrdw_newinsert_res_json.get('rscode')
            response_result = tjjhlrdw_newinsert_res_json.get('result')

            ###使用pytest.assume进行断言，失败一个后，可用正常允许其它用例
            # pytest.assume(agency_res.status_code == 200)
            # pytest.assume(response_rscode == 200 )
            # pytest.assume(response_result == "请求成功")

            assert tjjhlrdw_newinsert_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"
        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s",e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step01)调减计划录入(单位)")
    @allure.title("调减计划录入(单位)：未送审列表")
    def testtjjhlrdwLoadTableDatas(self):
        tjjhlrdw_loadTableDatas_url = base_url + '/payfront/plan-service/v3/payplanvoucher/front/loadtabledatas'
        tjjhlrdw_loadTableDatas_headers = {"Content-Type": "application/json",
                                            "tokenid": tokenids}
        tjjhlrdw_loadTableDatas_data = {
            "condition": {},
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "statusCode": "1",
            "menuId": "490E0A13B01FC073F77F47B392022AC4",
            "leftTreeCode": "",
            "isHaveZero": "0",
            "classname": "com.boss.payplan.ui.page.PayPlanVoucherPage",
            "appId": "pay_plan_voucher",
            "roleId": "201EC9F7611B11B38E60BA5B10633BDB",
            "params": {
                "accountClsId": "29BE185FAA92B21FA421DC48DBCC0937",
                "accountType": "63"
            },
            "pageNum": 1,
            "pageSize": 20,
            "sort": " agency_code asc,create_time desc",
            "otherCondition": "subtract"
        }

        # 将dict转换为str
        tjjhlrdw_loadTableDatas_data_str = json.dumps(tjjhlrdw_loadTableDatas_data)
        try:
            tjjhlrdw_loadTableDatas_start = time.time()  # 开始时间
            tjjhlrdw_loadTableDatas_res = requests.post(tjjhlrdw_loadTableDatas_url,
                                                         headers=tjjhlrdw_loadTableDatas_headers,
                                                         data=tjjhlrdw_loadTableDatas_data_str)
            tjjhlrdw_loadTableDatas_res_json = tjjhlrdw_loadTableDatas_res.json()
            tjjhlrdw_loadTableDatas_end = time.time()  # 结束时间
            tjjhlrdw_loadTableDatas_res_time = tjjhlrdw_loadTableDatas_end - tjjhlrdw_loadTableDatas_start
            tjjhlrdw_loadTableDatas_res_time_ms = tjjhlrdw_loadTableDatas_res_time * 1000
            print("\n")
            print(f"响应时间：{tjjhlrdw_loadTableDatas_res_time_ms}毫秒")
            # print(tjjhlrdw_loadTableDatas_res.text)

            global tjjhlrdw_plan_id
            tjjhlrdw_plan_id = tjjhlrdw_loadTableDatas_res_json.get("data").get("rows")[0]["id"]
            print("计划id：",tjjhlrdw_plan_id)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(tjjhlrdw_loadTableDatas_url, tjjhlrdw_loadTableDatas_data_str,
                                       tjjhlrdw_loadTableDatas_headers))
            logss.logger.info("返回结果：{}".format(tjjhlrdw_loadTableDatas_res.text))
            ###断言
            response_rscode = tjjhlrdw_loadTableDatas_res_json.get('rscode')
            response_result = tjjhlrdw_loadTableDatas_res_json.get('result')

            # pytest.assume(tjjhlrdw_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert tjjhlrdw_loadTableDatas_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step01)调减计划录入(单位)")
    @allure.title("调减计划录入(单位)：送审")
    def testtjjhlrdwAudit(self):
        tjjhlrdw_audit_url = base_url + '/payfront/plan-service/v3/payplanvoucher/action/audit'
        tjjhlrdw_audit_headers = {"Content-Type": "application/json",
                                       "tokenid": tokenids}
        tjjhlrdw_audit_data = {
            "actionName": "送审",
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "appId": "pay_plan_voucher",
            "menuId": "490E0A13B01FC073F77F47B392022AC4",
            "actionType": "2",
            "glType": 0,
            "ids": [
                tjjhlrdw_plan_id
            ]
        }

        # 将dict转换为str
        tjjhlrdw_audit_data_str = json.dumps(tjjhlrdw_audit_data)
        try:
            tjjhlrdw_audit_start = time.time()  # 开始时间
            tjjhlrdw_audit_res = requests.post(tjjhlrdw_audit_url,
                                                    headers=tjjhlrdw_audit_headers,
                                                    data=tjjhlrdw_audit_data_str)
            tjjhlrdw_audit_res_json = tjjhlrdw_audit_res.json()
            tjjhlrdw_audit_end = time.time()  # 结束时间
            tjjhlrdw_audit_res_time = tjjhlrdw_audit_end - tjjhlrdw_audit_start
            tjjhlrdw_audit_res_time_ms = tjjhlrdw_audit_res_time * 1000
            print("\n")
            print(f"响应时间：{tjjhlrdw_audit_res_time_ms}毫秒")
            # print(tjjhlrdw_audit_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(tjjhlrdw_audit_url, tjjhlrdw_audit_data_str,
                                       tjjhlrdw_audit_headers))
            logss.logger.info("返回结果：{}".format(tjjhlrdw_audit_res.text))
            ###断言
            response_rscode = tjjhlrdw_audit_res_json.get('rscode')
            response_result = tjjhlrdw_audit_res_json.get('result')

            # pytest.assume(tjjhlrdw_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert tjjhlrdw_audit_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step02)用款计划审核(复审)")
    @allure.title("用款计划审核(复审)：审核")
    def testYkjhshfsAudit(self):
        ykjhshfs_audit_url = base_url + '/payfront/plan-service/v3/payplanvoucher/action/audit'
        ykjhshfs_audit_headers = {"Content-Type": "application/json",
                                          "tokenid": tokenids}
        ykjhshfs_audit_data = {
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "actionName": "审核",
            "appId": "pay_plan_voucher",
            "menuId": "47CFF09F6ADCB6BF236CDAE8D8F33C73",
            "actionType": "2",
            "glType": 0,
            "ids": [
                tjjhlrdw_plan_id
            ]
        }

        # 将dict转换为str
        ykjhshfs_audit_data_str = json.dumps(ykjhshfs_audit_data)
        try:
            ykjhshfs_audit_start = time.time()  # 开始时间
            ykjhshfs_audit_res = requests.post(ykjhshfs_audit_url,
                                                       headers=ykjhshfs_audit_headers,
                                                       data=ykjhshfs_audit_data_str)
            ykjhshfs_audit_res_json = ykjhshfs_audit_res.json()
            ykjhshfs_audit_end = time.time()  # 结束时间
            ykjhshfs_audit_res_time = ykjhshfs_audit_end - ykjhshfs_audit_start
            ykjhshfs_audit_res_time_ms = ykjhshfs_audit_res_time * 1000
            print("\n")
            print(f"响应时间：{ykjhshfs_audit_res_time_ms}毫秒")
            # print(ykjhshfs_audit_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(ykjhshfs_audit_url, ykjhshfs_audit_data_str,
                                       ykjhshfs_audit_headers))
            logss.logger.info("返回结果：{}".format(ykjhshfs_audit_res.text))
            ###断言
            response_rscode = ykjhshfs_audit_res_json.get('rscode')
            response_result = ykjhshfs_audit_res_json.get('result')

            # pytest.assume(ykjhlrdw_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert ykjhshfs_audit_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step03)用款计划批复")
    @allure.title("用款计划批复：批复")
    def testYkjhpfReplyplan(self):
        ykjhpf_replyplan_url = base_url + '/payfront/plan-service/v3/payplanvoucher/front/action/replyplan'
        ykjhpf_replyplan_headers = {"Content-Type": "application/json",
                                          "tokenid": tokenids}
        ykjhpf_replyplan_data = {
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "actionName": "批复",
            "appId": "pay_plan_voucher",
            "menuId": "6CF559B30C55449DB03F5067F88AE2E7",
            "actionType": "2",
            "glType": 3,
            "advice": "ces",
            "ids": [
                tjjhlrdw_plan_id
            ]
        }

        # 将dict转换为str
        ykjhpf_replyplan_data_str = json.dumps(ykjhpf_replyplan_data)
        try:
            ykjhpf_replyplan_start = time.time()  # 开始时间
            ykjhpf_replyplan_res = requests.post(ykjhpf_replyplan_url,
                                                       headers=ykjhpf_replyplan_headers,
                                                       data=ykjhpf_replyplan_data_str)
            ykjhpf_replyplan_res_json = ykjhpf_replyplan_res.json()
            ykjhpf_replyplan_end = time.time()  # 结束时间
            ykjhpf_replyplan_res_time = ykjhpf_replyplan_end - ykjhpf_replyplan_start
            ykjhpf_replyplan_res_time_ms = ykjhpf_replyplan_res_time * 1000
            print("\n")
            print(f"响应时间：{ykjhpf_replyplan_res_time_ms}毫秒")
            # print(ykjhpf_replyplan_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(ykjhpf_replyplan_url, ykjhpf_replyplan_data_str,
                                       ykjhpf_replyplan_headers))
            logss.logger.info("返回结果：{}".format(ykjhpf_replyplan_res.text))
            ###断言
            response_rscode = ykjhpf_replyplan_res_json.get('rscode')
            response_result = ykjhpf_replyplan_res_json.get('result')

            # pytest.assume(ykjhlrdw_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert ykjhpf_replyplan_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常


@allure.feature('(case05)调减计划(代编)')
class Testplandbless:
    @allure.story("(step01)调减计划录入(代编)")
    @allure.title("调减计划录入(代编)：保存")
    def testtjjhlrdbNewinsert(self):
        tjjhlrdb_newinsert_url= base_url + '/payfront/plan-service/v3/payplanvoucher/front/action/newinsert'
        tjjhlrdb_newinsert_headers = {"Content-Type": "application/json",
                                           "tokenid": tokenids}
        tjjhlrdb_newinsert_data = {
            "appId": "pay_plan_voucher",
            "menuId": "857E0A13B01FC073F77F47B392022DDL",
            "actionType": "1",
            "glType": 1,
            "isBudget": 'false',
            "list": [
                {
                    "id": "1775326015709990912",
                    "use_des": "代编调减计划",
                    "month": "4",
                    "plan_app_amt": "-30",
                    "fileList": [],
                    "attachment_id": ""
                }
            ]
        }
        tjjhlrdb_newinsert_data_str = json.dumps(tjjhlrdb_newinsert_data)
        try:
            tjjhlrdb_newinsert_start=time.time()   #开始时间
            tjjhlrdb_newinsert_res = requests.post(tjjhlrdb_newinsert_url,
                                                        headers=tjjhlrdb_newinsert_headers,
                                                        data=tjjhlrdb_newinsert_data_str)
            tjjhlrdb_newinsert_res_json = tjjhlrdb_newinsert_res.json()
            tjjhlrdb_newinsert_end =time.time()   #结束时间
            tjjhlrdb_newinsert_res_time= tjjhlrdb_newinsert_end -tjjhlrdb_newinsert_start
            tjjhlrdb_newinsert_res_time_ms=  tjjhlrdb_newinsert_res_time * 1000
            print("\n")
            print(f"响应时间：{tjjhlrdb_newinsert_res_time_ms}毫秒")

            # print(tjjhlrdb_newinsert_res.text)
            logss.logger.info("请求参数：{}，{}，{}".format(tjjhlrdb_newinsert_url,tjjhlrdb_newinsert_data_str,tjjhlrdb_newinsert_headers))
            logss.logger.info("返回结果：{}".format(tjjhlrdb_newinsert_res.text))

            ###断言
            response_rscode = tjjhlrdb_newinsert_res_json.get('rscode')
            response_result = tjjhlrdb_newinsert_res_json.get('result')

            ###使用pytest.assume进行断言，失败一个后，可用正常允许其它用例
            # pytest.assume(agency_res.status_code == 200)
            # pytest.assume(response_rscode == 200 )
            # pytest.assume(response_result == "请求成功")

            assert tjjhlrdb_newinsert_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"
        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s",e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step01)调减计划录入(代编)")
    @allure.title("调减计划录入(代编)：未送审列表")
    def testtjjhlrdbLoadTableDatas(self):
        tjjhlrdb_loadTableDatas_url = base_url + '/payfront/plan-service/v3/payplanvoucher/front/loadtabledatas'
        tjjhlrdb_loadTableDatas_headers = {"Content-Type": "application/json",
                                            "tokenid": tokenids}
        tjjhlrdb_loadTableDatas_data = {
            "condition": {},
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "statusCode": "1",
            "menuId": "857E0A13B01FC073F77F47B392022DDL",
            "leftTreeCode": "",
            "isHaveZero": "0",
            "classname": "com.boss.payplan.ui.page.PayPlanVoucherPage",
            "appId": "pay_plan_voucher",
            "roleId": "201EC9F7611B11B38E60BA5B10633BDB",
            "params": {
                "accountClsId": "29BE185FAA92B21FA421DC48DBCC0937",
                "accountType": "63"
            },
            "pageNum": 1,
            "pageSize": 20,
            "sort": " agency_code asc,create_time desc",
            "otherCondition": "subtract"

        }

        # 将dict转换为str
        tjjhlrdb_loadTableDatas_data_str = json.dumps(tjjhlrdb_loadTableDatas_data)
        try:
            tjjhlrdb_loadTableDatas_start = time.time()  # 开始时间
            tjjhlrdb_loadTableDatas_res = requests.post(tjjhlrdb_loadTableDatas_url,
                                                         headers=tjjhlrdb_loadTableDatas_headers,
                                                         data=tjjhlrdb_loadTableDatas_data_str)
            tjjhlrdb_loadTableDatas_res_json = tjjhlrdb_loadTableDatas_res.json()
            tjjhlrdb_loadTableDatas_end = time.time()  # 结束时间
            tjjhlrdb_loadTableDatas_res_time = tjjhlrdb_loadTableDatas_end - tjjhlrdb_loadTableDatas_start
            tjjhlrdb_loadTableDatas_res_time_ms = tjjhlrdb_loadTableDatas_res_time * 1000
            print("\n")
            print(f"响应时间：{tjjhlrdb_loadTableDatas_res_time_ms}毫秒")
            # print(tjjhlrdb_loadTableDatas_res.text)

            global tjjhlrdb_plan_id
            tjjhlrdb_plan_id = tjjhlrdb_loadTableDatas_res_json.get("data").get("rows")[0]["id"]
            print("计划id：",tjjhlrdb_plan_id)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(tjjhlrdb_loadTableDatas_url, tjjhlrdb_loadTableDatas_data_str,
                                       tjjhlrdb_loadTableDatas_headers))
            logss.logger.info("返回结果：{}".format(tjjhlrdb_loadTableDatas_res.text))
            ###断言
            response_rscode = tjjhlrdb_loadTableDatas_res_json.get('rscode')
            response_result = tjjhlrdb_loadTableDatas_res_json.get('result')

            # pytest.assume(tjjhlrdb_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert tjjhlrdb_loadTableDatas_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step01)调减计划录入(代编)")
    @allure.title("调减计划录入(代编)：送审")
    def testtjjhlrdbAudit(self):
        tjjhlrdb_audit_url = base_url + '/payfront/plan-service/v3/payplanvoucher/action/audit'
        tjjhlrdb_audit_headers = {"Content-Type": "application/json",
                                       "tokenid": tokenids}
        tjjhlrdb_audit_data = {
            "actionName": "送审",
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "appId": "pay_plan_voucher",
            "menuId": "857E0A13B01FC073F77F47B392022DDL",
            "actionType": "2",
            "glType": 0,
            "ids": [
                tjjhlrdb_plan_id
            ]
        }

        # 将dict转换为str
        tjjhlrdb_audit_data_str = json.dumps(tjjhlrdb_audit_data)
        try:
            tjjhlrdb_audit_start = time.time()  # 开始时间
            tjjhlrdb_audit_res = requests.post(tjjhlrdb_audit_url,
                                                    headers=tjjhlrdb_audit_headers,
                                                    data=tjjhlrdb_audit_data_str)
            tjjhlrdb_audit_res_json = tjjhlrdb_audit_res.json()
            tjjhlrdb_audit_end = time.time()  # 结束时间
            tjjhlrdb_audit_res_time = tjjhlrdb_audit_end - tjjhlrdb_audit_start
            tjjhlrdb_audit_res_time_ms = tjjhlrdb_audit_res_time * 1000
            print("\n")
            print(f"响应时间：{tjjhlrdb_audit_res_time_ms}毫秒")
            # print(tjjhlrdb_audit_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(tjjhlrdb_audit_url, tjjhlrdb_audit_data_str,
                                       tjjhlrdb_audit_headers))
            logss.logger.info("返回结果：{}".format(tjjhlrdb_audit_res.text))
            ###断言
            response_rscode = tjjhlrdb_audit_res_json.get('rscode')
            response_result = tjjhlrdb_audit_res_json.get('result')

            # pytest.assume(tjjhlrdb_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert tjjhlrdb_audit_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step02)用款计划审核(复审)")
    @allure.title("用款计划审核(复审)：审核")
    def testYkjhshfsAudit(self):
        ykjhshfs_audit_url = base_url + '/payfront/plan-service/v3/payplanvoucher/action/audit'
        ykjhshfs_audit_headers = {"Content-Type": "application/json",
                                          "tokenid": tokenids}
        ykjhshfs_audit_data = {
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "actionName": "审核",
            "appId": "pay_plan_voucher",
            "menuId": "47CFF09F6ADCB6BF236CDAE8D8F33C73",
            "actionType": "2",
            "glType": 0,
            "ids": [
                tjjhlrdb_plan_id
            ]
        }

        # 将dict转换为str
        ykjhshfs_audit_data_str = json.dumps(ykjhshfs_audit_data)
        try:
            ykjhshfs_audit_start = time.time()  # 开始时间
            ykjhshfs_audit_res = requests.post(ykjhshfs_audit_url,
                                                       headers=ykjhshfs_audit_headers,
                                                       data=ykjhshfs_audit_data_str)
            ykjhshfs_audit_res_json = ykjhshfs_audit_res.json()
            ykjhshfs_audit_end = time.time()  # 结束时间
            ykjhshfs_audit_res_time = ykjhshfs_audit_end - ykjhshfs_audit_start
            ykjhshfs_audit_res_time_ms = ykjhshfs_audit_res_time * 1000
            print("\n")
            print(f"响应时间：{ykjhshfs_audit_res_time_ms}毫秒")
            # print(ykjhshfs_audit_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(ykjhshfs_audit_url, ykjhshfs_audit_data_str,
                                       ykjhshfs_audit_headers))
            logss.logger.info("返回结果：{}".format(ykjhshfs_audit_res.text))
            ###断言
            response_rscode = ykjhshfs_audit_res_json.get('rscode')
            response_result = ykjhshfs_audit_res_json.get('result')

            # pytest.assume(ykjhlrdw_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert ykjhshfs_audit_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step03)用款计划批复")
    @allure.title("用款计划批复：批复")
    def testYkjhpfReplyplan(self):
        ykjhpf_replyplan_url = base_url + '/payfront/plan-service/v3/payplanvoucher/front/action/replyplan'
        ykjhpf_replyplan_headers = {"Content-Type": "application/json",
                                          "tokenid": tokenids}
        ykjhpf_replyplan_data = {
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "actionName": "批复",
            "appId": "pay_plan_voucher",
            "menuId": "6CF559B30C55449DB03F5067F88AE2E7",
            "actionType": "2",
            "glType": 3,
            "advice": "ces",
            "ids": [
                tjjhlrdb_plan_id
            ]
        }

        # 将dict转换为str
        ykjhpf_replyplan_data_str = json.dumps(ykjhpf_replyplan_data)
        try:
            ykjhpf_replyplan_start = time.time()  # 开始时间
            ykjhpf_replyplan_res = requests.post(ykjhpf_replyplan_url,
                                                       headers=ykjhpf_replyplan_headers,
                                                       data=ykjhpf_replyplan_data_str)
            ykjhpf_replyplan_res_json = ykjhpf_replyplan_res.json()
            ykjhpf_replyplan_end = time.time()  # 结束时间
            ykjhpf_replyplan_res_time = ykjhpf_replyplan_end - ykjhpf_replyplan_start
            ykjhpf_replyplan_res_time_ms = ykjhpf_replyplan_res_time * 1000
            print("\n")
            print(f"响应时间：{ykjhpf_replyplan_res_time_ms}毫秒")
            # print(ykjhpf_replyplan_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(ykjhpf_replyplan_url, ykjhpf_replyplan_data_str,
                                       ykjhpf_replyplan_headers))
            logss.logger.info("返回结果：{}".format(ykjhpf_replyplan_res.text))
            ###断言
            response_rscode = ykjhpf_replyplan_res_json.get('rscode')
            response_result = ykjhpf_replyplan_res_json.get('result')

            # pytest.assume(ykjhlrdw_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert ykjhpf_replyplan_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常


if __name__ == '__main__':

    pytest.main()


# 切换路径
# cd E:\pypro\APItest2\selectlist\testcase\pre_111
# 执行测试用例
# pytest budgetflow.py --alluredir ./allure-results/
# 生成报告
# allure generate allure-results -o allure-reports/ --clean
# 打开报告
# allure open allure-reports/