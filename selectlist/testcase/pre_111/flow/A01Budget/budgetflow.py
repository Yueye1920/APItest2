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


@allure.feature('(case01)指标管理')
class Testbudget:
    @allure.story("(step01)指标录入")
    @allure.title("指标录入：保存")
    def testZblrCommonSave(self):
        zblr_commonSave_url= base_url + '/payfront/mp-b-budget-service/v1/budget/commonSave'
        zblr_commonSave_headers = {"Content-Type": "application/json",
                                           "tokenid": tokenids}
        zblr_commonSave_data = {
            "data": [
                {
                    "amount_big_": "壹拾万元整",
                    "bgt_mof_dep_name": "农业处",
                    "fund_type_name": "经费拨款补助",
                    "source_type_name": "年初预算",
                    "bgt_source_name": "当期拨款（支出）",
                    "exp_func_name": "行政运行",
                    "gov_bgt_eco_name": "工资奖金津补贴",
                    "dir_name": "",
                    "bgt_rem_name": "",
                    "amount": 100000,
                    "version_name": "",
                    "pro_name": "219011指标管理1512",
                    "sup_bgt_doc_no_name": "",
                    "sup_bgt_doc_no": "",
                    "agency_name": "湖北省果茶办公室",
                    "thr_exp_name": "",
                    "pay_type_name": "国库集中支付",
                    "manage_mof_dep_name": "",
                    "budget_level_name": "中央级",
                    "bgt_type_name": "预拨指标",
                    "found_type_name": "预估",
                    "is_dir_name": "",
                    "is_sub_name": "",
                    "is_mat_code": "2",
                    "is_mat_name": "否",
                    "is_gov_pur_name": "否",
                    "income_sort_name": "",
                    "pro_cat_name": "人员类",
                    "acc_type_name": "",
                    "budget_year": "",
                    "budgetsource_year": "2024",
                    "dep_bgt_eco_name": "基本工资",
                    "lzfs_": "001##正常支付##AF5319AD1C75B211449956D8F2997E7F",
                    "bgt_temp_name": "",
                    "agency_": "219011##湖北省果茶办公室##6B98F3B2EE02434479C8630869A96C60",
                    "bgt_mof_dep_": "09##农业处##0B256AD0C2B3209E7FA2AE25873896B8",
                    "budget_level_": "1##中央级##ADFCEF32115CB6261336494BB71CB66D",
                    "pro_cat_": "1##人员类##550401E14E90A32D7B39A9A6734695DE",
                    "fund_type_": "11111##经费拨款补助##DE1C8E16759F474C2D92CBBFB7BA6385",
                    "exp_func_": "2010101##行政运行##A8C36161E5A91CFCC8E039A5F315AA92",
                    "found_type_": "12##预估##E3BB7DF43981C10F177EA6A60BBEFFC2",
                    "gov_bgt_eco_": "50101##工资奖金津补贴##543B56A3BE5FC85C7E389E6CFC4A3AB2",
                    "dep_bgt_eco_": "30101##基本工资##F2684D4AE3086DBDA207A71B269729D0",
                    "is_gov_pur_": "2##否##2",
                    "bgt_type_": "11##预拨指标##4F53297E01C18CFC47D3F942A0958939",
                    "source_type_": "1##年初预算##A494A01709D991D416528C4C38E90170",
                    "pay_type_": "1##国库集中支付##24B2435F18D2B38581D2845E32D14773",
                    "bgt_source_": "01##当期拨款（支出）##62A6C38B276AB2117EAECFC2EFD4FEFF",
                    "agency__viewSort": "219011-湖北省果茶办公室",
                    "bgt_mof_dep__viewSort": "09-农业处",
                    "budget_level__viewSort": "1-中央级",
                    "pro_cat__viewSort": "1-人员类",
                    "fund_type__viewSort": "11111-经费拨款补助",
                    "exp_func__viewSort": "2010101-行政运行",
                    "found_type__viewSort": "12-预估",
                    "gov_bgt_eco__viewSort": "50101-工资奖金津补贴",
                    "dep_bgt_eco__viewSort": "30101-基本工资",
                    "is_gov_pur__viewSort": "2-否",
                    "bgt_type__viewSort": "11-预拨指标",
                    "source_type__viewSort": "1-年初预算",
                    "pay_type__viewSort": "1-国库集中支付",
                    "bgt_source__viewSort": "01-当期拨款（支出）",
                    "lzfs__viewSort": "001-正常支付",
                    "is_gov_pur_id": 2,
                    "is_gov_pur_code": 2,
                    "lzfs_id": "AF5319AD1C75B211449956D8F2997E7F",
                    "lzfs_code": "001",
                    "lzfs_name": "正常支付",
                    "agency_id": "6B98F3B2EE02434479C8630869A96C60",
                    "agency_code": "219011",
                    "bgt_mof_dep_id": "0B256AD0C2B3209E7FA2AE25873896B8",
                    "bgt_mof_dep_code": "09",
                    "budget_level_id": "ADFCEF32115CB6261336494BB71CB66D",
                    "budget_level_code": "1",
                    "pro_cat_id": "550401E14E90A32D7B39A9A6734695DE",
                    "pro_cat_code": "1",
                    "fund_type_id": "DE1C8E16759F474C2D92CBBFB7BA6385",
                    "fund_type_code": "11111",
                    "exp_func": "",
                    "exp_func_id": "A8C36161E5A91CFCC8E039A5F315AA92",
                    "exp_func_code": "2010101",
                    "found_type_id": "E3BB7DF43981C10F177EA6A60BBEFFC2",
                    "found_type_code": "12",
                    "gov_bgt_eco_id": "543B56A3BE5FC85C7E389E6CFC4A3AB2",
                    "gov_bgt_eco_code": "50101",
                    "dep_bgt_eco": "",
                    "dep_bgt_eco_id": "F2684D4AE3086DBDA207A71B269729D0",
                    "dep_bgt_eco_code": "30101",
                    "bgt_type_id": "4F53297E01C18CFC47D3F942A0958939",
                    "bgt_type_code": "11",
                    "source_type_id": "A494A01709D991D416528C4C38E90170",
                    "source_type_code": "1",
                    "pay_type_id": "24B2435F18D2B38581D2845E32D14773",
                    "pay_type_code": "1",
                    "bgt_source_id": "62A6C38B276AB2117EAECFC2EFD4FEFF",
                    "bgt_source_code": "01",
                    "bgt_doc_title": "219011指标管理1512",
                    "doc_date": "2024-04-01",
                    "bgt_dec": "219011指标管理1512",
                    "cor_bgt_doc_id": "",
                    "cor_bgt_doc_code": "",
                    "cor_bgt_doc_name": "2024-0401-1512",
                    "cor_bgt_doc_no": "2024-0401-1512",
                    "cor_bgt_doc_no_id": "",
                    "cor_bgt_doc_no_code": "",
                    "cor_bgt_doc_no_name": "2024-0401-1512",
                    "voucher_code": "141001",
                    "is_mat_": "2-否",
                    "is_mat_id": "2"
                }
            ],
            "supType": "BUDGETINPUTCHECKELE",
            "appid": "budget-total",
            "menuguid": "BB39585CD1574D94B7D3DB7553930001",
            "actionType": "1",
            "glType": "0",
            "actionName": "新增",
            "action": "",
            "status": "1"

        }
        zblr_commonSave_data_str = json.dumps(zblr_commonSave_data)
        try:
            zblr_commonSave_start=time.time()   #开始时间
            zblr_commonSave_res = requests.post(zblr_commonSave_url,
                                                        headers=zblr_commonSave_headers,
                                                        data=zblr_commonSave_data_str)
            zblr_commonSave_res_json = zblr_commonSave_res.json()
            zblr_commonSave_end =time.time()   #结束时间
            zblr_commonSave_res_time= zblr_commonSave_end -zblr_commonSave_start
            zblr_commonSave_res_time_ms=  zblr_commonSave_res_time * 1000
            print("\n")
            print(f"响应时间：{zblr_commonSave_res_time_ms}毫秒")

            # print(zblr_commonSave_res.text)
            logss.logger.info("请求参数：{}，{}，{}".format(zblr_commonSave_url,zblr_commonSave_data_str,zblr_commonSave_headers))
            logss.logger.info("返回结果：{}".format(zblr_commonSave_res.text))

            ###断言
            response_rscode = zblr_commonSave_res_json.get('rscode')
            response_result = zblr_commonSave_res_json.get('result')

            ###使用pytest.assume进行断言，失败一个后，可用正常允许其它用例
            # pytest.assume(agency_res.status_code == 200)
            # pytest.assume(response_rscode == 200 )
            # pytest.assume(response_result == "请求成功")

            assert zblr_commonSave_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"
        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s",e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step01)指标录入")
    @allure.title("指标录入：额度列表")
    def testZblrLoadTableDatas(self):
        zblr_loadTableDatas_url = base_url + '/payfront/mp-b-budget-service/v1/budget/loadTableDatas'
        zblr_loadTableDatas_headers = {"Content-Type": "application/json",
                                            "tokenid": tokenids}
        zblr_loadTableDatas_data = {
            "appid": "budget-total",
            "menuguid": "BB39585CD1574D94B7D3DB7553930001",
            "querycondition": {},
            "roleId": "201EC9F7611B11B38E60BA5B10633BDB",
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "status": "1",
            "leftcondition": "",
            "sort": " agency_code,create_time desc",
            "pageNum": 1,
            "pageSize": 20
        }

        # 将dict转换为str
        zblr_loadTableDatas_data_str = json.dumps(zblr_loadTableDatas_data)
        try:
            zblr_loadTableDatas_start = time.time()  # 开始时间
            zblr_loadTableDatas_res = requests.post(zblr_loadTableDatas_url,
                                                         headers=zblr_loadTableDatas_headers,
                                                         data=zblr_loadTableDatas_data_str)
            zblr_loadTableDatas_res_json = zblr_loadTableDatas_res.json()
            zblr_loadTableDatas_end = time.time()  # 结束时间
            zblr_loadTableDatas_res_time = zblr_loadTableDatas_end - zblr_loadTableDatas_start
            zblr_loadTableDatas_res_time_ms = zblr_loadTableDatas_res_time * 1000
            print("\n")
            print(f"响应时间：{zblr_loadTableDatas_res_time_ms}毫秒")
            # print(zblr_loadTableDatas_res.text)

            global zblr_adj_sub_id
            zblr_adj_sub_id = zblr_loadTableDatas_res_json.get("data").get("rows")[0]["id"]
            print("指标id：",zblr_adj_sub_id)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(zblr_loadTableDatas_url, zblr_loadTableDatas_data_str,
                                       zblr_loadTableDatas_headers))
            logss.logger.info("返回结果：{}".format(zblr_loadTableDatas_res.text))
            ###断言
            response_rscode = zblr_loadTableDatas_res_json.get('rscode')
            response_result = zblr_loadTableDatas_res_json.get('result')

            # pytest.assume(zblr_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert zblr_loadTableDatas_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step01)指标录入")
    @allure.title("指标录入：送审")
    def testZblrCommonoperation(self):
        zblr_commonoperation_url = base_url + '/payfront/mp-b-budget-service/v1/common/budget/commonoperation'
        zblr_commonoperation_headers = {"Content-Type": "application/json",
                                       "tokenid": tokenids}
        zblr_commonoperation_data = {
            "data": [
                zblr_adj_sub_id
            ],
            "appid": "budget-total",
            "menuguid": "BB39585CD1574D94B7D3DB7553930001",
            "actionType": "2",
            "glType": "0",
            "actionName": "送审",
            "action": "audit",
            "status": "1"
        }

        # 将dict转换为str
        zblr_commonoperation_data_str = json.dumps(zblr_commonoperation_data)
        try:
            zblr_commonoperation_start = time.time()  # 开始时间
            zblr_commonoperation_res = requests.post(zblr_commonoperation_url,
                                                    headers=zblr_commonoperation_headers,
                                                    data=zblr_commonoperation_data_str)
            zblr_commonoperation_res_json = zblr_commonoperation_res.json()
            zblr_commonoperation_end = time.time()  # 结束时间
            zblr_commonoperation_res_time = zblr_commonoperation_end - zblr_commonoperation_start
            zblr_commonoperation_res_time_ms = zblr_commonoperation_res_time * 1000
            print("\n")
            print(f"响应时间：{zblr_commonoperation_res_time_ms}毫秒")
            # print(zblr_commonoperation_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(zblr_commonoperation_url, zblr_commonoperation_data_str,
                                       zblr_commonoperation_headers))
            logss.logger.info("返回结果：{}".format(zblr_commonoperation_res.text))
            ###断言
            response_rscode = zblr_commonoperation_res_json.get('rscode')
            response_result = zblr_commonoperation_res_json.get('result')

            # pytest.assume(zblr_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert zblr_commonoperation_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step02)业务处室审核")
    @allure.title("业务处室审核：审核")
    def testYwcsshCommonoperation(self):
        ywcssh_commonoperation_url = base_url + '/payfront/mp-b-budget-service/v1/common/budget/commonoperation'
        ywcssh_commonoperation_headers = {"Content-Type": "application/json",
                                       "tokenid": tokenids}
        ywcssh_commonoperation_data = {
            "data": [
                zblr_adj_sub_id
            ],
            "appid": "budget-total",
            "menuguid": "BB39585CD1574D94B7D3DB7553930002",
            "actionType": "2",
            "glType": "0",
            "actionName": "审核",
            "action": "audit"
        }

        # 将dict转换为str
        ywcssh_commonoperation_data_str = json.dumps(ywcssh_commonoperation_data)
        try:
            ywcssh_commonoperation_start = time.time()  # 开始时间
            ywcssh_commonoperation_res = requests.post(ywcssh_commonoperation_url,
                                                    headers=ywcssh_commonoperation_headers,
                                                    data=ywcssh_commonoperation_data_str)
            ywcssh_commonoperation_res_json = ywcssh_commonoperation_res.json()
            ywcssh_commonoperation_end = time.time()  # 结束时间
            ywcssh_commonoperation_res_time = ywcssh_commonoperation_end - ywcssh_commonoperation_start
            ywcssh_commonoperation_res_time_ms = ywcssh_commonoperation_res_time * 1000
            print("\n")
            print(f"响应时间：{ywcssh_commonoperation_res_time_ms}毫秒")
            # print(ywcssh_commonoperation_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(ywcssh_commonoperation_url, ywcssh_commonoperation_data_str,
                                       ywcssh_commonoperation_headers))
            logss.logger.info("返回结果：{}".format(ywcssh_commonoperation_res.text))
            ###断言
            response_rscode = ywcssh_commonoperation_res_json.get('rscode')
            response_result = ywcssh_commonoperation_res_json.get('result')

            # pytest.assume(zblr_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert ywcssh_commonoperation_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step03)指标审核")
    @allure.title("指标审核：审核")
    def testZbshCommonoperation(self):
        zbsh_commonoperation_url = base_url + '/payfront/mp-b-budget-service/v1/common/budget/commonoperation'
        zbsh_commonoperation_headers = {"Content-Type": "application/json",
                                          "tokenid": tokenids}
        zbsh_commonoperation_data = {
            "data": [
                zblr_adj_sub_id
            ],
            "appid": "budget-total",
            "menuguid": "BB39585CD1574D94B7D3DB7553930003",
            "actionType": "2",
            "glType": "0",
            "actionName": "审核",
            "action": "audit"
        }

        # 将dict转换为str
        zbsh_commonoperation_data_str = json.dumps(zbsh_commonoperation_data)
        try:
            zbsh_commonoperation_start = time.time()  # 开始时间
            zbsh_commonoperation_res = requests.post(zbsh_commonoperation_url,
                                                       headers=zbsh_commonoperation_headers,
                                                       data=zbsh_commonoperation_data_str)
            zbsh_commonoperation_res_json = zbsh_commonoperation_res.json()
            zbsh_commonoperation_end = time.time()  # 结束时间
            zbsh_commonoperation_res_time = zbsh_commonoperation_end - zbsh_commonoperation_start
            zbsh_commonoperation_res_time_ms = zbsh_commonoperation_res_time * 1000
            print("\n")
            print(f"响应时间：{zbsh_commonoperation_res_time_ms}毫秒")
            # print(zbsh_commonoperation_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(zbsh_commonoperation_url, zbsh_commonoperation_data_str,
                                       zbsh_commonoperation_headers))
            logss.logger.info("返回结果：{}".format(zbsh_commonoperation_res.text))
            ###断言
            response_rscode = zbsh_commonoperation_res_json.get('rscode')
            response_result = zbsh_commonoperation_res_json.get('result')

            # pytest.assume(zblr_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert zbsh_commonoperation_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step04)指标下达")
    @allure.title("指标下达：下达")
    def testZbxdCommonoperation(self):
        zbxd_commonoperation_url = base_url + '/payfront/mp-b-budget-service/v1/common/budget/commonoperation'
        zbxd_commonoperation_headers = {"Content-Type": "application/json",
                                          "tokenid": tokenids}
        zbxd_commonoperation_data = {
            "data": [
                zblr_adj_sub_id
            ],
            "appid": "budget-total",
            "menuguid": "BB39585CD1574D94B7D3DB7553930004",
            "actionType": "2",
            "glType": "3",
            "actionName": "下达",
            "action": "audit"
        }

        # 将dict转换为str
        zbxd_commonoperation_data_str = json.dumps(zbxd_commonoperation_data)
        try:
            zbxd_commonoperation_start = time.time()  # 开始时间
            zbxd_commonoperation_res = requests.post(zbxd_commonoperation_url,
                                                       headers=zbxd_commonoperation_headers,
                                                       data=zbxd_commonoperation_data_str)
            zbxd_commonoperation_res_json = zbxd_commonoperation_res.json()
            zbxd_commonoperation_end = time.time()  # 结束时间
            zbxd_commonoperation_res_time = zbxd_commonoperation_end - zbxd_commonoperation_start
            zbxd_commonoperation_res_time_ms = zbxd_commonoperation_res_time * 1000
            print("\n")
            print(f"响应时间：{zbxd_commonoperation_res_time_ms}毫秒")
            # print(zbxd_commonoperation_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(zbxd_commonoperation_url, zbxd_commonoperation_data_str,
                                       zbxd_commonoperation_headers))
            logss.logger.info("返回结果：{}".format(zbxd_commonoperation_res.text))
            ###断言
            response_rscode = zbxd_commonoperation_res_json.get('rscode')
            response_result = zbxd_commonoperation_res_json.get('result')

            # pytest.assume(zblr_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert zbxd_commonoperation_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常


@allure.feature('(case02)指标调减')
class Testbudgetless:
    @allure.story("(step01)指标调减录入")
    @allure.title("指标调减录入：保存")
    def testZbtjlrCommonSave(self):
        zbtjlr_commonSave_url= base_url + '/payfront/mp-b-budget-service/v1/budget/commonSave'
        zbtjlr_commonSave_headers = {"Content-Type": "application/json",
                                           "tokenid": tokenids}
        zbtjlr_commonSave_data = {
            "action": "",
            "actionName": "新增",
            "actionType": "1",
            "appid": "budget-total-dec",
            "glType": "1",
            "menuguid": "FA4894120DA54CCDBD99DE8A30FD2486",
            "attachment_id": "4B3178A9719242E69E899B078598894C",
            "status": "1",
            "data": [
                {
                    "budget_level_code": "1",
                    "bgt_type_id": "4F53297E01C18CFC47D3F942A0958939",
                    "bgt_mof_dep": "09农业处",
                    "found_type_code": "12",
                    "agency_code": "219011",
                    "bgt_source_id": "62A6C38B276AB2117EAECFC2EFD4FEFF",
                    "canuse_amt": 100000,
                    "dis_amt": 0,
                    "found_type": "12-预估",
                    "bgt_mof_dep_name": "农业处",
                    "manage_mof_dep": "09-农业处",
                    "pay_type_code": "1",
                    "bgt_type_code": "11",
                    "fiscal_year": "2024",
                    "manage_mof_dep_id": "0B256AD0C2B3209E7FA2AE25873896B8",
                    "gov_bgt_eco": "50101-工资奖金津补贴",
                    "is_more_pay": "2",
                    "direct_flag_name": "其它",
                    "dep_bgt_eco_id": "F2684D4AE3086DBDA207A71B269729D0",
                    "use_amt": 0,
                    "mof_div_code": "420000000",
                    "agency_id": "6B98F3B2EE02434479C8630869A96C60",
                    "source_type": "1-年初预算",
                    "bgt_mof_dep_id": "0B256AD0C2B3209E7FA2AE25873896B8",
                    "version": "2024-04-02 10:53:11",
                    "budget_level": "1-中央级",
                    "is_gov_pur_id": "2",
                    "zdzjjqpt_name": "否",
                    "todo_node": "BB39585CD1574D94B7D3DB7553930004",
                    "use_amt1": 0,
                    "is_mat_id": "2",
                    "exp_func_name": "行政运行",
                    "pro_name": "219011指标管理1512",
                    "lzfs_code": "001",
                    "found_type_id": "E3BB7DF43981C10F177EA6A60BBEFFC2",
                    "aviamt": "100000",
                    "fund_type": "11111-经费拨款补助",
                    "is_mat_code": "2",
                    "gov_bgt_eco_code": "50101",
                    "canuseamt": "100000.00",
                    "update_time": "2024-04-02 10:53:11",
                    "bgt_source_code": "01",
                    "bkqjsx": "01-当期拨款（支出）",
                    "pay_type_id": "24B2435F18D2B38581D2845E32D14773",
                    "exp_func_code": "2010101",
                    "budget_type": "1",
                    "agency_name": "湖北省果茶办公室",
                    "agency": "219011-湖北省果茶办公室",
                    "bat_num": "0",
                    "work_flow_id": "budget-total",
                    "fund_type_name": "经费拨款补助",
                    "cur_amt": "100000",
                    "bgt_mof_dep_code": "09",
                    "cor_bgt_doc_no": "2024-0401-1512",
                    "bkqjsx_code": "01",
                    "pro_cat_code": "1",
                    "pro_id": "491E2C2258164E9BA77DC5F88A26AAFA",
                    "bgt_type_name": "预拨指标",
                    "doc_date": "2024-04-01 00:00:00",
                    "pay_type_name": "国库集中支付",
                    "zblynd_name": "2024",
                    "manage_mof_dep_name": "农业处",
                    "acc_type": "-",
                    "dep_bgt_eco_name": "基本工资",
                    "todo_name": "指标下达",
                    "fund_type_id": "DE1C8E16759F474C2D92CBBFB7BA6385",
                    "source_type_id": "A494A01709D991D416528C4C38E90170",
                    "voucher_code": "141003",
                    "is_track": 1,
                    "done_node": "BB39585CD1574D94B7D3DB7553930003",
                    "zdzjjqpt_code": "2",
                    "is_not_control_pay": "2",
                    "clear_amt": 0,
                    "exp_func_id": "A8C36161E5A91CFCC8E039A5F315AA92",
                    "bgt_type": "11-预拨指标",
                    "bkqjsx_name": "当期拨款（支出）",
                    "plan_caliber_id": "d90f49adb78db8343547023025efcf4d",
                    "bgt_id": "B8534E87EBE74872A8AD576B99C551E4",
                    "pay_caliber_id": "B8534E87EBE74872A8AD576B99C551E4",
                    "xpay_amt": 0,
                    "gov_bgt_eco_id": "543B56A3BE5FC85C7E389E6CFC4A3AB2",
                    "pay_amt": 0,
                    "create_time": "2024-04-02 10:53:11",
                    "direct_flag_code": "09",
                    "is_adjust": 1,
                    "found_type_name": "预估",
                    "budget_level_name": "中央级",
                    "threesafe_symbolcat": "000-非“三保”支出",
                    "budget_level_id": "ADFCEF32115CB6261336494BB71CB66D",
                    "pro": "42000024219P007000049-219011指标管理1512",
                    "is_manager": "2",
                    "is_gov_pur_code": "2",
                    "dep_bgt_eco": "30101基本工资",
                    "creater": "1F0795D7E8724F998426100EB01D6195",
                    "bgt_doc_title": "219011指标管理1512",
                    "threesafe_symbolcat_name": "非“三保”支出",
                    "fund_type_code": "11111",
                    "origin_model_code": "2",
                    "bgt_source_name": "当期拨款（支出）",
                    "adj_date": "2024-04-01 16:50:25",
                    "useamt": 0,
                    "source_type_name": "年初预算",
                    "is_contrlbyplan": "2",
                    "updater": "1F0795D7E8724F998426100EB01D6195",
                    "pro_cat": "1-人员类",
                    "bgt_exe_flag": "1",
                    "is_mat_name": "否",
                    "is_deleted": 2,
                    "source_type_code": "1",
                    "last_user": "1F0795D7E8724F998426100EB01D6195",
                    "manage_mof_dep_code": "09",
                    "is_gov_pur_name": "否",
                    "threesafe_symbolcat_code": "000",
                    "pro_cat_name": "人员类",
                    "once_done_node": "BB39585CD1574D94B7D3DB7553930002,BB39585CD1574D94B7D3DB7553930001",
                    "pay_type": "1-国库集中支付",
                    "pro_cat_id": "550401E14E90A32D7B39A9A6734695DE",
                    "lzfs_id": "AF5319AD1C75B211449956D8F2997E7F",
                    "zblynd_code": "2024",
                    "pro_code": "42000024219P007000049",
                    "amount": -100,
                    "is_gov_pur": "2-否",
                    "bgt_dec": "219011指标管理1512",
                    "is_end": "1",
                    "lzfs": "001-正常支付",
                    "exp_func": "2010101-行政运行",
                    "dep_bgt_eco_code": "30101",
                    "gov_bgt_eco_name": "工资奖金津补贴",
                    "lzfs_name": "正常支付",
                    "pagehelper_row_id": 1,
                    "statusCode": "9",
                    "useamt1": "0.00",
                    "progress": "0%",
                    "_XID": "row_77",
                    "pro_code__viewSort": "42000024219P007000049",
                    "aviamt__viewSort": "100,000.00",
                    "useamt1__viewSort": "0.00",
                    "canuseamt__viewSort": "100,000.00",
                    "dep_bgt_eco_code__viewSort": "30101",
                    "dep_bgt_eco_name__viewSort": "基本工资",
                    "bgt_doc_title__viewSort": "219011指标管理1512",
                    "cor_bgt_doc_no__viewSort": "2024-0401-1512",
                    "source_type_code__viewSort": "1",
                    "source_type_name__viewSort": "年初预算",
                    "found_type_code__viewSort": "12",
                    "found_type_name__viewSort": "预估",
                    "bgt_dec__viewSort": "219011指标管理1512",
                    "bgt_type_code__viewSort": "11",
                    "bgt_type_name__viewSort": "预拨指标",
                    "fiscal_year__viewSort": "2024",
                    "budget_level_name__viewSort": "中央级",
                    "aviamt__moneySwitchinput": "100000",
                    "useamt1__moneySwitchinput": "0",
                    "cur_amt__moneySwitchinput": "100000"
                }
            ]

        }
        zbtjlr_commonSave_data_str = json.dumps(zbtjlr_commonSave_data)
        try:
            zbtjlr_commonSave_start=time.time()   #开始时间
            zbtjlr_commonSave_res = requests.post(zbtjlr_commonSave_url,
                                                        headers=zbtjlr_commonSave_headers,
                                                        data=zbtjlr_commonSave_data_str)
            zbtjlr_commonSave_res_json = zbtjlr_commonSave_res.json()
            zbtjlr_commonSave_end =time.time()   #结束时间
            zbtjlr_commonSave_res_time= zbtjlr_commonSave_end -zbtjlr_commonSave_start
            zbtjlr_commonSave_res_time_ms=  zbtjlr_commonSave_res_time * 1000
            print("\n")
            print(f"响应时间：{zbtjlr_commonSave_res_time_ms}毫秒")

            # print(zblr_commonSave_res.text)
            logss.logger.info("请求参数：{}，{}，{}".format(zbtjlr_commonSave_url,zbtjlr_commonSave_data_str,zbtjlr_commonSave_headers))
            logss.logger.info("返回结果：{}".format(zbtjlr_commonSave_res.text))

            ###断言
            response_rscode = zbtjlr_commonSave_res_json.get('rscode')
            response_result = zbtjlr_commonSave_res_json.get('result')

            ###使用pytest.assume进行断言，失败一个后，可用正常允许其它用例
            # pytest.assume(agency_res.status_code == 200)
            # pytest.assume(response_rscode == 200 )
            # pytest.assume(response_result == "请求成功")

            assert zbtjlr_commonSave_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"
        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s",e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step01)指标调减录入")
    @allure.title("指标调减录入：未送审列表")
    def testZbtjlrLoadTableDatas(self):
        zbtjlr_loadTableDatas_url = base_url + '/payfront/mp-b-budget-service/v1/budget/loadTableDatas'
        zbtjlr_loadTableDatas_headers = {"Content-Type": "application/json",
                                            "tokenid": tokenids}
        zbtjlr_loadTableDatas_data = {
            "status": "1",
            "menuguid": "FA4894120DA54CCDBD99DE8A30FD2486",
            "menuId": "FA4894120DA54CCDBD99DE8A30FD2486",
            "is_have_zero": 'false',
            "appid": "budget-total-dec",
            "roleId": "201EC9F7611B11B38E60BA5B10633BDB",
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "limit": 20,
            "querycondition": {},
            "pageNum": 1,
            "pageSize": 20,
            "sort": " agency_code,create_time desc",
            "offset": 0
        }

        # 将dict转换为str
        zbtjlr_loadTableDatas_data_str = json.dumps(zbtjlr_loadTableDatas_data)
        try:
            zbtjlr_loadTableDatas_start = time.time()  # 开始时间
            zbtjlr_loadTableDatas_res = requests.post(zbtjlr_loadTableDatas_url,
                                                         headers=zbtjlr_loadTableDatas_headers,
                                                         data=zbtjlr_loadTableDatas_data_str)
            zbtjlr_loadTableDatas_res_json = zbtjlr_loadTableDatas_res.json()
            zbtjlr_loadTableDatas_end = time.time()  # 结束时间
            zbtjlr_loadTableDatas_res_time = zbtjlr_loadTableDatas_end - zbtjlr_loadTableDatas_start
            zbtjlr_loadTableDatas_res_time_ms = zbtjlr_loadTableDatas_res_time * 1000
            print("\n")
            print(f"响应时间：{zbtjlr_loadTableDatas_res_time_ms}毫秒")
            # print(zblr_loadTableDatas_res.text)

            global zbtjlr_adj_sub_id
            zbtjlr_adj_sub_id = zbtjlr_loadTableDatas_res_json.get("data").get("rows")[0]["id"]
            print("指标id：",zbtjlr_adj_sub_id)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(zbtjlr_loadTableDatas_url, zbtjlr_loadTableDatas_data_str,
                                       zbtjlr_loadTableDatas_headers))
            logss.logger.info("返回结果：{}".format(zbtjlr_loadTableDatas_res.text))
            ###断言
            response_rscode = zbtjlr_loadTableDatas_res_json.get('rscode')
            response_result = zbtjlr_loadTableDatas_res_json.get('result')

            # pytest.assume(zblr_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert zbtjlr_loadTableDatas_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step01)指标调减录入")
    @allure.title("指标调减录入：送审")
    def testZbtjlrtjCommonoperation(self):
        zbtjlr_commonoperation_url = base_url + '/payfront/mp-b-budget-service/v1/common/budget/commonoperation'
        zbtjlr_commonoperation_headers = {"Content-Type": "application/json",
                                       "tokenid": tokenids}
        zbtjlr_commonoperation_data = {
            "data": [
                zbtjlr_adj_sub_id
            ],
            "appid": "budget-total-dec",
            "menuguid": "FA4894120DA54CCDBD99DE8A30FD2486",
            "actionType": "2",
            "glType": "0",
            "actionName": "送审",
            "action": "audit"
        }

        # 将dict转换为str
        zbtjlr_commonoperation_data_str = json.dumps(zbtjlr_commonoperation_data)
        try:
            zbtjlr_commonoperation_start = time.time()  # 开始时间
            zbtjlr_commonoperation_res = requests.post(zbtjlr_commonoperation_url,
                                                    headers=zbtjlr_commonoperation_headers,
                                                    data=zbtjlr_commonoperation_data_str)
            zbtjlr_commonoperation_res_json = zbtjlr_commonoperation_res.json()
            zbtjlr_commonoperation_end = time.time()  # 结束时间
            zbtjlr_commonoperation_res_time = zbtjlr_commonoperation_end - zbtjlr_commonoperation_start
            zbtjlr_commonoperation_res_time_ms = zbtjlr_commonoperation_res_time * 1000
            print("\n")
            print(f"响应时间：{zbtjlr_commonoperation_res_time_ms}毫秒")
            # print(zblr_commonoperation_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(zbtjlr_commonoperation_url, zbtjlr_commonoperation_data_str,
                                       zbtjlr_commonoperation_headers))
            logss.logger.info("返回结果：{}".format(zbtjlr_commonoperation_res.text))
            ###断言
            response_rscode = zbtjlr_commonoperation_res_json.get('rscode')
            response_result = zbtjlr_commonoperation_res_json.get('result')

            # pytest.assume(zblr_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert zbtjlr_commonoperation_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step02)指标调减处室审核")
    @allure.title("指标调减处室审核：审核")
    def testZbtjcsshCommonoperation(self):
        zbtjcsh_commonoperation_url = base_url + '/payfront/mp-b-budget-service/v1/common/budget/commonoperation'
        zbtjcsh_commonoperation_headers = {"Content-Type": "application/json",
                                       "tokenid": tokenids}
        zbtjcsh_commonoperation_data = {
            "data": [
                zbtjlr_adj_sub_id
            ],
            "appid": "budget-total-dec",
            "menuguid": "FA4894120DA54CCDBD99DE8A30FD2487",
            "actionType": "2",
            "glType": "0",
            "actionName": "审核",
            "action": "audit"
        }

        # 将dict转换为str
        zbtjcsh_commonoperation_data_str = json.dumps(zbtjcsh_commonoperation_data)
        try:
            zbtjcsh_commonoperation_start = time.time()  # 开始时间
            zbtjcsh_commonoperation_res = requests.post(zbtjcsh_commonoperation_url,
                                                    headers=zbtjcsh_commonoperation_headers,
                                                    data=zbtjcsh_commonoperation_data_str)
            zbtjcsh_commonoperation_res_json = zbtjcsh_commonoperation_res.json()
            zbtjcsh_commonoperation_end = time.time()  # 结束时间
            zbtjcsh_commonoperation_res_time = zbtjcsh_commonoperation_end - zbtjcsh_commonoperation_start
            zbtjcsh_commonoperation_res_time_ms = zbtjcsh_commonoperation_res_time * 1000
            print("\n")
            print(f"响应时间：{zbtjcsh_commonoperation_res_time_ms}毫秒")
            # print(ywcssh_commonoperation_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(zbtjcsh_commonoperation_url, zbtjcsh_commonoperation_data_str,
                                       zbtjcsh_commonoperation_headers))
            logss.logger.info("返回结果：{}".format(zbtjcsh_commonoperation_res.text))
            ###断言
            response_rscode = zbtjcsh_commonoperation_res_json.get('rscode')
            response_result = zbtjcsh_commonoperation_res_json.get('result')

            # pytest.assume(zblr_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert zbtjcsh_commonoperation_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step03)指标调减审核")
    @allure.title("指标调减审核：审核")
    def testZbtjshCommonoperation(self):
        zbtjsh_commonoperation_url = base_url + '/payfront/mp-b-budget-service/v1/common/budget/commonoperation'
        zbtjsh_commonoperation_headers = {"Content-Type": "application/json",
                                          "tokenid": tokenids}
        zbtjsh_commonoperation_data = {
            "data": [
                zbtjlr_adj_sub_id
            ],
            "appid": "budget-total-dec",
            "menuguid": "FA4894120DA54CCDBD99DE8A30FD2488",
            "actionType": "2",
            "glType": "0",
            "actionName": "审核",
            "action": "audit"
        }

        # 将dict转换为str
        zbtjsh_commonoperation_data_str = json.dumps(zbtjsh_commonoperation_data)
        try:
            zbtjsh_commonoperation_start = time.time()  # 开始时间
            zbtjsh_commonoperation_res = requests.post(zbtjsh_commonoperation_url,
                                                       headers=zbtjsh_commonoperation_headers,
                                                       data=zbtjsh_commonoperation_data_str)
            zbtjsh_commonoperation_res_json = zbtjsh_commonoperation_res.json()
            zbtjsh_commonoperation_end = time.time()  # 结束时间
            zbtjsh_commonoperation_res_time = zbtjsh_commonoperation_end - zbtjsh_commonoperation_start
            zbtjsh_commonoperation_res_time_ms = zbtjsh_commonoperation_res_time * 1000
            print("\n")
            print(f"响应时间：{zbtjsh_commonoperation_res_time_ms}毫秒")
            # print(zbsh_commonoperation_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(zbtjsh_commonoperation_url, zbtjsh_commonoperation_data_str,
                                       zbtjsh_commonoperation_headers))
            logss.logger.info("返回结果：{}".format(zbtjsh_commonoperation_res.text))
            ###断言
            response_rscode = zbtjsh_commonoperation_res_json.get('rscode')
            response_result = zbtjsh_commonoperation_res_json.get('result')

            # pytest.assume(zblr_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert zbtjsh_commonoperation_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step04)指标调减下达")
    @allure.title("指标调减下达：下达")
    def testZbtjxdCommonoperation(self):
        zbtjxd_commonoperation_url = base_url + '/payfront/mp-b-budget-service/v1/common/budget/commonoperation'
        zbtjxd_commonoperation_headers = {"Content-Type": "application/json",
                                          "tokenid": tokenids}
        zbtjxd_commonoperation_data = {
            "data": [
                zbtjlr_adj_sub_id
            ],
            "appid": "budget-total-dec",
            "menuguid": "FA4894120DA54CCDBD99DE8A30FD2489",
            "actionType": "2",
            "glType": "3",
            "actionName": "下达",
            "action": "audit"
        }

        # 将dict转换为str
        zbtjxd_commonoperation_data_str = json.dumps(zbtjxd_commonoperation_data)
        try:
            zbtjxd_commonoperation_start = time.time()  # 开始时间
            zbtjxd_commonoperation_res = requests.post(zbtjxd_commonoperation_url,
                                                       headers=zbtjxd_commonoperation_headers,
                                                       data=zbtjxd_commonoperation_data_str)
            zbtjxd_commonoperation_res_json = zbtjxd_commonoperation_res.json()
            zbtjxd_commonoperation_end = time.time()  # 结束时间
            zbtjxd_commonoperation_res_time = zbtjxd_commonoperation_end - zbtjxd_commonoperation_start
            zbtjxd_commonoperation_res_time_ms = zbtjxd_commonoperation_res_time * 1000
            print("\n")
            print(f"响应时间：{zbtjxd_commonoperation_res_time_ms}毫秒")
            # print(zbxd_commonoperation_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(zbtjxd_commonoperation_url, zbtjxd_commonoperation_data_str,
                                       zbtjxd_commonoperation_headers))
            logss.logger.info("返回结果：{}".format(zbtjxd_commonoperation_res.text))
            ###断言
            response_rscode = zbtjxd_commonoperation_res_json.get('rscode')
            response_result = zbtjxd_commonoperation_res_json.get('result')

            # pytest.assume(zblr_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert zbtjxd_commonoperation_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常


@allure.feature('(case03)专户指标管理')
class Testzhbudget:
    @allure.story("(step01)专户指标录入")
    @allure.title("专户指标录入：保存")
    def testZhZblrCommonSave(self):
        zhzblr_commonSave_url= base_url + '/payfront/mp-b-budget-service/v1/budget/commonSave'
        zhzblr_commonSave_headers = {"Content-Type": "application/json",
                                           "tokenid": tokenids}
        zhzblr_commonSave_data = {
            "data": [
                {
                    "amount_big_": "壹拾万元整",
                    "bgt_mof_dep_name": "农业处",
                    "acc_type_name": "社保补助",
                    "source_type_name": "年初预算",
                    "bgt_source_name": "当期拨款（支出）",
                    "exp_func_name": "行政运行",
                    "gov_bgt_eco_name": "其他支出",
                    "dir_name": "",
                    "bgt_rem_name": "",
                    "amount": 100000,
                    "version_name": "",
                    "pro_name": "219011湖北省果茶办公室专户指标下达",
                    "sup_bgt_doc_no_name": "",
                    "sup_bgt_doc_no": "",
                    "agency_name": "湖北省果茶办公室",
                    "thr_exp_name": "",
                    "pay_type_name": "实拨方式",
                    "manage_mof_dep_name": "",
                    "budget_level_name": "中央级",
                    "bgt_type_name": "预拨指标",
                    "found_type_name": "预估",
                    "is_dir_name": "",
                    "is_sub_name": "",
                    "is_mat_name": "否",
                    "is_gov_pur_name": "否",
                    "income_sort_name": "",
                    "pro_cat_name": "人员类",
                    "budget_year": "",
                    "budgetsource_year": "2024",
                    "dep_bgt_eco_name": "其他支出",
                    "bgt_temp_name": "",
                    "menu_id": "",
                    "agency_": "219011##湖北省果茶办公室##6B98F3B2EE02434479C8630869A96C60",
                    "bgt_mof_dep_": "09##农业处##0B256AD0C2B3209E7FA2AE25873896B8",
                    "budget_level_": "1##中央级##ADFCEF32115CB6261336494BB71CB66D",
                    "pro_cat_": "1##人员类##550401E14E90A32D7B39A9A6734695DE",
                    "acc_type_": "310101##社保补助##D3828BFDBF8EE69B76117257F5C6QXC8",
                    "exp_func_": "2010101##行政运行##A8C36161E5A91CFCC8E039A5F315AA92",
                    "found_type_": "12##预估##E3BB7DF43981C10F177EA6A60BBEFFC2",
                    "gov_bgt_eco_": "59999##其他支出##8FD675E6E35433727B9F95A91B89C755",
                    "dep_bgt_eco_": "39999##其他支出##CA781C52380AE0990E88447C02D3AA43",
                    "is_gov_pur_": "2##否##2",
                    "bgt_type_": "11##预拨指标##4F53297E01C18CFC47D3F942A0958939",
                    "source_type_": "1##年初预算##A494A01709D991D416528C4C38E90170",
                    "pay_type_": "2##实拨方式##E30441DFEE0353F3D238AA6ACC49BC5C",
                    "bgt_source_": "01##当期拨款（支出）##62A6C38B276AB2117EAECFC2EFD4FEFF",
                    "amount__moneySwitchinput": "100,000.00",
                    "agency__viewSort": "219011-湖北省果茶办公室",
                    "bgt_mof_dep__viewSort": "09-农业处",
                    "budget_level__viewSort": "1-中央级",
                    "pro_cat__viewSort": "1-人员类",
                    "acc_type__viewSort": "310101-社保补助",
                    "exp_func__viewSort": "2010101-行政运行",
                    "found_type__viewSort": "12-预估",
                    "gov_bgt_eco__viewSort": "59999-其他支出",
                    "dep_bgt_eco__viewSort": "39999-其他支出",
                    "is_gov_pur__viewSort": "2-否",
                    "bgt_type__viewSort": "11-预拨指标",
                    "source_type__viewSort": "1-年初预算",
                    "pay_type__viewSort": "2-实拨方式",
                    "bgt_source__viewSort": "01-当期拨款（支出）",
                    "is_gov_pur_id": 2,
                    "is_gov_pur_code": 2,
                    "gov_bgt_eco_id": "8FD675E6E35433727B9F95A91B89C755",
                    "gov_bgt_eco_code": "59999",
                    "dep_bgt_eco": "",
                    "dep_bgt_eco_id": "CA781C52380AE0990E88447C02D3AA43",
                    "dep_bgt_eco_code": "39999",
                    "pay_type_id": "E30441DFEE0353F3D238AA6ACC49BC5C",
                    "pay_type_code": "2",
                    "agency_id": "6B98F3B2EE02434479C8630869A96C60",
                    "agency_code": "219011",
                    "bgt_mof_dep_id": "0B256AD0C2B3209E7FA2AE25873896B8",
                    "bgt_mof_dep_code": "09",
                    "budget_level_id": "ADFCEF32115CB6261336494BB71CB66D",
                    "budget_level_code": "1",
                    "pro_cat_id": "550401E14E90A32D7B39A9A6734695DE",
                    "pro_cat_code": "1",
                    "acc_type_id": "D3828BFDBF8EE69B76117257F5C6QXC8",
                    "acc_type_code": "310101",
                    "exp_func_id": "A8C36161E5A91CFCC8E039A5F315AA92",
                    "exp_func_code": "2010101",
                    "found_type_id": "E3BB7DF43981C10F177EA6A60BBEFFC2",
                    "found_type_code": "12",
                    "bgt_type_id": "4F53297E01C18CFC47D3F942A0958939",
                    "bgt_type_code": "11",
                    "source_type_id": "A494A01709D991D416528C4C38E90170",
                    "source_type_code": "1",
                    "bgt_source_id": "62A6C38B276AB2117EAECFC2EFD4FEFF",
                    "bgt_source_code": "01",
                    "bgt_doc_title": "219011湖北省果茶办公室专户指标下达",
                    "doc_date": "2024-04-02",
                    "bgt_dec": "219011湖北省果茶办公室专户指标下达",
                    "cor_bgt_doc_id": "",
                    "cor_bgt_doc_code": "",
                    "cor_bgt_doc_name": "2024-0402-1534",
                    "cor_bgt_doc_no": "2024-0402-1534",
                    "cor_bgt_doc_no_id": "",
                    "cor_bgt_doc_no_code": "",
                    "cor_bgt_doc_no_name": "2024-0402-1534",
                    "voucher_code": "588",
                    "is_mat_id": "D4077C4CE6BE498E954CA18E16622BE9",
                    "is_mat_": "2-否",
                    "is_mat_code": "2"
                }
            ],
            "supType": "BUDGET_REAL_CHECKE",
            "appid": "budget-total-special",
            "menuguid": "12AF6C923D79B21197A9F604ADEEE77A",
            "actionType": "1",
            "glType": "0",
            "actionName": "新增",
            "action": "",
            "status": "1"
        }
        zhzblr_commonSave_data_str = json.dumps(zhzblr_commonSave_data)
        try:
            zhzblr_commonSave_start=time.time()   #开始时间
            zhzblr_commonSave_res = requests.post(zhzblr_commonSave_url,
                                                        headers=zhzblr_commonSave_headers,
                                                        data=zhzblr_commonSave_data_str)
            zhzblr_commonSave_res_json = zhzblr_commonSave_res.json()
            zhzblr_commonSave_end =time.time()   #结束时间
            zhzblr_commonSave_res_time= zhzblr_commonSave_end -zhzblr_commonSave_start
            zhzblr_commonSave_res_time_ms=  zhzblr_commonSave_res_time * 1000
            print("\n")
            print(f"响应时间：{zhzblr_commonSave_res_time_ms}毫秒")

            # print(zblr_commonSave_res.text)
            logss.logger.info("请求参数：{}，{}，{}".format(zhzblr_commonSave_url,zhzblr_commonSave_data_str,zhzblr_commonSave_headers))
            logss.logger.info("返回结果：{}".format(zhzblr_commonSave_res.text))

            ###断言
            response_rscode = zhzblr_commonSave_res_json.get('rscode')
            response_result = zhzblr_commonSave_res_json.get('result')

            ###使用pytest.assume进行断言，失败一个后，可用正常允许其它用例
            # pytest.assume(agency_res.status_code == 200)
            # pytest.assume(response_rscode == 200 )
            # pytest.assume(response_result == "请求成功")

            assert zhzblr_commonSave_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"
        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s",e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step01)专户指标录入")
    @allure.title("专户指标录入：额度列表")
    def testZhZblrLoadTableDatas(self):
        zhzblr_loadTableDatas_url = base_url + '/payfront/mp-b-budget-service/v1/budget/loadTableDatas'
        zhzblr_loadTableDatas_headers = {"Content-Type": "application/json",
                                            "tokenid": tokenids}
        zhzblr_loadTableDatas_data = {
            "appid": "budget-total-special",
            "menuguid": "12AF6C923D79B21197A9F604ADEEE77A",
            "querycondition": {},
            "roleId": "201EC9F7611B11B38E60BA5B10633BDB",
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "status": "1",
            "leftcondition": "",
            "sort": " agency_code,create_time desc",
            "pageNum": 1,
            "pageSize": 20
        }

        # 将dict转换为str
        zhzblr_loadTableDatas_data_str = json.dumps(zhzblr_loadTableDatas_data)
        try:
            zhzblr_loadTableDatas_start = time.time()  # 开始时间
            zhzblr_loadTableDatas_res = requests.post(zhzblr_loadTableDatas_url,
                                                         headers=zhzblr_loadTableDatas_headers,
                                                         data=zhzblr_loadTableDatas_data_str)
            zhzblr_loadTableDatas_res_json = zhzblr_loadTableDatas_res.json()
            zhzblr_loadTableDatas_end = time.time()  # 结束时间
            zhzblr_loadTableDatas_res_time = zhzblr_loadTableDatas_end - zhzblr_loadTableDatas_start
            zhzblr_loadTableDatas_res_time_ms = zhzblr_loadTableDatas_res_time * 1000
            print("\n")
            print(f"响应时间：{zhzblr_loadTableDatas_res_time_ms}毫秒")
            # print(zblr_loadTableDatas_res.text)

            global zhzblr_adj_sub_id
            zhzblr_adj_sub_id = zhzblr_loadTableDatas_res_json.get("data").get("rows")[0]["id"]
            print("指标id：",zhzblr_adj_sub_id)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(zhzblr_loadTableDatas_url, zhzblr_loadTableDatas_data_str,
                                       zhzblr_loadTableDatas_headers))
            logss.logger.info("返回结果：{}".format(zhzblr_loadTableDatas_res.text))
            ###断言
            response_rscode = zhzblr_loadTableDatas_res_json.get('rscode')
            response_result = zhzblr_loadTableDatas_res_json.get('result')

            # pytest.assume(zblr_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert zhzblr_loadTableDatas_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step01)专户指标录入")
    @allure.title("专户指标录入：送审")
    def testZhZblrCommonoperation(self):
        zhzblr_commonoperation_url = base_url + '/payfront/mp-b-budget-service/v1/common/budget/commonoperation'
        zhzblr_commonoperation_headers = {"Content-Type": "application/json",
                                       "tokenid": tokenids}
        zhzblr_commonoperation_data = {
            "data": [
                zhzblr_adj_sub_id
            ],
            "appid": "budget-total-special",
            "menuguid": "12AF6C923D79B21197A9F604ADEEE77A",
            "actionType": "2",
            "glType": "0",
            "actionName": "送审",
            "action": "audit",
            "status": "1"
        }

        # 将dict转换为str
        zhzblr_commonoperation_data_str = json.dumps(zhzblr_commonoperation_data)
        try:
            zhzblr_commonoperation_start = time.time()  # 开始时间
            zhzblr_commonoperation_res = requests.post(zhzblr_commonoperation_url,
                                                    headers=zhzblr_commonoperation_headers,
                                                    data=zhzblr_commonoperation_data_str)
            zhzblr_commonoperation_res_json = zhzblr_commonoperation_res.json()
            zhzblr_commonoperation_end = time.time()  # 结束时间
            zhzblr_commonoperation_res_time = zhzblr_commonoperation_end - zhzblr_commonoperation_start
            zhzblr_commonoperation_res_time_ms = zhzblr_commonoperation_res_time * 1000
            print("\n")
            print(f"响应时间：{zhzblr_commonoperation_res_time_ms}毫秒")
            # print(zblr_commonoperation_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(zhzblr_commonoperation_url, zhzblr_commonoperation_data_str,
                                       zhzblr_commonoperation_headers))
            logss.logger.info("返回结果：{}".format(zhzblr_commonoperation_res.text))
            ###断言
            response_rscode = zhzblr_commonoperation_res_json.get('rscode')
            response_result = zhzblr_commonoperation_res_json.get('result')

            # pytest.assume(zblr_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert zhzblr_commonoperation_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step02)专户指标处室审核")
    @allure.title("专户指标处室审核：审核")
    def testZhZbcsshCommonoperation(self):
        zhzbcssh_commonoperation_url = base_url + '/payfront/mp-b-budget-service/v1/common/budget/commonoperation'
        zhzbcssh_commonoperation_headers = {"Content-Type": "application/json",
                                       "tokenid": tokenids}
        zhzbcssh_commonoperation_data = {
            "data": [
                zhzblr_adj_sub_id
            ],
            "appid": "budget-total-special",
            "menuguid": "59151C10A980B211A5AFBFD2AACFBD6F",
            "actionType": "2",
            "glType": "0",
            "actionName": "审核",
            "action": "audit"
        }

        # 将dict转换为str
        zhzbcssh_commonoperation_data_str = json.dumps(zhzbcssh_commonoperation_data)
        try:
            zhzbcssh_commonoperation_start = time.time()  # 开始时间
            zhzbcssh_commonoperation_res = requests.post(zhzbcssh_commonoperation_url,
                                                    headers=zhzbcssh_commonoperation_headers,
                                                    data=zhzbcssh_commonoperation_data_str)
            zhzbcssh_commonoperation_res_json = zhzbcssh_commonoperation_res.json()
            zhzbcssh_commonoperation_end = time.time()  # 结束时间
            zhzbcssh_commonoperation_res_time = zhzbcssh_commonoperation_end - zhzbcssh_commonoperation_start
            zhzbcssh_commonoperation_res_time_ms = zhzbcssh_commonoperation_res_time * 1000
            print("\n")
            print(f"响应时间：{zhzbcssh_commonoperation_res_time_ms}毫秒")
            # print(ywcssh_commonoperation_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(zhzbcssh_commonoperation_url, zhzbcssh_commonoperation_data_str,
                                       zhzbcssh_commonoperation_headers))
            logss.logger.info("返回结果：{}".format(zhzbcssh_commonoperation_res.text))
            ###断言
            response_rscode = zhzbcssh_commonoperation_res_json.get('rscode')
            response_result = zhzbcssh_commonoperation_res_json.get('result')

            # pytest.assume(zblr_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert zhzbcssh_commonoperation_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step03)专户指标审核")
    @allure.title("专户指标审核：审核")
    def testZhZbshCommonoperation(self):
        zhzbsh_commonoperation_url = base_url + '/payfront/mp-b-budget-service/v1/common/budget/commonoperation'
        zhzbsh_commonoperation_headers = {"Content-Type": "application/json",
                                          "tokenid": tokenids}
        zhzbsh_commonoperation_data = {
            "data": [
                zhzblr_adj_sub_id
            ],
            "appid": "budget-total-special",
            "menuguid": "85151C10A980B211D6914E330A58FF1F",
            "actionType": "2",
            "glType": "0",
            "actionName": "审核",
            "action": "audit"
        }

        # 将dict转换为str
        zhzbsh_commonoperation_data_str = json.dumps(zhzbsh_commonoperation_data)
        try:
            zhzbsh_commonoperation_start = time.time()  # 开始时间
            zhzbsh_commonoperation_res = requests.post(zhzbsh_commonoperation_url,
                                                       headers=zhzbsh_commonoperation_headers,
                                                       data=zhzbsh_commonoperation_data_str)
            zhzbsh_commonoperation_res_json = zhzbsh_commonoperation_res.json()
            zhzbsh_commonoperation_end = time.time()  # 结束时间
            zhzbsh_commonoperation_res_time = zhzbsh_commonoperation_end - zhzbsh_commonoperation_start
            zhzbsh_commonoperation_res_time_ms = zhzbsh_commonoperation_res_time * 1000
            print("\n")
            print(f"响应时间：{zhzbsh_commonoperation_res_time_ms}毫秒")
            # print(zbsh_commonoperation_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(zhzbsh_commonoperation_url, zhzbsh_commonoperation_data_str,
                                       zhzbsh_commonoperation_headers))
            logss.logger.info("返回结果：{}".format(zhzbsh_commonoperation_res.text))
            ###断言
            response_rscode = zhzbsh_commonoperation_res_json.get('rscode')
            response_result = zhzbsh_commonoperation_res_json.get('result')

            # pytest.assume(zblr_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert zhzbsh_commonoperation_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step04)专户指标下达")
    @allure.title("专户指标下达：下达")
    def testZhZbxdCommonoperation(self):
        zhzbxd_commonoperation_url = base_url + '/payfront/mp-b-budget-service/v1/common/budget/commonoperation'
        zhzbxd_commonoperation_headers = {"Content-Type": "application/json",
                                          "tokenid": tokenids}
        zhzbxd_commonoperation_data = {
            "data": [
                zhzblr_adj_sub_id
            ],
            "appid": "budget-total-special",
            "menuguid": "8B151C10A980B211B99810E5BB71E52B",
            "actionType": "2",
            "glType": "3",
            "actionName": "下达",
            "action": "audit"
        }

        # 将dict转换为str
        zhzbxd_commonoperation_data_str = json.dumps(zhzbxd_commonoperation_data)
        try:
            zhzbxd_commonoperation_start = time.time()  # 开始时间
            zhzbxd_commonoperation_res = requests.post(zhzbxd_commonoperation_url,
                                                       headers=zhzbxd_commonoperation_headers,
                                                       data=zhzbxd_commonoperation_data_str)
            zhzbxd_commonoperation_res_json = zhzbxd_commonoperation_res.json()
            zhzbxd_commonoperation_end = time.time()  # 结束时间
            zhzbxd_commonoperation_res_time = zhzbxd_commonoperation_end - zhzbxd_commonoperation_start
            zhzbxd_commonoperation_res_time_ms = zhzbxd_commonoperation_res_time * 1000
            print("\n")
            print(f"响应时间：{zhzbxd_commonoperation_res_time_ms}毫秒")
            # print(zbxd_commonoperation_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(zhzbxd_commonoperation_url, zhzbxd_commonoperation_data_str,
                                       zhzbxd_commonoperation_headers))
            logss.logger.info("返回结果：{}".format(zhzbxd_commonoperation_res.text))
            ###断言
            response_rscode = zhzbxd_commonoperation_res_json.get('rscode')
            response_result = zhzbxd_commonoperation_res_json.get('result')

            # pytest.assume(zblr_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert zhzbxd_commonoperation_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常


@allure.feature('(case04)专户指标调减')
class Testzhbudgetless:
    @allure.story("(step01)专户指标调减录入")
    @allure.title("专户指标调减录入：保存")
    def testZhZbtjlrCommonSave(self):
        zhzbtjlr_commonSave_url= base_url + '/payfront/mp-b-budget-service/v1/budget/commonSave'
        zhzbtjlr_commonSave_headers = {"Content-Type": "application/json",
                                           "tokenid": tokenids}
        zhzbtjlr_commonSave_data = {
            "action": "",
            "actionName": "新增",
            "actionType": "1",
            "appid": "budget-special-dec",
            "glType": "1",
            "menuguid": "D8A9D66F3E7A11B2A735FEB615457DFE",
            "attachment_id": "7BB91FEBF2D44390AD5A16C3822D0865",
            "status": "1",
            "data": [
                {
                    "budget_level_code": "1",
                    "bgt_type_id": "4F53297E01C18CFC47D3F942A0958939",
                    "bgt_mof_dep": "09农业处",
                    "found_type_code": "12",
                    "agency_code": "219011",
                    "bgt_source_id": "62A6C38B276AB2117EAECFC2EFD4FEFF",
                    "canuse_amt": 100000,
                    "dis_amt": 0,
                    "found_type": "12-预估",
                    "bgt_mof_dep_name": "农业处",
                    "manage_mof_dep": "09-农业处",
                    "pay_type_code": "2",
                    "bgt_type_code": "11",
                    "fiscal_year": "2024",
                    "manage_mof_dep_id": "0B256AD0C2B3209E7FA2AE25873896B8",
                    "gov_bgt_eco": "59999-其他支出",
                    "is_more_pay": "2",
                    "direct_flag_name": "其它",
                    "dep_bgt_eco_id": "CA781C52380AE0990E88447C02D3AA43",
                    "use_amt": 0,
                    "mof_div_code": "420000000",
                    "agency_id": "6B98F3B2EE02434479C8630869A96C60",
                    "source_type": "1-年初预算",
                    "bgt_mof_dep_id": "0B256AD0C2B3209E7FA2AE25873896B8",
                    "version": "2024-04-02 16:10:04",
                    "budget_level": "1-中央级",
                    "is_gov_pur_id": "2",
                    "zdzjjqpt_name": "否",
                    "todo_node": "8B151C10A980B211B99810E5BB71E52B",
                    "use_amt1": 0,
                    "is_mat_id": "D4077C4CE6BE498E954CA18E16622BE9",
                    "exp_func_name": "行政运行",
                    "pro_name": "219011湖北省果茶办公室专户指标下达",
                    "found_type_id": "E3BB7DF43981C10F177EA6A60BBEFFC2",
                    "aviamt": "100000",
                    "fund_type": "-",
                    "voucher_no": "指标录入（专户）单",
                    "is_mat_code": "2",
                    "gov_bgt_eco_code": "59999",
                    "canuseamt": "100000",
                    "update_time": "2024-04-02 16:10:04",
                    "bgt_source_code": "01",
                    "bkqjsx": "01-当期拨款（支出）",
                    "pay_type_id": "E30441DFEE0353F3D238AA6ACC49BC5C",
                    "exp_func_code": "2010101",
                    "budget_type": "2",
                    "acc_type_code": "310101",
                    "agency_name": "湖北省果茶办公室",
                    "agency": "219011-湖北省果茶办公室",
                    "bat_num": "0",
                    "work_flow_id": "budget-total-special",
                    "cur_amt": 100000,
                    "bgt_mof_dep_code": "09",
                    "cor_bgt_doc_no": "2024-0402-1534",
                    "bkqjsx_code": "01",
                    "pro_cat_code": "1",
                    "pro_id": "AA87D4ED2156408AB54151908AE3E99B",
                    "bgt_type_name": "预拨指标",
                    "doc_date": "2024-04-02 00:00:00",
                    "pay_type_name": "实拨方式",
                    "zblynd_name": "2024",
                    "manage_mof_dep_name": "农业处",
                    "acc_type": "310101-社保补助",
                    "dep_bgt_eco_name": "其他支出",
                    "todo_name": "指标下达(专户)",
                    "source_type_id": "A494A01709D991D416528C4C38E90170",
                    "voucher_code": "588",
                    "is_track": 1,
                    "done_node": "85151C10A980B211D6914E330A58FF1F",
                    "zdzjjqpt_code": "2",
                    "is_not_control_pay": "2",
                    "clear_amt": 0,
                    "exp_func_id": "A8C36161E5A91CFCC8E039A5F315AA92",
                    "bgt_type": "11-预拨指标",
                    "bkqjsx_name": "当期拨款（支出）",
                    "plan_caliber_id": "e5bd68b426f0925e47793a50e50cdd9a",
                    "bgt_id": "C07D4D341BD64AE390DD7E3FEAF0B73D",
                    "pay_caliber_id": "C07D4D341BD64AE390DD7E3FEAF0B73D",
                    "xpay_amt": 0,
                    "gov_bgt_eco_id": "8FD675E6E35433727B9F95A91B89C755",
                    "pay_amt": 0,
                    "create_time": "2024-04-02 16:10:04",
                    "direct_flag_code": "09",
                    "is_adjust": 1,
                    "found_type_name": "预估",
                    "budget_level_name": "中央级",
                    "threesafe_symbolcat": "000-非“三保”支出",
                    "budget_level_id": "ADFCEF32115CB6261336494BB71CB66D",
                    "pro": "42000024219P007000059-219011湖北省果茶办公室专户指标下达",
                    "is_manager": "2",
                    "is_gov_pur_code": "2",
                    "dep_bgt_eco": "39999其他支出",
                    "creater": "1F0795D7E8724F998426100EB01D6195",
                    "acc_type_id": "D3828BFDBF8EE69B76117257F5C6QXC8",
                    "bgt_doc_title": "219011湖北省果茶办公室专户指标下达",
                    "threesafe_symbolcat_name": "非“三保”支出",
                    "origin_model_code": "2",
                    "bgt_source_name": "当期拨款（支出）",
                    "adj_date": "2024-04-02 15:37:05",
                    "useamt": "0",
                    "source_type_name": "年初预算",
                    "is_contrlbyplan": "2",
                    "acc_type_name": "社保补助",
                    "updater": "1F0795D7E8724F998426100EB01D6195",
                    "pro_cat": "1-人员类",
                    "bgt_exe_flag": "1",
                    "is_mat_name": "否",
                    "is_deleted": 2,
                    "source_type_code": "1",
                    "last_user": "1F0795D7E8724F998426100EB01D6195",
                    "manage_mof_dep_code": "09",
                    "is_gov_pur_name": "否",
                    "threesafe_symbolcat_code": "000",
                    "pro_cat_name": "人员类",
                    "once_done_node": "59151C10A980B211A5AFBFD2AACFBD6F,12AF6C923D79B21197A9F604ADEEE77A",
                    "pay_type": "2-实拨方式",
                    "pro_cat_id": "550401E14E90A32D7B39A9A6734695DE",
                    "zblynd_code": "2024",
                    "pro_code": "42000024219P007000059",
                    "amount": -100,
                    "is_gov_pur": "2-否",
                    "bgt_dec": "219011湖北省果茶办公室专户指标下达",
                    "is_end": "1",
                    "lzfs": "-",
                    "exp_func": "2010101-行政运行",
                    "dep_bgt_eco_code": "39999",
                    "gov_bgt_eco_name": "其他支出",
                    "pagehelper_row_id": 1,
                    "statusCode": "9",
                    "progress": "0%",
                    "sum_id": "",
                    "create_user": "",
                    "_XID": "row_994",
                    "acc_type_name__viewSort": "社保补助",
                    "acc_type_code__viewSort": "310101",
                    "pro_code__viewSort": "42000024219P007000059",
                    "pro_cat_code__viewSort": "1",
                    "pro_cat_name__viewSort": "人员类",
                    "aviamt__viewSort": "100,000.00",
                    "useamt__viewSort": "0.00",
                    "canuseamt__viewSort": "100,000.00",
                    "sum_id__viewSort": "",
                    "dep_bgt_eco__viewSort": "39999其他支出",
                    "bgt_doc_title__viewSort": "219011湖北省果茶办公室专户指标下达",
                    "cor_bgt_doc_no__viewSort": "2024-0402-1534",
                    "source_type_code__viewSort": "1",
                    "source_type_name__viewSort": "年初预算",
                    "found_type_code__viewSort": "12",
                    "found_type_name__viewSort": "预估",
                    "bgt_dec__viewSort": "219011湖北省果茶办公室专户指标下达",
                    "bgt_type_code__viewSort": "11",
                    "bgt_type_name__viewSort": "预拨指标",
                    "bgt_source_code__viewSort": "01",
                    "bgt_source_name__viewSort": "当期拨款（支出）",
                    "zblynd_code__viewSort": "2024",
                    "fiscal_year__viewSort": "2024",
                    "budget_level_name__viewSort": "中央级",
                    "create_user__viewSort": ""
                }
            ]
        }
        zhzbtjlr_commonSave_data_str = json.dumps(zhzbtjlr_commonSave_data)
        try:
            zhzbtjlr_commonSave_start=time.time()   #开始时间
            zhzbtjlr_commonSave_res = requests.post(zhzbtjlr_commonSave_url,
                                                        headers=zhzbtjlr_commonSave_headers,
                                                        data=zhzbtjlr_commonSave_data_str)
            zhzbtjlr_commonSave_res_json = zhzbtjlr_commonSave_res.json()
            zhzbtjlr_commonSave_end =time.time()   #结束时间
            zhzbtjlr_commonSave_res_time= zhzbtjlr_commonSave_end -zhzbtjlr_commonSave_start
            zhzbtjlr_commonSave_res_time_ms=  zhzbtjlr_commonSave_res_time * 1000
            print("\n")
            print(f"响应时间：{zhzbtjlr_commonSave_res_time_ms}毫秒")

            # print(zblr_commonSave_res.text)
            logss.logger.info("请求参数：{}，{}，{}".format(zhzbtjlr_commonSave_url,zhzbtjlr_commonSave_data_str,zhzbtjlr_commonSave_headers))
            logss.logger.info("返回结果：{}".format(zhzbtjlr_commonSave_res.text))

            ###断言
            response_rscode = zhzbtjlr_commonSave_res_json.get('rscode')
            response_result = zhzbtjlr_commonSave_res_json.get('result')

            ###使用pytest.assume进行断言，失败一个后，可用正常允许其它用例
            # pytest.assume(agency_res.status_code == 200)
            # pytest.assume(response_rscode == 200 )
            # pytest.assume(response_result == "请求成功")

            assert zhzbtjlr_commonSave_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"
        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s",e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step01)专户指标调减录入")
    @allure.title("专户指标调减录入：未送审列表")
    def testZhZbtjlrLoadTableDatas(self):
        zhzbtjlr_loadTableDatas_url = base_url + '/payfront/mp-b-budget-service/v1/budget/loadTableDatas'
        zhzbtjlr_loadTableDatas_headers = {"Content-Type": "application/json",
                                            "tokenid": tokenids}
        zhzbtjlr_loadTableDatas_data = {
            "status": "1",
            "menuguid": "D8A9D66F3E7A11B2A735FEB615457DFE",
            "menuId": "D8A9D66F3E7A11B2A735FEB615457DFE",
            "is_have_zero": 'false',
            "appid": "budget-special-dec",
            "roleId": "201EC9F7611B11B38E60BA5B10633BDB",
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "offset": 0,
            "limit": 20,
            "accountClsId": "334474CAEF1B11B28B15C4A0215C7EBB",
            "querycondition": {},
            "pageNum": 1,
            "pageSize": 20,
            "sort": " agency_code,create_time desc"
        }

        # 将dict转换为str
        zhzbtjlr_loadTableDatas_data_str = json.dumps(zhzbtjlr_loadTableDatas_data)
        try:
            zhzbtjlr_loadTableDatas_start = time.time()  # 开始时间
            zhzbtjlr_loadTableDatas_res = requests.post(zhzbtjlr_loadTableDatas_url,
                                                         headers=zhzbtjlr_loadTableDatas_headers,
                                                         data=zhzbtjlr_loadTableDatas_data_str)
            zhzbtjlr_loadTableDatas_res_json = zhzbtjlr_loadTableDatas_res.json()
            zhzbtjlr_loadTableDatas_end = time.time()  # 结束时间
            zhzbtjlr_loadTableDatas_res_time = zhzbtjlr_loadTableDatas_end - zhzbtjlr_loadTableDatas_start
            zhzbtjlr_loadTableDatas_res_time_ms = zhzbtjlr_loadTableDatas_res_time * 1000
            print("\n")
            print(f"响应时间：{zhzbtjlr_loadTableDatas_res_time_ms}毫秒")
            # print(zblr_loadTableDatas_res.text)

            global zhzbtjlr_adj_sub_id
            zhzbtjlr_adj_sub_id = zhzbtjlr_loadTableDatas_res_json.get("data").get("rows")[0]["id"]
            print("指标id：",zbtjlr_adj_sub_id)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(zhzbtjlr_loadTableDatas_url, zhzbtjlr_loadTableDatas_data_str,
                                       zhzbtjlr_loadTableDatas_headers))
            logss.logger.info("返回结果：{}".format(zhzbtjlr_loadTableDatas_res.text))
            ###断言
            response_rscode = zhzbtjlr_loadTableDatas_res_json.get('rscode')
            response_result = zhzbtjlr_loadTableDatas_res_json.get('result')

            # pytest.assume(zblr_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert zhzbtjlr_loadTableDatas_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step01)专户指标调减录入")
    @allure.title("专户指标调减录入：送审")
    def testZhZbtjlrtjCommonoperation(self):
        zhzbtjlr_commonoperation_url = base_url + '/payfront/mp-b-budget-service/v1/common/budget/commonoperation'
        zhzbtjlr_commonoperation_headers = {"Content-Type": "application/json",
                                       "tokenid": tokenids}
        zhzbtjlr_commonoperation_data = {
            "data": [
                zhzbtjlr_adj_sub_id
            ],
            "appid": "budget-special-dec",
            "menuguid": "D8A9D66F3E7A11B2A735FEB615457DFE",
            "actionType": "2",
            "glType": "0",
            "actionName": "送审",
            "action": "audit"
        }

        # 将dict转换为str
        zhzbtjlr_commonoperation_data_str = json.dumps(zhzbtjlr_commonoperation_data)
        try:
            zhzbtjlr_commonoperation_start = time.time()  # 开始时间
            zhzbtjlr_commonoperation_res = requests.post(zhzbtjlr_commonoperation_url,
                                                    headers=zhzbtjlr_commonoperation_headers,
                                                    data=zhzbtjlr_commonoperation_data_str)
            zhzbtjlr_commonoperation_res_json = zhzbtjlr_commonoperation_res.json()
            zhzbtjlr_commonoperation_end = time.time()  # 结束时间
            zhzbtjlr_commonoperation_res_time = zhzbtjlr_commonoperation_end - zhzbtjlr_commonoperation_start
            zhzbtjlr_commonoperation_res_time_ms = zhzbtjlr_commonoperation_res_time * 1000
            print("\n")
            print(f"响应时间：{zhzbtjlr_commonoperation_res_time_ms}毫秒")
            # print(zblr_commonoperation_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(zhzbtjlr_commonoperation_url, zhzbtjlr_commonoperation_data_str,
                                       zhzbtjlr_commonoperation_headers))
            logss.logger.info("返回结果：{}".format(zhzbtjlr_commonoperation_res.text))
            ###断言
            response_rscode = zhzbtjlr_commonoperation_res_json.get('rscode')
            response_result = zhzbtjlr_commonoperation_res_json.get('result')

            # pytest.assume(zblr_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert zhzbtjlr_commonoperation_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step02)专户指标调减处室审核")
    @allure.title("专户指标调减处室审核：审核")
    def testZhZbtjcsshCommonoperation(self):
        zhzbtjcssh_commonoperation_url = base_url + '/payfront/mp-b-budget-service/v1/common/budget/commonoperation'
        zhzbtjcssh_commonoperation_headers = {"Content-Type": "application/json",
                                       "tokenid": tokenids}
        zhzbtjcssh_commonoperation_data = {
            "data": [
                zhzbtjlr_adj_sub_id
            ],
            "appid": "budget-special-dec",
            "menuguid": "2C68F5243E7A11B2A44F024D1CAD7FF5",
            "actionType": "2",
            "glType": "0",
            "actionName": "审核",
            "action": "audit"
        }

        # 将dict转换为str
        zhzbtjcssh_commonoperation_data_str = json.dumps(zhzbtjcssh_commonoperation_data)
        try:
            zhzbtjcssh_commonoperation_start = time.time()  # 开始时间
            zhzbtjcssh_commonoperation_res = requests.post(zhzbtjcssh_commonoperation_url,
                                                    headers=zhzbtjcssh_commonoperation_headers,
                                                    data=zhzbtjcssh_commonoperation_data_str)
            zhzbtjcssh_commonoperation_res_json = zhzbtjcssh_commonoperation_res.json()
            zhzbtjcssh_commonoperation_end = time.time()  # 结束时间
            zhzbtjcssh_commonoperation_res_time = zhzbtjcssh_commonoperation_end - zhzbtjcssh_commonoperation_start
            zhzbtjcssh_commonoperation_res_time_ms = zhzbtjcssh_commonoperation_res_time * 1000
            print("\n")
            print(f"响应时间：{zhzbtjcssh_commonoperation_res_time_ms}毫秒")
            # print(ywcssh_commonoperation_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(zhzbtjcssh_commonoperation_url, zhzbtjcssh_commonoperation_data_str,
                                       zhzbtjcssh_commonoperation_headers))
            logss.logger.info("返回结果：{}".format(zhzbtjcssh_commonoperation_res.text))
            ###断言
            response_rscode = zhzbtjcssh_commonoperation_res_json.get('rscode')
            response_result = zhzbtjcssh_commonoperation_res_json.get('result')

            # pytest.assume(zblr_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert zhzbtjcssh_commonoperation_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step03)专户指标调减审核")
    @allure.title("专户指标调减审核：审核")
    def testZhZbtjshCommonoperation(self):
        zhzbtjsh_commonoperation_url = base_url + '/payfront/mp-b-budget-service/v1/common/budget/commonoperation'
        zhzbtjsh_commonoperation_headers = {"Content-Type": "application/json",
                                          "tokenid": tokenids}
        zhzbtjsh_commonoperation_data = {
            "data": [
                zhzbtjlr_adj_sub_id
            ],
            "appid": "budget-special-dec",
            "menuguid": "32C5137F3E7B11B293A16BD9B16A5D2D",
            "actionType": "2",
            "glType": "0",
            "actionName": "审核",
            "action": "audit"
        }

        # 将dict转换为str
        zhzbtjsh_commonoperation_data_str = json.dumps(zhzbtjsh_commonoperation_data)
        try:
            zhzbtjsh_commonoperation_start = time.time()  # 开始时间
            zhzbtjsh_commonoperation_res = requests.post(zhzbtjsh_commonoperation_url,
                                                       headers=zhzbtjsh_commonoperation_headers,
                                                       data=zhzbtjsh_commonoperation_data_str)
            zhzbtjsh_commonoperation_res_json = zhzbtjsh_commonoperation_res.json()
            zhzbtjsh_commonoperation_end = time.time()  # 结束时间
            zhzbtjsh_commonoperation_res_time = zhzbtjsh_commonoperation_end - zhzbtjsh_commonoperation_start
            zhzbtjsh_commonoperation_res_time_ms = zhzbtjsh_commonoperation_res_time * 1000
            print("\n")
            print(f"响应时间：{zhzbtjsh_commonoperation_res_time_ms}毫秒")
            # print(zbsh_commonoperation_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(zhzbtjsh_commonoperation_url, zhzbtjsh_commonoperation_data_str,
                                       zhzbtjsh_commonoperation_headers))
            logss.logger.info("返回结果：{}".format(zhzbtjsh_commonoperation_res.text))
            ###断言
            response_rscode = zhzbtjsh_commonoperation_res_json.get('rscode')
            response_result = zhzbtjsh_commonoperation_res_json.get('result')

            # pytest.assume(zblr_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert zhzbtjsh_commonoperation_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step04)专户指标调减下达")
    @allure.title("专户指标调减下达：下达")
    def testZhZbtjxdCommonoperation(self):
        zhzbtjxd_commonoperation_url = base_url + '/payfront/mp-b-budget-service/v1/common/budget/commonoperation'
        zhzbtjxd_commonoperation_headers = {"Content-Type": "application/json",
                                          "tokenid": tokenids}
        zhzbtjxd_commonoperation_data = {
            "data": [
                zhzbtjlr_adj_sub_id
            ],
            "appid": "budget-special-dec",
            "menuguid": "969F1AE73E7B11B2B64F8FA7927257FE",
            "actionType": "2",
            "glType": "3",
            "actionName": "下达",
            "action": "audit"
        }

        # 将dict转换为str
        zhzbtjxd_commonoperation_data_str = json.dumps(zhzbtjxd_commonoperation_data)
        try:
            zhzbtjxd_commonoperation_start = time.time()  # 开始时间
            zhzbtjxd_commonoperation_res = requests.post(zhzbtjxd_commonoperation_url,
                                                       headers=zhzbtjxd_commonoperation_headers,
                                                       data=zhzbtjxd_commonoperation_data_str)
            zhzbtjxd_commonoperation_res_json = zhzbtjxd_commonoperation_res.json()
            zbtjxd_commonoperation_end = time.time()  # 结束时间
            zbtjxd_commonoperation_res_time = zbtjxd_commonoperation_end - zhzbtjxd_commonoperation_start
            zbtjxd_commonoperation_res_time_ms = zbtjxd_commonoperation_res_time * 1000
            print("\n")
            print(f"响应时间：{zbtjxd_commonoperation_res_time_ms}毫秒")
            # print(zbxd_commonoperation_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(zhzbtjxd_commonoperation_url, zhzbtjxd_commonoperation_data_str,
                                       zhzbtjxd_commonoperation_headers))
            logss.logger.info("返回结果：{}".format(zhzbtjxd_commonoperation_res.text))
            ###断言
            response_rscode = zhzbtjxd_commonoperation_res_json.get('rscode')
            response_result = zhzbtjxd_commonoperation_res_json.get('result')

            # pytest.assume(zblr_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert zhzbtjxd_commonoperation_res.status_code == 200
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