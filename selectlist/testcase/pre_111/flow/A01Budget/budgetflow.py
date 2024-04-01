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


@allure.feature('指标管理')
class Testbudget:
    @allure.story("指标管理")
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

    @allure.story("指标管理")
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

            print(zblr_loadTableDatas_res.text)
            adj_sub_id = zblr_loadTableDatas_res_json.get("data").get("rows")[0]["id"]
            print("指标id：",adj_sub_id)
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