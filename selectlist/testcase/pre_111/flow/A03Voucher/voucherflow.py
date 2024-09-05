# coding=utf-8
import time
import allure
import pytest
import requests
import json
import sys
import os

import xmltodict

sys.path.append("E:/pypro/APItest2/selectpost/common")
from common.header_token import *
from logs.loggerController import logs


logss = logs()
tokenids = YamlHander().read_yaml()
base_url ='http://10.17.8.111'


@allure.feature('(case01)国库集中支付')
class TestVoucher:
    @allure.story("(step01)支付申请录入(单位)")
    @allure.title("支付申请录入(单位)：保存")
    def testZfsqlrdwInsert(self):
        zfsqlrdw_insert_url= base_url + '/payfront/pay-voucher-service/v3/payvoucherbill/front/action/insert'
        zfsqlrdw_insert_headers = {"Content-Type": "application/json",
                                           "tokenid": tokenids}
        zfsqlrdw_insert_data = {
            "appId": "pay_voucher",
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "menuId": "2C27DDF8B6A7688077BA81F9F37EE5EB",
            "actionType": "1",
            "actionName": "新增",
            "glType": "1",
            "params": {
                "accountClsId": "4E72561AB3CD477EB8DFD51813EC2FB2",
                "accountType": "63",
                "isFinancial": "0",
                "batchUserEleType": "1",
                "enableRelation": "false",
                "relations": "gov_bgt_eco;dep_bgt_eco;set_mode;fund_traobj_type",
                "showContact": "false",
                "contactType": "0"
            },
            "datas": [
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
                    "zdzjjqpt": "2-否",
                    "sumguid": "1775326015709990912",
                    "manage_mof_dep": "09-农业处",
                    "pay_type_code": "1",
                    "bgt_type_code": "11",
                    "fiscal_year": "2024",
                    "manage_mof_dep_id": "0B256AD0C2B3209E7FA2AE25873896B8",
                    "gov_bgt_eco": "",
                    "is_more_pay": "2",
                    "dep_bgt_eco_id": "F2684D4AE3086DBDA207A71B269729D0",
                    "planuseamt": 30,
                    "mof_div_code": "420000000",
                    "agency_id": "6B98F3B2EE02434479C8630869A96C60",
                    "direct_flag": "09-其它",
                    "source_type": "1-年初预算",
                    "bgt_mof_dep_id": "0B256AD0C2B3209E7FA2AE25873896B8",
                    "version": "2024-04-02 11:05:43",
                    "budget_level": "1-中央级",
                    "is_gov_pur_id": "2",
                    "zdzjjqpt_name": "否",
                    "todo_node": "BB39585CD1574D94B7D3DB7553930004",
                    "is_mat_id": "2",
                    "exp_func_name": "行政运行",
                    "pro_name": "219011指标管理1512",
                    "lzfs_code": "001",
                    "found_type_id": "E3BB7DF43981C10F177EA6A60BBEFFC2",
                    "aviamt": 100000,
                    "fund_type": "11111-经费拨款补助",
                    "is_mat_code": "2",
                    "gov_bgt_eco_code": "50101",
                    "canuseamt": 100000,
                    "update_time": "2024-04-02 11:05:43",
                    "bgt_source_code": "01",
                    "ccid": "03e09993b7636e52f8f7bb67a746552a",
                    "pay_type_id": "24B2435F18D2B38581D2845E32D14773",
                    "exp_func_code": "2010101",
                    "agency_name": "湖北省果茶办公室",
                    "agency": "219011-湖北省果茶办公室",
                    "bat_num": "0",
                    "frozenamt": 0,
                    "work_flow_id": "budget-total",
                    "fund_type_name": "经费拨款补助",
                    "cur_amt": 0,
                    "bgt_mof_dep_code": "09",
                    "cor_bgt_doc_no": "2024-0401-1512",
                    "pro_cat_code": "1",
                    "pro_id": "A42E27B4640B4234A48DEC69CA3E3156",
                    "bgt_type_name": "预拨指标",
                    "doc_date": "2024-04-01 00:00:00",
                    "pay_type_name": "国库集中支付",
                    "manage_mof_dep_name": "农业处",
                    "dep_bgt_eco_name": "基本工资",
                    "todo_name": "指标下达",
                    "fund_type_id": "DE1C8E16759F474C2D92CBBFB7BA6385",
                    "source_type_id": "A494A01709D991D416528C4C38E90170",
                    "voucher_code": "141001",
                    "is_track": 1,
                    "done_node": "BB39585CD1574D94B7D3DB7553930003",
                    "zdzjjqpt_code": "2",
                    "is_not_control_pay": "2",
                    "clear_amt": 0,
                    "exp_func_id": "A8C36161E5A91CFCC8E039A5F315AA92",
                    "plan_caliber_id": "d90f49adb78db8343547023025efcf4d",
                    "bgt_id": "71617A68FBD7407290063B7B89B221AF",
                    "pay_caliber_id": "71617A68FBD7407290063B7B89B221AF",
                    "xpay_amt": 0,
                    "gov_bgt_eco_id": "543B56A3BE5FC85C7E389E6CFC4A3AB2",
                    "pay_amt": 2,
                    "create_time": "2024-04-02 11:05:43",
                    "is_adjust": 1,
                    "found_type_name": "预估",
                    "budget_level_name": "中央级",
                    "planaviamt": 2000,
                    "threesafe_symbolcat": "000-非“三保”支出",
                    "budget_level_id": "ADFCEF32115CB6261336494BB71CB66D",
                    "pro": "42000024219P007000051-219011指标管理1512",
                    "is_manager": "2",
                    "is_gov_pur_code": "2",
                    "dep_bgt_eco": "F2684D4AE3086DBDA207A71B269729D0##30101##基本工资",
                    "creater": "1F0795D7E8724F998426100EB01D6195",
                    "bgt_doc_title": "219011指标管理1512",
                    "threesafe_symbolcat_name": "非“三保”支出",
                    "fund_type_code": "11111",
                    "origin_model_code": "2",
                    "bgt_source_name": "当期拨款（支出）",
                    "adj_date": "2024-04-02 11:02:54",
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
                    "pro_code": "42000024219P007000051",
                    "amount": 100000,
                    "bgt_dec": "219011指标管理1512",
                    "is_end": "1",
                    "exp_func": "2010101-行政运行",
                    "dep_bgt_eco_code": "30101",
                    "gov_bgt_eco_name": "工资奖金津补贴",
                    "plancanuseamt": 1970,
                    "agency_acct_name": "",
                    "agency_acct_no": "",
                    "pay_bank_name": "中国工商银行武汉市武珞路支行",
                    "social_credit_code": "",
                    "pay_acct_name": "湖北省果茶办公室",
                    "payee_acct_name": "湖北鼎力恒建设有限公司",
                    "pay_acct_no": "3202006009200009203",
                    "payee_acct_no": "3202010619100148797",
                    "pay_acct_bank_name": "中国工商银行武汉市武珞路支行",
                    "payee_acct_bank_name": "工商银行武汉空港支行",
                    "payee_acct_code": "",
                    "fund_traobj_type": "576DE01E1B3326464E6B75DE8984BD2C##11##与部门外同级政府单位",
                    "fund_traobj_type_id": "576DE01E1B3326464E6B75DE8984BD2C",
                    "fund_traobj_type_code": "11",
                    "fund_traobj_type_name": "与部门外同级政府单位",
                    "internal_dep": "4C1D9565CB9D48948F89E4784AE804E7##11##办公室",
                    "internal_dep_id": "4C1D9565CB9D48948F89E4784AE804E7",
                    "internal_dep_code": "11",
                    "internal_dep_name": "办公室",
                    "set_mode": "F522AB99C43B9A2A4DD4C30CB75B50C7##1##电子转账支付",
                    "set_mode_id": "F522AB99C43B9A2A4DD4C30CB75B50C7",
                    "set_mode_code": "1",
                    "set_mode_name": "电子转账支付",
                    "use_des": "支付流程",
                    "pay_app_amt": 2,
                    "pay_app_amt_big": "贰元整",
                    "contract_no": "",
                    "acc_type_id": "D3828BFDBF8EE69B76117257F5C6QXC3",
                    "acc_type_code": "21",
                    "acc_type_name": "单位零余额账户",
                    "is_advancefunds": "2",
                    "pay_acct_id": "658BB562BD4B4024B05538BAB938F48B",
                    "pay_acct_code": "219011",
                    "pay_bank_id": "3FD7C114D95647F7AD3FB31568EA0979",
                    "pay_bank_code": "102521000335",
                    "attachment_id": "",
                    "plan_balance_id": "1775326015709990912",
                    "fileList": [],
                    "ext": {
                        "is_advancefunds": "2",
                        "is_pural": "0"
                    }
                }
            ]
        }
        zfsqlrdw_insert_data_str = json.dumps(zfsqlrdw_insert_data)
        try:
            zfsqlrdw_insert_start=time.time()   #开始时间
            zfsqlrdw_insert_res = requests.post(zfsqlrdw_insert_url,
                                                        headers=zfsqlrdw_insert_headers,
                                                        data=zfsqlrdw_insert_data_str)
            zfsqlrdw_insert_res_json = zfsqlrdw_insert_res.json()
            zfsqlrdw_insert_end =time.time()   #结束时间
            zfsqlrdw_insert_res_time= zfsqlrdw_insert_end -zfsqlrdw_insert_start
            zfsqlrdw_insert_res_time_ms=  zfsqlrdw_insert_res_time * 1000
            print("\n")
            print(f"响应时间：{zfsqlrdw_insert_res_time_ms}毫秒")

            # print(zfsqlrdw_insert_res.text)
            logss.logger.info("请求参数：{}，{}，{}".format(zfsqlrdw_insert_url,zfsqlrdw_insert_data_str,zfsqlrdw_insert_headers))
            logss.logger.info("返回结果：{}".format(zfsqlrdw_insert_res.text))

            ###断言
            response_rscode = zfsqlrdw_insert_res_json.get('rscode')
            response_result = zfsqlrdw_insert_res_json.get('result')

            ###使用pytest.assume进行断言，失败一个后，可用正常允许其它用例
            # pytest.assume(agency_res.status_code == 200)
            # pytest.assume(response_rscode == 200 )
            # pytest.assume(response_result == "请求成功")

            assert zfsqlrdw_insert_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"
        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s",e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step01)支付申请录入(单位)")
    @allure.title("支付申请录入(单位)：未送审列表")
    def testZfsqlrdwLoadTableDatas(self):
        zfsqlrdw_loadTableDatas_url = base_url + '/payfront/pay-voucher-service/v3/payvoucherbill/loadtabledatas'
        zfsqlrdw_loadTableDatas_headers = {"Content-Type": "application/json",
                                            "tokenid": tokenids}
        zfsqlrdw_loadTableDatas_data = {
            "statusCode": "1",
            "menuId": "2C27DDF8B6A7688077BA81F9F37EE5EB",
            "leftTreeCode": "",
            "isHaveZero": "0",
            "appId": "pay_voucher",
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "roleId": "201EC9F7611B11B38E60BA5B10633BDB",
            "params": {
                "accountClsId": "4E72561AB3CD477EB8DFD51813EC2FB2",
                "accountType": "63",
                "isFinancial": "0",
                "batchUserEleType": "1",
                "enableRelation": "false",
                "relations": "gov_bgt_eco;dep_bgt_eco;set_mode;fund_traobj_type",
                "showContact": "false",
                "contactType": "0"
            },
            "pageNum": 1,
            "pageSize": 1000000,
            "sort": "fi_order asc,create_time desc,pay_cert_no desc",
            "condition": {}
        }

        # 将dict转换为str
        zfsqlrdw_loadTableDatas_data_str = json.dumps(zfsqlrdw_loadTableDatas_data)
        try:
            zfsqlrdw_loadTableDatas_start = time.time()  # 开始时间
            zfsqlrdw_loadTableDatas_res = requests.post(zfsqlrdw_loadTableDatas_url,
                                                         headers=zfsqlrdw_loadTableDatas_headers,
                                                         data=zfsqlrdw_loadTableDatas_data_str)
            zfsqlrdw_loadTableDatas_res_json = zfsqlrdw_loadTableDatas_res.json()
            zfsqlrdw_loadTableDatas_end = time.time()  # 结束时间
            zfsqlrdw_loadTableDatas_res_time = zfsqlrdw_loadTableDatas_end - zfsqlrdw_loadTableDatas_start
            zfsqlrdw_loadTableDatas_res_time_ms = zfsqlrdw_loadTableDatas_res_time * 1000
            print("\n")
            print(f"响应时间：{zfsqlrdw_loadTableDatas_res_time_ms}毫秒")
            # print(zfsqlrdw_loadTableDatas_res.text)

            global zfsqlrdw_id
            zfsqlrdw_id = zfsqlrdw_loadTableDatas_res_json.get("data").get("rows")[0]["id"]
            print("支付数据id：", zfsqlrdw_id)

            global zfsqlrdw_pay_cert_id
            zfsqlrdw_pay_cert_id = zfsqlrdw_loadTableDatas_res_json.get("data").get("rows")[0]["pay_cert_id"]
            print("支付凭证id：",zfsqlrdw_pay_cert_id)

            global zfsqlrdw_pay_cert_no
            zfsqlrdw_pay_cert_no = zfsqlrdw_loadTableDatas_res_json.get("data").get("rows")[0]["pay_cert_no"]
            print("支付凭证号：", zfsqlrdw_pay_cert_no)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(zfsqlrdw_loadTableDatas_url, zfsqlrdw_loadTableDatas_data_str,
                                       zfsqlrdw_loadTableDatas_headers))
            logss.logger.info("返回结果：{}".format(zfsqlrdw_loadTableDatas_res.text))
            ###断言
            response_rscode = zfsqlrdw_loadTableDatas_res_json.get('rscode')
            response_result = zfsqlrdw_loadTableDatas_res_json.get('result')

            # pytest.assume(zfsqlrdw_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert zfsqlrdw_loadTableDatas_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step01)支付申请录入(单位)")
    @allure.title("支付申请录入(单位)：送审")
    def testZfsqlrdwAuditbycheck(self):
        zfsqlrdw_auditbycheck_url = base_url + '/payfront/pay-voucher-service/v3/payvoucherbill/front/action/auditbycheck'
        zfsqlrdw_auditbycheck_headers = {"Content-Type": "application/json",
                                       "tokenid": tokenids}
        zfsqlrdw_auditbycheck_data = {
            "actionName": "送审",
            "appId": "pay_voucher",
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "menuId": "2C27DDF8B6A7688077BA81F9F37EE5EB",
            "actionType": "2",
            "glType": "0",
            "ids": [
                zfsqlrdw_id
            ]
        }

        # 将dict转换为str
        zfsqlrdw_auditbycheck_data_str = json.dumps(zfsqlrdw_auditbycheck_data)
        try:
            zfsqlrdw_auditbycheck_start = time.time()  # 开始时间
            zfsqlrdw_auditbycheck_res = requests.post(zfsqlrdw_auditbycheck_url,
                                                    headers=zfsqlrdw_auditbycheck_headers,
                                                    data=zfsqlrdw_auditbycheck_data_str)
            zfsqlrdw_auditbycheck_res_json = zfsqlrdw_auditbycheck_res.json()
            zfsqlrdw_auditbycheck_end = time.time()  # 结束时间
            zfsqlrdw_auditbycheck_res_time = zfsqlrdw_auditbycheck_end - zfsqlrdw_auditbycheck_start
            zfsqlrdw_auditbycheck_res_time_ms = zfsqlrdw_auditbycheck_res_time * 1000
            print("\n")
            print(f"响应时间：{zfsqlrdw_auditbycheck_res_time_ms}毫秒")
            # print(zfsqlrdw_auditbycheck_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(zfsqlrdw_auditbycheck_url, zfsqlrdw_auditbycheck_data_str,
                                       zfsqlrdw_auditbycheck_headers))
            logss.logger.info("返回结果：{}".format(zfsqlrdw_auditbycheck_res.text))
            ###断言
            response_rscode = zfsqlrdw_auditbycheck_res_json.get('rscode')
            response_result = zfsqlrdw_auditbycheck_res_json.get('result')

            # pytest.assume(zfsqlrdw_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert zfsqlrdw_auditbycheck_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step02)支付申请审核(单位)")
    @allure.title("支付申请审核(单位)：审核")
    def testZfsqshdwAuditByWarn(self):
        zfsqshdw_auditByWarn_url = base_url + '/payfront/pay-voucher-service/v3/payvoucherbill/front/action/auditByWarn'
        zfsqshdw_auditByWarn_headers = {"Content-Type": "application/json",
                                       "tokenid": tokenids}
        zfsqshdw_auditByWarn_data = {
            "actionName": "审核",
            "appId": "pay_voucher",
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "menuId": "55023A7EC8574A28AF301FC3D83B1D9F",
            "actionType": "2",
            "glType": "0",
            "ids": [
                zfsqlrdw_id
            ],
            "params": {
                "checkReviewAgain": "1"
            }
        }

        # 将dict转换为str
        zfsqshdw_auditByWarn_data_str = json.dumps(zfsqshdw_auditByWarn_data)
        try:
            zfsqshdw_auditByWarn_start = time.time()  # 开始时间
            zfsqshdw_auditByWarn_res = requests.post(zfsqshdw_auditByWarn_url,
                                                    headers=zfsqshdw_auditByWarn_headers,
                                                    data=zfsqshdw_auditByWarn_data_str)
            zfsqshdw_auditByWarn_res_json = zfsqshdw_auditByWarn_res.json()
            zfsqshdw_auditByWarn_end = time.time()  # 结束时间
            zfsqshdw_auditByWarn_res_time = zfsqshdw_auditByWarn_end - zfsqshdw_auditByWarn_start
            zfsqshdw_auditByWarn_res_time_ms = zfsqshdw_auditByWarn_res_time * 1000
            print("\n")
            print(f"响应时间：{zfsqshdw_auditByWarn_res_time_ms}毫秒")
            # print(zfsqshdw_auditByWarn_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(zfsqshdw_auditByWarn_url, zfsqshdw_auditByWarn_data_str,
                                       zfsqshdw_auditByWarn_headers))
            logss.logger.info("返回结果：{}".format(zfsqshdw_auditByWarn_res.text))
            ###断言
            response_rscode = zfsqshdw_auditByWarn_res_json.get('rscode')
            response_result = zfsqshdw_auditByWarn_res_json.get('result')

            # pytest.assume(zblr_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert zfsqshdw_auditByWarn_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step03)支付凭证签名")
    @allure.title("支付凭证签名：获取印章位置")
    def testZfpzqmStampPositions(self):
        zfpzqm_StampPositions_url = base_url + '/payfront/pay-common-service/v1/queryVoucherSignStampPositions'
        zfpzqm_StampPositions_headers = {"Content-Type": "application/json",
                                          "tokenid": tokenids}
        zfpzqm_StampPositions_data = {
            "vtCode": "5214",
            "voucherNoList": [
                zfsqlrdw_pay_cert_no
            ],
            "actionId": "FE18A1DB6BC74993A33F09875B4A5FFF"
        }

        # 将dict转换为str
        zfpzqm_StampPositions_data_str = json.dumps(zfpzqm_StampPositions_data)
        try:
            zfpzqm_StampPositions_start = time.time()  # 开始时间
            zfpzqm_StampPositions_res = requests.post(zfpzqm_StampPositions_url,
                                                       headers=zfpzqm_StampPositions_headers,
                                                       data=zfpzqm_StampPositions_data_str)
            zfpzqm_StampPositions_res_json = zfpzqm_StampPositions_res.json()
            zfpzqm_StampPositions_end = time.time()  # 结束时间
            zfpzqm_StampPositions_res_time = zfpzqm_StampPositions_end - zfpzqm_StampPositions_start
            zfpzqm_StampPositions_res_time_ms = zfpzqm_StampPositions_res_time * 1000
            print("\n")
            print(f"响应时间：{zfpzqm_StampPositions_res_time_ms}毫秒")
            # print(zfpzqm_StampPositions_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(zfpzqm_StampPositions_url, zfpzqm_StampPositions_data_str,
                                       zfpzqm_StampPositions_headers))
            logss.logger.info("返回结果：{}".format(zfpzqm_StampPositions_res.text))
            ###断言
            response_rscode = zfpzqm_StampPositions_res_json.get('rscode')
            response_result = zfpzqm_StampPositions_res_json.get('result')

            # pytest.assume(zblr_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert zfpzqm_StampPositions_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step03)支付凭证签名")
    @allure.title("支付凭证签名：获取签名参数")
    def testZfpzqmepayHttpParams(self):
        zfpzqm_epayHttpParams_url = base_url + '/payfront/pay-common-service/v1/epayHttpParams'
        zfpzqm_epayHttpParams_headers = {"Content-Type": "application/json",
                                          "tokenid": tokenids}
        zfpzqm_epayHttpParams_data = {
            "bill_no": [
                zfsqlrdw_pay_cert_no
            ],
            "payBusTypeCodes": [
                "1"
            ],
            "action_id": "FE18A1DB6BC74993A33F09875B4A5FFF",
            "work_flow_id": "pay_voucher",
            "isDoWorkFlow": 'true',
            "isSignStamp": 'true',
            "vtCode": "5214",
            "signType": "0",
            "position": "cz_dwfz",
            "detailPosition": "cz_dwfz",
            "menuId": "FE18A1DB6BC74993A33F09875B4A5FFF",
            "actionType": "2",
            "actionName": "直接签名",
            "glType": "0",
            "ids": [
                zfsqlrdw_pay_cert_id
            ],
            "stampurl": "pay-voucher-service/v3/payvoucherbill/action/sign",
            "admDivCode": "420000000",
            "justShow": 'false'
        }

        # 将dict转换为str
        zfpzqm_epayHttpParams_data_str = json.dumps(zfpzqm_epayHttpParams_data)
        try:
            zfpzqm_epayHttpParams_start = time.time()  # 开始时间
            zfpzqm_epayHttpParams_res = requests.post(zfpzqm_epayHttpParams_url,
                                                       headers=zfpzqm_epayHttpParams_headers,
                                                       data=zfpzqm_epayHttpParams_data_str)
            zfpzqm_epayHttpParams_res_json = zfpzqm_epayHttpParams_res.json()
            zfpzqm_epayHttpParams_end = time.time()  # 结束时间
            zfpzqm_epayHttpParams_res_time = zfpzqm_epayHttpParams_end - zfpzqm_epayHttpParams_start
            zfpzqm_epayHttpParams_res_time_ms = zfpzqm_epayHttpParams_res_time * 1000
            print("\n")
            print(f"响应时间：{zfpzqm_epayHttpParams_res_time_ms}毫秒")
            # print(zfpzqm_epayHttpParams_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(zfpzqm_epayHttpParams_url, zfpzqm_epayHttpParams_data_str,
                                       zfpzqm_epayHttpParams_headers))
            logss.logger.info("返回结果：{}".format(zfpzqm_epayHttpParams_res.text))
            ###断言
            response_rscode = zfpzqm_epayHttpParams_res_json.get('rscode')
            response_result = zfpzqm_epayHttpParams_res_json.get('result')

            # pytest.assume(zblr_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert zfpzqm_epayHttpParams_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step03)支付凭证签名")
    @allure.title("支付凭证签名：签名")
    def testZfpzqmsign(self):
        zfpzqm_sign_url = base_url + '/payfront/pay-voucher-service/v3/payvoucherbill/action/sign'
        zfpzqm_sign_headers = {"Content-Type": "application/json",
                                          "tokenid": tokenids}
        zfpzqm_sign_data = {
            "vt_code": "5214",
            "vouchers": "<?xml version=\"1.0\" encoding=\"GBK\" ?>\n<MOF>\n    <VoucherCount>1</VoucherCount>\n    <VoucherBody VoucherNo=\"zfsqlrdw_pay_cert_no\" AdmDivCode=\"420000\" StYear=\"2024\" VtCode=\"5214\">\n        <VoucherFlag>0</VoucherFlag>\n        <Voucher>PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iR0JLIj8+Cgo8Vm91Y2hlcj4KICA8SWQ+MTNCNzJBNDA4Qjk0NEY3N0EwRDYxRjI5NzAxRUMzNTg8L0lkPgogIDxBZG1EaXZDb2RlPjQyMDAwMDwvQWRtRGl2Q29kZT4KICA8U3RZZWFyPjIwMjQ8L1N0WWVhcj4KICA8VnRDb2RlPjUyMTQ8L1Z0Q29kZT4KICA8Vm91RGF0ZT4yMDI0MDQwOTwvVm91RGF0ZT4KICA8Vm91Y2hlck5vPlcwMDI0MTgwMDAwNzk8L1ZvdWNoZXJObz4KICA8QmlsbE5vPlNRVzAwMjQxODAwMDAxNDwvQmlsbE5vPgogIDxGdW5kVHlwZUNvZGU+MTExMTE8L0Z1bmRUeXBlQ29kZT4KICA8RnVuZFR5cGVOYW1lPr6tt9Gypr/usrnW+jwvRnVuZFR5cGVOYW1lPgogIDxCZ3RUeXBlQ29kZT4xMTwvQmd0VHlwZUNvZGU+CiAgPEJndFR5cGVOYW1lPtSksqbWuLHqPC9CZ3RUeXBlTmFtZT4KICA8UGF5VHlwZUNvZGU+MTwvUGF5VHlwZUNvZGU+CiAgPFBheVR5cGVOYW1lPrn6v+K8r9bQ1qe4tjwvUGF5VHlwZU5hbWU+CiAgPFByb0NhdENvZGU+PC9Qcm9DYXRDb2RlPgogIDxQcm9DYXROYW1lPjwvUHJvQ2F0TmFtZT4KICA8TU9GRGVwQ29kZT4wOTwvTU9GRGVwQ29kZT4KICA8TU9GRGVwTmFtZT7FqdK1tKY8L01PRkRlcE5hbWU+CiAgPFN1cERlcENvZGU+MjE5PC9TdXBEZXBDb2RlPgogIDxTdXBEZXBOYW1lPrr+sbHKocWp0rXFqbTlzPw8L1N1cERlcE5hbWU+CiAgPEFnZW5jeUNvZGU+MjE5MDExPC9BZ2VuY3lDb2RlPgogIDxBZ2VuY3lOYW1lPrr+sbHKobn7suiw7LmrytI8L0FnZW5jeU5hbWU+CiAgPEV4cEZ1bmNDb2RlPjIwMTAxMDE8L0V4cEZ1bmNDb2RlPgogIDxFeHBGdW5jTmFtZT7Q0NX+1MvQ0DwvRXhwRnVuY05hbWU+CiAgPEV4cEZ1bmNDb2RlMT4yMDE8L0V4cEZ1bmNDb2RlMT4KICA8RXhwRnVuY05hbWUxPtK7sOO5q7myt/7O8dans/Y8L0V4cEZ1bmNOYW1lMT4KICA8RXhwRnVuY0NvZGUyPjAxPC9FeHBGdW5jQ29kZTI+CiAgPEV4cEZ1bmNOYW1lMj7Iy7TzysLO8TwvRXhwRnVuY05hbWUyPgogIDxFeHBGdW5jQ29kZTM+MDE8L0V4cEZ1bmNDb2RlMz4KICA8RXhwRnVuY05hbWUzPtDQ1f7Uy9DQPC9FeHBGdW5jTmFtZTM+CiAgPEdvdkV4cEVjb0NvZGU+PC9Hb3ZFeHBFY29Db2RlPgogIDxHb3ZFeHBFY29OYW1lPjwvR292RXhwRWNvTmFtZT4KICA8RGVwRXhwRWNvQ29kZT4zMDEwMTwvRGVwRXhwRWNvQ29kZT4KICA8RGVwRXhwRWNvTmFtZT67+bG+uaTXyjwvRGVwRXhwRWNvTmFtZT4KICA8RGVwUHJvQ29kZT40MjAwMDAyNDIxOVAwMDcwMDAwNTE8L0RlcFByb0NvZGU+CiAgPERlcFByb05hbWU+MjE5MDEx1rix6rncwO0xNTEyPC9EZXBQcm9OYW1lPgogIDxTZXRNb2RlQ29kZT4xPC9TZXRNb2RlQ29kZT4KICA8U2V0TW9kZU5hbWU+tefX09eq1cvWp7i2PC9TZXRNb2RlTmFtZT4KICA8UGF5QmFua0NvZGU+MTAyNTIxMDAwMzM1PC9QYXlCYW5rQ29kZT4KICA8UGF5QmFua05hbWU+1tC5+rmkyczS+NDQzuS6usrQzuTn88K31qfQ0DwvUGF5QmFua05hbWU+CiAgPENsZWFyQmFua0NvZGU+PC9DbGVhckJhbmtDb2RlPgogIDxDbGVhckJhbmtOYW1lPjwvQ2xlYXJCYW5rTmFtZT4KICA8Q2xlYXJBY2N0Tm8+PC9DbGVhckFjY3RObz4KICA8Q2xlYXJBY2N0TmFtZT48L0NsZWFyQWNjdE5hbWU+CiAgPENsZWFyQWNjdEJhbmtOYW1lPjwvQ2xlYXJBY2N0QmFua05hbWU+CiAgPFBheWVlQWNjdE5vPjMyMDIwMTA2MTkxMDAxNDg3OTc8L1BheWVlQWNjdE5vPgogIDxQYXllZUFjY3ROYW1lPrr+sbG2psGmuuO9qMno09DP3rmry748L1BheWVlQWNjdE5hbWU+CiAgPFBheWVlQWNjdEJhbmtOYW1lPrmkyczS+NDQzuS6ur/VuNvWp9DQPC9QYXllZUFjY3RCYW5rTmFtZT4KICA8UGF5ZWVBY2N0QmFua05vPjwvUGF5ZWVBY2N0QmFua05vPgogIDxQYXlBY2N0Tm8+MzIwMjAwNjAwOTIwMDAwOTIwMzwvUGF5QWNjdE5vPgogIDxQYXlBY2N0TmFtZT66/rGxyqG5+7LosOy5q8rSPC9QYXlBY2N0TmFtZT4KICA8UGF5QWNjdEJhbmtOYW1lPtbQufq5pMnM0vjQ0M7kurrK0M7k5/PCt9an0NA8L1BheUFjY3RCYW5rTmFtZT4KICA8UGF5U3VtbWFyeUNvZGU+PC9QYXlTdW1tYXJ5Q29kZT4KICA8UGF5U3VtbWFyeU5hbWU+1qe4tsH3s8w8L1BheVN1bW1hcnlOYW1lPgogIDxQYXlBbXQ+Mi4wMDwvUGF5QW10PgogIDxCdXNpbmVzc1R5cGVDb2RlPjE8L0J1c2luZXNzVHlwZUNvZGU+CiAgPEJ1c2luZXNzVHlwZU5hbWU+xtXNqNK1zvE8L0J1c2luZXNzVHlwZU5hbWU+CiAgPFRheEJpbGxObz48L1RheEJpbGxObz4KICA8VGF4YXllcklEPjwvVGF4YXllcklEPgogIDxUYXhPcmdDb2RlPjwvVGF4T3JnQ29kZT4KICA8R292UHJvY3VyZW1lbnRJRD48L0dvdlByb2N1cmVtZW50SUQ+CiAgPENoZWNrTm8+PC9DaGVja05vPgogIDxQYXlDb2RlPjwvUGF5Q29kZT4KICA8Rm9yZWlnbkFtdD4wPC9Gb3JlaWduQW10PgogIDxDdXJyZW5jeUNvZGU+Q05ZPC9DdXJyZW5jeUNvZGU+CiAgPEVzdFJhdD48L0VzdFJhdD4KICA8QW10VW5pdD48L0FtdFVuaXQ+CiAgPFhQYXlEYXRlPjwvWFBheURhdGU+CiAgPFhBZ2VudEJ1c2luZXNzTm8+PC9YQWdlbnRCdXNpbmVzc05vPgogIDxYQ2hlY2tObz48L1hDaGVja05vPgogIDxYUGF5QW10PjA8L1hQYXlBbXQ+CiAgPFhQYXllZUFjY3RCYW5rTmFtZT48L1hQYXllZUFjY3RCYW5rTmFtZT4KICA8WFBheWVlQWNjdE5vPjwvWFBheWVlQWNjdE5vPgogIDxYUGF5ZWVBY2N0TmFtZT48L1hQYXllZUFjY3ROYW1lPgogIDxIb2xkMT4xMjwvSG9sZDE+CiAgPEhvbGQyPjwvSG9sZDI+CiAgPERldGFpbExpc3Q+CiAgICA8RGV0YWlsPgogICAgICA8SWQ+NTA0M0IyOEVBNkQ2NDcyN0EzM0MzNUJGOENCREY0ODY8L0lkPgogICAgICA8Vm91Y2hlckJpbGxJZD4xM0I3MkE0MDhCOTQ0Rjc3QTBENjFGMjk3MDFFQzM1ODwvVm91Y2hlckJpbGxJZD4KICAgICAgPFZvdWNoZXJCaWxsTm8+VzAwMjQxODAwMDA3OTwvVm91Y2hlckJpbGxObz4KICAgICAgPFZvdWNoZXJEZXRhaWxObz5TUVcwMDI0MTgwMDAwMTQ8L1ZvdWNoZXJEZXRhaWxObz4KICAgICAgPEZ1bmRUeXBlQ29kZT4xMTExMTwvRnVuZFR5cGVDb2RlPgogICAgICA8RnVuZFR5cGVOYW1lPr6tt9Gypr/usrnW+jwvRnVuZFR5cGVOYW1lPgogICAgICA8Qmd0VHlwZUNvZGU+MTE8L0JndFR5cGVDb2RlPgogICAgICA8Qmd0VHlwZU5hbWU+1KSypta4seo8L0JndFR5cGVOYW1lPgogICAgICA8UHJvQ2F0Q29kZT48L1Byb0NhdENvZGU+CiAgICAgIDxQcm9DYXROYW1lPjwvUHJvQ2F0TmFtZT4KICAgICAgPFBheUtpbmRDb2RlPjwvUGF5S2luZENvZGU+CiAgICAgIDxQYXlLaW5kTmFtZT48L1BheUtpbmROYW1lPgogICAgICA8TU9GRGVwQ29kZT48L01PRkRlcENvZGU+CiAgICAgIDxNT0ZEZXBOYW1lPjwvTU9GRGVwTmFtZT4KICAgICAgPFN1cERlcENvZGU+MjE5PC9TdXBEZXBDb2RlPgogICAgICA8U3VwRGVwTmFtZT66/rGxyqHFqdK1xam05cz8PC9TdXBEZXBOYW1lPgogICAgICA8QWdlbmN5Q29kZT4yMTkwMTE8L0FnZW5jeUNvZGU+CiAgICAgIDxBZ2VuY3lOYW1lPrr+sbHKobn7suiw7LmrytI8L0FnZW5jeU5hbWU+CiAgICAgIDxFeHBGdW5jQ29kZT4yMDEwMTAxPC9FeHBGdW5jQ29kZT4KICAgICAgPEV4cEZ1bmNOYW1lPtDQ1f7Uy9DQPC9FeHBGdW5jTmFtZT4KICAgICAgPEdvdkV4cEVjb0NvZGU+PC9Hb3ZFeHBFY29Db2RlPgogICAgICA8R292RXhwRWNvTmFtZT48L0dvdkV4cEVjb05hbWU+CiAgICAgIDxEZXBFeHBFY29Db2RlPjwvRGVwRXhwRWNvQ29kZT4KICAgICAgPERlcEV4cEVjb05hbWU+PC9EZXBFeHBFY29OYW1lPgogICAgICA8RGVwUHJvQ29kZT48L0RlcFByb0NvZGU+CiAgICAgIDxEZXBQcm9OYW1lPjwvRGVwUHJvTmFtZT4KICAgICAgPFBheWVlQWNjdE5vPjMyMDIwMTA2MTkxMDAxNDg3OTc8L1BheWVlQWNjdE5vPgogICAgICA8UGF5ZWVBY2N0TmFtZT66/rGxtqbBprrjvajJ6NPQz965q8u+PC9QYXllZUFjY3ROYW1lPgogICAgICA8UGF5ZWVBY2N0QmFua05hbWU+uaTJzNL40NDO5Lq6v9W429an0NA8L1BheWVlQWNjdEJhbmtOYW1lPgogICAgICA8UGF5ZWVBY2N0QmFua05vPjwvUGF5ZWVBY2N0QmFua05vPgogICAgICA8VHJhY2tpbmdJRD48L1RyYWNraW5nSUQ+CiAgICAgIDxQYXlBbXQ+Mi4wMDwvUGF5QW10PgogICAgICA8UmVtYXJrPjwvUmVtYXJrPgogICAgICA8Rm9yZWlnbkFtdD4wPC9Gb3JlaWduQW10PgogICAgICA8Q3VycmVuY3lDb2RlPkNOWTwvQ3VycmVuY3lDb2RlPgogICAgICA8RXN0UmF0PjwvRXN0UmF0PgogICAgICA8UmVjZWl2ZXJDb2RlPjwvUmVjZWl2ZXJDb2RlPgogICAgICA8QW10VW5pdD48L0FtdFVuaXQ+CiAgICAgIDxYUGF5RGF0ZT48L1hQYXlEYXRlPgogICAgICA8WEFnZW50QnVzaW5lc3NObz48L1hBZ2VudEJ1c2luZXNzTm8+CiAgICAgIDxYQ2hlY2tObz48L1hDaGVja05vPgogICAgICA8WFBheUFtdD48L1hQYXlBbXQ+CiAgICAgIDxYQWRkV29yZD48L1hBZGRXb3JkPgogICAgICA8WFBheWVlQWNjdEJhbmtOYW1lPjwvWFBheWVlQWNjdEJhbmtOYW1lPgogICAgICA8WFBheWVlQWNjdE5vPjwvWFBheWVlQWNjdE5vPgogICAgICA8WFBheWVlQWNjdE5hbWU+PC9YUGF5ZWVBY2N0TmFtZT4KICAgICAgPEhvbGQxPjwvSG9sZDE+CiAgICAgIDxIb2xkMj48L0hvbGQyPgogICAgICA8SG9sZDM+PC9Ib2xkMz4KICAgICAgPEhvbGQ0PjwvSG9sZDQ+CiAgICA8L0RldGFpbD4KICA8L0RldGFpbExpc3Q+CjwvVm91Y2hlcj4K</Voucher>\n        <SignStampList />\n        <SignatureList>\n            <Signature No=\"cz_dwfz\" SN=\"3f38e4aaee0c2acb\">MIIFlgYJKoZIhvcNAQcCoIIFhzCCBYMCAQExCzAJBgUrDgMCGgUAMAsGCSqGSIb3DQEHAaCCBGQwggRgMIIDSKADAgECAgg/OOSq7gwqyzANBgkqhkiG9w0BAQUFADBKMQswCQYDVQQGEwJDTjEMMAoGA1UEChMDTU9GMS0wKwYDVQQDEyRQcml2YXRlIENlcnRpZmljYXRlIEF1dGhvcml0eSBPZiBNT0YwHhcNMjEwODE2MTc0NjI4WhcNMjkxMTAyMTc0NjI4WjCBkzELMAkGA1UEBhMCQ04xDDAKBgNVBAoMA01PRjELMAkGA1UECgwCMDExCzAJBgNVBAgMAjQyMQswCQYDVQQHDAIwNjELMAkGA1UEBwwCMDAxCzAJBgNVBAsMAjA0MRswGQYDVQQMDBI0MjA2MDAxOTgzMDEwNDI1NjMxGDAWBgNVBAMMD+ilhOmYs+W4guacrOe6pzCBnzANBgkqhkiG9w0BAQEFAAOBjQAwgYkCgYEAzeXNBTvF+1Xr0WkTpYYso8c9Z6QbKPVTJyS7GLRnjaxPuF95UEMXZYKPSQLlLxMCwPg9pIPwysZgKsJfPnuMbgg6L0y6Id0lcjsLCtUO5Z5XdJwj3FglQcVb4TQzkpyktN36u8rKiEs5MHq+IGFpB4HM8VJhZK0DXkMHR+lZ5zECAwEAAaOCAYIwggF+MB8GA1UdIwQYMBaAFJb4S7KJrQAb2Qm/dCDwB+CLzQtbMB0GA1UdDgQWBBSdMb2OF61MoZaAfnn1mN9mYCfJIjALBgNVHQ8EBAMCA8gwgfEGA1UdHwSB6TCB5jBCoECgPqQ8MDoxCzAJBgNVBAYTAmNuMQwwCgYDVQQKDANtb2YxDDAKBgNVBAsMA0NSTDEPMA0GA1UEAwwGY3JsNDEzMCagJKAihiBodHRwOi8vY3JsLmNhLm1vZi9jcmwvY3JsNDEzLmNybDB4oHagdIZybGRhcDovL2xkYXAuY2EubW9mOjM4OS9DTj1jcmw0MTMsT1U9Q1JMLG89bW9mLGM9Y24/Y2VydGlmaWNhdGVSZXZvY2F0aW9uTGlzdD9iYXNlP29iamVjdGNsYXNzPWNSTERpc3RyaWJ1dGlvblBvaW50MDsGA1UdJQQ0MDIGCCsGAQUFBwMCBggrBgEFBQcDAwYIKwYBBQUHAwQGCCsGAQUFBwMIBggrBgEFBQcDCTANBgkqhkiG9w0BAQUFAAOCAQEAHLam+IAmxRAFOjcF+utB+TLsQLwpqaHjj5AlYstJeSBZLLAkypwVaPEcqK7WSczeQzOhOX4LhNon9xCdY+fmYBEG99tsQfC7FhO7dDODmKwwjOYco6ZxsVWEU/SWoMrYgcD/VIFlbFeQjPGYR+JDfkif7oRWp1EAotmyglss5p4tgyq17HjXkXMhKzcp6IT3maW1ZM0/8+LtXu8PMj47N5IFcb0kKDuVrCZQvFJxwGFz7aXxn5vumIBv4vfc579rWinsotw9BVMH7zcjbkV8zYyNq6j46VE9vWJ6WuKQd8pzkHulxuTWfY4Q4yQRLWo1txXW+RC+YNelE2e7Qkw84jGB+zCB+AIBATBWMEoxCzAJBgNVBAYTAkNOMQwwCgYDVQQKEwNNT0YxLTArBgNVBAMTJFByaXZhdGUgQ2VydGlmaWNhdGUgQXV0aG9yaXR5IE9mIE1PRgIIPzjkqu4MKsswCQYFKw4DAhoFADANBgkqhkiG9w0BAQEFAASBgL/StXzqUUb+JpQ87kjK0zsyz0jcK4vr5X6vRnbri+rwep//kv/UXz83/x8belE6Z2JqyHcgItdKVrIXRQGYirwPAWGOE+cZ2eJHbqqUZnvNz7cJzPHO9CvTJjofipkHLvvGOinlaxYqeDYnZN30a7a3sSCFhyIIPBJ15S+vOWfm</Signature>\n        </SignatureList>\n    </VoucherBody>\n</MOF>\n",
            "details": "",
            "bill_no": "",
            "payBusTypeCodes": [
                "1"
            ],
            "action_id": "FE18A1DB6BC74993A33F09875B4A5FFF",
            "work_flow_id": "pay_voucher",
            "isDoWorkFlow": 'true',
            "isSignStamp": 'true',
            "vtCode": "5214",
            "signType": "0",
            "position": "cz_dwfz",
            "detailPosition": "cz_dwfz",
            "menuId": "FE18A1DB6BC74993A33F09875B4A5FFF",
            "actionType": "2",
            "actionName": "直接签名",
            "glType": "0",
            "ids": [
                zfsqlrdw_pay_cert_id
            ],
            "stampurl": "pay-voucher-service/v3/payvoucherbill/action/sign",
            "admDivCode": "420000000",
            "justShow": 'false',
            "voucherNos": [
                zfsqlrdw_pay_cert_no
            ]
        }

        # 提取data中的xml报文内容
        zfpzqm_xml = zfpzqm_sign_data.get("vouchers")
        # print(zfsqlrdw_xml)
        # 将xml报文解析为dict字典
        data_dict = xmltodict.parse(zfpzqm_xml)
        # print(data_dict)
        # 提取字典中voucherno
        voucherno = data_dict['MOF']['VoucherBody']['@VoucherNo']
        print(voucherno)
        # 将字典中的voucherno修改为全部变量pay_cert_no
        data_dict['MOF']['VoucherBody']['@VoucherNo'] = zfsqlrdw_pay_cert_no
        # 将修改后字典转换为xml数据
        zfsqlrqm_xmls = xmltodict.unparse(data_dict, pretty=True)
        # print(zfsqlrdw_xmls)

        # 将data修改
        zfpzqm_sign_data_fix = {
            "vt_code": "5214",
            "vouchers": zfsqlrqm_xmls,
            "details": "",
            "bill_no": "",
            "payBusTypeCodes": [
                "1"
            ],
            "action_id": "FE18A1DB6BC74993A33F09875B4A5FFF",
            "work_flow_id": "pay_voucher",
            "isDoWorkFlow": 'true',
            "isSignStamp": 'true',
            "vtCode": "5214",
            "signType": "0",
            "position": "cz_dwfz",
            "detailPosition": "cz_dwfz",
            "menuId": "FE18A1DB6BC74993A33F09875B4A5FFF",
            "actionType": "2",
            "actionName": "直接签名",
            "glType": "0",
            "ids": [
                zfsqlrdw_pay_cert_id
            ],
            "stampurl": "pay-voucher-service/v3/payvoucherbill/action/sign",
            "admDivCode": "420000000",
            "justShow": 'false',
            "voucherNos": [
                zfsqlrdw_pay_cert_no
            ]
        }

        # print(zfpzqm_sign_data_fix)

        # 使用修改后的data进行转为str
        zfpzqm_sign_data_str = json.dumps(zfpzqm_sign_data_fix)

        try:
            zfpzqm_sign_start = time.time()  # 开始时间
            zfpzqm_sign_res = requests.post(zfpzqm_sign_url,
                                                       headers=zfpzqm_sign_headers,
                                                       data=zfpzqm_sign_data_str)
            zfpzqm_sign_res_json = zfpzqm_sign_res.json()
            zfpzqm_sign_end = time.time()  # 结束时间
            zfpzqm_sign_res_time = zfpzqm_sign_end - zfpzqm_sign_start
            zfpzqm_sign_res_time_ms = zfpzqm_sign_res_time * 1000
            print("\n")
            print(f"响应时间：{zfpzqm_sign_res_time_ms}毫秒")
            # print(zfpzqm_sign_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(zfpzqm_sign_url, zfpzqm_sign_data_str,
                                       zfpzqm_sign_headers))
            logss.logger.info("返回结果：{}".format(zfpzqm_sign_res.text))
            ###断言
            response_rscode = zfpzqm_sign_res_json.get('rscode')
            response_result = zfpzqm_sign_res_json.get('result')

            # pytest.assume(zblr_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert zfpzqm_sign_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step04)支付凭证签章")
    @allure.title("支付凭证签章：获取印章位置")
    def testZfpzqzStampPositions(self):
        zfpzqz_StampPositions_url = base_url + '/payfront/pay-common-service/v1/queryVoucherSignStampPositions'
        zfpzqz_StampPositions_headers = {"Content-Type": "application/json",
                                          "tokenid": tokenids}
        zfpzqz_StampPositions_data = {
            "vtCode": "5214",
            "voucherNoList": [
                zfsqlrdw_pay_cert_no
            ],
            "actionId": "FDD7B601AC0645D88794E89466B4DADA"
        }

        # 将dict转换为str
        zfpzqz_StampPositions_data_str = json.dumps(zfpzqz_StampPositions_data)
        try:
            zfpzqz_StampPositions_start = time.time()  # 开始时间
            zfpzqz_StampPositions_res = requests.post(zfpzqz_StampPositions_url,
                                                       headers=zfpzqz_StampPositions_headers,
                                                       data=zfpzqz_StampPositions_data_str)
            zfpzqz_StampPositions_res_json = zfpzqz_StampPositions_res.json()
            zfpzqz_StampPositions_end = time.time()  # 结束时间
            zfpzqz_StampPositions_res_time = zfpzqz_StampPositions_end - zfpzqz_StampPositions_start
            zfpzqz_StampPositions_res_time_ms = zfpzqz_StampPositions_res_time * 1000
            print("\n")
            print(f"响应时间：{zfpzqz_StampPositions_res_time_ms}毫秒")
            # print(zfpzqz_StampPositions_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(zfpzqz_StampPositions_url, zfpzqz_StampPositions_data_str,
                                       zfpzqz_StampPositions_headers))
            logss.logger.info("返回结果：{}".format(zfpzqz_StampPositions_res.text))
            ###断言
            response_rscode = zfpzqz_StampPositions_res_json.get('rscode')
            response_result = zfpzqz_StampPositions_res_json.get('result')

            # pytest.assume(zblr_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert zfpzqz_StampPositions_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step04)支付凭证签章")
    @allure.title("支付凭证签章：获取签章参数")
    def testZfpzqzepayHttpParams(self):
        zfpzqz_epayHttpParams_url = base_url + '/payfront/pay-common-service/v1/epayHttpParams'
        zfpzqz_epayHttpParams_headers = {"Content-Type": "application/json",
                                          "tokenid": tokenids}
        zfpzqz_epayHttpParams_data = {
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "opid": "FDD7B601AC0645D88794E89466B4DADA01BB237B45CC4421B6E8051877538BF3",
            "bill_no": [
                zfsqlrdw_pay_cert_no
            ],
            "payBusTypeCodes": [
                "1"
            ],
            "action_id": "FDD7B601AC0645D88794E89466B4DADA",
            "work_flow_id": "pay_voucher_bill",
            "isDoWorkFlow": 'true',
            "isSignStamp": 'true',
            "appId": "pay_voucher",
            "menuId": "FDD7B601AC0645D88794E89466B4DADA",
            "actionType": "2",
            "actionName": "直接签章",
            "vtCode": "5214",
            "glType": "0",
            "ids": [
                zfsqlrdw_pay_cert_id
            ],
            "stampurl": "pay-voucher-service/v3/payvoucherbill/action/stamp",
            "admDivCode": "420000000",
            "justShow": 'false'
        }

        # 将dict转换为str
        zfpzqz_epayHttpParams_data_str = json.dumps(zfpzqz_epayHttpParams_data)
        try:
            zfpzqz_epayHttpParams_start = time.time()  # 开始时间
            zfpzqz_epayHttpParams_res = requests.post(zfpzqz_epayHttpParams_url,
                                                       headers=zfpzqz_epayHttpParams_headers,
                                                       data=zfpzqz_epayHttpParams_data_str)
            zfpzqz_epayHttpParams_res_json = zfpzqz_epayHttpParams_res.json()
            zfpzqz_epayHttpParams_end = time.time()  # 结束时间
            zfpzqz_epayHttpParams_res_time = zfpzqz_epayHttpParams_end - zfpzqz_epayHttpParams_start
            zfpzqz_epayHttpParams_res_time_ms = zfpzqz_epayHttpParams_res_time * 1000
            print("\n")
            print(f"响应时间：{zfpzqz_epayHttpParams_res_time_ms}毫秒")
            # print(zfpzqz_epayHttpParams_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(zfpzqz_epayHttpParams_url, zfpzqz_epayHttpParams_data_str,
                                       zfpzqz_epayHttpParams_headers))
            logss.logger.info("返回结果：{}".format(zfpzqz_epayHttpParams_res.text))
            ###断言
            response_rscode = zfpzqz_epayHttpParams_res_json.get('rscode')
            response_result = zfpzqz_epayHttpParams_res_json.get('result')

            # pytest.assume(zblr_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert zfpzqz_epayHttpParams_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step04)支付凭证签章")
    @allure.title("支付凭证签章：签章")
    def testZfpzqzstamp(self):
        zfpzqz_stamp_url = base_url + '/payfront/pay-voucher-service/v3/payvoucherbill/action/stamp'
        zfpzqz_stamp_headers = {"Content-Type": "application/json",
                                          "tokenid": tokenids}
        zfpzqz_stamp_data = {
            "vt_code": "5214",
            "vouchers": "<?xml version=\"1.0\" encoding=\"GBK\" ?>\n<MOF>\n    <VoucherCount>1</VoucherCount>\n    <VoucherBody VoucherNo=\"zfsqlrdw_pay_cert_no\" AdmDivCode=\"420000\" StYear=\"2024\" VtCode=\"5214\">\n        <VoucherFlag>0</VoucherFlag>\n        <Voucher>PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iR0JLIj8+Cgo8Vm91Y2hlcj4KICA8SWQ+MDFCQjIzN0I0NUNDNDQyMUI2RTgwNTE4Nzc1MzhCRjM8L0lkPgogIDxBZG1EaXZDb2RlPjQyMDAwMDwvQWRtRGl2Q29kZT4KICA8U3RZZWFyPjIwMjQ8L1N0WWVhcj4KICA8VnRDb2RlPjUyMTQ8L1Z0Q29kZT4KICA8Vm91RGF0ZT4yMDI0MDQwNzwvVm91RGF0ZT4KICA8Vm91Y2hlck5vPlcwMDI0MTgwMDAwNzI8L1ZvdWNoZXJObz4KICA8QmlsbE5vPlNRVzAwMjQxODAwMDAwNDwvQmlsbE5vPgogIDxGdW5kVHlwZUNvZGU+MTExMTE8L0Z1bmRUeXBlQ29kZT4KICA8RnVuZFR5cGVOYW1lPr6tt9Gypr/usrnW+jwvRnVuZFR5cGVOYW1lPgogIDxCZ3RUeXBlQ29kZT4xMTwvQmd0VHlwZUNvZGU+CiAgPEJndFR5cGVOYW1lPtSksqbWuLHqPC9CZ3RUeXBlTmFtZT4KICA8UGF5VHlwZUNvZGU+MTwvUGF5VHlwZUNvZGU+CiAgPFBheVR5cGVOYW1lPrn6v+K8r9bQ1qe4tjwvUGF5VHlwZU5hbWU+CiAgPFByb0NhdENvZGU+PC9Qcm9DYXRDb2RlPgogIDxQcm9DYXROYW1lPjwvUHJvQ2F0TmFtZT4KICA8TU9GRGVwQ29kZT4wOTwvTU9GRGVwQ29kZT4KICA8TU9GRGVwTmFtZT7FqdK1tKY8L01PRkRlcE5hbWU+CiAgPFN1cERlcENvZGU+MjE5PC9TdXBEZXBDb2RlPgogIDxTdXBEZXBOYW1lPrr+sbHKocWp0rXFqbTlzPw8L1N1cERlcE5hbWU+CiAgPEFnZW5jeUNvZGU+MjE5MDExPC9BZ2VuY3lDb2RlPgogIDxBZ2VuY3lOYW1lPrr+sbHKobn7suiw7LmrytI8L0FnZW5jeU5hbWU+CiAgPEV4cEZ1bmNDb2RlPjIwMTAxMDE8L0V4cEZ1bmNDb2RlPgogIDxFeHBGdW5jTmFtZT7Q0NX+1MvQ0DwvRXhwRnVuY05hbWU+CiAgPEV4cEZ1bmNDb2RlMT4yMDE8L0V4cEZ1bmNDb2RlMT4KICA8RXhwRnVuY05hbWUxPtK7sOO5q7myt/7O8dans/Y8L0V4cEZ1bmNOYW1lMT4KICA8RXhwRnVuY0NvZGUyPjAxPC9FeHBGdW5jQ29kZTI+CiAgPEV4cEZ1bmNOYW1lMj7Iy7TzysLO8TwvRXhwRnVuY05hbWUyPgogIDxFeHBGdW5jQ29kZTM+MDE8L0V4cEZ1bmNDb2RlMz4KICA8RXhwRnVuY05hbWUzPtDQ1f7Uy9DQPC9FeHBGdW5jTmFtZTM+CiAgPEdvdkV4cEVjb0NvZGU+PC9Hb3ZFeHBFY29Db2RlPgogIDxHb3ZFeHBFY29OYW1lPjwvR292RXhwRWNvTmFtZT4KICA8RGVwRXhwRWNvQ29kZT4zMDEwMTwvRGVwRXhwRWNvQ29kZT4KICA8RGVwRXhwRWNvTmFtZT67+bG+uaTXyjwvRGVwRXhwRWNvTmFtZT4KICA8RGVwUHJvQ29kZT40MjAwMDAyNDIxOVAwMDcwMDAwNTE8L0RlcFByb0NvZGU+CiAgPERlcFByb05hbWU+MjE5MDEx1rix6rncwO0xNTEyPC9EZXBQcm9OYW1lPgogIDxTZXRNb2RlQ29kZT4xPC9TZXRNb2RlQ29kZT4KICA8U2V0TW9kZU5hbWU+tefX09eq1cvWp7i2PC9TZXRNb2RlTmFtZT4KICA8UGF5QmFua0NvZGU+MTAyNTIxMDAwMzM1PC9QYXlCYW5rQ29kZT4KICA8UGF5QmFua05hbWU+1tC5+rmkyczS+NDQzuS6usrQzuTn88K31qfQ0DwvUGF5QmFua05hbWU+CiAgPENsZWFyQmFua0NvZGU+PC9DbGVhckJhbmtDb2RlPgogIDxDbGVhckJhbmtOYW1lPjwvQ2xlYXJCYW5rTmFtZT4KICA8Q2xlYXJBY2N0Tm8+PC9DbGVhckFjY3RObz4KICA8Q2xlYXJBY2N0TmFtZT48L0NsZWFyQWNjdE5hbWU+CiAgPENsZWFyQWNjdEJhbmtOYW1lPjwvQ2xlYXJBY2N0QmFua05hbWU+CiAgPFBheWVlQWNjdE5vPjMyMDIwMTA2MTkxMDAxNDg3OTc8L1BheWVlQWNjdE5vPgogIDxQYXllZUFjY3ROYW1lPrr+sbG2psGmuuO9qMno09DP3rmry748L1BheWVlQWNjdE5hbWU+CiAgPFBheWVlQWNjdEJhbmtOYW1lPrmkyczS+NDQzuS6ur/VuNvWp9DQPC9QYXllZUFjY3RCYW5rTmFtZT4KICA8UGF5ZWVBY2N0QmFua05vPjwvUGF5ZWVBY2N0QmFua05vPgogIDxQYXlBY2N0Tm8+MzIwMjAwNjAwOTIwMDAwOTIwMzwvUGF5QWNjdE5vPgogIDxQYXlBY2N0TmFtZT66/rGxyqG5+7LosOy5q8rSPC9QYXlBY2N0TmFtZT4KICA8UGF5QWNjdEJhbmtOYW1lPtbQufq5pMnM0vjQ0M7kurrK0M7k5/PCt9an0NA8L1BheUFjY3RCYW5rTmFtZT4KICA8UGF5U3VtbWFyeUNvZGU+PC9QYXlTdW1tYXJ5Q29kZT4KICA8UGF5U3VtbWFyeU5hbWU+1qe4tsH3s8w8L1BheVN1bW1hcnlOYW1lPgogIDxQYXlBbXQ+Mi4wMDwvUGF5QW10PgogIDxCdXNpbmVzc1R5cGVDb2RlPjE8L0J1c2luZXNzVHlwZUNvZGU+CiAgPEJ1c2luZXNzVHlwZU5hbWU+xtXNqNK1zvE8L0J1c2luZXNzVHlwZU5hbWU+CiAgPFRheEJpbGxObz48L1RheEJpbGxObz4KICA8VGF4YXllcklEPjwvVGF4YXllcklEPgogIDxUYXhPcmdDb2RlPjwvVGF4T3JnQ29kZT4KICA8R292UHJvY3VyZW1lbnRJRD48L0dvdlByb2N1cmVtZW50SUQ+CiAgPENoZWNrTm8+PC9DaGVja05vPgogIDxQYXlDb2RlPjwvUGF5Q29kZT4KICA8Rm9yZWlnbkFtdD4wPC9Gb3JlaWduQW10PgogIDxDdXJyZW5jeUNvZGU+Q05ZPC9DdXJyZW5jeUNvZGU+CiAgPEVzdFJhdD48L0VzdFJhdD4KICA8QW10VW5pdD48L0FtdFVuaXQ+CiAgPFhQYXlEYXRlPjwvWFBheURhdGU+CiAgPFhBZ2VudEJ1c2luZXNzTm8+PC9YQWdlbnRCdXNpbmVzc05vPgogIDxYQ2hlY2tObz48L1hDaGVja05vPgogIDxYUGF5QW10PjA8L1hQYXlBbXQ+CiAgPFhQYXllZUFjY3RCYW5rTmFtZT48L1hQYXllZUFjY3RCYW5rTmFtZT4KICA8WFBheWVlQWNjdE5vPjwvWFBheWVlQWNjdE5vPgogIDxYUGF5ZWVBY2N0TmFtZT48L1hQYXllZUFjY3ROYW1lPgogIDxIb2xkMT4xMjwvSG9sZDE+CiAgPEhvbGQyPjwvSG9sZDI+CiAgPERldGFpbExpc3Q+CiAgICA8RGV0YWlsPgogICAgICA8SWQ+OEYzMDg3RTQyRTQxNDk4RDkwRjEwRjZDRDJERTFEODU8L0lkPgogICAgICA8Vm91Y2hlckJpbGxJZD4wMUJCMjM3QjQ1Q0M0NDIxQjZFODA1MTg3NzUzOEJGMzwvVm91Y2hlckJpbGxJZD4KICAgICAgPFZvdWNoZXJCaWxsTm8+VzAwMjQxODAwMDA3MjwvVm91Y2hlckJpbGxObz4KICAgICAgPFZvdWNoZXJEZXRhaWxObz5TUVcwMDI0MTgwMDAwMDQ8L1ZvdWNoZXJEZXRhaWxObz4KICAgICAgPEZ1bmRUeXBlQ29kZT4xMTExMTwvRnVuZFR5cGVDb2RlPgogICAgICA8RnVuZFR5cGVOYW1lPr6tt9Gypr/usrnW+jwvRnVuZFR5cGVOYW1lPgogICAgICA8Qmd0VHlwZUNvZGU+MTE8L0JndFR5cGVDb2RlPgogICAgICA8Qmd0VHlwZU5hbWU+1KSypta4seo8L0JndFR5cGVOYW1lPgogICAgICA8UHJvQ2F0Q29kZT48L1Byb0NhdENvZGU+CiAgICAgIDxQcm9DYXROYW1lPjwvUHJvQ2F0TmFtZT4KICAgICAgPFBheUtpbmRDb2RlPjwvUGF5S2luZENvZGU+CiAgICAgIDxQYXlLaW5kTmFtZT48L1BheUtpbmROYW1lPgogICAgICA8TU9GRGVwQ29kZT48L01PRkRlcENvZGU+CiAgICAgIDxNT0ZEZXBOYW1lPjwvTU9GRGVwTmFtZT4KICAgICAgPFN1cERlcENvZGU+MjE5PC9TdXBEZXBDb2RlPgogICAgICA8U3VwRGVwTmFtZT66/rGxyqHFqdK1xam05cz8PC9TdXBEZXBOYW1lPgogICAgICA8QWdlbmN5Q29kZT4yMTkwMTE8L0FnZW5jeUNvZGU+CiAgICAgIDxBZ2VuY3lOYW1lPrr+sbHKobn7suiw7LmrytI8L0FnZW5jeU5hbWU+CiAgICAgIDxFeHBGdW5jQ29kZT4yMDEwMTAxPC9FeHBGdW5jQ29kZT4KICAgICAgPEV4cEZ1bmNOYW1lPtDQ1f7Uy9DQPC9FeHBGdW5jTmFtZT4KICAgICAgPEdvdkV4cEVjb0NvZGU+PC9Hb3ZFeHBFY29Db2RlPgogICAgICA8R292RXhwRWNvTmFtZT48L0dvdkV4cEVjb05hbWU+CiAgICAgIDxEZXBFeHBFY29Db2RlPjwvRGVwRXhwRWNvQ29kZT4KICAgICAgPERlcEV4cEVjb05hbWU+PC9EZXBFeHBFY29OYW1lPgogICAgICA8RGVwUHJvQ29kZT48L0RlcFByb0NvZGU+CiAgICAgIDxEZXBQcm9OYW1lPjwvRGVwUHJvTmFtZT4KICAgICAgPFBheWVlQWNjdE5vPjMyMDIwMTA2MTkxMDAxNDg3OTc8L1BheWVlQWNjdE5vPgogICAgICA8UGF5ZWVBY2N0TmFtZT66/rGxtqbBprrjvajJ6NPQz965q8u+PC9QYXllZUFjY3ROYW1lPgogICAgICA8UGF5ZWVBY2N0QmFua05hbWU+uaTJzNL40NDO5Lq6v9W429an0NA8L1BheWVlQWNjdEJhbmtOYW1lPgogICAgICA8UGF5ZWVBY2N0QmFua05vPjwvUGF5ZWVBY2N0QmFua05vPgogICAgICA8VHJhY2tpbmdJRD48L1RyYWNraW5nSUQ+CiAgICAgIDxQYXlBbXQ+Mi4wMDwvUGF5QW10PgogICAgICA8UmVtYXJrPjwvUmVtYXJrPgogICAgICA8Rm9yZWlnbkFtdD4wPC9Gb3JlaWduQW10PgogICAgICA8Q3VycmVuY3lDb2RlPkNOWTwvQ3VycmVuY3lDb2RlPgogICAgICA8RXN0UmF0PjwvRXN0UmF0PgogICAgICA8UmVjZWl2ZXJDb2RlPjwvUmVjZWl2ZXJDb2RlPgogICAgICA8QW10VW5pdD48L0FtdFVuaXQ+CiAgICAgIDxYUGF5RGF0ZT48L1hQYXlEYXRlPgogICAgICA8WEFnZW50QnVzaW5lc3NObz48L1hBZ2VudEJ1c2luZXNzTm8+CiAgICAgIDxYQ2hlY2tObz48L1hDaGVja05vPgogICAgICA8WFBheUFtdD48L1hQYXlBbXQ+CiAgICAgIDxYQWRkV29yZD48L1hBZGRXb3JkPgogICAgICA8WFBheWVlQWNjdEJhbmtOYW1lPjwvWFBheWVlQWNjdEJhbmtOYW1lPgogICAgICA8WFBheWVlQWNjdE5vPjwvWFBheWVlQWNjdE5vPgogICAgICA8WFBheWVlQWNjdE5hbWU+PC9YUGF5ZWVBY2N0TmFtZT4KICAgICAgPEhvbGQxPjwvSG9sZDE+CiAgICAgIDxIb2xkMj48L0hvbGQyPgogICAgICA8SG9sZDM+PC9Ib2xkMz4KICAgICAgPEhvbGQ0PjwvSG9sZDQ+CiAgICA8L0RldGFpbD4KICA8L0RldGFpbExpc3Q+CjwvVm91Y2hlcj4K</Voucher>\n        <SignStampList>\n            <SignStamp No=\"cz_dwgz\" SN=\"7344e8d63bb64f73add978f24d25ec8f\">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</SignStamp>\n        </SignStampList>\n        <SignatureList />\n    </VoucherBody>\n</MOF>\n",
            "details": "",
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "opid": "FDD7B601AC0645D88794E89466B4DADA01BB237B45CC4421B6E8051877538BF3",
            "bill_no": "",
            "payBusTypeCodes": [
                "1"
            ],
            "action_id": "FDD7B601AC0645D88794E89466B4DADA",
            "work_flow_id": "pay_voucher_bill",
            "isDoWorkFlow": 'true',
            "isSignStamp": 'true',
            "appId": "pay_voucher",
            "menuId": "FDD7B601AC0645D88794E89466B4DADA",
            "actionType": "2",
            "actionName": "直接签章",
            "vtCode": "5214",
            "glType": "0",
            "ids": [
                zfsqlrdw_pay_cert_id
            ],
            "stampurl": "pay-voucher-service/v3/payvoucherbill/action/stamp",
            "admDivCode": "420000000",
            "justShow": 'false',
            "voucherNos": [
                zfsqlrdw_pay_cert_no
            ]
        }

        # 提取data中的xml报文内容
        zfpzqz_xml = zfpzqz_stamp_data.get("vouchers")
        # print(zfsqlrdw_xml)
        # 将xml报文解析为dict字典
        data_dict = xmltodict.parse(zfpzqz_xml)
        # print(data_dict)
        # 提取字典中voucherno
        voucherno = data_dict['MOF']['VoucherBody']['@VoucherNo']
        print(voucherno)
        # 将字典中的voucherno修改为全部变量pay_cert_no
        data_dict['MOF']['VoucherBody']['@VoucherNo'] = zfsqlrdw_pay_cert_no
        # 将修改后字典转换为xml数据
        zfpzqz_xmls = xmltodict.unparse(data_dict, pretty=True)
        # print(zfsqlrdw_xmls)

        # 将data修改
        zfpzqz_sign_data_fix = {
            "vt_code": "5214",
            "vouchers": zfpzqz_xmls,
            "details": "",
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "opid": "FDD7B601AC0645D88794E89466B4DADA01BB237B45CC4421B6E8051877538BF3",
            "bill_no": "",
            "payBusTypeCodes": [
                "1"
            ],
            "action_id": "FDD7B601AC0645D88794E89466B4DADA",
            "work_flow_id": "pay_voucher_bill",
            "isDoWorkFlow": 'true',
            "isSignStamp": 'true',
            "appId": "pay_voucher",
            "menuId": "FDD7B601AC0645D88794E89466B4DADA",
            "actionType": "2",
            "actionName": "直接签章",
            "vtCode": "5214",
            "glType": "0",
            "ids": [
                zfsqlrdw_pay_cert_id
            ],
            "stampurl": "pay-voucher-service/v3/payvoucherbill/action/stamp",
            "admDivCode": "420000000",
            "justShow": 'false',
            "voucherNos": [
                zfsqlrdw_pay_cert_no
            ]
        }

        # print(zfpzqm_sign_data_fix)

        # 使用修改后的data进行转为str
        zfpzqz_stamp_data_str = json.dumps(zfpzqz_sign_data_fix)



        # 将dict转换为str
        # zfpzqz_stamp_data_str = json.dumps(zfpzqz_stamp_data)
        try:
            zfpzqz_stamp_start = time.time()  # 开始时间
            zfpzqz_stamp_res = requests.post(zfpzqz_stamp_url,
                                                       headers=zfpzqz_stamp_headers,
                                                       data=zfpzqz_stamp_data_str)
            zfpzqz_stamp_res_json = zfpzqz_stamp_res.json()
            zfpzqz_stamp_end = time.time()  # 结束时间
            zfpzqz_stamp_res_time = zfpzqz_stamp_end - zfpzqz_stamp_start
            zfpzqz_stamp_res_time_ms = zfpzqz_stamp_res_time * 1000
            print("\n")
            print(f"响应时间：{zfpzqz_stamp_res_time_ms}毫秒")
            # print(zfpzqz_stamp_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(zfpzqz_stamp_url, zfpzqz_stamp_data_str,
                                       zfpzqz_stamp_headers))
            logss.logger.info("返回结果：{}".format(zfpzqz_stamp_res.text))
            ###断言
            response_rscode = zfpzqz_stamp_res_json.get('rscode')
            response_result = zfpzqz_stamp_res_json.get('result')

            # pytest.assume(zblr_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert zfpzqz_stamp_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常


    @allure.story("(step05)支付凭证发送")
    @allure.title("支付凭证发送：发送")
    def testzfpzfssend(self):
        zfpzfs_send_url = base_url + '/payfront/pay-voucher-service/v3/payvoucherbill/front/action/send'
        zfpzfs_send_headers = {"Content-Type": "application/json",
                                          "tokenid": tokenids}
        zfpzfs_send_data = {
            "actionName": "发送",
            "appId": "pay_voucher",
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "menuId": "F14B851DDF3E4599AA25E5F603B29932",
            "actionType": "2",
            "glType": "0",
            "ids": [
                zfsqlrdw_pay_cert_id
            ],
            "voucherNos": [
                zfsqlrdw_pay_cert_no
            ],
            "vtCode": "5214",
            "vt_code": "5214",
            "actionId": "F14B851DDF3E4599AA25E5F603B29932"
        }

        # 将dict转换为str
        zfpzfs_send_data_str = json.dumps(zfpzfs_send_data)
        try:
            zfpzfs_send_start = time.time()  # 开始时间
            zfpzfs_send_res = requests.post(zfpzfs_send_url,
                                                       headers=zfpzfs_send_headers,
                                                       data=zfpzfs_send_data_str)
            zfpzfs_send_res_json = zfpzfs_send_res.json()
            zfpzfs_send_end = time.time()  # 结束时间
            zfpzfs_send_res_time = zfpzfs_send_end - zfpzfs_send_start
            zfpzfs_send_res_time_ms = zfpzfs_send_res_time * 1000
            print("\n")
            print(f"响应时间：{zfpzfs_send_res_time_ms}毫秒")
            # print(zfpzfs_send_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(zfpzfs_send_url, zfpzfs_send_data_str,
                                       zfpzfs_send_headers))
            logss.logger.info("返回结果：{}".format(zfpzfs_send_res.text))
            ###断言
            response_rscode = zfpzfs_send_res_json.get('rscode')
            response_result = zfpzfs_send_res_json.get('result')

            # pytest.assume(zblr_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert zfpzfs_send_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常


@allure.feature('(case02)国库集中支付代编')
class TestVoucherdb:
    @allure.story("(step01)支付申请录入(代编)")
    @allure.title("支付申请录入(代编)：保存")
    def testZfsqlrdbInsert(self):
        zfsqlrdb_insert_url= base_url + '/payfront/pay-voucher-service/v3/payvoucherbill/front/action/insert'
        zfsqlrdb_insert_headers = {"Content-Type": "application/json",
                                           "tokenid": tokenids}
        zfsqlrdb_insert_data = {
            "appId": "pay_voucher",
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "menuId": "01192C92AC1D486498F846947528C4A9",
            "actionType": "1",
            "actionName": "新增",
            "glType": "1",
            "params": {
                "accountClsId": "4E72561AB3CD477EB8DFD51813EC2FB2",
                "accountType": "63",
                "isFinancial": "1",
                "cptName": "pay89",
                "batchUserEleType": "1",
                "showContact": "false"
            },
            "datas": [
                {
                    "budget_level_code": "1",
                    "bgt_type_id": "4F53297E01C18CFC47D3F942A0958939",
                    "bgt_mof_dep": "09农业处",
                    "found_type_code": "12",
                    "agency_code": "219011",
                    "bgt_source_id": "62A6C38B276AB2117EAECFC2EFD4FEFF",
                    "canuse_amt": 99996,
                    "dis_amt": 0,
                    "found_type": "12-预估",
                    "bgt_mof_dep_name": "农业处",
                    "zdzjjqpt": "2-否",
                    "sumguid": "1775326015709990912",
                    "manage_mof_dep": "09-农业处",
                    "pay_type_code": "1",
                    "bgt_type_code": "11",
                    "fiscal_year": "2024",
                    "manage_mof_dep_id": "0B256AD0C2B3209E7FA2AE25873896B8",
                    "gov_bgt_eco": "",
                    "is_more_pay": "2",
                    "dep_bgt_eco_id": "F2684D4AE3086DBDA207A71B269729D0",
                    "planuseamt": 34,
                    "mof_div_code": "420000000",
                    "agency_id": "6B98F3B2EE02434479C8630869A96C60",
                    "direct_flag": "09-其它",
                    "source_type": "1-年初预算",
                    "bgt_mof_dep_id": "0B256AD0C2B3209E7FA2AE25873896B8",
                    "version": "2024-04-07 11:11:38",
                    "budget_level": "1-中央级",
                    "is_gov_pur_id": "2",
                    "zdzjjqpt_name": "否",
                    "todo_node": "BB39585CD1574D94B7D3DB7553930004",
                    "is_mat_id": "2",
                    "exp_func_name": "行政运行",
                    "pro_name": "219011指标管理1512",
                    "lzfs_code": "001",
                    "found_type_id": "E3BB7DF43981C10F177EA6A60BBEFFC2",
                    "aviamt": 100000,
                    "fund_type": "11111-经费拨款补助",
                    "is_mat_code": "2",
                    "gov_bgt_eco_code": "50101",
                    "canuseamt": 99996,
                    "update_time": "2024-04-02 11:05:43",
                    "bgt_source_code": "01",
                    "ccid": "03e09993b7636e52f8f7bb67a746552a",
                    "pay_type_id": "24B2435F18D2B38581D2845E32D14773",
                    "exp_func_code": "2010101",
                    "agency_name": "湖北省果茶办公室",
                    "agency": "219011-湖北省果茶办公室",
                    "bat_num": "0",
                    "frozenamt": 0,
                    "work_flow_id": "budget-total",
                    "fund_type_name": "经费拨款补助",
                    "cur_amt": 0,
                    "bgt_mof_dep_code": "09",
                    "cor_bgt_doc_no": "2024-0401-1512",
                    "pro_cat_code": "1",
                    "pro_id": "A42E27B4640B4234A48DEC69CA3E3156",
                    "bgt_type_name": "预拨指标",
                    "doc_date": "2024-04-01 00:00:00",
                    "pay_type_name": "国库集中支付",
                    "manage_mof_dep_name": "农业处",
                    "dep_bgt_eco_name": "基本工资",
                    "todo_name": "指标下达",
                    "fund_type_id": "DE1C8E16759F474C2D92CBBFB7BA6385",
                    "source_type_id": "A494A01709D991D416528C4C38E90170",
                    "voucher_code": "141001",
                    "is_track": 1,
                    "done_node": "BB39585CD1574D94B7D3DB7553930003",
                    "zdzjjqpt_code": "2",
                    "is_not_control_pay": "2",
                    "clear_amt": 0,
                    "exp_func_id": "A8C36161E5A91CFCC8E039A5F315AA92",
                    "plan_caliber_id": "d90f49adb78db8343547023025efcf4d",
                    "bgt_id": "71617A68FBD7407290063B7B89B221AF",
                    "pay_caliber_id": "71617A68FBD7407290063B7B89B221AF",
                    "xpay_amt": 0,
                    "gov_bgt_eco_id": "543B56A3BE5FC85C7E389E6CFC4A3AB2",
                    "pay_amt": 3,
                    "create_time": "2024-04-02 11:05:43",
                    "is_adjust": 1,
                    "found_type_name": "预估",
                    "budget_level_name": "中央级",
                    "planaviamt": 2000,
                    "threesafe_symbolcat": "000-非“三保”支出",
                    "budget_level_id": "ADFCEF32115CB6261336494BB71CB66D",
                    "pro": "42000024219P007000051-219011指标管理1512",
                    "is_manager": "2",
                    "is_gov_pur_code": "2",
                    "dep_bgt_eco": "F2684D4AE3086DBDA207A71B269729D0##30101##基本工资",
                    "creater": "1F0795D7E8724F998426100EB01D6195",
                    "bgt_doc_title": "219011指标管理1512",
                    "threesafe_symbolcat_name": "非“三保”支出",
                    "fund_type_code": "11111",
                    "origin_model_code": "2",
                    "bgt_source_name": "当期拨款（支出）",
                    "adj_date": "2024-04-02 11:02:54",
                    "useamt": 4,
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
                    "pro_code": "42000024219P007000051",
                    "amount": 100000,
                    "bgt_dec": "219011指标管理1512",
                    "is_end": "1",
                    "exp_func": "2010101-行政运行",
                    "dep_bgt_eco_code": "30101",
                    "gov_bgt_eco_name": "工资奖金津补贴",
                    "plancanuseamt": 1966,
                    "agency_acct_name": "",
                    "agency_acct_no": "",
                    "pay_bank_name": "中国银行股份有限公司武汉水果湖支行",
                    "social_credit_code": "",
                    "pay_acct_name": "湖北省财政厅国库收付局",
                    "payee_acct_name": "中国石化销售股份有限公司湖北武汉石油分公司",
                    "pay_acct_no": "565157523274",
                    "payee_acct_no": "17016201040011294",
                    "pay_acct_bank_name": "中国银行股份有限公司武汉水果湖支行",
                    "payee_acct_bank_name": "农行硚口支行营业室",
                    "payee_acct_code": "",
                    "fund_traobj_type": "9D4021E8DAB4AC98BFE776E3BADDB098##12##与部门外非同级政府单位",
                    "fund_traobj_type_id": "9D4021E8DAB4AC98BFE776E3BADDB098",
                    "fund_traobj_type_code": "12",
                    "fund_traobj_type_name": "与部门外非同级政府单位",
                    "internal_dep": "4C1D9565CB9D48948F89E4784AE804E7##11##办公室",
                    "internal_dep_id": "4C1D9565CB9D48948F89E4784AE804E7",
                    "internal_dep_code": "11",
                    "internal_dep_name": "办公室",
                    "set_mode": "F522AB99C43B9A2A4DD4C30CB75B50C7##1##电子转账支付",
                    "set_mode_id": "F522AB99C43B9A2A4DD4C30CB75B50C7",
                    "set_mode_code": "1",
                    "set_mode_name": "电子转账支付",
                    "use_des": "国库集中支付代编",
                    "pay_app_amt": 3,
                    "pay_app_amt_big": "叁元整",
                    "contract_no": "",
                    "acc_type_id": "D3828BFDBF8EE69B76117257F5C6QXC4",
                    "acc_type_code": "22",
                    "acc_type_name": "财政零余额账户",
                    "is_advancefunds": "2",
                    "pay_acct_id": "0x6A115293F546EB11E7BF33B87B7EDB11F",
                    "pay_acct_code": "104521004200",
                    "pay_bank_id": "7CD841709EB64A53B4D8122509DEA3F2",
                    "pay_bank_code": "104521004200",
                    "attachment_id": "",
                    "plan_balance_id": "1775326015709990912",
                    "fileList": [],
                    "ext": {
                        "is_advancefunds": "2",
                        "is_pural": "0"
                    }
                }
            ]
        }
        zfsqlrdb_insert_data_str = json.dumps(zfsqlrdb_insert_data)
        try:
            zfsqlrdb_insert_start=time.time()   #开始时间
            zfsqlrdb_insert_res = requests.post(zfsqlrdb_insert_url,
                                                        headers=zfsqlrdb_insert_headers,
                                                        data=zfsqlrdb_insert_data_str)
            zfsqlrdb_insert_res_json = zfsqlrdb_insert_res.json()
            zfsqlrdb_insert_end =time.time()   #结束时间
            zfsqlrdb_insert_res_time= zfsqlrdb_insert_end -zfsqlrdb_insert_start
            zfsqlrdb_insert_res_time_ms=  zfsqlrdb_insert_res_time * 1000
            print("\n")
            print(f"响应时间：{zfsqlrdb_insert_res_time_ms}毫秒")

            # print(zfsqlrdb_insert_res.text)
            logss.logger.info("请求参数：{}，{}，{}".format(zfsqlrdb_insert_url,zfsqlrdb_insert_data_str,zfsqlrdb_insert_headers))
            logss.logger.info("返回结果：{}".format(zfsqlrdb_insert_res.text))

            ###断言
            response_rscode = zfsqlrdb_insert_res_json.get('rscode')
            response_result = zfsqlrdb_insert_res_json.get('result')

            ###使用pytest.assume进行断言，失败一个后，可用正常允许其它用例
            # pytest.assume(agency_res.status_code == 200)
            # pytest.assume(response_rscode == 200 )
            # pytest.assume(response_result == "请求成功")

            assert zfsqlrdb_insert_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"
        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s",e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step01)支付申请录入(代编)")
    @allure.title("支付申请录入(代编)：未送审列表")
    def testZfsqlrdbLoadTableDatas(self):
        zfsqlrdb_loadTableDatas_url = base_url + '/payfront/pay-voucher-service/v3/payvoucherbill/loadtabledatas'
        zfsqlrdb_loadTableDatas_headers = {"Content-Type": "application/json",
                                            "tokenid": tokenids}
        zfsqlrdb_loadTableDatas_data = {
            "statusCode": "1",
            "menuId": "01192C92AC1D486498F846947528C4A9",
            "leftTreeCode": "",
            "isHaveZero": "0",
            "appId": "pay_voucher",
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "roleId": "201EC9F7611B11B38E60BA5B10633BDB",
            "params": {
                "accountClsId": "4E72561AB3CD477EB8DFD51813EC2FB2",
                "accountType": "63",
                "isFinancial": "1",
                "cptName": "pay89",
                "batchUserEleType": "1",
                "showContact": "false"
            },
            "pageNum": 1,
            "pageSize": 50,
            "sort": "fi_order asc,create_time desc,pay_cert_no desc",
            "condition": {}
        }

        # 将dict转换为str
        zfsqlrdb_loadTableDatas_data_str = json.dumps(zfsqlrdb_loadTableDatas_data)
        try:
            zfsqlrdb_loadTableDatas_start = time.time()  # 开始时间
            zfsqlrdb_loadTableDatas_res = requests.post(zfsqlrdb_loadTableDatas_url,
                                                         headers=zfsqlrdb_loadTableDatas_headers,
                                                         data=zfsqlrdb_loadTableDatas_data_str)
            zfsqlrdb_loadTableDatas_res_json = zfsqlrdb_loadTableDatas_res.json()
            zfsqlrdb_loadTableDatas_end = time.time()  # 结束时间
            zfsqlrdb_loadTableDatas_res_time = zfsqlrdb_loadTableDatas_end - zfsqlrdb_loadTableDatas_start
            zfsqlrdb_loadTableDatas_res_time_ms = zfsqlrdb_loadTableDatas_res_time * 1000
            print("\n")
            print(f"响应时间：{zfsqlrdb_loadTableDatas_res_time_ms}毫秒")
            # print(zfsqlrdb_loadTableDatas_res.text)

            global zfsqlrdb_id
            zfsqlrdb_id = zfsqlrdb_loadTableDatas_res_json.get("data").get("rows")[0]["id"]
            print("支付数据id：", zfsqlrdb_id)

            global zfsqlrdb_pay_cert_id
            zfsqlrdb_pay_cert_id = zfsqlrdb_loadTableDatas_res_json.get("data").get("rows")[0]["pay_cert_id"]
            print("支付凭证id：",zfsqlrdb_pay_cert_id)

            global zfsqlrdb_pay_cert_no
            zfsqlrdb_pay_cert_no = zfsqlrdb_loadTableDatas_res_json.get("data").get("rows")[0]["pay_cert_no"]
            print("支付凭证号：", zfsqlrdb_pay_cert_no)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(zfsqlrdb_loadTableDatas_url, zfsqlrdb_loadTableDatas_data_str,
                                       zfsqlrdb_loadTableDatas_headers))
            logss.logger.info("返回结果：{}".format(zfsqlrdb_loadTableDatas_res.text))
            ###断言
            response_rscode = zfsqlrdb_loadTableDatas_res_json.get('rscode')
            response_result = zfsqlrdb_loadTableDatas_res_json.get('result')

            # pytest.assume(zfsqlrdb_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert zfsqlrdb_loadTableDatas_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step01)支付申请录入(代编)")
    @allure.title("支付申请录入(代编)：送审")
    def testZfsqlrdbAuditbycheck(self):
        zfsqlrdb_auditbycheck_url = base_url + '/payfront/pay-voucher-service/v3/payvoucherbill/front/action/auditbycheck'
        zfsqlrdb_auditbycheck_headers = {"Content-Type": "application/json",
                                       "tokenid": tokenids}
        zfsqlrdb_auditbycheck_data = {
            "actionName": "送审",
            "appId": "pay_voucher",
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "menuId": "01192C92AC1D486498F846947528C4A9",
            "actionType": "2",
            "glType": "0",
            "ids": [
                zfsqlrdb_id
            ]
        }

        # 将dict转换为str
        zfsqlrdb_auditbycheck_data_str = json.dumps(zfsqlrdb_auditbycheck_data)
        try:
            zfsqlrdb_auditbycheck_start = time.time()  # 开始时间
            zfsqlrdb_auditbycheck_res = requests.post(zfsqlrdb_auditbycheck_url,
                                                    headers=zfsqlrdb_auditbycheck_headers,
                                                    data=zfsqlrdb_auditbycheck_data_str)
            zfsqlrdb_auditbycheck_res_json = zfsqlrdb_auditbycheck_res.json()
            zfsqlrdb_auditbycheck_end = time.time()  # 结束时间
            zfsqlrdb_auditbycheck_res_time = zfsqlrdb_auditbycheck_end - zfsqlrdb_auditbycheck_start
            zfsqlrdb_auditbycheck_res_time_ms = zfsqlrdb_auditbycheck_res_time * 1000
            print("\n")
            print(f"响应时间：{zfsqlrdb_auditbycheck_res_time_ms}毫秒")
            # print(zfsqlrdb_auditbycheck_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(zfsqlrdb_auditbycheck_url, zfsqlrdb_auditbycheck_data_str,
                                       zfsqlrdb_auditbycheck_headers))
            logss.logger.info("返回结果：{}".format(zfsqlrdb_auditbycheck_res.text))
            ###断言
            response_rscode = zfsqlrdb_auditbycheck_res_json.get('rscode')
            response_result = zfsqlrdb_auditbycheck_res_json.get('result')

            # pytest.assume(zfsqlrdb_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert zfsqlrdb_auditbycheck_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step02)支付申请审核(代编)")
    @allure.title("支付申请审核(代编)：审核")
    def testZfsqshdbAuditByWarn(self):
        zfsqshdb_auditByWarn_url = base_url + '/payfront/pay-voucher-service/v3/payvoucherbill/front/action/auditByWarn'
        zfsqshdb_auditByWarn_headers = {"Content-Type": "application/json",
                                       "tokenid": tokenids}
        zfsqshdb_auditByWarn_data = {
            "actionName": "审核",
            "appId": "pay_voucher",
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "menuId": "AAB993F02C1BB4BE78BF47B5EA168EC1",
            "actionType": "2",
            "glType": "0",
            "ids": [
                zfsqlrdb_id
            ],
            "params": {
                "checkReviewAgain": "1"
            }
        }

        # 将dict转换为str
        zfsqshdb_auditByWarn_data_str = json.dumps(zfsqshdb_auditByWarn_data)
        try:
            zfsqshdb_auditByWarn_start = time.time()  # 开始时间
            zfsqshdb_auditByWarn_res = requests.post(zfsqshdb_auditByWarn_url,
                                                    headers=zfsqshdb_auditByWarn_headers,
                                                    data=zfsqshdb_auditByWarn_data_str)
            zfsqshdb_auditByWarn_res_json = zfsqshdb_auditByWarn_res.json()
            zfsqshdb_auditByWarn_end = time.time()  # 结束时间
            zfsqshdb_auditByWarn_res_time = zfsqshdb_auditByWarn_end - zfsqshdb_auditByWarn_start
            zfsqshdb_auditByWarn_res_time_ms = zfsqshdb_auditByWarn_res_time * 1000
            print("\n")
            print(f"响应时间：{zfsqshdb_auditByWarn_res_time_ms}毫秒")
            # print(zfsqshdb_auditByWarn_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(zfsqshdb_auditByWarn_url, zfsqshdb_auditByWarn_data_str,
                                       zfsqshdb_auditByWarn_headers))
            logss.logger.info("返回结果：{}".format(zfsqshdb_auditByWarn_res.text))
            ###断言
            response_rscode = zfsqshdb_auditByWarn_res_json.get('rscode')
            response_result = zfsqshdb_auditByWarn_res_json.get('result')

            # pytest.assume(zblr_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert zfsqshdb_auditByWarn_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step03)支付申请复核(财政)")
    @allure.title("支付申请复核(财政)：审核")
    def testZfsqfhczaudit(self):
        zfsqfhcz_audit_url = base_url + '/payfront/pay-voucher-service/v3/payvoucherbill/action/audit'
        zfsqfhcz_audit_headers = {"Content-Type": "application/json",
                                       "tokenid": tokenids}
        zfsqfhcz_audit_data = {
            "actionName": "审核",
            "appId": "pay_voucher",
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "menuId": "B4BE78BEA168EC1AAB9F47B593F02C1B",
            "actionType": "2",
            "glType": "0",
            "ids": [
                zfsqlrdb_id
            ]

        }

        # 将dict转换为str
        zfsqfhcz_audit_data_str = json.dumps(zfsqfhcz_audit_data)
        try:
            zfsqfhcz_audit_start = time.time()  # 开始时间
            zfsqfhcz_audit_res = requests.post(zfsqfhcz_audit_url,
                                                    headers=zfsqfhcz_audit_headers,
                                                    data=zfsqfhcz_audit_data_str)
            zfsqfhcz_audit_res_json = zfsqfhcz_audit_res.json()
            zfsqfhcz_audit_end = time.time()  # 结束时间
            zfsqfhcz_audit_res_time = zfsqfhcz_audit_end - zfsqfhcz_audit_start
            zfsqfhcz_audit_res_time_ms = zfsqfhcz_audit_res_time * 1000
            print("\n")
            print(f"响应时间：{zfsqfhcz_audit_res_time_ms}毫秒")
            # print(zfsqfhcz_audit_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(zfsqfhcz_audit_url, zfsqfhcz_audit_data_str,
                                       zfsqfhcz_audit_headers))
            logss.logger.info("返回结果：{}".format(zfsqfhcz_audit_res.text))
            ###断言
            response_rscode = zfsqfhcz_audit_res_json.get('rscode')
            response_result = zfsqfhcz_audit_res_json.get('result')

            # pytest.assume(zblr_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert zfsqfhcz_audit_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step04)支付凭证生成(财政)")
    @allure.title("支付凭证生成(财政)：生成")
    def testzfpzscczaudit(self):
        zfpzsccz_audit_url = base_url + '/payfront/pay-voucher-service/v3/payvoucherbill/action/audit'
        zfpzsccz_audit_headers = {"Content-Type": "application/json",
                                       "tokenid": tokenids}
        zfpzsccz_audit_data = {
            "actionName": "生成",
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "appId": "pay_voucher",
            "menuId": "74401623794779F9A2E652311143A04F",
            "actionType": "2",
            "glType": "1",
            "ids": [
                zfsqlrdb_id
            ],
            "params": {
                "picpath": "img/indexpic/voucher_query.png",
                "menuNotRefresh": "true",
                "nextNode": "B198CFFC387EA6D1E1307A101AA5A5F2",
                "accountType": "63",
                "nextWorkflow": "pay_voucher_bill",
                "nextNodes": "B198CFFC387EA6D1E1307A101AA5A5F2",
                "isCreateBill": "1",
                "showContact": "false",
                "contactType": "1"
            }

        }

        # 将dict转换为str
        zfpzsccz_audit_data_str = json.dumps(zfpzsccz_audit_data)
        try:
            zfpzsccz_audit_start = time.time()  # 开始时间
            zfpzsccz_audit_res = requests.post(zfpzsccz_audit_url,
                                                    headers=zfpzsccz_audit_headers,
                                                    data=zfpzsccz_audit_data_str)
            zfpzsccz_audit_res_json = zfpzsccz_audit_res.json()
            zfpzsccz_audit_end = time.time()  # 结束时间
            zfpzsccz_audit_res_time = zfpzsccz_audit_end - zfpzsccz_audit_start
            zfpzsccz_audit_res_time_ms = zfpzsccz_audit_res_time * 1000
            print("\n")
            print(f"响应时间：{zfpzsccz_audit_res_time_ms}毫秒")
            # print(zfpzsccz_audit_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(zfpzsccz_audit_url, zfpzsccz_audit_data_str,
                                       zfpzsccz_audit_headers))
            logss.logger.info("返回结果：{}".format(zfpzsccz_audit_res.text))
            ###断言
            response_rscode = zfpzsccz_audit_res_json.get('rscode')
            response_result = zfpzsccz_audit_res_json.get('result')

            # pytest.assume(zblr_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert zfpzsccz_audit_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step05)支付凭证初审签章(财政)")
    @allure.title("支付凭证初审签章(财政)：获取印章位置")
    def testzfpzcsqzczStampPositions(self):
        zfpzcsqzcz_StampPositions_url = base_url + '/payfront/pay-common-service/v1/queryVoucherSignStampPositions'
        zfpzcsqzcz_StampPositions_headers = {"Content-Type": "application/json",
                                          "tokenid": tokenids}
        zfpzcsqzcz_StampPositions_data = {
            "vtCode": "5214",
            "voucherNoList": [
                zfsqlrdb_pay_cert_no
            ],
            "actionId": "B198CFFC387EA6D1E1307A101AA5A5F2"
        }

        # 将dict转换为str
        zfpzcsqzcz_StampPositions_data_str = json.dumps(zfpzcsqzcz_StampPositions_data)
        try:
            zfpzcsqzcz_StampPositions_start = time.time()  # 开始时间
            zfpzcsqzcz_StampPositions_res = requests.post(zfpzcsqzcz_StampPositions_url,
                                                       headers=zfpzcsqzcz_StampPositions_headers,
                                                       data=zfpzcsqzcz_StampPositions_data_str)
            zfpzcsqzcz_StampPositions_res_json = zfpzcsqzcz_StampPositions_res.json()
            zfpzcsqzcz_StampPositions_end = time.time()  # 结束时间
            zfpzcsqzcz_StampPositions_res_time = zfpzcsqzcz_StampPositions_end - zfpzcsqzcz_StampPositions_start
            zfpzcsqzcz_StampPositions_res_time_ms = zfpzcsqzcz_StampPositions_res_time * 1000
            print("\n")
            print(f"响应时间：{zfpzcsqzcz_StampPositions_res_time_ms}毫秒")
            # print(zfpzcsqzcz_StampPositions_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(zfpzcsqzcz_StampPositions_url, zfpzcsqzcz_StampPositions_data_str,
                                       zfpzcsqzcz_StampPositions_headers))
            logss.logger.info("返回结果：{}".format(zfpzcsqzcz_StampPositions_res.text))
            ###断言
            response_rscode = zfpzcsqzcz_StampPositions_res_json.get('rscode')
            response_result = zfpzcsqzcz_StampPositions_res_json.get('result')

            # pytest.assume(zblr_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert zfpzcsqzcz_StampPositions_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step05)支付凭证初审签章(财政)")
    @allure.title("支付凭证初审签章(财政)：获取签名参数")
    def testzfpzcsqzczepayHttpParams(self):
        zfpzcsqzcz_epayHttpParams_url = base_url + '/payfront/pay-common-service/v1/epayHttpParams'
        zfpzcsqzcz_epayHttpParams_headers = {"Content-Type": "application/json",
                                          "tokenid": tokenids}
        zfpzcsqzcz_epayHttpParams_data = {
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "opid": "B198CFFC387EA6D1E1307A101AA5A5F258CAB89AF1A04EF3B7E19C1DBCFDA502",
            "bill_no": [
                zfsqlrdb_pay_cert_no
            ],
            "payBusTypeCodes": [
                "1"
            ],
            "action_id": "B198CFFC387EA6D1E1307A101AA5A5F2",
            "work_flow_id": "pay_voucher_bill",
            "isDoWorkFlow": 'true',
            "isSignStamp": 'true',
            "appId": "pay_voucher",
            "menuId": "B198CFFC387EA6D1E1307A101AA5A5F2",
            "actionType": "2",
            "actionName": "直接签章",
            "vtCode": "5214",
            "glType": "0",
            "ids": [
                zfsqlrdb_pay_cert_id
            ],
            "stampurl": "pay-voucher-service/v3/payvoucherbill/action/stamp",
            "admDivCode": "420000000",
            "justShow": 'false'
        }

        # 将dict转换为str
        zfpzcsqzcz_epayHttpParams_data_str = json.dumps(zfpzcsqzcz_epayHttpParams_data)
        try:
            zfpzcsqzcz_epayHttpParams_start = time.time()  # 开始时间
            zfpzcsqzcz_epayHttpParams_res = requests.post(zfpzcsqzcz_epayHttpParams_url,
                                                       headers=zfpzcsqzcz_epayHttpParams_headers,
                                                       data=zfpzcsqzcz_epayHttpParams_data_str)
            zfpzcsqzcz_epayHttpParams_res_json = zfpzcsqzcz_epayHttpParams_res.json()
            zfpzcsqzcz_epayHttpParams_end = time.time()  # 结束时间
            zfpzcsqzcz_epayHttpParams_res_time = zfpzcsqzcz_epayHttpParams_end - zfpzcsqzcz_epayHttpParams_start
            zfpzcsqzcz_epayHttpParams_res_time_ms = zfpzcsqzcz_epayHttpParams_res_time * 1000
            print("\n")
            print(f"响应时间：{zfpzcsqzcz_epayHttpParams_res_time_ms}毫秒")
            # print(zfpzcsqzcz_epayHttpParams_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(zfpzcsqzcz_epayHttpParams_url, zfpzcsqzcz_epayHttpParams_data_str,
                                       zfpzcsqzcz_epayHttpParams_headers))
            logss.logger.info("返回结果：{}".format(zfpzcsqzcz_epayHttpParams_res.text))
            ###断言
            response_rscode = zfpzcsqzcz_epayHttpParams_res_json.get('rscode')
            response_result = zfpzcsqzcz_epayHttpParams_res_json.get('result')

            # pytest.assume(zblr_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert zfpzcsqzcz_epayHttpParams_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step05)支付凭证初审签章(财政)")
    @allure.title("支付凭证初审签章(财政)：签名")
    def testzfpzcsqzczsign(self):
        zfpzcsqzcz_sign_url = base_url + '/payfront/pay-voucher-service/v3/payvoucherbill/action/sign'
        zfpzcsqzcz_sign_headers = {"Content-Type": "application/json",
                                          "tokenid": tokenids}
        zfpzcsqzcz_sign_data = {
            "vt_code": "5214",
            "vouchers": "<?xml version=\"1.0\" encoding=\"GBK\" ?>\n<MOF>\n    <VoucherCount>1</VoucherCount>\n    <VoucherBody VoucherNo=\"zfsqlrdb_pay_cert_no\" AdmDivCode=\"420000\" StYear=\"2024\" VtCode=\"5214\">\n        <VoucherFlag>0</VoucherFlag>\n        <Voucher>PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iR0JLIj8+Cgo8Vm91Y2hlcj4KICA8SWQ+NThDQUI4OUFGMUEwNEVGM0I3RTE5QzFEQkNGREE1MDI8L0lkPgogIDxBZG1EaXZDb2RlPjQyMDAwMDwvQWRtRGl2Q29kZT4KICA8U3RZZWFyPjIwMjQ8L1N0WWVhcj4KICA8VnRDb2RlPjUyMTQ8L1Z0Q29kZT4KICA8Vm91RGF0ZT4yMDI0MDQwODwvVm91RGF0ZT4KICA8Vm91Y2hlck5vPlcwMDI0QzEwMDAwMDU0PC9Wb3VjaGVyTm8+CiAgPEJpbGxObz5TUVcwMDI0MTgwMDAwMDY8L0JpbGxObz4KICA8RnVuZFR5cGVDb2RlPjExMTExPC9GdW5kVHlwZUNvZGU+CiAgPEZ1bmRUeXBlTmFtZT6+rbfRsqa/7rK51vo8L0Z1bmRUeXBlTmFtZT4KICA8Qmd0VHlwZUNvZGU+MTE8L0JndFR5cGVDb2RlPgogIDxCZ3RUeXBlTmFtZT7UpLKm1rix6jwvQmd0VHlwZU5hbWU+CiAgPFBheVR5cGVDb2RlPjE8L1BheVR5cGVDb2RlPgogIDxQYXlUeXBlTmFtZT65+r/ivK/W0NanuLY8L1BheVR5cGVOYW1lPgogIDxQcm9DYXRDb2RlPjwvUHJvQ2F0Q29kZT4KICA8UHJvQ2F0TmFtZT48L1Byb0NhdE5hbWU+CiAgPE1PRkRlcENvZGU+MDk8L01PRkRlcENvZGU+CiAgPE1PRkRlcE5hbWU+xanStbSmPC9NT0ZEZXBOYW1lPgogIDxTdXBEZXBDb2RlPjIxOTwvU3VwRGVwQ29kZT4KICA8U3VwRGVwTmFtZT66/rGxyqHFqdK1xam05cz8PC9TdXBEZXBOYW1lPgogIDxBZ2VuY3lDb2RlPjIxOTAxMTwvQWdlbmN5Q29kZT4KICA8QWdlbmN5TmFtZT66/rGxyqG5+7LosOy5q8rSPC9BZ2VuY3lOYW1lPgogIDxFeHBGdW5jQ29kZT4yMDEwMTAxPC9FeHBGdW5jQ29kZT4KICA8RXhwRnVuY05hbWU+0NDV/tTL0NA8L0V4cEZ1bmNOYW1lPgogIDxFeHBGdW5jQ29kZTE+MjAxPC9FeHBGdW5jQ29kZTE+CiAgPEV4cEZ1bmNOYW1lMT7Su7Djuau5srf+zvHWp7P2PC9FeHBGdW5jTmFtZTE+CiAgPEV4cEZ1bmNDb2RlMj4wMTwvRXhwRnVuY0NvZGUyPgogIDxFeHBGdW5jTmFtZTI+yMu088rCzvE8L0V4cEZ1bmNOYW1lMj4KICA8RXhwRnVuY0NvZGUzPjAxPC9FeHBGdW5jQ29kZTM+CiAgPEV4cEZ1bmNOYW1lMz7Q0NX+1MvQ0DwvRXhwRnVuY05hbWUzPgogIDxHb3ZFeHBFY29Db2RlPjwvR292RXhwRWNvQ29kZT4KICA8R292RXhwRWNvTmFtZT48L0dvdkV4cEVjb05hbWU+CiAgPERlcEV4cEVjb0NvZGU+MzAxMDE8L0RlcEV4cEVjb0NvZGU+CiAgPERlcEV4cEVjb05hbWU+u/mxvrmk18o8L0RlcEV4cEVjb05hbWU+CiAgPERlcFByb0NvZGU+NDIwMDAwMjQyMTlQMDA3MDAwMDUxPC9EZXBQcm9Db2RlPgogIDxEZXBQcm9OYW1lPjIxOTAxMda4seq53MDtMTUxMjwvRGVwUHJvTmFtZT4KICA8U2V0TW9kZUNvZGU+MTwvU2V0TW9kZUNvZGU+CiAgPFNldE1vZGVOYW1lPrXn19PXqtXL1qe4tjwvU2V0TW9kZU5hbWU+CiAgPFBheUJhbmtDb2RlPjEwNDUyMTAwNDIwMDwvUGF5QmFua0NvZGU+CiAgPFBheUJhbmtOYW1lPtbQufrS+NDQucm33dPQz965q8u+zuS6usuuufu6/tan0NA8L1BheUJhbmtOYW1lPgogIDxDbGVhckJhbmtDb2RlPjwvQ2xlYXJCYW5rQ29kZT4KICA8Q2xlYXJCYW5rTmFtZT48L0NsZWFyQmFua05hbWU+CiAgPENsZWFyQWNjdE5vPjwvQ2xlYXJBY2N0Tm8+CiAgPENsZWFyQWNjdE5hbWU+PC9DbGVhckFjY3ROYW1lPgogIDxDbGVhckFjY3RCYW5rTmFtZT48L0NsZWFyQWNjdEJhbmtOYW1lPgogIDxQYXllZUFjY3RObz4xNzAxNjIwMTA0MDAxMTI5NDwvUGF5ZWVBY2N0Tm8+CiAgPFBheWVlQWNjdE5hbWU+1tC5+sqvu6/P+srbucm33dPQz965q8u+uv6xsc7kurrKr9PNt9a5q8u+PC9QYXllZUFjY3ROYW1lPgogIDxQYXllZUFjY3RCYW5rTmFtZT7FqdDQs36/2tan0NDTqtK1ytI8L1BheWVlQWNjdEJhbmtOYW1lPgogIDxQYXllZUFjY3RCYW5rTm8+PC9QYXllZUFjY3RCYW5rTm8+CiAgPFBheUFjY3RObz41NjUxNTc1MjMyNzQ8L1BheUFjY3RObz4KICA8UGF5QWNjdE5hbWU+uv6xscqhssbV/sz8ufq/4srVuLa+1jwvUGF5QWNjdE5hbWU+CiAgPFBheUFjY3RCYW5rTmFtZT7W0Ln60vjQ0LnJt93T0M/euavLvs7kurrLrrn7uv7Wp9DQPC9QYXlBY2N0QmFua05hbWU+CiAgPFBheVN1bW1hcnlDb2RlPjwvUGF5U3VtbWFyeUNvZGU+CiAgPFBheVN1bW1hcnlOYW1lPrn6v+K8r9bQ1qe4trT6seA8L1BheVN1bW1hcnlOYW1lPgogIDxQYXlBbXQ+My4wMDwvUGF5QW10PgogIDxCdXNpbmVzc1R5cGVDb2RlPjE8L0J1c2luZXNzVHlwZUNvZGU+CiAgPEJ1c2luZXNzVHlwZU5hbWU+xtXNqNK1zvE8L0J1c2luZXNzVHlwZU5hbWU+CiAgPFRheEJpbGxObz48L1RheEJpbGxObz4KICA8VGF4YXllcklEPjwvVGF4YXllcklEPgogIDxUYXhPcmdDb2RlPjwvVGF4T3JnQ29kZT4KICA8R292UHJvY3VyZW1lbnRJRD48L0dvdlByb2N1cmVtZW50SUQ+CiAgPENoZWNrTm8+PC9DaGVja05vPgogIDxQYXlDb2RlPjwvUGF5Q29kZT4KICA8Rm9yZWlnbkFtdD4wPC9Gb3JlaWduQW10PgogIDxDdXJyZW5jeUNvZGU+Q05ZPC9DdXJyZW5jeUNvZGU+CiAgPEVzdFJhdD48L0VzdFJhdD4KICA8QW10VW5pdD48L0FtdFVuaXQ+CiAgPFhQYXlEYXRlPjwvWFBheURhdGU+CiAgPFhBZ2VudEJ1c2luZXNzTm8+PC9YQWdlbnRCdXNpbmVzc05vPgogIDxYQ2hlY2tObz48L1hDaGVja05vPgogIDxYUGF5QW10PjA8L1hQYXlBbXQ+CiAgPFhQYXllZUFjY3RCYW5rTmFtZT48L1hQYXllZUFjY3RCYW5rTmFtZT4KICA8WFBheWVlQWNjdE5vPjwvWFBheWVlQWNjdE5vPgogIDxYUGF5ZWVBY2N0TmFtZT48L1hQYXllZUFjY3ROYW1lPgogIDxIb2xkMT4xMjwvSG9sZDE+CiAgPEhvbGQyPjwvSG9sZDI+CiAgPERldGFpbExpc3Q+CiAgICA8RGV0YWlsPgogICAgICA8SWQ+RDk1NEZBMjJBMDUzNEQ2RUEwRDI5RDVBOUJGODZFNEY8L0lkPgogICAgICA8Vm91Y2hlckJpbGxJZD41OENBQjg5QUYxQTA0RUYzQjdFMTlDMURCQ0ZEQTUwMjwvVm91Y2hlckJpbGxJZD4KICAgICAgPFZvdWNoZXJCaWxsTm8+VzAwMjRDMTAwMDAwNTQ8L1ZvdWNoZXJCaWxsTm8+CiAgICAgIDxWb3VjaGVyRGV0YWlsTm8+U1FXMDAyNDE4MDAwMDA2PC9Wb3VjaGVyRGV0YWlsTm8+CiAgICAgIDxGdW5kVHlwZUNvZGU+MTExMTE8L0Z1bmRUeXBlQ29kZT4KICAgICAgPEZ1bmRUeXBlTmFtZT6+rbfRsqa/7rK51vo8L0Z1bmRUeXBlTmFtZT4KICAgICAgPEJndFR5cGVDb2RlPjExPC9CZ3RUeXBlQ29kZT4KICAgICAgPEJndFR5cGVOYW1lPtSksqbWuLHqPC9CZ3RUeXBlTmFtZT4KICAgICAgPFByb0NhdENvZGU+PC9Qcm9DYXRDb2RlPgogICAgICA8UHJvQ2F0TmFtZT48L1Byb0NhdE5hbWU+CiAgICAgIDxQYXlLaW5kQ29kZT48L1BheUtpbmRDb2RlPgogICAgICA8UGF5S2luZE5hbWU+PC9QYXlLaW5kTmFtZT4KICAgICAgPE1PRkRlcENvZGU+PC9NT0ZEZXBDb2RlPgogICAgICA8TU9GRGVwTmFtZT48L01PRkRlcE5hbWU+CiAgICAgIDxTdXBEZXBDb2RlPjIxOTwvU3VwRGVwQ29kZT4KICAgICAgPFN1cERlcE5hbWU+uv6xscqhxanStcWptOXM/DwvU3VwRGVwTmFtZT4KICAgICAgPEFnZW5jeUNvZGU+MjE5MDExPC9BZ2VuY3lDb2RlPgogICAgICA8QWdlbmN5TmFtZT66/rGxyqG5+7LosOy5q8rSPC9BZ2VuY3lOYW1lPgogICAgICA8RXhwRnVuY0NvZGU+MjAxMDEwMTwvRXhwRnVuY0NvZGU+CiAgICAgIDxFeHBGdW5jTmFtZT7Q0NX+1MvQ0DwvRXhwRnVuY05hbWU+CiAgICAgIDxHb3ZFeHBFY29Db2RlPjwvR292RXhwRWNvQ29kZT4KICAgICAgPEdvdkV4cEVjb05hbWU+PC9Hb3ZFeHBFY29OYW1lPgogICAgICA8RGVwRXhwRWNvQ29kZT48L0RlcEV4cEVjb0NvZGU+CiAgICAgIDxEZXBFeHBFY29OYW1lPjwvRGVwRXhwRWNvTmFtZT4KICAgICAgPERlcFByb0NvZGU+PC9EZXBQcm9Db2RlPgogICAgICA8RGVwUHJvTmFtZT48L0RlcFByb05hbWU+CiAgICAgIDxQYXllZUFjY3RObz4xNzAxNjIwMTA0MDAxMTI5NDwvUGF5ZWVBY2N0Tm8+CiAgICAgIDxQYXllZUFjY3ROYW1lPtbQufrKr7uvz/rK27nJt93T0M/euavLvrr+sbHO5Lq6yq/TzbfWuavLvjwvUGF5ZWVBY2N0TmFtZT4KICAgICAgPFBheWVlQWNjdEJhbmtOYW1lPsWp0NCzfr/a1qfQ0NOq0rXK0jwvUGF5ZWVBY2N0QmFua05hbWU+CiAgICAgIDxQYXllZUFjY3RCYW5rTm8+PC9QYXllZUFjY3RCYW5rTm8+CiAgICAgIDxUcmFja2luZ0lEPjwvVHJhY2tpbmdJRD4KICAgICAgPFBheUFtdD4zLjAwPC9QYXlBbXQ+CiAgICAgIDxSZW1hcms+PC9SZW1hcms+CiAgICAgIDxGb3JlaWduQW10PjA8L0ZvcmVpZ25BbXQ+CiAgICAgIDxDdXJyZW5jeUNvZGU+Q05ZPC9DdXJyZW5jeUNvZGU+CiAgICAgIDxFc3RSYXQ+PC9Fc3RSYXQ+CiAgICAgIDxSZWNlaXZlckNvZGU+PC9SZWNlaXZlckNvZGU+CiAgICAgIDxBbXRVbml0PjwvQW10VW5pdD4KICAgICAgPFhQYXlEYXRlPjwvWFBheURhdGU+CiAgICAgIDxYQWdlbnRCdXNpbmVzc05vPjwvWEFnZW50QnVzaW5lc3NObz4KICAgICAgPFhDaGVja05vPjwvWENoZWNrTm8+CiAgICAgIDxYUGF5QW10PjwvWFBheUFtdD4KICAgICAgPFhBZGRXb3JkPjwvWEFkZFdvcmQ+CiAgICAgIDxYUGF5ZWVBY2N0QmFua05hbWU+PC9YUGF5ZWVBY2N0QmFua05hbWU+CiAgICAgIDxYUGF5ZWVBY2N0Tm8+PC9YUGF5ZWVBY2N0Tm8+CiAgICAgIDxYUGF5ZWVBY2N0TmFtZT48L1hQYXllZUFjY3ROYW1lPgogICAgICA8SG9sZDE+PC9Ib2xkMT4KICAgICAgPEhvbGQyPjwvSG9sZDI+CiAgICAgIDxIb2xkMz48L0hvbGQzPgogICAgICA8SG9sZDQ+PC9Ib2xkND4KICAgIDwvRGV0YWlsPgogIDwvRGV0YWlsTGlzdD4KPC9Wb3VjaGVyPgo=</Voucher>\n        <SignStampList>\n            <SignStamp No=\"cz_dwgz\" SN=\"0850ada9e8e443089a30b3fc606d70b2\">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</SignStamp>\n        </SignStampList>\n        <SignatureList />\n    </VoucherBody>\n</MOF>\n",
            "details": "",
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "opid": "B198CFFC387EA6D1E1307A101AA5A5F258CAB89AF1A04EF3B7E19C1DBCFDA502",
            "bill_no": "",
            "payBusTypeCodes": [
                "1"
            ],
            "action_id": "B198CFFC387EA6D1E1307A101AA5A5F2",
            "work_flow_id": "pay_voucher_bill",
            "isDoWorkFlow": 'true',
            "isSignStamp": 'true',
            "appId": "pay_voucher",
            "menuId": "B198CFFC387EA6D1E1307A101AA5A5F2",
            "actionType": "2",
            "actionName": "直接签章",
            "vtCode": "5214",
            "glType": "0",
            "ids": [
                zfsqlrdb_pay_cert_id
            ],
            "stampurl": "pay-voucher-service/v3/payvoucherbill/action/stamp",
            "admDivCode": "420000000",
            "justShow": 'false',
            "voucherNos": [
                zfsqlrdb_pay_cert_no
            ]
        }

        # 将dict转换为str
        zfpzcsqzcz_sign_data_str = json.dumps(zfpzcsqzcz_sign_data)
        try:
            zfpzcsqzcz_sign_start = time.time()  # 开始时间
            zfpzcsqzcz_sign_res = requests.post(zfpzcsqzcz_sign_url,
                                                       headers=zfpzcsqzcz_sign_headers,
                                                       data=zfpzcsqzcz_sign_data_str)
            zfpzcsqzcz_sign_res_json = zfpzcsqzcz_sign_res.json()
            zfpzcsqzcz_sign_end = time.time()  # 结束时间
            zfpzcsqzcz_sign_res_time = zfpzcsqzcz_sign_end - zfpzcsqzcz_sign_start
            zfpzcsqzcz_sign_res_time_ms = zfpzcsqzcz_sign_res_time * 1000
            print("\n")
            print(f"响应时间：{zfpzcsqzcz_sign_res_time_ms}毫秒")
            # print(zfpzcsqzcz_sign_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(zfpzcsqzcz_sign_url, zfpzcsqzcz_sign_data_str,
                                       zfpzcsqzcz_sign_headers))
            logss.logger.info("返回结果：{}".format(zfpzcsqzcz_sign_res.text))
            ###断言
            response_rscode = zfpzcsqzcz_sign_res_json.get('rscode')
            response_result = zfpzcsqzcz_sign_res_json.get('result')

            # pytest.assume(zblr_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert zfpzcsqzcz_sign_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step06)支付凭证复核签章(财政)")
    @allure.title("支付凭证复核签章(财政)：获取印章位置")
    def testzfpzfhqzczStampPositions(self):
        zfpzfhqzcz_StampPositions_url = base_url + '/payfront/pay-common-service/v1/queryVoucherSignStampPositions'
        zfpzfhqzcz_StampPositions_headers = {"Content-Type": "application/json",
                                          "tokenid": tokenids}
        zfpzfhqzcz_StampPositions_data = {
            "vtCode": "5214",
            "voucherNoList": [
                zfsqlrdb_pay_cert_no
            ],
            "actionId": "60D0E448D73949A28EB2C188B8D2333E"
        }

        # 将dict转换为str
        zfpzfhqzcz_StampPositions_data_str = json.dumps(zfpzfhqzcz_StampPositions_data)
        try:
            zfpzfhqzcz_StampPositions_start = time.time()  # 开始时间
            zfpzfhqzcz_StampPositions_res = requests.post(zfpzfhqzcz_StampPositions_url,
                                                       headers=zfpzfhqzcz_StampPositions_headers,
                                                       data=zfpzfhqzcz_StampPositions_data_str)
            zfpzfhqzcz_StampPositions_res_json = zfpzfhqzcz_StampPositions_res.json()
            zfpzfhqzcz_StampPositions_end = time.time()  # 结束时间
            zfpzfhqzcz_StampPositions_res_time = zfpzfhqzcz_StampPositions_end - zfpzfhqzcz_StampPositions_start
            zfpzfhqzcz_StampPositions_res_time_ms = zfpzfhqzcz_StampPositions_res_time * 1000
            print("\n")
            print(f"响应时间：{zfpzfhqzcz_StampPositions_res_time_ms}毫秒")
            # print(zfpzfhqzcz_StampPositions_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(zfpzfhqzcz_StampPositions_url, zfpzfhqzcz_StampPositions_data_str,
                                       zfpzfhqzcz_StampPositions_headers))
            logss.logger.info("返回结果：{}".format(zfpzfhqzcz_StampPositions_res.text))
            ###断言
            response_rscode = zfpzfhqzcz_StampPositions_res_json.get('rscode')
            response_result = zfpzfhqzcz_StampPositions_res_json.get('result')

            # pytest.assume(zblr_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert zfpzfhqzcz_StampPositions_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step06)支付凭证复核签章(财政)")
    @allure.title("支付凭证复核签章(财政)：获取签章参数")
    def testzfpzfhqzczepayHttpParams(self):
        zfpzfhqzcz_epayHttpParams_url = base_url + '/payfront/pay-common-service/v1/epayHttpParams'
        zfpzfhqzcz_epayHttpParams_headers = {"Content-Type": "application/json",
                                          "tokenid": tokenids}
        zfpzfhqzcz_epayHttpParams_data = {
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "opid": "60D0E448D73949A28EB2C188B8D2333E58CAB89AF1A04EF3B7E19C1DBCFDA502",
            "bill_no": [
                zfsqlrdb_pay_cert_no
            ],
            "payBusTypeCodes": [
                "1"
            ],
            "action_id": "60D0E448D73949A28EB2C188B8D2333E",
            "work_flow_id": "pay_voucher_bill",
            "isDoWorkFlow": 'true',
            "isSignStamp": 'true',
            "appId": "pay_voucher",
            "menuId": "60D0E448D73949A28EB2C188B8D2333E",
            "actionType": "2",
            "actionName": "直接签章",
            "vtCode": "5214",
            "glType": "0",
            "ids": [
                zfsqlrdb_pay_cert_id
            ],
            "stampurl": "pay-voucher-service/v3/payvoucherbill/action/stamp",
            "admDivCode": "420000000",
            "justShow": 'false'
        }

        # 将dict转换为str
        zfpzfhqzcz_epayHttpParams_data_str = json.dumps(zfpzfhqzcz_epayHttpParams_data)
        try:
            zfpzfhqzcz_epayHttpParams_start = time.time()  # 开始时间
            zfpzfhqzcz_epayHttpParams_res = requests.post(zfpzfhqzcz_epayHttpParams_url,
                                                       headers=zfpzfhqzcz_epayHttpParams_headers,
                                                       data=zfpzfhqzcz_epayHttpParams_data_str)
            zfpzfhqzcz_epayHttpParams_res_json = zfpzfhqzcz_epayHttpParams_res.json()
            zfpzfhqzcz_epayHttpParams_end = time.time()  # 结束时间
            zfpzfhqzcz_epayHttpParams_res_time = zfpzfhqzcz_epayHttpParams_end - zfpzfhqzcz_epayHttpParams_start
            zfpzfhqzcz_epayHttpParams_res_time_ms = zfpzfhqzcz_epayHttpParams_res_time * 1000
            print("\n")
            print(f"响应时间：{zfpzfhqzcz_epayHttpParams_res_time_ms}毫秒")
            # print(zfpzfhqzcz_epayHttpParams_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(zfpzfhqzcz_epayHttpParams_url, zfpzfhqzcz_epayHttpParams_data_str,
                                       zfpzfhqzcz_epayHttpParams_headers))
            logss.logger.info("返回结果：{}".format(zfpzfhqzcz_epayHttpParams_res.text))
            ###断言
            response_rscode = zfpzfhqzcz_epayHttpParams_res_json.get('rscode')
            response_result = zfpzfhqzcz_epayHttpParams_res_json.get('result')

            # pytest.assume(zblr_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert zfpzfhqzcz_epayHttpParams_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step06)支付凭证复核签章(财政)")
    @allure.title("支付凭证复核签章(财政)：签章")
    def testzfpzfhqzczstamp(self):
        zfpzfhqzcz_stamp_url = base_url + '/payfront/pay-voucher-service/v3/payvoucherbill/action/stamp'
        zfpzfhqzcz_stamp_headers = {"Content-Type": "application/json",
                                          "tokenid": tokenids}
        zfpzfhqzcz_stamp_data = {
            "vt_code": "5214",
            "vouchers": "<?xml version=\"1.0\" encoding=\"GBK\" ?>\n<MOF>\n    <VoucherCount>1</VoucherCount>\n    <VoucherBody VoucherNo=\"zfsqlrdb_pay_cert_no\" AdmDivCode=\"420000\" StYear=\"2024\" VtCode=\"5214\">\n        <VoucherFlag>0</VoucherFlag>\n        <Voucher>PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iR0JLIj8+Cgo8Vm91Y2hlcj4KICA8SWQ+NThDQUI4OUFGMUEwNEVGM0I3RTE5QzFEQkNGREE1MDI8L0lkPgogIDxBZG1EaXZDb2RlPjQyMDAwMDwvQWRtRGl2Q29kZT4KICA8U3RZZWFyPjIwMjQ8L1N0WWVhcj4KICA8VnRDb2RlPjUyMTQ8L1Z0Q29kZT4KICA8Vm91RGF0ZT4yMDI0MDQwODwvVm91RGF0ZT4KICA8Vm91Y2hlck5vPlcwMDI0QzEwMDAwMDU0PC9Wb3VjaGVyTm8+CiAgPEJpbGxObz5TUVcwMDI0MTgwMDAwMDY8L0JpbGxObz4KICA8RnVuZFR5cGVDb2RlPjExMTExPC9GdW5kVHlwZUNvZGU+CiAgPEZ1bmRUeXBlTmFtZT6+rbfRsqa/7rK51vo8L0Z1bmRUeXBlTmFtZT4KICA8Qmd0VHlwZUNvZGU+MTE8L0JndFR5cGVDb2RlPgogIDxCZ3RUeXBlTmFtZT7UpLKm1rix6jwvQmd0VHlwZU5hbWU+CiAgPFBheVR5cGVDb2RlPjE8L1BheVR5cGVDb2RlPgogIDxQYXlUeXBlTmFtZT65+r/ivK/W0NanuLY8L1BheVR5cGVOYW1lPgogIDxQcm9DYXRDb2RlPjwvUHJvQ2F0Q29kZT4KICA8UHJvQ2F0TmFtZT48L1Byb0NhdE5hbWU+CiAgPE1PRkRlcENvZGU+MDk8L01PRkRlcENvZGU+CiAgPE1PRkRlcE5hbWU+xanStbSmPC9NT0ZEZXBOYW1lPgogIDxTdXBEZXBDb2RlPjIxOTwvU3VwRGVwQ29kZT4KICA8U3VwRGVwTmFtZT66/rGxyqHFqdK1xam05cz8PC9TdXBEZXBOYW1lPgogIDxBZ2VuY3lDb2RlPjIxOTAxMTwvQWdlbmN5Q29kZT4KICA8QWdlbmN5TmFtZT66/rGxyqG5+7LosOy5q8rSPC9BZ2VuY3lOYW1lPgogIDxFeHBGdW5jQ29kZT4yMDEwMTAxPC9FeHBGdW5jQ29kZT4KICA8RXhwRnVuY05hbWU+0NDV/tTL0NA8L0V4cEZ1bmNOYW1lPgogIDxFeHBGdW5jQ29kZTE+MjAxPC9FeHBGdW5jQ29kZTE+CiAgPEV4cEZ1bmNOYW1lMT7Su7Djuau5srf+zvHWp7P2PC9FeHBGdW5jTmFtZTE+CiAgPEV4cEZ1bmNDb2RlMj4wMTwvRXhwRnVuY0NvZGUyPgogIDxFeHBGdW5jTmFtZTI+yMu088rCzvE8L0V4cEZ1bmNOYW1lMj4KICA8RXhwRnVuY0NvZGUzPjAxPC9FeHBGdW5jQ29kZTM+CiAgPEV4cEZ1bmNOYW1lMz7Q0NX+1MvQ0DwvRXhwRnVuY05hbWUzPgogIDxHb3ZFeHBFY29Db2RlPjwvR292RXhwRWNvQ29kZT4KICA8R292RXhwRWNvTmFtZT48L0dvdkV4cEVjb05hbWU+CiAgPERlcEV4cEVjb0NvZGU+MzAxMDE8L0RlcEV4cEVjb0NvZGU+CiAgPERlcEV4cEVjb05hbWU+u/mxvrmk18o8L0RlcEV4cEVjb05hbWU+CiAgPERlcFByb0NvZGU+NDIwMDAwMjQyMTlQMDA3MDAwMDUxPC9EZXBQcm9Db2RlPgogIDxEZXBQcm9OYW1lPjIxOTAxMda4seq53MDtMTUxMjwvRGVwUHJvTmFtZT4KICA8U2V0TW9kZUNvZGU+MTwvU2V0TW9kZUNvZGU+CiAgPFNldE1vZGVOYW1lPrXn19PXqtXL1qe4tjwvU2V0TW9kZU5hbWU+CiAgPFBheUJhbmtDb2RlPjEwNDUyMTAwNDIwMDwvUGF5QmFua0NvZGU+CiAgPFBheUJhbmtOYW1lPtbQufrS+NDQucm33dPQz965q8u+zuS6usuuufu6/tan0NA8L1BheUJhbmtOYW1lPgogIDxDbGVhckJhbmtDb2RlPjwvQ2xlYXJCYW5rQ29kZT4KICA8Q2xlYXJCYW5rTmFtZT48L0NsZWFyQmFua05hbWU+CiAgPENsZWFyQWNjdE5vPjwvQ2xlYXJBY2N0Tm8+CiAgPENsZWFyQWNjdE5hbWU+PC9DbGVhckFjY3ROYW1lPgogIDxDbGVhckFjY3RCYW5rTmFtZT48L0NsZWFyQWNjdEJhbmtOYW1lPgogIDxQYXllZUFjY3RObz4xNzAxNjIwMTA0MDAxMTI5NDwvUGF5ZWVBY2N0Tm8+CiAgPFBheWVlQWNjdE5hbWU+1tC5+sqvu6/P+srbucm33dPQz965q8u+uv6xsc7kurrKr9PNt9a5q8u+PC9QYXllZUFjY3ROYW1lPgogIDxQYXllZUFjY3RCYW5rTmFtZT7FqdDQs36/2tan0NDTqtK1ytI8L1BheWVlQWNjdEJhbmtOYW1lPgogIDxQYXllZUFjY3RCYW5rTm8+PC9QYXllZUFjY3RCYW5rTm8+CiAgPFBheUFjY3RObz41NjUxNTc1MjMyNzQ8L1BheUFjY3RObz4KICA8UGF5QWNjdE5hbWU+uv6xscqhssbV/sz8ufq/4srVuLa+1jwvUGF5QWNjdE5hbWU+CiAgPFBheUFjY3RCYW5rTmFtZT7W0Ln60vjQ0LnJt93T0M/euavLvs7kurrLrrn7uv7Wp9DQPC9QYXlBY2N0QmFua05hbWU+CiAgPFBheVN1bW1hcnlDb2RlPjwvUGF5U3VtbWFyeUNvZGU+CiAgPFBheVN1bW1hcnlOYW1lPrn6v+K8r9bQ1qe4trT6seA8L1BheVN1bW1hcnlOYW1lPgogIDxQYXlBbXQ+My4wMDwvUGF5QW10PgogIDxCdXNpbmVzc1R5cGVDb2RlPjE8L0J1c2luZXNzVHlwZUNvZGU+CiAgPEJ1c2luZXNzVHlwZU5hbWU+xtXNqNK1zvE8L0J1c2luZXNzVHlwZU5hbWU+CiAgPFRheEJpbGxObz48L1RheEJpbGxObz4KICA8VGF4YXllcklEPjwvVGF4YXllcklEPgogIDxUYXhPcmdDb2RlPjwvVGF4T3JnQ29kZT4KICA8R292UHJvY3VyZW1lbnRJRD48L0dvdlByb2N1cmVtZW50SUQ+CiAgPENoZWNrTm8+PC9DaGVja05vPgogIDxQYXlDb2RlPjwvUGF5Q29kZT4KICA8Rm9yZWlnbkFtdD4wPC9Gb3JlaWduQW10PgogIDxDdXJyZW5jeUNvZGU+Q05ZPC9DdXJyZW5jeUNvZGU+CiAgPEVzdFJhdD48L0VzdFJhdD4KICA8QW10VW5pdD48L0FtdFVuaXQ+CiAgPFhQYXlEYXRlPjwvWFBheURhdGU+CiAgPFhBZ2VudEJ1c2luZXNzTm8+PC9YQWdlbnRCdXNpbmVzc05vPgogIDxYQ2hlY2tObz48L1hDaGVja05vPgogIDxYUGF5QW10PjA8L1hQYXlBbXQ+CiAgPFhQYXllZUFjY3RCYW5rTmFtZT48L1hQYXllZUFjY3RCYW5rTmFtZT4KICA8WFBheWVlQWNjdE5vPjwvWFBheWVlQWNjdE5vPgogIDxYUGF5ZWVBY2N0TmFtZT48L1hQYXllZUFjY3ROYW1lPgogIDxIb2xkMT4xMjwvSG9sZDE+CiAgPEhvbGQyPjwvSG9sZDI+CiAgPERldGFpbExpc3Q+CiAgICA8RGV0YWlsPgogICAgICA8SWQ+RDk1NEZBMjJBMDUzNEQ2RUEwRDI5RDVBOUJGODZFNEY8L0lkPgogICAgICA8Vm91Y2hlckJpbGxJZD41OENBQjg5QUYxQTA0RUYzQjdFMTlDMURCQ0ZEQTUwMjwvVm91Y2hlckJpbGxJZD4KICAgICAgPFZvdWNoZXJCaWxsTm8+VzAwMjRDMTAwMDAwNTQ8L1ZvdWNoZXJCaWxsTm8+CiAgICAgIDxWb3VjaGVyRGV0YWlsTm8+U1FXMDAyNDE4MDAwMDA2PC9Wb3VjaGVyRGV0YWlsTm8+CiAgICAgIDxGdW5kVHlwZUNvZGU+MTExMTE8L0Z1bmRUeXBlQ29kZT4KICAgICAgPEZ1bmRUeXBlTmFtZT6+rbfRsqa/7rK51vo8L0Z1bmRUeXBlTmFtZT4KICAgICAgPEJndFR5cGVDb2RlPjExPC9CZ3RUeXBlQ29kZT4KICAgICAgPEJndFR5cGVOYW1lPtSksqbWuLHqPC9CZ3RUeXBlTmFtZT4KICAgICAgPFByb0NhdENvZGU+PC9Qcm9DYXRDb2RlPgogICAgICA8UHJvQ2F0TmFtZT48L1Byb0NhdE5hbWU+CiAgICAgIDxQYXlLaW5kQ29kZT48L1BheUtpbmRDb2RlPgogICAgICA8UGF5S2luZE5hbWU+PC9QYXlLaW5kTmFtZT4KICAgICAgPE1PRkRlcENvZGU+PC9NT0ZEZXBDb2RlPgogICAgICA8TU9GRGVwTmFtZT48L01PRkRlcE5hbWU+CiAgICAgIDxTdXBEZXBDb2RlPjIxOTwvU3VwRGVwQ29kZT4KICAgICAgPFN1cERlcE5hbWU+uv6xscqhxanStcWptOXM/DwvU3VwRGVwTmFtZT4KICAgICAgPEFnZW5jeUNvZGU+MjE5MDExPC9BZ2VuY3lDb2RlPgogICAgICA8QWdlbmN5TmFtZT66/rGxyqG5+7LosOy5q8rSPC9BZ2VuY3lOYW1lPgogICAgICA8RXhwRnVuY0NvZGU+MjAxMDEwMTwvRXhwRnVuY0NvZGU+CiAgICAgIDxFeHBGdW5jTmFtZT7Q0NX+1MvQ0DwvRXhwRnVuY05hbWU+CiAgICAgIDxHb3ZFeHBFY29Db2RlPjwvR292RXhwRWNvQ29kZT4KICAgICAgPEdvdkV4cEVjb05hbWU+PC9Hb3ZFeHBFY29OYW1lPgogICAgICA8RGVwRXhwRWNvQ29kZT48L0RlcEV4cEVjb0NvZGU+CiAgICAgIDxEZXBFeHBFY29OYW1lPjwvRGVwRXhwRWNvTmFtZT4KICAgICAgPERlcFByb0NvZGU+PC9EZXBQcm9Db2RlPgogICAgICA8RGVwUHJvTmFtZT48L0RlcFByb05hbWU+CiAgICAgIDxQYXllZUFjY3RObz4xNzAxNjIwMTA0MDAxMTI5NDwvUGF5ZWVBY2N0Tm8+CiAgICAgIDxQYXllZUFjY3ROYW1lPtbQufrKr7uvz/rK27nJt93T0M/euavLvrr+sbHO5Lq6yq/TzbfWuavLvjwvUGF5ZWVBY2N0TmFtZT4KICAgICAgPFBheWVlQWNjdEJhbmtOYW1lPsWp0NCzfr/a1qfQ0NOq0rXK0jwvUGF5ZWVBY2N0QmFua05hbWU+CiAgICAgIDxQYXllZUFjY3RCYW5rTm8+PC9QYXllZUFjY3RCYW5rTm8+CiAgICAgIDxUcmFja2luZ0lEPjwvVHJhY2tpbmdJRD4KICAgICAgPFBheUFtdD4zLjAwPC9QYXlBbXQ+CiAgICAgIDxSZW1hcms+PC9SZW1hcms+CiAgICAgIDxGb3JlaWduQW10PjA8L0ZvcmVpZ25BbXQ+CiAgICAgIDxDdXJyZW5jeUNvZGU+Q05ZPC9DdXJyZW5jeUNvZGU+CiAgICAgIDxFc3RSYXQ+PC9Fc3RSYXQ+CiAgICAgIDxSZWNlaXZlckNvZGU+PC9SZWNlaXZlckNvZGU+CiAgICAgIDxBbXRVbml0PjwvQW10VW5pdD4KICAgICAgPFhQYXlEYXRlPjwvWFBheURhdGU+CiAgICAgIDxYQWdlbnRCdXNpbmVzc05vPjwvWEFnZW50QnVzaW5lc3NObz4KICAgICAgPFhDaGVja05vPjwvWENoZWNrTm8+CiAgICAgIDxYUGF5QW10PjwvWFBheUFtdD4KICAgICAgPFhBZGRXb3JkPjwvWEFkZFdvcmQ+CiAgICAgIDxYUGF5ZWVBY2N0QmFua05hbWU+PC9YUGF5ZWVBY2N0QmFua05hbWU+CiAgICAgIDxYUGF5ZWVBY2N0Tm8+PC9YUGF5ZWVBY2N0Tm8+CiAgICAgIDxYUGF5ZWVBY2N0TmFtZT48L1hQYXllZUFjY3ROYW1lPgogICAgICA8SG9sZDE+PC9Ib2xkMT4KICAgICAgPEhvbGQyPjwvSG9sZDI+CiAgICAgIDxIb2xkMz48L0hvbGQzPgogICAgICA8SG9sZDQ+PC9Ib2xkND4KICAgIDwvRGV0YWlsPgogIDwvRGV0YWlsTGlzdD4KPC9Wb3VjaGVyPgo=</Voucher>\n        <SignStampList>\n            <SignStamp No=\"cz_dwsz\" SN=\"7344e8d63bb64f73add978f24d25ec8f\">MIIuXwIBAgSCJD0wgiQ5AgECBCA3MzQ0ZThkNjNiYjY0ZjczYWRkOTc4ZjI0ZDI1ZWM4ZgQM1qe4trLiytTTodXCBAQ3MTAzAgEBMIIZmwIBAgIBAAIBAASCGXVHSUY4OWGfAKoA9wAA+neo+hxI+ilW//n9/fL0+7vU/uzy82d4+Thm/ePr+2ia/cni+wYX+VmG+YWb8kNW+HWI/Nvj+5jH9SM3/eLx+sPK/dHl/Mvb/d3p/vX4+rK6/BIr//z+/Im8/dPd+gs2/vn6/RIy9zNI/tr0/uv4+7zM/eju/LPN9lRp//b9/Asi+f/+/MLS/eHm6jdY/cHc/fj0/Njd/f73/P/+/LLD/Kq7/MrT+hs8/PPs+6O6/Q0r6ypF96Oq/vD4/dbp+5y85ll2+5Gz+iJO9CxM/Bg1+6zC9P/98yND+yJB+qOy+4Gj/KvM/JSt/LrE9HKR/Ius/BM88iNL+ipO6UVj+6TD+4Wt62iE9Dxc9Bw+//z79REz+2uN/dDV9DNS/v/79ho0+p2s+jJd+520+nOb80Nh80Vr9ZOs+nqd+5S7+pOl+3SS81J7/RAk+Tpc+4yh8zNc+kJi/bjg+zty+0169WyO+mKL+0xs+IKN9Etr7B069hQs9Utx+0p1+3uU+TBT9VNz/AMf9k1i8TpR7neT8ytA+mN/84Sh7nmF81h9822C/Bcs//H8/uT3+myA95Od8Vtx85ys+kyF9XuS+itj+l5++qqx9U177TNK6kxz+0Jy9Q0r9qS7+16U9Yuf/azX9oqr+f/693Cc+kJs9WWO+ihF9gsg9Ku88nyc+Uhj9EFx9RU985u0/AUr/ejn+llz+lOA/EN7/P/7/sXr7VNq/KHK85Ol7RQu+ThS9//z8mKB9qS1+K7A+Ja0+1Jw6y1V+5uj9AQg97XB9RAi9pK7+MXS8Iua97nL/Pz+8hot/ODf9p6+96m2+/n98I2l+H6v9bzD6Aon+NLf+bXK7Txi+c3T+fr59kV59+Xq9pqh9gcs7lyA9Rcm/Pz8/NHx+L+29vf2//////7//v/////+//7+/v7//v/+/v7++fD4/vP6/fT7+GNg6z5w+KGh+9XR+dHZ997W89zZ+9zU76y27bSt+LGm9+j3+B0j6A03+e/r7k+I7pKi8mqU+8XY+afD////IfkEAQAA/wAsAAAAAJ8AqgAACP8A/wkcSLCgwYMIEypcyLChw4cQI0qcSLGixYsYM2rcyLGjx48gQ4ocSbKkyZMoU6pcybKly5cwY8qcuXCczZsDw4EjCM7mv5tAefakSbRiz6M1d54DJRBpzqFFo0YcqpNECg5YQSQwQC5rt0XlfnIoCFWq2aQ9Lix54Q/BkFRj4iJ6y2TLKE4C4JpSYsgChggDnJ4dfNRrA0tO2ny5cYSIjhBIHAuBPKcxpcfIVGnZfDnUmbVlB8PU2bQcoyKfN4mCBqX1hsiYATEA9lqz60vCVDC+fVh2FzyS6lplJs4gTtEjq8ZQpmBaGWdyAkieTar6g0aoKEFwk0RDje8V7mD/FySCkB/Ovimr90xcbGkvyEMe9eQq8/leYbCYt+89nYkMXhUmoBcEcLVcZfhRp+Akb4WhBjUAvhefRzoxN0gZu5WXXxOt2GBgaO8JeFAW89lQF26s8EbbH50ANuFHJnTQ2wj23EIdABcUFuKAICLklFZX2bWgIpLx49eLEomzU2li+WKbWxLEhZRXT/F4XEJKjWVceHZMkFttkewRCo1imYNkUj+ViZd0eWlG5mgnkKHHkIiB1eOZQinZ0xV5uAXLB37csVVJWaK1TnTqVfeJVXhiucKea+jn5x5+CQZjT6A1VCAGSmR44xNpNbolCXfJFUV/WS4JEqQsaKmqQjYF/8IGnX9N+GpXM2TpJH0IjEGjjksamFOIFBHH5iPeLZNjU2WOpSeA3YCx36d6ElZclUHS4hksiCwQFpZv6KNBBs1GIcQwIExkRByqFAPBYvfIdq2S7xbo3lNSxCbFK9q4aCu9hwEHwHM6+njBFNlIolwy8BqjbqfzSTYvB48krBRZ+QDop4IFZBVfOLwWCdWdPAEKCladZubtw6d24O15Hs5LV7UYp+XGkDx8K1oKvEjaqyfhTDWLIKc4qZelD8UARceTEaNHHwQGuzSB9wr1Ew8a3gjDWXqewZhdvh6DVmFiaDgIMbnOUDVEHqiy1RfbzXaaUrmEAQNQr9Z8n9bOjv+GcR+6BUrLAJpGvAMZnT2r1t1ThVMHGQRg17aNh7PYjbmBbXVtTc0tSGbecN7WcU1iaetloACnHTltKySZ1zj6gXPdwfU1mB0D42p6NbxtLgs6Srfu7cSRmrKDTwCfqc7CAZsOLa/rHkTgdtkxGO554bvzdsI4M5HKmQI+/G5wFV81WwTvhnSaCLls0yEAz0sXIgLjP1EXLdEysA0px+KfRLd1OAoak0j3qA/dZTboChIC2McQqeHoEa+IHApkUJVUyOtDaXIIBY9hAPnxL4Mr8d5rlLAIizACQy7IBhYcUKfSfeAFIHRU/aKBCySkoR3AaJVp3jWnClAtSV3JHpH/IiELmqVkEXUL3NZIA8QgaIJguHjBC9O0gFORQIPM+EQq8rEMUrQiETfQXA7mlB13aCRG1wth0ewXNQE2rm1gKAwUfxIpwjVwXZURh3bg8TpWPUZtGbmbB61zxSNC4kvzw6C6WCW1COTkXIWDwRB+0MFKtAJ5dMQdHDd3ERJRAA5k/KP/Mqkbl1Gxf7DKHCHEeElIyKwvd4zR8ljBRSLIIwWy2sQMahBG+BRLVUH85AeTs8G15GtwwESlowR5hmcd4gE4uMn54vBDg2EKgTF7F6h22Us3vrFgFvhNinJByWFdqk+7dIbONtKJIaiDiveoXpMecTFrVmBFq/Rei+oX/zZlLhOYQgxFF7xFskCuKIAxNEoj4SkGXHmQkyNKHQ+t8AZppI0Kbltb+4BUHKr8wDn3sZM3N7I6zNQTIyNzjn9YpQ/apEgdqMxCJVTYKkeUslJRlJxGk5bDdc1LTWxM6BkVoxtGmEYw/kyKtCzA0GNgA4xwSIdQr2YI1l3FBDbyYUdlYJ4CKkldi4kFIKuEgsDJgQpGRGmTigqtAZXTKPx0Zl94NKKiveCqjMxCk3KANyyWq1uj8tkKC1qsA2aiB3qz4gCFZjcOguMJE/iPllJZlq7ADFPquIMtFxlOmEaTFSRM6AA+OjBRcsQHKkUWYvNkrnMVbCrUG84mIYrFHP+AJjGRcgVAsdjHDkrnlj4RSpu8uFOW2WF7khVKVXk1V9oWzmJNkVWusIettebQuAMFRRW0lz+y2G5pU3Vda5op1u4+EpmyCFhSR2UOxbnAAIEsqRnNybnfQkhD8NDAEHGwpWF2kpdNU857KCogfl3hro1rVnmlilLM5oMnVjtlnJ6IDq6MM4qP1STFfhVd/q3XYPsxJbOIxZM1kS+8ZgFnyipliZdmrHTXMAOfOhasJMDGMWMtLDa31MJbRQlRFNDZh18yWnq24AFWVdpmhMG8NlZjNQikIikjQw0UM2QJu4EhxkKMAe+iTUa+CMJ/iluUEWxsktccKA5VQF5rgLn/Db/wxqZKrDUrg4tBUVVug07Ai0WV7J0c7BlcnCuVHrwhRYqIWWv/kmFxBkLGBN1giGxaJCByAKPHlAez9GQb/hpDGdS0MDX/SqmvWgvAB/DgNncBVTa6LWOcnNKZbxVLJDOmAnqb6aIwxY9SMeNvJgvfzuhV5620CEpqW12QR5oTyM7qrECkTCFI9BS+XBNowxlDu4JVGsMuMDBcSxca26C5bhfjbiKcwCFyZzXffm29HkV0CYJLymjQERMm+GuhLu3OzE7iHXZuCa5S0G3XsiqgshGUcaa8QL9ODm4EgDC/IcfrRfEifGAWdlxVxzWBMYqqFbLYweSNxifA6lih/1Wm9UY3LE/uhdVeeOqT6PBmo7alwmkt9EFpaPMsENWpx0I3DGx7cp9FE2msBdS/KXsXdxhoFY9rAJ8tCB2eE7Z7TpvM8QRGHkCIKYV8pZ8GES0MLix24elOaj4uK8aeXs5NQyZyMbmUHgZM20hfnS5PRUZmeDIIaLWGwpjSxplcmU6dL5oSFyJwvn2B8+pkAdx++z7lQgb+vcvjlyeA6khmpzhVjw11zhkrN/+k8nSAvyNQDzc3CRfwUiNucNBc1fRnmfB0oEV6syMDvl/at1kkoUrcsYflI9gJpWkgu+47vKFf9oPqLeCeSQa1KmI3fKhKDJWPniQ2zp7s70dPjv+fV1VvkgqvoLMUQTMIrtB6E9r8RIR8ku4N3vjW7oWtiOg/UN3QYm36s0DQZSJhaHLQXp7XSc7iDlBzRnr0bMQ1Kl7THKNGUq2SHK1BAQGHgIEkRFKwWomFF2BxJjZWf0hyQvYTUWZ2UxQifmwyfKNBOToQZwiBae9TgpV3JhQDGw7wO+MgaLiTgTKRZgH2FBTyfhThRI9BCXrVX0UFhKRDTEWmdANFhB3hWAcIVkpUV6AkdU4YE+5mUlBYDbZ3e77BYJH3M533MfuHZ9LGgrvAQZR3ZdPCCFp4a11oMFB4eGYVFi74XIJnL520hWwGOkdmd6ASQyASLFsFiFfza6f/lUy4REQzVwAKpntxd3TPtG2SFUT3kjehkYM7FjyGSFtY4XqytjJKsW3ywU2T0gTlQQWVqDgDoj8cSDRmQEkxw2hpAWvLRkWSp26EqIN/4wPYImbEZg9iw2lTZGmasym7KFt6aGAvBAZiAGqnEATpo0U0UI34Y0JRiEJ04m1dZwS+uIfGsXMZFIk6xGDe81j94mbuRYJYNHHCo3Vnxgk/FnWCxyds8kReRyRlmAC/5HrecTvb0C22Fi97RGfPFowxSIl0hi5hxgNQV0XtiGlfoSS5l2BfKIXDhRk/1iHQkWoI0mJElR839WDOZyWMdgrQUnbf1w5nuGMFQYMX4B5d/xMuT3SN1xB6WUSP9PKGVANvC3MoCBQ3GQI+ToVx5BMoyJN+iAJNHSJ/d4Z7p/MoCYRD1zaT8cSITXGCwudUD1JRPHJbPTdqVLkjQtglI5lpc5NxGDlILQh8ZHgLhcBCx7UC3DGVpzJDXFkHDrkBNLA2BTBB/ZQA7gNqxIEumdR79rcgbyYlqMUejTYZJhZkjzgPh2CAo2B4UeWTfsmQD5k3NCAxnUhHlSQN2Hg2PYcJLpOCEpBsfUhW+XIYEtA72oBbsbkAzYAYbGgJ0ReHsBVpZCk5mPKVxCiaJ1aTDVM1mSNjapAJaMBRMaYWUQc0/SKcaOKOfQKXIOMP0diW6v8UIbOJglbgSR3ojjexDr/2SWannNJXMlE2Mn1Wezi3f5+2BQXSMljZlwgYIKYSRlQlnp0Tf8JCgQ2oflo0NfVxcFgVA1vmJRd3jrMSPWRDU84odP2gRzT0hzj3h7KXd1lXamHyHUQUmYrZUfHlk0mkQti0F6mzhgJZbQDJAiOCegV2CYtXiOGymlKnjXiGjCNZROxHgaCVj7UTm81RosvHWfiXoV3ViI4jCOi2A8nAlQ5DoeoHetWzeBZTWiU6MDB6P4PTUjR2Wq2IckrqokpZnt4VYOlSiaYUDYqRCJmocI/0bJVwo1n4fyRkbYtDHJ6FnytgPNi2FndYXyXJhjT/gh9/cn3w53UcEmltNTSV6VKRpZx8+hqy6R4Pwmf3eWn0skuC+luJWjwmclYEamYluZwMaI+fUioo8nQmanfmdYPG0SWcainK0gxQpw91op+ohUTO+JRN2kRwY5sRiGcICT4mo52xtHgkSYOIhH/p6ENvChkeKJppU5PUdIu6EEDf5iGd6ULdAK1+CFVg6pGTeRmFUoVlySV0SFjSc5V1OIXxGV2epTydx6FqcjYU8hvjESZ/OIKRhaToKpw/Ek0SIoemeRAzZatG5a0PZmrCEpQ4CbCnVZrSaY+USjnQ4Ri9Rw5Jc6xbQhYNwQRSSIiVKS6eCBhcuoj1dFVVqG1J/7mv5IIDgIOPsNGeGjShlEWEr0VYKSOgaGceVOAPhBaWVkKFNfuPZAmBG2NRJQuhQWuKseC0Epcg8thyuVQ+KeaP+GhHPlKg8xN83hAI4WcoYFi2J1hoKmussCJETOWGAZeKSXiuVXmIUUEOZfUgqteY3BCGd9uRMVVnfct6b5RRA8g48tey6KdZtoqT/ylDlPcOwYA06BdoKomC7aZ4VUIsMaUrJGeEyTeKeVe5eHi5bnq1OElXTRGuYxi4D/eAjuKAo7eK3qh/+sOSFxc8MeYLlredLPS2t5tlp8qMyTtw/zmqBaeEeRI+M6p6BCg3DrELJMeATJeWM6l3VbG4k/+LnmpbM/CVNGvIRvkaWH3qprLkQ+ABs9sYDKZatZz3SmSrVP3oIEJ5T9gavUSZoLdGr3sClukrXhQ1BZ3RnXhJS2yzQptgIbJiOfeUG1qGYj7XJzvJYuy5djawov1Yt2yrkCYrh10qi7F7Cy92vUl4j8eTRalmo5qiCzq7WSejWU3pDY+JvNR7OmuAWL5kFF8ggJ2owWnJMLiIR13Jr/OoWaliq/GEfbw3ZKAIC2d6e0XQki1pX3RQTQ2UDWjjU6yjYGVCWdqltnOzdlKXqciXkERaW76BUFY8NH2mQl/HBHjliKharN/ADV4BDcYowFbBQsuhYRyyWSbEcDSrO5z/ElRWHG/8uj5G+KYFCVK5tbJ9x52Hkx5KWKVM8J8fTIdVO0bvFogdPB+NcA7/yrBj1xY6KQnX4RnUKB7fgKqibFHPMKey8wNrLG8caTsnQMqv24gy2sBtx01oM8b0ZZ5U2pPbNRyQFIiIK140WSy24AGl48pdhA94p8arzGuM1MuSWmEbkstXQnoXaGrSDE0J2205ixr8aHC/gMIfxqGM1Fg9yBVaS7749KdeRAJPaQWm4DEaVD9vPMLbxzfo3EAwxnmaOFMJXRP/HM73sB1YowXEULKdCWrjjHkoICjYJMUJOQeEw4ngq1rzh5oEUQnMgwYa1s88FRjRmTV2uYXJ/6nCqqmXz2B4RnWzVGl9ebu8UQOebTzPyLlpupWal/QoESZa9ryjtGB80fd6P9trUxCPmewIwEXSXayDQnzIqukMUdI6jbOlAzFGO1EPQpkHqrzUfxYiOqomMJWyOvp8aN0JN/M4GKk4P4tIoNZg58uk0AO/ghw9jcEazqWZwZgjd4w6L8kOoHxyaYBHutaTH7qZCxbJZW0fpQC9r8WRhyR45za8qcRPUDYpEPS3WM2yoLOzuZlCwGqVLtXXZMy/IqJH7Hl2PoLIARvN22mXxLqJAxaCNs0OAL0Pxq0FqnU21Lg1aBKaA9Z/GO1fRlqj6IA9A1BGiohuuyPco+0KrP9ZLeoo1p3Nu20TcWQVR/qDqajgSEV4ANSyw6t2dNJrcctIQGdrexkwO9ndpCnVwXrG3Jc3uZcyw6NoZT4hOzNXzT/GfaZXX/lnhagp39ltuTZQCv5t1Cg8twXHN+RX4aLz0O3WK/yqPM1cDXlcicDIUfl8tDkAbAk4KswHlo374WY4Iih9ckrdQOSUa/nnpKLtYMv0lQjduliSPbc5JnZ2dXoXSeylUKO3MP3zP6XwrMnrcF7VIkW6u9YSlHicq8odf9OXKmWqtECdzLS4ilmhzbm5ORcjTBdW5VPxrwLlIJmjhUT6smYOJ8DSMi6dowUN5+pCf5hj3jwRDNn4uzj/COWqQZKtk3fvvJEqUZSWuW5Zfm9xEJtMQuTBZ+lX/m8tsHoyHkI5GRxj+9/NdszIkQ54vaF0o7TtnJCSus7xRaNhuoRlbSS7Z2+p7maGypKFTRmaJnBsvkF6YazJKNWxO54Y07DAgzJLNDke0GSZ49OTp+nTvWikaGz4xofS65zNXn4DmguWR+12CLc9iiG1UjI8ea4g4wLlOov+483Ce8IBWEId5RaY2n/cO33hDn4MhNPYZunffVRhfsX4wgNqqRxfB0qWJOuE8rxfgpnMfovOXnG2PoBqLnwdnfBzzjvHtzOCPmPiJt4SpUt5JYbT3qmfK7qtflXtJIGOPqN+/0524v7xH4OY37XH2BKk0YV3tHqeRyXQJGYl1wlrlfOpLI/z+WtkohJzcHaZ0qcUhyoQrBZANiMu5TqgsknXI0Dv6NVYmGfb9BFr0z4XMt2VDi93VNVa2L2JyIiMVD8MvZaM+2BzLimj704qFSlZap5yVtRMRm7eGq/ZiLvvNEG6ABkd43kVZ0iOUtpnyih6qBFkVKyXnFAhJRDhDhK7KD8xxTvlCgmMyNwoA1LaKPlpjKJ4csUWPCf3YZ06+c1p4nxbDxWLMI0K6p1koy8qEWo/dko+siggzKGS7lh1TTKo4U5jOl1Iwl8xhJ9wgsr7keT81mGZVkdiGTtXLuTYvv/osvjt+bgVjox/hdKf6Xw5HdkBy2/f2RNuGsC3391KakPy0eXvfffH9q+c2hKPgsoDEP8EDhRXMByHFBeCFSOliQ0DiBGFufIgw8tAjBk1buTY0eNHkCE5pgO36MWfLkhKEeKzUqKhhSUHJCT4b8ZMgwJlmsBwwkGqN1B0uHz4MkYWczlFLmXa1GlTg2gETODkLAAgh36KDrOS6M4pNU4+/Xh3dJXZn44CCQqjaihRiVQLySr51O5dvHgP4izh01fRIRu+YFFJWLAKwEIHI1sc17FQsbiQysxb2fLljJQn71XG9THWzw0VJX45F9uIHuBsjquL2fXrp61XG+RJLkFShAVM8MDh3bBQ79DAXZneSRtjQdjJlYOUvZkgwuKtatAQw0RaRUYtEnrBEV119Oczlo8nX978efTp1a9n3979e/jx5c+nX9/+ffz59e/n3x9vQAA7AgEAAgEAAgEAAgEAAgEPAgEAAgUA/wAAAASCBFUwggRRMIIDOaADAgECAggR7ZlReZborTANBgkqhkiG9w0BAQUFADBKMQswCQYDVQQGEwJDTjEMMAoGA1UEChMDTU9GMS0wKwYDVQQDEyRQcml2YXRlIENlcnRpZmljYXRlIEF1dGhvcml0eSBPZiBNT0YwHhcNMjEwNDAyMDE1OTUzWhcNMzEwMzMxMDE1OTUzWjCBjjELMAkGA1UEBhMCQ04xDDAKBgNVBAoMA01PRjELMAkGA1UECgwCMDExCzAJBgNVBAgMAjQyMQswCQYDVQQHDAIwMDELMAkGA1UEBwwCMDAxCzAJBgNVBAsMAjAwMRMwEQYDVQQMDAo0MjAwMDAwMDAwMRswGQYDVQQDDBLmuZbljJfnnIHotKLmlL/ljoUwgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAIv6yQJ6DM+Z8L4OHlI5913h6E0P2DybH/U4EOCx4wBcL8G7c/X9YtKpIw+b6262l5RTetSnNNAv0wWjQP1/6e0cxaQyyjSg0Af/gr3Kqq4ObHH9LxGVNEvVrDBVpbsxKmfBOqHtCyeEkxNZsFyeNyNWnTxaqFuqs5tXqf9XGO0zAgMBAAGjggF4MIIBdDAfBgNVHSMEGDAWgBSW+Euyia0AG9kJv3Qg8Afgi80LWzAdBgNVHQ4EFgQUnaWlKIOGhBVL45tK34pI/qNcVY8wCwYDVR0PBAQDAgPIMIHxBgNVHR8EgekwgeYwQqBAoD6kPDA6MQswCQYDVQQGEwJjbjEMMAoGA1UECgwDbW9mMQwwCgYDVQQLDANDUkwxDzANBgNVBAMMBmNybDM4MDAmoCSgIoYgaHR0cDovL2NybC5jYS5tb2YvY3JsL2NybDM4MC5jcmwweKB2oHSGcmxkYXA6Ly9sZGFwLmNhLm1vZjozODkvQ049Y3JsMzgwLE9VPUNSTCxvPW1vZixjPWNuP2NlcnRpZmljYXRlUmV2b2NhdGlvbkxpc3Q/YmFzZT9vYmplY3RjbGFzcz1jUkxEaXN0cmlidXRpb25Qb2ludDAxBgNVHSUEKjAoBggrBgEFBQcDAgYIKwYBBQUHAwMGCCsGAQUFBwMEBggrBgEFBQcDCTANBgkqhkiG9w0BAQUFAAOCAQEABCltmaSX7Ocy6eqBhWTgSojnvFjQF69UW9bWzkxvbphqabqpAtzaxm3GSUF1rQeVc/txF2ngVW0axFb3ftmzOLRfxlLFawwXsK4q4dWMEF0fx1FnsObVZjHPoY499bOsbTz4PT6qdthi+jQHnteUfUTJfsgt9VSofeyBVJz5JjA9KWozjy57h8qnP7LRIWCiA9oKJpXhy5UJtrhHQggBAC2Qq6C1cyJAO6KUhOK4d1qOaDcVLqL33A4YepJT5aY4s6eCIJVjZGcZ/pVw/4LdXH9LmbuYr3CuwXzhO5Al4CiI1/EOEzqZJcznv9ISLJ8+pfEKFh0WflE648vsIkqFewQvQ0491qe4trLiytTTodXCIE89Q1RKIFJHPTQyMDYwMCBNRD0wMDAgT1JHPW51bGwEFTIwMjEtMDgtMTggMDA6MDA6MDAuMAQVMDAwMS0wMS0wMyAwMDowMDowMC4wBBUyMDIxLTA4LTE4IDAwOjAwOjAwLjAEggWLMIIFhwYJKoZIhvcNAQcCoIIFeDCCBXQCAQExCzAJBgUrDgMCGgUAMAsGCSqGSIb3DQEHAaCCBFUwggRRMIIDOaADAgECAggR7ZlReZborTANBgkqhkiG9w0BAQUFADBKMQswCQYDVQQGEwJDTjEMMAoGA1UEChMDTU9GMS0wKwYDVQQDEyRQcml2YXRlIENlcnRpZmljYXRlIEF1dGhvcml0eSBPZiBNT0YwHhcNMjEwNDAyMDE1OTUzWhcNMzEwMzMxMDE1OTUzWjCBjjELMAkGA1UEBhMCQ04xDDAKBgNVBAoMA01PRjELMAkGA1UECgwCMDExCzAJBgNVBAgMAjQyMQswCQYDVQQHDAIwMDELMAkGA1UEBwwCMDAxCzAJBgNVBAsMAjAwMRMwEQYDVQQMDAo0MjAwMDAwMDAwMRswGQYDVQQDDBLmuZbljJfnnIHotKLmlL/ljoUwgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAIv6yQJ6DM+Z8L4OHlI5913h6E0P2DybH/U4EOCx4wBcL8G7c/X9YtKpIw+b6262l5RTetSnNNAv0wWjQP1/6e0cxaQyyjSg0Af/gr3Kqq4ObHH9LxGVNEvVrDBVpbsxKmfBOqHtCyeEkxNZsFyeNyNWnTxaqFuqs5tXqf9XGO0zAgMBAAGjggF4MIIBdDAfBgNVHSMEGDAWgBSW+Euyia0AG9kJv3Qg8Afgi80LWzAdBgNVHQ4EFgQUnaWlKIOGhBVL45tK34pI/qNcVY8wCwYDVR0PBAQDAgPIMIHxBgNVHR8EgekwgeYwQqBAoD6kPDA6MQswCQYDVQQGEwJjbjEMMAoGA1UECgwDbW9mMQwwCgYDVQQLDANDUkwxDzANBgNVBAMMBmNybDM4MDAmoCSgIoYgaHR0cDovL2NybC5jYS5tb2YvY3JsL2NybDM4MC5jcmwweKB2oHSGcmxkYXA6Ly9sZGFwLmNhLm1vZjozODkvQ049Y3JsMzgwLE9VPUNSTCxvPW1vZixjPWNuP2NlcnRpZmljYXRlUmV2b2NhdGlvbkxpc3Q/YmFzZT9vYmplY3RjbGFzcz1jUkxEaXN0cmlidXRpb25Qb2ludDAxBgNVHSUEKjAoBggrBgEFBQcDAgYIKwYBBQUHAwMGCCsGAQUFBwMEBggrBgEFBQcDCTANBgkqhkiG9w0BAQUFAAOCAQEABCltmaSX7Ocy6eqBhWTgSojnvFjQF69UW9bWzkxvbphqabqpAtzaxm3GSUF1rQeVc/txF2ngVW0axFb3ftmzOLRfxlLFawwXsK4q4dWMEF0fx1FnsObVZjHPoY499bOsbTz4PT6qdthi+jQHnteUfUTJfsgt9VSofeyBVJz5JjA9KWozjy57h8qnP7LRIWCiA9oKJpXhy5UJtrhHQggBAC2Qq6C1cyJAO6KUhOK4d1qOaDcVLqL33A4YepJT5aY4s6eCIJVjZGcZ/pVw/4LdXH9LmbuYr3CuwXzhO5Al4CiI1/EOEzqZJcznv9ISLJ8+pfEKFh0WflE648vsIkqFezGB+zCB+AIBATBWMEoxCzAJBgNVBAYTAkNOMQwwCgYDVQQKEwNNT0YxLTArBgNVBAMTJFByaXZhdGUgQ2VydGlmaWNhdGUgQXV0aG9yaXR5IE9mIE1PRgIIEe2ZUXmW6K0wCQYFKw4DAhoFADANBgkqhkiG9w0BAQEFAASBgBAdR7j7nGyPrEjLCg2Hh2MHS1bkiBMFR2Dvbfr+8fDdu+tdFi+wUHOr6Eebu6Qs/xQbFw5x85kzdvGPl0G76aMqKClDjHS03lnyNR/4k+MNOuT0gKAzQtQDFn6HiqMdOOq4+xh4QGA48xSISdWaNmr8iVcjQyMpZ+QJ9ow9xhZwBBMyMDI0LTA0LTA4IDE0OjA1OjA2BIIEZDCCBGAwggNIoAMCAQICCD845KruDCrLMA0GCSqGSIb3DQEBBQUAMEoxCzAJBgNVBAYTAkNOMQwwCgYDVQQKEwNNT0YxLTArBgNVBAMTJFByaXZhdGUgQ2VydGlmaWNhdGUgQXV0aG9yaXR5IE9mIE1PRjAeFw0yMTA4MTYxNzQ2MjhaFw0yOTExMDIxNzQ2MjhaMIGTMQswCQYDVQQGEwJDTjEMMAoGA1UECgwDTU9GMQswCQYDVQQKDAIwMTELMAkGA1UECAwCNDIxCzAJBgNVBAcMAjA2MQswCQYDVQQHDAIwMDELMAkGA1UECwwCMDQxGzAZBgNVBAwMEjQyMDYwMDE5ODMwMTA0MjU2MzEYMBYGA1UEAwwP6KWE6Ziz5biC5pys57qnMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDN5c0FO8X7VevRaROlhiyjxz1npBso9VMnJLsYtGeNrE+4X3lQQxdlgo9JAuUvEwLA+D2kg/DKxmAqwl8+e4xuCDovTLoh3SVyOwsK1Q7lnld0nCPcWCVBxVvhNDOSnKS03fq7ysqISzkwer4gYWkHgczxUmFkrQNeQwdH6VnnMQIDAQABo4IBgjCCAX4wHwYDVR0jBBgwFoAUlvhLsomtABvZCb90IPAH4IvNC1swHQYDVR0OBBYEFJ0xvY4XrUyhloB+efWY32ZgJ8kiMAsGA1UdDwQEAwIDyDCB8QYDVR0fBIHpMIHmMEKgQKA+pDwwOjELMAkGA1UEBhMCY24xDDAKBgNVBAoMA21vZjEMMAoGA1UECwwDQ1JMMQ8wDQYDVQQDDAZjcmw0MTMwJqAkoCKGIGh0dHA6Ly9jcmwuY2EubW9mL2NybC9jcmw0MTMuY3JsMHigdqB0hnJsZGFwOi8vbGRhcC5jYS5tb2Y6Mzg5L0NOPWNybDQxMyxPVT1DUkwsbz1tb2YsYz1jbj9jZXJ0aWZpY2F0ZVJldm9jYXRpb25MaXN0P2Jhc2U/b2JqZWN0Y2xhc3M9Y1JMRGlzdHJpYnV0aW9uUG9pbnQwOwYDVR0lBDQwMgYIKwYBBQUHAwIGCCsGAQUFBwMDBggrBgEFBQcDBAYIKwYBBQUHAwgGCCsGAQUFBwMJMA0GCSqGSIb3DQEBBQUAA4IBAQActqb4gCbFEAU6NwX660H5MuxAvCmpoeOPkCViy0l5IFkssCTKnBVo8RyortZJzN5DM6E5fguE2if3EJ1j5+ZgEQb322xB8LsWE7t0M4OYrDCM5hyjpnGxVYRT9JagytiBwP9UgWVsV5CM8ZhH4kN+SJ/uhFanUQCi2bKCWyzmni2DKrXseNeRcyErNynohPeZpbVkzT/z4u1e7w8yPjs3kgVxvSQoO5WsJlC8UnHAYXPtpfGfm+6YgG/i99znv2taKeyi3D0FUwfvNyNuRXzNjI2rqPjpUT29Ynpa4pB3ynOQe6XG5NZ9jhDjJBEtajW3Fdb5EL5g16UTZ7tCTDziBIIFmjCCBZYGCSqGSIb3DQEHAqCCBYcwggWDAgEBMQswCQYFKw4DAhoFADALBgkqhkiG9w0BBwGgggRkMIIEYDCCA0igAwIBAgIIPzjkqu4MKsswDQYJKoZIhvcNAQEFBQAwSjELMAkGA1UEBhMCQ04xDDAKBgNVBAoTA01PRjEtMCsGA1UEAxMkUHJpdmF0ZSBDZXJ0aWZpY2F0ZSBBdXRob3JpdHkgT2YgTU9GMB4XDTIxMDgxNjE3NDYyOFoXDTI5MTEwMjE3NDYyOFowgZMxCzAJBgNVBAYTAkNOMQwwCgYDVQQKDANNT0YxCzAJBgNVBAoMAjAxMQswCQYDVQQIDAI0MjELMAkGA1UEBwwCMDYxCzAJBgNVBAcMAjAwMQswCQYDVQQLDAIwNDEbMBkGA1UEDAwSNDIwNjAwMTk4MzAxMDQyNTYzMRgwFgYDVQQDDA/opYTpmLPluILmnKznuqcwgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAM3lzQU7xftV69FpE6WGLKPHPWekGyj1Uyckuxi0Z42sT7hfeVBDF2WCj0kC5S8TAsD4PaSD8MrGYCrCXz57jG4IOi9MuiHdJXI7CwrVDuWeV3ScI9xYJUHFW+E0M5KcpLTd+rvKyohLOTB6viBhaQeBzPFSYWStA15DB0fpWecxAgMBAAGjggGCMIIBfjAfBgNVHSMEGDAWgBSW+Euyia0AG9kJv3Qg8Afgi80LWzAdBgNVHQ4EFgQUnTG9jhetTKGWgH559ZjfZmAnySIwCwYDVR0PBAQDAgPIMIHxBgNVHR8EgekwgeYwQqBAoD6kPDA6MQswCQYDVQQGEwJjbjEMMAoGA1UECgwDbW9mMQwwCgYDVQQLDANDUkwxDzANBgNVBAMMBmNybDQxMzAmoCSgIoYgaHR0cDovL2NybC5jYS5tb2YvY3JsL2NybDQxMy5jcmwweKB2oHSGcmxkYXA6Ly9sZGFwLmNhLm1vZjozODkvQ049Y3JsNDEzLE9VPUNSTCxvPW1vZixjPWNuP2NlcnRpZmljYXRlUmV2b2NhdGlvbkxpc3Q/YmFzZT9vYmplY3RjbGFzcz1jUkxEaXN0cmlidXRpb25Qb2ludDA7BgNVHSUENDAyBggrBgEFBQcDAgYIKwYBBQUHAwMGCCsGAQUFBwMEBggrBgEFBQcDCAYIKwYBBQUHAwkwDQYJKoZIhvcNAQEFBQADggEBABy2pviAJsUQBTo3BfrrQfky7EC8Kamh44+QJWLLSXkgWSywJMqcFWjxHKiu1knM3kMzoTl+C4TaJ/cQnWPn5mARBvfbbEHwuxYTu3Qzg5isMIzmHKOmcbFVhFP0lqDK2IHA/1SBZWxXkIzxmEfiQ35In+6EVqdRAKLZsoJbLOaeLYMqtex415FzISs3KeiE95mltWTNP/Pi7V7vDzI+OzeSBXG9JCg7lawmULxSccBhc+2l8Z+b7piAb+L33Oe/a1op7KLcPQVTB+83I25FfM2Mjauo+OlRPb1ielrikHfKc5B7pcbk1n2OEOMkES1qNbcV1vkQvmDXpRNnu0JMPOIxgfswgfgCAQEwVjBKMQswCQYDVQQGEwJDTjEMMAoGA1UEChMDTU9GMS0wKwYDVQQDEyRQcml2YXRlIENlcnRpZmljYXRlIEF1dGhvcml0eSBPZiBNT0YCCD845KruDCrLMAkGBSsOAwIaBQAwDQYJKoZIhvcNAQEBBQAEgYCUkLzFkmp9AJzsqS99HAOHu43z1hL5sCNeshZkZgxCF5TpLLtQisyiZCNLXygcUz9u1S+pk6Z0+x6yVo+HcTIQCntW0O2Ys4c58WONIcF0UNJelmLlW4l2O51FJJJ0dMHCQVRAeBjDPp6Q+0lwl/OmA2FLlFvOhe4oE3F4bGDG6A==</SignStamp>\n        </SignStampList>\n        <SignatureList />\n    </VoucherBody>\n</MOF>\n",
            "details": "",
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "opid": "60D0E448D73949A28EB2C188B8D2333E58CAB89AF1A04EF3B7E19C1DBCFDA502",
            "bill_no": "",
            "payBusTypeCodes": [
                "1"
            ],
            "action_id": "60D0E448D73949A28EB2C188B8D2333E",
            "work_flow_id": "pay_voucher_bill",
            "isDoWorkFlow": 'true',
            "isSignStamp": 'true',
            "appId": "pay_voucher",
            "menuId": "60D0E448D73949A28EB2C188B8D2333E",
            "actionType": "2",
            "actionName": "直接签章",
            "vtCode": "5214",
            "glType": "0",
            "ids": [
                zfsqlrdb_pay_cert_id
            ],
            "stampurl": "pay-voucher-service/v3/payvoucherbill/action/stamp",
            "admDivCode": "420000000",
            "justShow": 'false',
            "voucherNos": [
                zfsqlrdb_pay_cert_no
            ]
        }

        # 将dict转换为str
        zfpzfhqzcz_stamp_data_str = json.dumps(zfpzfhqzcz_stamp_data)
        try:
            zfpzfhqzcz_stamp_start = time.time()  # 开始时间
            zfpzfhqzcz_stamp_res = requests.post(zfpzfhqzcz_stamp_url,
                                                       headers=zfpzfhqzcz_stamp_headers,
                                                       data=zfpzfhqzcz_stamp_data_str)
            zfpzfhqzcz_stamp_res_json = zfpzfhqzcz_stamp_res.json()
            zfpzfhqzcz_stamp_end = time.time()  # 结束时间
            zfpzfhqzcz_stamp_res_time = zfpzfhqzcz_stamp_end - zfpzfhqzcz_stamp_start
            zfpzfhqzcz_stamp_res_time_ms = zfpzfhqzcz_stamp_res_time * 1000
            print("\n")
            print(f"响应时间：{zfpzfhqzcz_stamp_res_time_ms}毫秒")
            # print(zfpzfhqzcz_stamp_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(zfpzfhqzcz_stamp_url, zfpzfhqzcz_stamp_data_str,
                                       zfpzfhqzcz_stamp_headers))
            logss.logger.info("返回结果：{}".format(zfpzfhqzcz_stamp_res.text))
            ###断言
            response_rscode = zfpzfhqzcz_stamp_res_json.get('rscode')
            response_result = zfpzfhqzcz_stamp_res_json.get('result')

            # pytest.assume(zblr_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert zfpzfhqzcz_stamp_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step07)支付凭证发送(财政)")
    @allure.title("支付凭证发送(财政)：发送")
    def testzfpzfsczsend(self):
        zfpzfscz_send_url = base_url + '/payfront/pay-voucher-service/v3/payvoucherbill/front/action/send'
        zfpzfscz_send_headers = {"Content-Type": "application/json",
                                          "tokenid": tokenids}
        zfpzfscz_send_data = {
            "actionName": "发送",
            "appId": "pay_voucher",
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "menuId": "47C1B830A8EB483C8CC0C815761A2DE3",
            "actionType": "2",
            "glType": "0",
            "ids": [
                zfsqlrdb_pay_cert_id
            ],
            "voucherNos": [
                zfsqlrdb_pay_cert_no
            ],
            "vtCode": "5214",
            "vt_code": "5214",
            "actionId": "47C1B830A8EB483C8CC0C815761A2DE3"
        }

        # 将dict转换为str
        zfpzfscz_send_data_str = json.dumps(zfpzfscz_send_data)
        try:
            zfpzfscz_send_start = time.time()  # 开始时间
            zfpzfscz_send_res = requests.post(zfpzfscz_send_url,
                                                       headers=zfpzfscz_send_headers,
                                                       data=zfpzfscz_send_data_str)
            zfpzfscz_send_res_json = zfpzfscz_send_res.json()
            zfpzfscz_send_end = time.time()  # 结束时间
            zfpzfscz_send_res_time = zfpzfscz_send_end - zfpzfscz_send_start
            zfpzfscz_send_res_time_ms = zfpzfscz_send_res_time * 1000
            print("\n")
            print(f"响应时间：{zfpzfscz_send_res_time_ms}毫秒")
            # print(zfpzfscz_send_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(zfpzfscz_send_url, zfpzfscz_send_data_str,
                                       zfpzfscz_send_headers))
            logss.logger.info("返回结果：{}".format(zfpzfscz_send_res.text))
            ###断言
            response_rscode = zfpzfscz_send_res_json.get('rscode')
            response_result = zfpzfscz_send_res_json.get('result')

            # pytest.assume(zblr_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert zfpzfscz_send_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常


@allure.feature('(case03)国库集中支付交投')
class TestVouchergk:
    @allure.story("(step01)国库集中支付申请录入")
    @allure.title("国库集中支付申请录入：保存")
    def testgkjzzfsqlrInsert(self):
        gkjzzfsqlr_insert_url= base_url + '/payfront/pay-voucher-service/v3/payvoucherbill/front/action/insert'
        gkjzzfsqlr_insert_headers = {"Content-Type": "application/json",
                                           "tokenid": tokenids}
        gkjzzfsqlr_insert_data = {
            "appId": "pay_voucher",
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "menuId": "D009D52AA14111EBBD508F93D7A97BB7",
            "actionType": "1",
            "actionName": "新增",
            "glType": "1",
            "params": {
                "accountClsId": "4E72561AB3CD477EB8DFD51813EC2FB2",
                "accountType": "63",
                "isFinancial": "1",
                "cptName": "pay89",
                "batchUserEleType": "1",
                "showContact": "false",
                "contactType": "0"
            },
            "datas": [
                {
                    "budget_level_code": "1",
                    "bgt_type_id": "4F53297E01C18CFC47D3F942A0958939",
                    "bgt_mof_dep": "09农业处",
                    "found_type_code": "12",
                    "agency_code": "219011",
                    "bgt_source_id": "62A6C38B276AB2117EAECFC2EFD4FEFF",
                    "canuse_amt": 99993,
                    "dis_amt": 0,
                    "found_type": "12-预估",
                    "bgt_mof_dep_name": "农业处",
                    "zdzjjqpt": "2-否",
                    "sumguid": "1775326015709990912",
                    "manage_mof_dep": "09-农业处",
                    "pay_type_code": "1",
                    "bgt_type_code": "11",
                    "fiscal_year": "2024",
                    "manage_mof_dep_id": "0B256AD0C2B3209E7FA2AE25873896B8",
                    "gov_bgt_eco": "",
                    "is_more_pay": "2",
                    "dep_bgt_eco_id": "F2684D4AE3086DBDA207A71B269729D0",
                    "planuseamt": 37,
                    "mof_div_code": "420000000",
                    "agency_id": "6B98F3B2EE02434479C8630869A96C60",
                    "direct_flag": "09-其它",
                    "source_type": "1-年初预算",
                    "bgt_mof_dep_id": "0B256AD0C2B3209E7FA2AE25873896B8",
                    "version": "2024-04-07 14:34:50",
                    "budget_level": "1-中央级",
                    "is_gov_pur_id": "2",
                    "zdzjjqpt_name": "否",
                    "todo_node": "BB39585CD1574D94B7D3DB7553930004",
                    "is_mat_id": "2",
                    "exp_func_name": "行政运行",
                    "pro_name": "219011指标管理1512",
                    "lzfs_code": "001",
                    "found_type_id": "E3BB7DF43981C10F177EA6A60BBEFFC2",
                    "aviamt": 100000,
                    "fund_type": "11111-经费拨款补助",
                    "is_mat_code": "2",
                    "gov_bgt_eco_code": "50101",
                    "canuseamt": 99993,
                    "update_time": "2024-04-02 11:05:43",
                    "bgt_source_code": "01",
                    "ccid": "03e09993b7636e52f8f7bb67a746552a",
                    "pay_type_id": "24B2435F18D2B38581D2845E32D14773",
                    "exp_func_code": "2010101",
                    "agency_name": "湖北省果茶办公室",
                    "agency": "219011-湖北省果茶办公室",
                    "bat_num": "0",
                    "frozenamt": 0,
                    "work_flow_id": "budget-total",
                    "fund_type_name": "经费拨款补助",
                    "cur_amt": 0,
                    "bgt_mof_dep_code": "09",
                    "cor_bgt_doc_no": "2024-0401-1512",
                    "pro_cat_code": "1",
                    "pro_id": "A42E27B4640B4234A48DEC69CA3E3156",
                    "bgt_type_name": "预拨指标",
                    "doc_date": "2024-04-01 00:00:00",
                    "pay_type_name": "国库集中支付",
                    "manage_mof_dep_name": "农业处",
                    "dep_bgt_eco_name": "基本工资",
                    "todo_name": "指标下达",
                    "fund_type_id": "DE1C8E16759F474C2D92CBBFB7BA6385",
                    "source_type_id": "A494A01709D991D416528C4C38E90170",
                    "voucher_code": "141001",
                    "is_track": 1,
                    "done_node": "BB39585CD1574D94B7D3DB7553930003",
                    "zdzjjqpt_code": "2",
                    "is_not_control_pay": "2",
                    "clear_amt": 0,
                    "exp_func_id": "A8C36161E5A91CFCC8E039A5F315AA92",
                    "plan_caliber_id": "d90f49adb78db8343547023025efcf4d",
                    "bgt_id": "71617A68FBD7407290063B7B89B221AF",
                    "pay_caliber_id": "71617A68FBD7407290063B7B89B221AF",
                    "xpay_amt": 0,
                    "gov_bgt_eco_id": "543B56A3BE5FC85C7E389E6CFC4A3AB2",
                    "pay_amt": 5,
                    "create_time": "2024-04-02 11:05:43",
                    "is_adjust": 1,
                    "found_type_name": "预估",
                    "budget_level_name": "中央级",
                    "planaviamt": 2000,
                    "threesafe_symbolcat": "000-非“三保”支出",
                    "budget_level_id": "ADFCEF32115CB6261336494BB71CB66D",
                    "pro": "42000024219P007000051-219011指标管理1512",
                    "is_manager": "2",
                    "is_gov_pur_code": "2",
                    "dep_bgt_eco": "F2684D4AE3086DBDA207A71B269729D0##30101##基本工资",
                    "creater": "1F0795D7E8724F998426100EB01D6195",
                    "bgt_doc_title": "219011指标管理1512",
                    "threesafe_symbolcat_name": "非“三保”支出",
                    "fund_type_code": "11111",
                    "origin_model_code": "2",
                    "bgt_source_name": "当期拨款（支出）",
                    "adj_date": "2024-04-02 11:02:54",
                    "useamt": 7,
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
                    "pro_code": "42000024219P007000051",
                    "amount": 100000,
                    "bgt_dec": "219011指标管理1512",
                    "is_end": "1",
                    "exp_func": "2010101-行政运行",
                    "dep_bgt_eco_code": "30101",
                    "gov_bgt_eco_name": "工资奖金津补贴",
                    "plancanuseamt": 1963,
                    "agency_acct_name": "",
                    "agency_acct_no": "",
                    "pay_bank_name": "中国银行股份有限公司武汉水果湖支行",
                    "social_credit_code": "",
                    "pay_acct_name": "湖北省财政厅国库收付局",
                    "payee_acct_name": "湖北鼎力恒建设有限公司",
                    "pay_acct_no": "565157523274",
                    "payee_acct_no": "3202010619100148797",
                    "pay_acct_bank_name": "中国银行股份有限公司武汉水果湖支行",
                    "payee_acct_bank_name": "工商银行武汉空港支行",
                    "payee_acct_code": "",
                    "fund_traobj_type": "576DE01E1B3326464E6B75DE8984BD2C##11##与部门外同级政府单位",
                    "fund_traobj_type_id": "576DE01E1B3326464E6B75DE8984BD2C",
                    "fund_traobj_type_code": "11",
                    "fund_traobj_type_name": "与部门外同级政府单位",
                    "internal_dep": "4C1D9565CB9D48948F89E4784AE804E7##11##办公室",
                    "internal_dep_id": "4C1D9565CB9D48948F89E4784AE804E7",
                    "internal_dep_code": "11",
                    "internal_dep_name": "办公室",
                    "set_mode": "F522AB99C43B9A2A4DD4C30CB75B50C7##1##电子转账支付",
                    "set_mode_id": "F522AB99C43B9A2A4DD4C30CB75B50C7",
                    "set_mode_code": "1",
                    "set_mode_name": "电子转账支付",
                    "use_des": "国库集中支付录入",
                    "pay_app_amt": 5,
                    "pay_app_amt_big": "伍元整",
                    "contract_no": "",
                    "acc_type_id": "D3828BFDBF8EE69B76117257F5C6QXC4",
                    "acc_type_code": "22",
                    "acc_type_name": "财政零余额账户",
                    "is_advancefunds": "2",
                    "pay_acct_id": "0x6A115293F546EB11E7BF33B87B7EDB11F",
                    "pay_acct_code": "104521004200",
                    "pay_bank_id": "7CD841709EB64A53B4D8122509DEA3F2",
                    "pay_bank_code": "104521004200",
                    "attachment_id": "",
                    "plan_balance_id": "1775326015709990912",
                    "fileList": [],
                    "ext": {
                        "is_advancefunds": "2",
                        "is_pural": "0"
                    }
                }
            ]
        }
        gkjzzfsqlr_insert_data_str = json.dumps(gkjzzfsqlr_insert_data)
        try:
            gkjzzfsqlr_insert_start=time.time()   #开始时间
            gkjzzfsqlr_insert_res = requests.post(gkjzzfsqlr_insert_url,
                                                        headers=gkjzzfsqlr_insert_headers,
                                                        data=gkjzzfsqlr_insert_data_str)
            gkjzzfsqlr_insert_res_json = gkjzzfsqlr_insert_res.json()
            gkjzzfsqlr_insert_end =time.time()   #结束时间
            gkjzzfsqlr_insert_res_time= gkjzzfsqlr_insert_end -gkjzzfsqlr_insert_start
            gkjzzfsqlr_insert_res_time_ms=  gkjzzfsqlr_insert_res_time * 1000
            print("\n")
            print(f"响应时间：{gkjzzfsqlr_insert_res_time_ms}毫秒")

            # print(gkjzzfsqlr_insert_res.text)
            logss.logger.info("请求参数：{}，{}，{}".format(gkjzzfsqlr_insert_url,gkjzzfsqlr_insert_data_str,gkjzzfsqlr_insert_headers))
            logss.logger.info("返回结果：{}".format(gkjzzfsqlr_insert_res.text))

            ###断言
            response_rscode = gkjzzfsqlr_insert_res_json.get('rscode')
            response_result = gkjzzfsqlr_insert_res_json.get('result')

            ###使用pytest.assume进行断言，失败一个后，可用正常允许其它用例
            # pytest.assume(agency_res.status_code == 200)
            # pytest.assume(response_rscode == 200 )
            # pytest.assume(response_result == "请求成功")

            assert gkjzzfsqlr_insert_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"
        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s",e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step01)国库集中支付申请录入)")
    @allure.title("国库集中支付申请录入：未送审列表")
    def testgkjzzfsqlrLoadTableDatas(self):
        gkjzzfsqlr_loadTableDatas_url = base_url + '/payfront/pay-voucher-service/v3/payvoucherbill/loadtabledatas'
        gkjzzfsqlr_loadTableDatas_headers = {"Content-Type": "application/json",
                                            "tokenid": tokenids}
        gkjzzfsqlr_loadTableDatas_data = {
            "statusCode": "1",
            "menuId": "D009D52AA14111EBBD508F93D7A97BB7",
            "leftTreeCode": "",
            "isHaveZero": "0",
            "appId": "pay_voucher",
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "roleId": "201EC9F7611B11B38E60BA5B10633BDB",
            "params": {
                "accountClsId": "4E72561AB3CD477EB8DFD51813EC2FB2",
                "accountType": "63",
                "isFinancial": "1",
                "cptName": "pay89",
                "batchUserEleType": "1",
                "showContact": "false",
                "contactType": "0"
            },
            "pageNum": 1,
            "pageSize": 1000000,
            "sort": "fi_order asc,create_time desc,pay_cert_no desc",
            "condition": {}
        }

        # 将dict转换为str
        gkjzzfsqlr_loadTableDatas_data_str = json.dumps(gkjzzfsqlr_loadTableDatas_data)
        try:
            gkjzzfsqlr_loadTableDatas_start = time.time()  # 开始时间
            gkjzzfsqlr_loadTableDatas_res = requests.post(gkjzzfsqlr_loadTableDatas_url,
                                                         headers=gkjzzfsqlr_loadTableDatas_headers,
                                                         data=gkjzzfsqlr_loadTableDatas_data_str)
            gkjzzfsqlr_loadTableDatas_res_json = gkjzzfsqlr_loadTableDatas_res.json()
            gkjzzfsqlr_loadTableDatas_end = time.time()  # 结束时间
            gkjzzfsqlr_loadTableDatas_res_time = gkjzzfsqlr_loadTableDatas_end - gkjzzfsqlr_loadTableDatas_start
            gkjzzfsqlr_loadTableDatas_res_time_ms = gkjzzfsqlr_loadTableDatas_res_time * 1000
            print("\n")
            print(f"响应时间：{gkjzzfsqlr_loadTableDatas_res_time_ms}毫秒")
            # print(gkjzzfsqlr_loadTableDatas_res.text)

            global gkjzzfsqlr_id
            gkjzzfsqlr_id = gkjzzfsqlr_loadTableDatas_res_json.get("data").get("rows")[0]["id"]
            print("支付数据id：", gkjzzfsqlr_id)

            global gkjzzfsqlr_pay_cert_id
            gkjzzfsqlr_pay_cert_id = gkjzzfsqlr_loadTableDatas_res_json.get("data").get("rows")[0]["pay_cert_id"]
            print("支付凭证id：",gkjzzfsqlr_pay_cert_id)

            global gkjzzfsqlr_pay_cert_no
            gkjzzfsqlr_pay_cert_no = gkjzzfsqlr_loadTableDatas_res_json.get("data").get("rows")[0]["pay_cert_no"]
            print("支付凭证号：", gkjzzfsqlr_pay_cert_no)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(gkjzzfsqlr_loadTableDatas_url, gkjzzfsqlr_loadTableDatas_data_str,
                                       gkjzzfsqlr_loadTableDatas_headers))
            logss.logger.info("返回结果：{}".format(gkjzzfsqlr_loadTableDatas_res.text))
            ###断言
            response_rscode = gkjzzfsqlr_loadTableDatas_res_json.get('rscode')
            response_result = gkjzzfsqlr_loadTableDatas_res_json.get('result')

            # pytest.assume(gkjzzfsqlr_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert gkjzzfsqlr_loadTableDatas_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step01)国库集中支付录入")
    @allure.title("国库集中支付申请录入：送审")
    def testgkjzzfsqlrAuditbycheck(self):
        gkjzzfsqlr_auditbycheck_url = base_url + '/payfront/pay-voucher-service/v3/payvoucherbill/front/action/auditbycheck'
        gkjzzfsqlr_auditbycheck_headers = {"Content-Type": "application/json",
                                       "tokenid": tokenids}
        gkjzzfsqlr_auditbycheck_data = {
            "actionName": "送审",
            "appId": "pay_voucher",
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "menuId": "D009D52AA14111EBBD508F93D7A97BB7",
            "actionType": "2",
            "glType": "0",
            "ids": [
                gkjzzfsqlr_id
            ]
        }

        # 将dict转换为str
        gkjzzfsqlr_auditbycheck_data_str = json.dumps(gkjzzfsqlr_auditbycheck_data)
        try:
            gkjzzfsqlr_auditbycheck_start = time.time()  # 开始时间
            gkjzzfsqlr_auditbycheck_res = requests.post(gkjzzfsqlr_auditbycheck_url,
                                                    headers=gkjzzfsqlr_auditbycheck_headers,
                                                    data=gkjzzfsqlr_auditbycheck_data_str)
            gkjzzfsqlr_auditbycheck_res_json = gkjzzfsqlr_auditbycheck_res.json()
            gkjzzfsqlr_auditbycheck_end = time.time()  # 结束时间
            gkjzzfsqlr_auditbycheck_res_time = gkjzzfsqlr_auditbycheck_end - gkjzzfsqlr_auditbycheck_start
            gkjzzfsqlr_auditbycheck_res_time_ms = gkjzzfsqlr_auditbycheck_res_time * 1000
            print("\n")
            print(f"响应时间：{gkjzzfsqlr_auditbycheck_res_time_ms}毫秒")
            # print(gkjzzfsqlr_auditbycheck_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(gkjzzfsqlr_auditbycheck_url, gkjzzfsqlr_auditbycheck_data_str,
                                       gkjzzfsqlr_auditbycheck_headers))
            logss.logger.info("返回结果：{}".format(gkjzzfsqlr_auditbycheck_res.text))
            ###断言
            response_rscode = gkjzzfsqlr_auditbycheck_res_json.get('rscode')
            response_result = gkjzzfsqlr_auditbycheck_res_json.get('result')

            # pytest.assume(gkjzzfsqlr_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert gkjzzfsqlr_auditbycheck_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step02)支付申请审核(单位)")
    @allure.title("支付申请审核(单位：审核")
    def testzfsqshdwAuditByWarn(self):
        zfsqshdw_auditByWarn_url = base_url + '/payfront/pay-voucher-service/v3/payvoucherbill/front/action/auditByWarn'
        zfsqshdw_auditByWarn_headers = {"Content-Type": "application/json",
                                       "tokenid": tokenids}
        zfsqshdw_auditByWarn_data = {
            "actionName": "审核",
            "appId": "pay_voucher",
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "menuId": "55023A7EC8574A28AF301FC3D83B1D9F",
            "actionType": "2",
            "glType": "0",
            "ids": [
                gkjzzfsqlr_id
            ],
            "params": {
                "checkReviewAgain": "1"
            }
        }

        # 将dict转换为str
        zfsqshdw_auditByWarn_data_str = json.dumps(zfsqshdw_auditByWarn_data)
        try:
            zfsqshdw_auditByWarn_start = time.time()  # 开始时间
            zfsqshdw_auditByWarn_res = requests.post(zfsqshdw_auditByWarn_url,
                                                    headers=zfsqshdw_auditByWarn_headers,
                                                    data=zfsqshdw_auditByWarn_data_str)
            zfsqshdw_auditByWarn_res_json = zfsqshdw_auditByWarn_res.json()
            zfsqshdw_auditByWarn_end = time.time()  # 结束时间
            zfsqshdw_auditByWarn_res_time = zfsqshdw_auditByWarn_end - zfsqshdw_auditByWarn_start
            zfsqshdw_auditByWarn_res_time_ms = zfsqshdw_auditByWarn_res_time * 1000
            print("\n")
            print(f"响应时间：{zfsqshdw_auditByWarn_res_time_ms}毫秒")
            # print(zfsqshdw_auditByWarn_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(zfsqshdw_auditByWarn_url, zfsqshdw_auditByWarn_data_str,
                                       zfsqshdw_auditByWarn_headers))
            logss.logger.info("返回结果：{}".format(zfsqshdw_auditByWarn_res.text))
            ###断言
            response_rscode = zfsqshdw_auditByWarn_res_json.get('rscode')
            response_result = zfsqshdw_auditByWarn_res_json.get('result')

            # pytest.assume(zblr_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert zfsqshdw_auditByWarn_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step03)支付申请复核(财政)")
    @allure.title("支付申请复核(财政)：审核")
    def testZfsqfhczaudit(self):
        zfsqfhcz_audit_url = base_url + '/payfront/pay-voucher-service/v3/payvoucherbill/action/audit'
        zfsqfhcz_audit_headers = {"Content-Type": "application/json",
                                       "tokenid": tokenids}
        zfsqfhcz_audit_data = {
            "actionName": "审核",
            "appId": "pay_voucher",
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "menuId": "B4BE78BEA168EC1AAB9F47B593F02C1B",
            "actionType": "2",
            "glType": "0",
            "ids": [
                gkjzzfsqlr_id
            ]

        }

        # 将dict转换为str
        zfsqfhcz_audit_data_str = json.dumps(zfsqfhcz_audit_data)
        try:
            zfsqfhcz_audit_start = time.time()  # 开始时间
            zfsqfhcz_audit_res = requests.post(zfsqfhcz_audit_url,
                                                    headers=zfsqfhcz_audit_headers,
                                                    data=zfsqfhcz_audit_data_str)
            zfsqfhcz_audit_res_json = zfsqfhcz_audit_res.json()
            zfsqfhcz_audit_end = time.time()  # 结束时间
            zfsqfhcz_audit_res_time = zfsqfhcz_audit_end - zfsqfhcz_audit_start
            zfsqfhcz_audit_res_time_ms = zfsqfhcz_audit_res_time * 1000
            print("\n")
            print(f"响应时间：{zfsqfhcz_audit_res_time_ms}毫秒")
            # print(zfsqfhcz_audit_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(zfsqfhcz_audit_url, zfsqfhcz_audit_data_str,
                                       zfsqfhcz_audit_headers))
            logss.logger.info("返回结果：{}".format(zfsqfhcz_audit_res.text))
            ###断言
            response_rscode = zfsqfhcz_audit_res_json.get('rscode')
            response_result = zfsqfhcz_audit_res_json.get('result')

            # pytest.assume(zblr_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert zfsqfhcz_audit_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step04)支付凭证生成(财政)")
    @allure.title("支付凭证生成(财政)：生成")
    def testzfpzscczaudit(self):
        zfpzsccz_audit_url = base_url + '/payfront/pay-voucher-service/v3/payvoucherbill/action/audit'
        zfpzsccz_audit_headers = {"Content-Type": "application/json",
                                       "tokenid": tokenids}
        zfpzsccz_audit_data = {
            "actionName": "生成",
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "appId": "pay_voucher",
            "menuId": "74401623794779F9A2E652311143A04F",
            "actionType": "2",
            "glType": "1",
            "ids": [
                gkjzzfsqlr_id
            ],
            "params": {
                "picpath": "img/indexpic/voucher_query.png",
                "menuNotRefresh": "true",
                "nextNode": "B198CFFC387EA6D1E1307A101AA5A5F2",
                "accountType": "63",
                "nextWorkflow": "pay_voucher_bill",
                "nextNodes": "B198CFFC387EA6D1E1307A101AA5A5F2",
                "isCreateBill": "1",
                "showContact": "false",
                "contactType": "1"
            }

        }

        # 将dict转换为str
        zfpzsccz_audit_data_str = json.dumps(zfpzsccz_audit_data)
        try:
            zfpzsccz_audit_start = time.time()  # 开始时间
            zfpzsccz_audit_res = requests.post(zfpzsccz_audit_url,
                                                    headers=zfpzsccz_audit_headers,
                                                    data=zfpzsccz_audit_data_str)
            zfpzsccz_audit_res_json = zfpzsccz_audit_res.json()
            zfpzsccz_audit_end = time.time()  # 结束时间
            zfpzsccz_audit_res_time = zfpzsccz_audit_end - zfpzsccz_audit_start
            zfpzsccz_audit_res_time_ms = zfpzsccz_audit_res_time * 1000
            print("\n")
            print(f"响应时间：{zfpzsccz_audit_res_time_ms}毫秒")
            # print(zfpzsccz_audit_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(zfpzsccz_audit_url, zfpzsccz_audit_data_str,
                                       zfpzsccz_audit_headers))
            logss.logger.info("返回结果：{}".format(zfpzsccz_audit_res.text))
            ###断言
            response_rscode = zfpzsccz_audit_res_json.get('rscode')
            response_result = zfpzsccz_audit_res_json.get('result')

            # pytest.assume(zblr_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert zfpzsccz_audit_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step05)支付凭证初审签章(财政)")
    @allure.title("支付凭证初审签章(财政)：获取印章位置")
    def testzfpzcsqzczStampPositions(self):
        zfpzcsqzcz_StampPositions_url = base_url + '/payfront/pay-common-service/v1/queryVoucherSignStampPositions'
        zfpzcsqzcz_StampPositions_headers = {"Content-Type": "application/json",
                                          "tokenid": tokenids}
        zfpzcsqzcz_StampPositions_data = {
            "vtCode": "5214",
            "voucherNoList": [
                gkjzzfsqlr_pay_cert_no
            ],
            "actionId": "B198CFFC387EA6D1E1307A101AA5A5F2"
        }

        # 将dict转换为str
        zfpzcsqzcz_StampPositions_data_str = json.dumps(zfpzcsqzcz_StampPositions_data)
        try:
            zfpzcsqzcz_StampPositions_start = time.time()  # 开始时间
            zfpzcsqzcz_StampPositions_res = requests.post(zfpzcsqzcz_StampPositions_url,
                                                       headers=zfpzcsqzcz_StampPositions_headers,
                                                       data=zfpzcsqzcz_StampPositions_data_str)
            zfpzcsqzcz_StampPositions_res_json = zfpzcsqzcz_StampPositions_res.json()
            zfpzcsqzcz_StampPositions_end = time.time()  # 结束时间
            zfpzcsqzcz_StampPositions_res_time = zfpzcsqzcz_StampPositions_end - zfpzcsqzcz_StampPositions_start
            zfpzcsqzcz_StampPositions_res_time_ms = zfpzcsqzcz_StampPositions_res_time * 1000
            print("\n")
            print(f"响应时间：{zfpzcsqzcz_StampPositions_res_time_ms}毫秒")
            # print(zfpzcsqzcz_StampPositions_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(zfpzcsqzcz_StampPositions_url, zfpzcsqzcz_StampPositions_data_str,
                                       zfpzcsqzcz_StampPositions_headers))
            logss.logger.info("返回结果：{}".format(zfpzcsqzcz_StampPositions_res.text))
            ###断言
            response_rscode = zfpzcsqzcz_StampPositions_res_json.get('rscode')
            response_result = zfpzcsqzcz_StampPositions_res_json.get('result')

            # pytest.assume(zblr_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert zfpzcsqzcz_StampPositions_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step05)支付凭证初审签章(财政)")
    @allure.title("支付凭证初审签章(财政)：获取签名参数")
    def testzfpzcsqzczepayHttpParams(self):
        zfpzcsqzcz_epayHttpParams_url = base_url + '/payfront/pay-common-service/v1/epayHttpParams'
        zfpzcsqzcz_epayHttpParams_headers = {"Content-Type": "application/json",
                                          "tokenid": tokenids}
        zfpzcsqzcz_epayHttpParams_data = {
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "opid": "B198CFFC387EA6D1E1307A101AA5A5F258CAB89AF1A04EF3B7E19C1DBCFDA502",
            "bill_no": [
                gkjzzfsqlr_pay_cert_no
            ],
            "payBusTypeCodes": [
                "1"
            ],
            "action_id": "B198CFFC387EA6D1E1307A101AA5A5F2",
            "work_flow_id": "pay_voucher_bill",
            "isDoWorkFlow": 'true',
            "isSignStamp": 'true',
            "appId": "pay_voucher",
            "menuId": "B198CFFC387EA6D1E1307A101AA5A5F2",
            "actionType": "2",
            "actionName": "直接签章",
            "vtCode": "5214",
            "glType": "0",
            "ids": [
                gkjzzfsqlr_pay_cert_id
            ],
            "stampurl": "pay-voucher-service/v3/payvoucherbill/action/stamp",
            "admDivCode": "420000000",
            "justShow": 'false'
        }

        # 将dict转换为str
        zfpzcsqzcz_epayHttpParams_data_str = json.dumps(zfpzcsqzcz_epayHttpParams_data)
        try:
            zfpzcsqzcz_epayHttpParams_start = time.time()  # 开始时间
            zfpzcsqzcz_epayHttpParams_res = requests.post(zfpzcsqzcz_epayHttpParams_url,
                                                       headers=zfpzcsqzcz_epayHttpParams_headers,
                                                       data=zfpzcsqzcz_epayHttpParams_data_str)
            zfpzcsqzcz_epayHttpParams_res_json = zfpzcsqzcz_epayHttpParams_res.json()
            zfpzcsqzcz_epayHttpParams_end = time.time()  # 结束时间
            zfpzcsqzcz_epayHttpParams_res_time = zfpzcsqzcz_epayHttpParams_end - zfpzcsqzcz_epayHttpParams_start
            zfpzcsqzcz_epayHttpParams_res_time_ms = zfpzcsqzcz_epayHttpParams_res_time * 1000
            print("\n")
            print(f"响应时间：{zfpzcsqzcz_epayHttpParams_res_time_ms}毫秒")
            # print(zfpzcsqzcz_epayHttpParams_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(zfpzcsqzcz_epayHttpParams_url, zfpzcsqzcz_epayHttpParams_data_str,
                                       zfpzcsqzcz_epayHttpParams_headers))
            logss.logger.info("返回结果：{}".format(zfpzcsqzcz_epayHttpParams_res.text))
            ###断言
            response_rscode = zfpzcsqzcz_epayHttpParams_res_json.get('rscode')
            response_result = zfpzcsqzcz_epayHttpParams_res_json.get('result')

            # pytest.assume(zblr_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert zfpzcsqzcz_epayHttpParams_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step05)支付凭证初审签章(财政)")
    @allure.title("支付凭证初审签章(财政)：签名")
    def testzfpzcsqzczsign(self):
        zfpzcsqzcz_sign_url = base_url + '/payfront/pay-voucher-service/v3/payvoucherbill/action/sign'
        zfpzcsqzcz_sign_headers = {"Content-Type": "application/json",
                                          "tokenid": tokenids}
        zfpzcsqzcz_sign_data = {
            "vt_code": "5214",
            "vouchers": "<?xml version=\"1.0\" encoding=\"GBK\" ?>\n<MOF>\n    <VoucherCount>1</VoucherCount>\n    <VoucherBody VoucherNo=\"gkjzzfsqlr_pay_cert_no\" AdmDivCode=\"420000\" StYear=\"2024\" VtCode=\"5214\">\n        <VoucherFlag>0</VoucherFlag>\n        <Voucher>PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iR0JLIj8+Cgo8Vm91Y2hlcj4KICA8SWQ+NThDQUI4OUFGMUEwNEVGM0I3RTE5QzFEQkNGREE1MDI8L0lkPgogIDxBZG1EaXZDb2RlPjQyMDAwMDwvQWRtRGl2Q29kZT4KICA8U3RZZWFyPjIwMjQ8L1N0WWVhcj4KICA8VnRDb2RlPjUyMTQ8L1Z0Q29kZT4KICA8Vm91RGF0ZT4yMDI0MDQwODwvVm91RGF0ZT4KICA8Vm91Y2hlck5vPlcwMDI0QzEwMDAwMDU0PC9Wb3VjaGVyTm8+CiAgPEJpbGxObz5TUVcwMDI0MTgwMDAwMDY8L0JpbGxObz4KICA8RnVuZFR5cGVDb2RlPjExMTExPC9GdW5kVHlwZUNvZGU+CiAgPEZ1bmRUeXBlTmFtZT6+rbfRsqa/7rK51vo8L0Z1bmRUeXBlTmFtZT4KICA8Qmd0VHlwZUNvZGU+MTE8L0JndFR5cGVDb2RlPgogIDxCZ3RUeXBlTmFtZT7UpLKm1rix6jwvQmd0VHlwZU5hbWU+CiAgPFBheVR5cGVDb2RlPjE8L1BheVR5cGVDb2RlPgogIDxQYXlUeXBlTmFtZT65+r/ivK/W0NanuLY8L1BheVR5cGVOYW1lPgogIDxQcm9DYXRDb2RlPjwvUHJvQ2F0Q29kZT4KICA8UHJvQ2F0TmFtZT48L1Byb0NhdE5hbWU+CiAgPE1PRkRlcENvZGU+MDk8L01PRkRlcENvZGU+CiAgPE1PRkRlcE5hbWU+xanStbSmPC9NT0ZEZXBOYW1lPgogIDxTdXBEZXBDb2RlPjIxOTwvU3VwRGVwQ29kZT4KICA8U3VwRGVwTmFtZT66/rGxyqHFqdK1xam05cz8PC9TdXBEZXBOYW1lPgogIDxBZ2VuY3lDb2RlPjIxOTAxMTwvQWdlbmN5Q29kZT4KICA8QWdlbmN5TmFtZT66/rGxyqG5+7LosOy5q8rSPC9BZ2VuY3lOYW1lPgogIDxFeHBGdW5jQ29kZT4yMDEwMTAxPC9FeHBGdW5jQ29kZT4KICA8RXhwRnVuY05hbWU+0NDV/tTL0NA8L0V4cEZ1bmNOYW1lPgogIDxFeHBGdW5jQ29kZTE+MjAxPC9FeHBGdW5jQ29kZTE+CiAgPEV4cEZ1bmNOYW1lMT7Su7Djuau5srf+zvHWp7P2PC9FeHBGdW5jTmFtZTE+CiAgPEV4cEZ1bmNDb2RlMj4wMTwvRXhwRnVuY0NvZGUyPgogIDxFeHBGdW5jTmFtZTI+yMu088rCzvE8L0V4cEZ1bmNOYW1lMj4KICA8RXhwRnVuY0NvZGUzPjAxPC9FeHBGdW5jQ29kZTM+CiAgPEV4cEZ1bmNOYW1lMz7Q0NX+1MvQ0DwvRXhwRnVuY05hbWUzPgogIDxHb3ZFeHBFY29Db2RlPjwvR292RXhwRWNvQ29kZT4KICA8R292RXhwRWNvTmFtZT48L0dvdkV4cEVjb05hbWU+CiAgPERlcEV4cEVjb0NvZGU+MzAxMDE8L0RlcEV4cEVjb0NvZGU+CiAgPERlcEV4cEVjb05hbWU+u/mxvrmk18o8L0RlcEV4cEVjb05hbWU+CiAgPERlcFByb0NvZGU+NDIwMDAwMjQyMTlQMDA3MDAwMDUxPC9EZXBQcm9Db2RlPgogIDxEZXBQcm9OYW1lPjIxOTAxMda4seq53MDtMTUxMjwvRGVwUHJvTmFtZT4KICA8U2V0TW9kZUNvZGU+MTwvU2V0TW9kZUNvZGU+CiAgPFNldE1vZGVOYW1lPrXn19PXqtXL1qe4tjwvU2V0TW9kZU5hbWU+CiAgPFBheUJhbmtDb2RlPjEwNDUyMTAwNDIwMDwvUGF5QmFua0NvZGU+CiAgPFBheUJhbmtOYW1lPtbQufrS+NDQucm33dPQz965q8u+zuS6usuuufu6/tan0NA8L1BheUJhbmtOYW1lPgogIDxDbGVhckJhbmtDb2RlPjwvQ2xlYXJCYW5rQ29kZT4KICA8Q2xlYXJCYW5rTmFtZT48L0NsZWFyQmFua05hbWU+CiAgPENsZWFyQWNjdE5vPjwvQ2xlYXJBY2N0Tm8+CiAgPENsZWFyQWNjdE5hbWU+PC9DbGVhckFjY3ROYW1lPgogIDxDbGVhckFjY3RCYW5rTmFtZT48L0NsZWFyQWNjdEJhbmtOYW1lPgogIDxQYXllZUFjY3RObz4xNzAxNjIwMTA0MDAxMTI5NDwvUGF5ZWVBY2N0Tm8+CiAgPFBheWVlQWNjdE5hbWU+1tC5+sqvu6/P+srbucm33dPQz965q8u+uv6xsc7kurrKr9PNt9a5q8u+PC9QYXllZUFjY3ROYW1lPgogIDxQYXllZUFjY3RCYW5rTmFtZT7FqdDQs36/2tan0NDTqtK1ytI8L1BheWVlQWNjdEJhbmtOYW1lPgogIDxQYXllZUFjY3RCYW5rTm8+PC9QYXllZUFjY3RCYW5rTm8+CiAgPFBheUFjY3RObz41NjUxNTc1MjMyNzQ8L1BheUFjY3RObz4KICA8UGF5QWNjdE5hbWU+uv6xscqhssbV/sz8ufq/4srVuLa+1jwvUGF5QWNjdE5hbWU+CiAgPFBheUFjY3RCYW5rTmFtZT7W0Ln60vjQ0LnJt93T0M/euavLvs7kurrLrrn7uv7Wp9DQPC9QYXlBY2N0QmFua05hbWU+CiAgPFBheVN1bW1hcnlDb2RlPjwvUGF5U3VtbWFyeUNvZGU+CiAgPFBheVN1bW1hcnlOYW1lPrn6v+K8r9bQ1qe4trT6seA8L1BheVN1bW1hcnlOYW1lPgogIDxQYXlBbXQ+My4wMDwvUGF5QW10PgogIDxCdXNpbmVzc1R5cGVDb2RlPjE8L0J1c2luZXNzVHlwZUNvZGU+CiAgPEJ1c2luZXNzVHlwZU5hbWU+xtXNqNK1zvE8L0J1c2luZXNzVHlwZU5hbWU+CiAgPFRheEJpbGxObz48L1RheEJpbGxObz4KICA8VGF4YXllcklEPjwvVGF4YXllcklEPgogIDxUYXhPcmdDb2RlPjwvVGF4T3JnQ29kZT4KICA8R292UHJvY3VyZW1lbnRJRD48L0dvdlByb2N1cmVtZW50SUQ+CiAgPENoZWNrTm8+PC9DaGVja05vPgogIDxQYXlDb2RlPjwvUGF5Q29kZT4KICA8Rm9yZWlnbkFtdD4wPC9Gb3JlaWduQW10PgogIDxDdXJyZW5jeUNvZGU+Q05ZPC9DdXJyZW5jeUNvZGU+CiAgPEVzdFJhdD48L0VzdFJhdD4KICA8QW10VW5pdD48L0FtdFVuaXQ+CiAgPFhQYXlEYXRlPjwvWFBheURhdGU+CiAgPFhBZ2VudEJ1c2luZXNzTm8+PC9YQWdlbnRCdXNpbmVzc05vPgogIDxYQ2hlY2tObz48L1hDaGVja05vPgogIDxYUGF5QW10PjA8L1hQYXlBbXQ+CiAgPFhQYXllZUFjY3RCYW5rTmFtZT48L1hQYXllZUFjY3RCYW5rTmFtZT4KICA8WFBheWVlQWNjdE5vPjwvWFBheWVlQWNjdE5vPgogIDxYUGF5ZWVBY2N0TmFtZT48L1hQYXllZUFjY3ROYW1lPgogIDxIb2xkMT4xMjwvSG9sZDE+CiAgPEhvbGQyPjwvSG9sZDI+CiAgPERldGFpbExpc3Q+CiAgICA8RGV0YWlsPgogICAgICA8SWQ+RDk1NEZBMjJBMDUzNEQ2RUEwRDI5RDVBOUJGODZFNEY8L0lkPgogICAgICA8Vm91Y2hlckJpbGxJZD41OENBQjg5QUYxQTA0RUYzQjdFMTlDMURCQ0ZEQTUwMjwvVm91Y2hlckJpbGxJZD4KICAgICAgPFZvdWNoZXJCaWxsTm8+VzAwMjRDMTAwMDAwNTQ8L1ZvdWNoZXJCaWxsTm8+CiAgICAgIDxWb3VjaGVyRGV0YWlsTm8+U1FXMDAyNDE4MDAwMDA2PC9Wb3VjaGVyRGV0YWlsTm8+CiAgICAgIDxGdW5kVHlwZUNvZGU+MTExMTE8L0Z1bmRUeXBlQ29kZT4KICAgICAgPEZ1bmRUeXBlTmFtZT6+rbfRsqa/7rK51vo8L0Z1bmRUeXBlTmFtZT4KICAgICAgPEJndFR5cGVDb2RlPjExPC9CZ3RUeXBlQ29kZT4KICAgICAgPEJndFR5cGVOYW1lPtSksqbWuLHqPC9CZ3RUeXBlTmFtZT4KICAgICAgPFByb0NhdENvZGU+PC9Qcm9DYXRDb2RlPgogICAgICA8UHJvQ2F0TmFtZT48L1Byb0NhdE5hbWU+CiAgICAgIDxQYXlLaW5kQ29kZT48L1BheUtpbmRDb2RlPgogICAgICA8UGF5S2luZE5hbWU+PC9QYXlLaW5kTmFtZT4KICAgICAgPE1PRkRlcENvZGU+PC9NT0ZEZXBDb2RlPgogICAgICA8TU9GRGVwTmFtZT48L01PRkRlcE5hbWU+CiAgICAgIDxTdXBEZXBDb2RlPjIxOTwvU3VwRGVwQ29kZT4KICAgICAgPFN1cERlcE5hbWU+uv6xscqhxanStcWptOXM/DwvU3VwRGVwTmFtZT4KICAgICAgPEFnZW5jeUNvZGU+MjE5MDExPC9BZ2VuY3lDb2RlPgogICAgICA8QWdlbmN5TmFtZT66/rGxyqG5+7LosOy5q8rSPC9BZ2VuY3lOYW1lPgogICAgICA8RXhwRnVuY0NvZGU+MjAxMDEwMTwvRXhwRnVuY0NvZGU+CiAgICAgIDxFeHBGdW5jTmFtZT7Q0NX+1MvQ0DwvRXhwRnVuY05hbWU+CiAgICAgIDxHb3ZFeHBFY29Db2RlPjwvR292RXhwRWNvQ29kZT4KICAgICAgPEdvdkV4cEVjb05hbWU+PC9Hb3ZFeHBFY29OYW1lPgogICAgICA8RGVwRXhwRWNvQ29kZT48L0RlcEV4cEVjb0NvZGU+CiAgICAgIDxEZXBFeHBFY29OYW1lPjwvRGVwRXhwRWNvTmFtZT4KICAgICAgPERlcFByb0NvZGU+PC9EZXBQcm9Db2RlPgogICAgICA8RGVwUHJvTmFtZT48L0RlcFByb05hbWU+CiAgICAgIDxQYXllZUFjY3RObz4xNzAxNjIwMTA0MDAxMTI5NDwvUGF5ZWVBY2N0Tm8+CiAgICAgIDxQYXllZUFjY3ROYW1lPtbQufrKr7uvz/rK27nJt93T0M/euavLvrr+sbHO5Lq6yq/TzbfWuavLvjwvUGF5ZWVBY2N0TmFtZT4KICAgICAgPFBheWVlQWNjdEJhbmtOYW1lPsWp0NCzfr/a1qfQ0NOq0rXK0jwvUGF5ZWVBY2N0QmFua05hbWU+CiAgICAgIDxQYXllZUFjY3RCYW5rTm8+PC9QYXllZUFjY3RCYW5rTm8+CiAgICAgIDxUcmFja2luZ0lEPjwvVHJhY2tpbmdJRD4KICAgICAgPFBheUFtdD4zLjAwPC9QYXlBbXQ+CiAgICAgIDxSZW1hcms+PC9SZW1hcms+CiAgICAgIDxGb3JlaWduQW10PjA8L0ZvcmVpZ25BbXQ+CiAgICAgIDxDdXJyZW5jeUNvZGU+Q05ZPC9DdXJyZW5jeUNvZGU+CiAgICAgIDxFc3RSYXQ+PC9Fc3RSYXQ+CiAgICAgIDxSZWNlaXZlckNvZGU+PC9SZWNlaXZlckNvZGU+CiAgICAgIDxBbXRVbml0PjwvQW10VW5pdD4KICAgICAgPFhQYXlEYXRlPjwvWFBheURhdGU+CiAgICAgIDxYQWdlbnRCdXNpbmVzc05vPjwvWEFnZW50QnVzaW5lc3NObz4KICAgICAgPFhDaGVja05vPjwvWENoZWNrTm8+CiAgICAgIDxYUGF5QW10PjwvWFBheUFtdD4KICAgICAgPFhBZGRXb3JkPjwvWEFkZFdvcmQ+CiAgICAgIDxYUGF5ZWVBY2N0QmFua05hbWU+PC9YUGF5ZWVBY2N0QmFua05hbWU+CiAgICAgIDxYUGF5ZWVBY2N0Tm8+PC9YUGF5ZWVBY2N0Tm8+CiAgICAgIDxYUGF5ZWVBY2N0TmFtZT48L1hQYXllZUFjY3ROYW1lPgogICAgICA8SG9sZDE+PC9Ib2xkMT4KICAgICAgPEhvbGQyPjwvSG9sZDI+CiAgICAgIDxIb2xkMz48L0hvbGQzPgogICAgICA8SG9sZDQ+PC9Ib2xkND4KICAgIDwvRGV0YWlsPgogIDwvRGV0YWlsTGlzdD4KPC9Wb3VjaGVyPgo=</Voucher>\n        <SignStampList>\n            <SignStamp No=\"cz_dwgz\" SN=\"0850ada9e8e443089a30b3fc606d70b2\">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</SignStamp>\n        </SignStampList>\n        <SignatureList />\n    </VoucherBody>\n</MOF>\n",
            "details": "",
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "opid": "B198CFFC387EA6D1E1307A101AA5A5F258CAB89AF1A04EF3B7E19C1DBCFDA502",
            "bill_no": "",
            "payBusTypeCodes": [
                "1"
            ],
            "action_id": "B198CFFC387EA6D1E1307A101AA5A5F2",
            "work_flow_id": "pay_voucher_bill",
            "isDoWorkFlow": 'true',
            "isSignStamp": 'true',
            "appId": "pay_voucher",
            "menuId": "B198CFFC387EA6D1E1307A101AA5A5F2",
            "actionType": "2",
            "actionName": "直接签章",
            "vtCode": "5214",
            "glType": "0",
            "ids": [
                gkjzzfsqlr_pay_cert_id
            ],
            "stampurl": "pay-voucher-service/v3/payvoucherbill/action/stamp",
            "admDivCode": "420000000",
            "justShow": 'false',
            "voucherNos": [
                gkjzzfsqlr_pay_cert_no
            ]
        }

        # 将dict转换为str
        zfpzcsqzcz_sign_data_str = json.dumps(zfpzcsqzcz_sign_data)
        try:
            zfpzcsqzcz_sign_start = time.time()  # 开始时间
            zfpzcsqzcz_sign_res = requests.post(zfpzcsqzcz_sign_url,
                                                       headers=zfpzcsqzcz_sign_headers,
                                                       data=zfpzcsqzcz_sign_data_str)
            zfpzcsqzcz_sign_res_json = zfpzcsqzcz_sign_res.json()
            zfpzcsqzcz_sign_end = time.time()  # 结束时间
            zfpzcsqzcz_sign_res_time = zfpzcsqzcz_sign_end - zfpzcsqzcz_sign_start
            zfpzcsqzcz_sign_res_time_ms = zfpzcsqzcz_sign_res_time * 1000
            print("\n")
            print(f"响应时间：{zfpzcsqzcz_sign_res_time_ms}毫秒")
            # print(zfpzcsqzcz_sign_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(zfpzcsqzcz_sign_url, zfpzcsqzcz_sign_data_str,
                                       zfpzcsqzcz_sign_headers))
            logss.logger.info("返回结果：{}".format(zfpzcsqzcz_sign_res.text))
            ###断言
            response_rscode = zfpzcsqzcz_sign_res_json.get('rscode')
            response_result = zfpzcsqzcz_sign_res_json.get('result')

            # pytest.assume(zblr_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert zfpzcsqzcz_sign_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step06)支付凭证复核签章(财政)")
    @allure.title("支付凭证复核签章(财政)：获取印章位置")
    def testzfpzfhqzczStampPositions(self):
        zfpzfhqzcz_StampPositions_url = base_url + '/payfront/pay-common-service/v1/queryVoucherSignStampPositions'
        zfpzfhqzcz_StampPositions_headers = {"Content-Type": "application/json",
                                          "tokenid": tokenids}
        zfpzfhqzcz_StampPositions_data = {
            "vtCode": "5214",
            "voucherNoList": [
                gkjzzfsqlr_pay_cert_no
            ],
            "actionId": "60D0E448D73949A28EB2C188B8D2333E"
        }

        # 将dict转换为str
        zfpzfhqzcz_StampPositions_data_str = json.dumps(zfpzfhqzcz_StampPositions_data)
        try:
            zfpzfhqzcz_StampPositions_start = time.time()  # 开始时间
            zfpzfhqzcz_StampPositions_res = requests.post(zfpzfhqzcz_StampPositions_url,
                                                       headers=zfpzfhqzcz_StampPositions_headers,
                                                       data=zfpzfhqzcz_StampPositions_data_str)
            zfpzfhqzcz_StampPositions_res_json = zfpzfhqzcz_StampPositions_res.json()
            zfpzfhqzcz_StampPositions_end = time.time()  # 结束时间
            zfpzfhqzcz_StampPositions_res_time = zfpzfhqzcz_StampPositions_end - zfpzfhqzcz_StampPositions_start
            zfpzfhqzcz_StampPositions_res_time_ms = zfpzfhqzcz_StampPositions_res_time * 1000
            print("\n")
            print(f"响应时间：{zfpzfhqzcz_StampPositions_res_time_ms}毫秒")
            # print(zfpzfhqzcz_StampPositions_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(zfpzfhqzcz_StampPositions_url, zfpzfhqzcz_StampPositions_data_str,
                                       zfpzfhqzcz_StampPositions_headers))
            logss.logger.info("返回结果：{}".format(zfpzfhqzcz_StampPositions_res.text))
            ###断言
            response_rscode = zfpzfhqzcz_StampPositions_res_json.get('rscode')
            response_result = zfpzfhqzcz_StampPositions_res_json.get('result')

            # pytest.assume(zblr_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert zfpzfhqzcz_StampPositions_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step06)支付凭证复核签章(财政)")
    @allure.title("支付凭证复核签章(财政)：获取签章参数")
    def testzfpzfhqzczepayHttpParams(self):
        zfpzfhqzcz_epayHttpParams_url = base_url + '/payfront/pay-common-service/v1/epayHttpParams'
        zfpzfhqzcz_epayHttpParams_headers = {"Content-Type": "application/json",
                                          "tokenid": tokenids}
        zfpzfhqzcz_epayHttpParams_data = {
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "opid": "60D0E448D73949A28EB2C188B8D2333E58CAB89AF1A04EF3B7E19C1DBCFDA502",
            "bill_no": [
                gkjzzfsqlr_pay_cert_no
            ],
            "payBusTypeCodes": [
                "1"
            ],
            "action_id": "60D0E448D73949A28EB2C188B8D2333E",
            "work_flow_id": "pay_voucher_bill",
            "isDoWorkFlow": 'true',
            "isSignStamp": 'true',
            "appId": "pay_voucher",
            "menuId": "60D0E448D73949A28EB2C188B8D2333E",
            "actionType": "2",
            "actionName": "直接签章",
            "vtCode": "5214",
            "glType": "0",
            "ids": [
                gkjzzfsqlr_pay_cert_id
            ],
            "stampurl": "pay-voucher-service/v3/payvoucherbill/action/stamp",
            "admDivCode": "420000000",
            "justShow": 'false'
        }

        # 将dict转换为str
        zfpzfhqzcz_epayHttpParams_data_str = json.dumps(zfpzfhqzcz_epayHttpParams_data)
        try:
            zfpzfhqzcz_epayHttpParams_start = time.time()  # 开始时间
            zfpzfhqzcz_epayHttpParams_res = requests.post(zfpzfhqzcz_epayHttpParams_url,
                                                       headers=zfpzfhqzcz_epayHttpParams_headers,
                                                       data=zfpzfhqzcz_epayHttpParams_data_str)
            zfpzfhqzcz_epayHttpParams_res_json = zfpzfhqzcz_epayHttpParams_res.json()
            zfpzfhqzcz_epayHttpParams_end = time.time()  # 结束时间
            zfpzfhqzcz_epayHttpParams_res_time = zfpzfhqzcz_epayHttpParams_end - zfpzfhqzcz_epayHttpParams_start
            zfpzfhqzcz_epayHttpParams_res_time_ms = zfpzfhqzcz_epayHttpParams_res_time * 1000
            print("\n")
            print(f"响应时间：{zfpzfhqzcz_epayHttpParams_res_time_ms}毫秒")
            # print(zfpzfhqzcz_epayHttpParams_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(zfpzfhqzcz_epayHttpParams_url, zfpzfhqzcz_epayHttpParams_data_str,
                                       zfpzfhqzcz_epayHttpParams_headers))
            logss.logger.info("返回结果：{}".format(zfpzfhqzcz_epayHttpParams_res.text))
            ###断言
            response_rscode = zfpzfhqzcz_epayHttpParams_res_json.get('rscode')
            response_result = zfpzfhqzcz_epayHttpParams_res_json.get('result')

            # pytest.assume(zblr_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert zfpzfhqzcz_epayHttpParams_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step06)支付凭证复核签章(财政)")
    @allure.title("支付凭证复核签章(财政)：签章")
    def testzfpzfhqzczstamp(self):
        zfpzfhqzcz_stamp_url = base_url + '/payfront/pay-voucher-service/v3/payvoucherbill/action/stamp'
        zfpzfhqzcz_stamp_headers = {"Content-Type": "application/json",
                                          "tokenid": tokenids}
        zfpzfhqzcz_stamp_data = {
            "vt_code": "5214",
            "vouchers": "<?xml version=\"1.0\" encoding=\"GBK\" ?>\n<MOF>\n    <VoucherCount>1</VoucherCount>\n    <VoucherBody VoucherNo=\"gkjzzfsqlr_pay_cert_no\" AdmDivCode=\"420000\" StYear=\"2024\" VtCode=\"5214\">\n        <VoucherFlag>0</VoucherFlag>\n        <Voucher>PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iR0JLIj8+Cgo8Vm91Y2hlcj4KICA8SWQ+NThDQUI4OUFGMUEwNEVGM0I3RTE5QzFEQkNGREE1MDI8L0lkPgogIDxBZG1EaXZDb2RlPjQyMDAwMDwvQWRtRGl2Q29kZT4KICA8U3RZZWFyPjIwMjQ8L1N0WWVhcj4KICA8VnRDb2RlPjUyMTQ8L1Z0Q29kZT4KICA8Vm91RGF0ZT4yMDI0MDQwODwvVm91RGF0ZT4KICA8Vm91Y2hlck5vPlcwMDI0QzEwMDAwMDU0PC9Wb3VjaGVyTm8+CiAgPEJpbGxObz5TUVcwMDI0MTgwMDAwMDY8L0JpbGxObz4KICA8RnVuZFR5cGVDb2RlPjExMTExPC9GdW5kVHlwZUNvZGU+CiAgPEZ1bmRUeXBlTmFtZT6+rbfRsqa/7rK51vo8L0Z1bmRUeXBlTmFtZT4KICA8Qmd0VHlwZUNvZGU+MTE8L0JndFR5cGVDb2RlPgogIDxCZ3RUeXBlTmFtZT7UpLKm1rix6jwvQmd0VHlwZU5hbWU+CiAgPFBheVR5cGVDb2RlPjE8L1BheVR5cGVDb2RlPgogIDxQYXlUeXBlTmFtZT65+r/ivK/W0NanuLY8L1BheVR5cGVOYW1lPgogIDxQcm9DYXRDb2RlPjwvUHJvQ2F0Q29kZT4KICA8UHJvQ2F0TmFtZT48L1Byb0NhdE5hbWU+CiAgPE1PRkRlcENvZGU+MDk8L01PRkRlcENvZGU+CiAgPE1PRkRlcE5hbWU+xanStbSmPC9NT0ZEZXBOYW1lPgogIDxTdXBEZXBDb2RlPjIxOTwvU3VwRGVwQ29kZT4KICA8U3VwRGVwTmFtZT66/rGxyqHFqdK1xam05cz8PC9TdXBEZXBOYW1lPgogIDxBZ2VuY3lDb2RlPjIxOTAxMTwvQWdlbmN5Q29kZT4KICA8QWdlbmN5TmFtZT66/rGxyqG5+7LosOy5q8rSPC9BZ2VuY3lOYW1lPgogIDxFeHBGdW5jQ29kZT4yMDEwMTAxPC9FeHBGdW5jQ29kZT4KICA8RXhwRnVuY05hbWU+0NDV/tTL0NA8L0V4cEZ1bmNOYW1lPgogIDxFeHBGdW5jQ29kZTE+MjAxPC9FeHBGdW5jQ29kZTE+CiAgPEV4cEZ1bmNOYW1lMT7Su7Djuau5srf+zvHWp7P2PC9FeHBGdW5jTmFtZTE+CiAgPEV4cEZ1bmNDb2RlMj4wMTwvRXhwRnVuY0NvZGUyPgogIDxFeHBGdW5jTmFtZTI+yMu088rCzvE8L0V4cEZ1bmNOYW1lMj4KICA8RXhwRnVuY0NvZGUzPjAxPC9FeHBGdW5jQ29kZTM+CiAgPEV4cEZ1bmNOYW1lMz7Q0NX+1MvQ0DwvRXhwRnVuY05hbWUzPgogIDxHb3ZFeHBFY29Db2RlPjwvR292RXhwRWNvQ29kZT4KICA8R292RXhwRWNvTmFtZT48L0dvdkV4cEVjb05hbWU+CiAgPERlcEV4cEVjb0NvZGU+MzAxMDE8L0RlcEV4cEVjb0NvZGU+CiAgPERlcEV4cEVjb05hbWU+u/mxvrmk18o8L0RlcEV4cEVjb05hbWU+CiAgPERlcFByb0NvZGU+NDIwMDAwMjQyMTlQMDA3MDAwMDUxPC9EZXBQcm9Db2RlPgogIDxEZXBQcm9OYW1lPjIxOTAxMda4seq53MDtMTUxMjwvRGVwUHJvTmFtZT4KICA8U2V0TW9kZUNvZGU+MTwvU2V0TW9kZUNvZGU+CiAgPFNldE1vZGVOYW1lPrXn19PXqtXL1qe4tjwvU2V0TW9kZU5hbWU+CiAgPFBheUJhbmtDb2RlPjEwNDUyMTAwNDIwMDwvUGF5QmFua0NvZGU+CiAgPFBheUJhbmtOYW1lPtbQufrS+NDQucm33dPQz965q8u+zuS6usuuufu6/tan0NA8L1BheUJhbmtOYW1lPgogIDxDbGVhckJhbmtDb2RlPjwvQ2xlYXJCYW5rQ29kZT4KICA8Q2xlYXJCYW5rTmFtZT48L0NsZWFyQmFua05hbWU+CiAgPENsZWFyQWNjdE5vPjwvQ2xlYXJBY2N0Tm8+CiAgPENsZWFyQWNjdE5hbWU+PC9DbGVhckFjY3ROYW1lPgogIDxDbGVhckFjY3RCYW5rTmFtZT48L0NsZWFyQWNjdEJhbmtOYW1lPgogIDxQYXllZUFjY3RObz4xNzAxNjIwMTA0MDAxMTI5NDwvUGF5ZWVBY2N0Tm8+CiAgPFBheWVlQWNjdE5hbWU+1tC5+sqvu6/P+srbucm33dPQz965q8u+uv6xsc7kurrKr9PNt9a5q8u+PC9QYXllZUFjY3ROYW1lPgogIDxQYXllZUFjY3RCYW5rTmFtZT7FqdDQs36/2tan0NDTqtK1ytI8L1BheWVlQWNjdEJhbmtOYW1lPgogIDxQYXllZUFjY3RCYW5rTm8+PC9QYXllZUFjY3RCYW5rTm8+CiAgPFBheUFjY3RObz41NjUxNTc1MjMyNzQ8L1BheUFjY3RObz4KICA8UGF5QWNjdE5hbWU+uv6xscqhssbV/sz8ufq/4srVuLa+1jwvUGF5QWNjdE5hbWU+CiAgPFBheUFjY3RCYW5rTmFtZT7W0Ln60vjQ0LnJt93T0M/euavLvs7kurrLrrn7uv7Wp9DQPC9QYXlBY2N0QmFua05hbWU+CiAgPFBheVN1bW1hcnlDb2RlPjwvUGF5U3VtbWFyeUNvZGU+CiAgPFBheVN1bW1hcnlOYW1lPrn6v+K8r9bQ1qe4trT6seA8L1BheVN1bW1hcnlOYW1lPgogIDxQYXlBbXQ+My4wMDwvUGF5QW10PgogIDxCdXNpbmVzc1R5cGVDb2RlPjE8L0J1c2luZXNzVHlwZUNvZGU+CiAgPEJ1c2luZXNzVHlwZU5hbWU+xtXNqNK1zvE8L0J1c2luZXNzVHlwZU5hbWU+CiAgPFRheEJpbGxObz48L1RheEJpbGxObz4KICA8VGF4YXllcklEPjwvVGF4YXllcklEPgogIDxUYXhPcmdDb2RlPjwvVGF4T3JnQ29kZT4KICA8R292UHJvY3VyZW1lbnRJRD48L0dvdlByb2N1cmVtZW50SUQ+CiAgPENoZWNrTm8+PC9DaGVja05vPgogIDxQYXlDb2RlPjwvUGF5Q29kZT4KICA8Rm9yZWlnbkFtdD4wPC9Gb3JlaWduQW10PgogIDxDdXJyZW5jeUNvZGU+Q05ZPC9DdXJyZW5jeUNvZGU+CiAgPEVzdFJhdD48L0VzdFJhdD4KICA8QW10VW5pdD48L0FtdFVuaXQ+CiAgPFhQYXlEYXRlPjwvWFBheURhdGU+CiAgPFhBZ2VudEJ1c2luZXNzTm8+PC9YQWdlbnRCdXNpbmVzc05vPgogIDxYQ2hlY2tObz48L1hDaGVja05vPgogIDxYUGF5QW10PjA8L1hQYXlBbXQ+CiAgPFhQYXllZUFjY3RCYW5rTmFtZT48L1hQYXllZUFjY3RCYW5rTmFtZT4KICA8WFBheWVlQWNjdE5vPjwvWFBheWVlQWNjdE5vPgogIDxYUGF5ZWVBY2N0TmFtZT48L1hQYXllZUFjY3ROYW1lPgogIDxIb2xkMT4xMjwvSG9sZDE+CiAgPEhvbGQyPjwvSG9sZDI+CiAgPERldGFpbExpc3Q+CiAgICA8RGV0YWlsPgogICAgICA8SWQ+RDk1NEZBMjJBMDUzNEQ2RUEwRDI5RDVBOUJGODZFNEY8L0lkPgogICAgICA8Vm91Y2hlckJpbGxJZD41OENBQjg5QUYxQTA0RUYzQjdFMTlDMURCQ0ZEQTUwMjwvVm91Y2hlckJpbGxJZD4KICAgICAgPFZvdWNoZXJCaWxsTm8+VzAwMjRDMTAwMDAwNTQ8L1ZvdWNoZXJCaWxsTm8+CiAgICAgIDxWb3VjaGVyRGV0YWlsTm8+U1FXMDAyNDE4MDAwMDA2PC9Wb3VjaGVyRGV0YWlsTm8+CiAgICAgIDxGdW5kVHlwZUNvZGU+MTExMTE8L0Z1bmRUeXBlQ29kZT4KICAgICAgPEZ1bmRUeXBlTmFtZT6+rbfRsqa/7rK51vo8L0Z1bmRUeXBlTmFtZT4KICAgICAgPEJndFR5cGVDb2RlPjExPC9CZ3RUeXBlQ29kZT4KICAgICAgPEJndFR5cGVOYW1lPtSksqbWuLHqPC9CZ3RUeXBlTmFtZT4KICAgICAgPFByb0NhdENvZGU+PC9Qcm9DYXRDb2RlPgogICAgICA8UHJvQ2F0TmFtZT48L1Byb0NhdE5hbWU+CiAgICAgIDxQYXlLaW5kQ29kZT48L1BheUtpbmRDb2RlPgogICAgICA8UGF5S2luZE5hbWU+PC9QYXlLaW5kTmFtZT4KICAgICAgPE1PRkRlcENvZGU+PC9NT0ZEZXBDb2RlPgogICAgICA8TU9GRGVwTmFtZT48L01PRkRlcE5hbWU+CiAgICAgIDxTdXBEZXBDb2RlPjIxOTwvU3VwRGVwQ29kZT4KICAgICAgPFN1cERlcE5hbWU+uv6xscqhxanStcWptOXM/DwvU3VwRGVwTmFtZT4KICAgICAgPEFnZW5jeUNvZGU+MjE5MDExPC9BZ2VuY3lDb2RlPgogICAgICA8QWdlbmN5TmFtZT66/rGxyqG5+7LosOy5q8rSPC9BZ2VuY3lOYW1lPgogICAgICA8RXhwRnVuY0NvZGU+MjAxMDEwMTwvRXhwRnVuY0NvZGU+CiAgICAgIDxFeHBGdW5jTmFtZT7Q0NX+1MvQ0DwvRXhwRnVuY05hbWU+CiAgICAgIDxHb3ZFeHBFY29Db2RlPjwvR292RXhwRWNvQ29kZT4KICAgICAgPEdvdkV4cEVjb05hbWU+PC9Hb3ZFeHBFY29OYW1lPgogICAgICA8RGVwRXhwRWNvQ29kZT48L0RlcEV4cEVjb0NvZGU+CiAgICAgIDxEZXBFeHBFY29OYW1lPjwvRGVwRXhwRWNvTmFtZT4KICAgICAgPERlcFByb0NvZGU+PC9EZXBQcm9Db2RlPgogICAgICA8RGVwUHJvTmFtZT48L0RlcFByb05hbWU+CiAgICAgIDxQYXllZUFjY3RObz4xNzAxNjIwMTA0MDAxMTI5NDwvUGF5ZWVBY2N0Tm8+CiAgICAgIDxQYXllZUFjY3ROYW1lPtbQufrKr7uvz/rK27nJt93T0M/euavLvrr+sbHO5Lq6yq/TzbfWuavLvjwvUGF5ZWVBY2N0TmFtZT4KICAgICAgPFBheWVlQWNjdEJhbmtOYW1lPsWp0NCzfr/a1qfQ0NOq0rXK0jwvUGF5ZWVBY2N0QmFua05hbWU+CiAgICAgIDxQYXllZUFjY3RCYW5rTm8+PC9QYXllZUFjY3RCYW5rTm8+CiAgICAgIDxUcmFja2luZ0lEPjwvVHJhY2tpbmdJRD4KICAgICAgPFBheUFtdD4zLjAwPC9QYXlBbXQ+CiAgICAgIDxSZW1hcms+PC9SZW1hcms+CiAgICAgIDxGb3JlaWduQW10PjA8L0ZvcmVpZ25BbXQ+CiAgICAgIDxDdXJyZW5jeUNvZGU+Q05ZPC9DdXJyZW5jeUNvZGU+CiAgICAgIDxFc3RSYXQ+PC9Fc3RSYXQ+CiAgICAgIDxSZWNlaXZlckNvZGU+PC9SZWNlaXZlckNvZGU+CiAgICAgIDxBbXRVbml0PjwvQW10VW5pdD4KICAgICAgPFhQYXlEYXRlPjwvWFBheURhdGU+CiAgICAgIDxYQWdlbnRCdXNpbmVzc05vPjwvWEFnZW50QnVzaW5lc3NObz4KICAgICAgPFhDaGVja05vPjwvWENoZWNrTm8+CiAgICAgIDxYUGF5QW10PjwvWFBheUFtdD4KICAgICAgPFhBZGRXb3JkPjwvWEFkZFdvcmQ+CiAgICAgIDxYUGF5ZWVBY2N0QmFua05hbWU+PC9YUGF5ZWVBY2N0QmFua05hbWU+CiAgICAgIDxYUGF5ZWVBY2N0Tm8+PC9YUGF5ZWVBY2N0Tm8+CiAgICAgIDxYUGF5ZWVBY2N0TmFtZT48L1hQYXllZUFjY3ROYW1lPgogICAgICA8SG9sZDE+PC9Ib2xkMT4KICAgICAgPEhvbGQyPjwvSG9sZDI+CiAgICAgIDxIb2xkMz48L0hvbGQzPgogICAgICA8SG9sZDQ+PC9Ib2xkND4KICAgIDwvRGV0YWlsPgogIDwvRGV0YWlsTGlzdD4KPC9Wb3VjaGVyPgo=</Voucher>\n        <SignStampList>\n            <SignStamp No=\"cz_dwsz\" SN=\"7344e8d63bb64f73add978f24d25ec8f\">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</SignStamp>\n        </SignStampList>\n        <SignatureList />\n    </VoucherBody>\n</MOF>\n",
            "details": "",
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "opid": "60D0E448D73949A28EB2C188B8D2333E58CAB89AF1A04EF3B7E19C1DBCFDA502",
            "bill_no": "",
            "payBusTypeCodes": [
                "1"
            ],
            "action_id": "60D0E448D73949A28EB2C188B8D2333E",
            "work_flow_id": "pay_voucher_bill",
            "isDoWorkFlow": 'true',
            "isSignStamp": 'true',
            "appId": "pay_voucher",
            "menuId": "60D0E448D73949A28EB2C188B8D2333E",
            "actionType": "2",
            "actionName": "直接签章",
            "vtCode": "5214",
            "glType": "0",
            "ids": [
                gkjzzfsqlr_pay_cert_id
            ],
            "stampurl": "pay-voucher-service/v3/payvoucherbill/action/stamp",
            "admDivCode": "420000000",
            "justShow": 'false',
            "voucherNos": [
                gkjzzfsqlr_pay_cert_no
            ]
        }

        # 将dict转换为str
        zfpzfhqzcz_stamp_data_str = json.dumps(zfpzfhqzcz_stamp_data)
        try:
            zfpzfhqzcz_stamp_start = time.time()  # 开始时间
            zfpzfhqzcz_stamp_res = requests.post(zfpzfhqzcz_stamp_url,
                                                       headers=zfpzfhqzcz_stamp_headers,
                                                       data=zfpzfhqzcz_stamp_data_str)
            zfpzfhqzcz_stamp_res_json = zfpzfhqzcz_stamp_res.json()
            zfpzfhqzcz_stamp_end = time.time()  # 结束时间
            zfpzfhqzcz_stamp_res_time = zfpzfhqzcz_stamp_end - zfpzfhqzcz_stamp_start
            zfpzfhqzcz_stamp_res_time_ms = zfpzfhqzcz_stamp_res_time * 1000
            print("\n")
            print(f"响应时间：{zfpzfhqzcz_stamp_res_time_ms}毫秒")
            # print(zfpzfhqzcz_stamp_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(zfpzfhqzcz_stamp_url, zfpzfhqzcz_stamp_data_str,
                                       zfpzfhqzcz_stamp_headers))
            logss.logger.info("返回结果：{}".format(zfpzfhqzcz_stamp_res.text))
            ###断言
            response_rscode = zfpzfhqzcz_stamp_res_json.get('rscode')
            response_result = zfpzfhqzcz_stamp_res_json.get('result')

            # pytest.assume(zblr_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert zfpzfhqzcz_stamp_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常

    @allure.story("(step07)支付凭证发送(财政)")
    @allure.title("支付凭证发送(财政)：发送")
    def testzfpzfsczsend(self):
        zfpzfscz_send_url = base_url + '/payfront/pay-voucher-service/v3/payvoucherbill/front/action/send'
        zfpzfscz_send_headers = {"Content-Type": "application/json",
                                          "tokenid": tokenids}
        zfpzfscz_send_data = {
            "actionName": "发送",
            "appId": "pay_voucher",
            "roleguid": "201EC9F7611B11B38E60BA5B10633BDB",
            "menuId": "47C1B830A8EB483C8CC0C815761A2DE3",
            "actionType": "2",
            "glType": "0",
            "ids": [
                gkjzzfsqlr_pay_cert_id
            ],
            "voucherNos": [
                gkjzzfsqlr_pay_cert_no
            ],
            "vtCode": "5214",
            "vt_code": "5214",
            "actionId": "47C1B830A8EB483C8CC0C815761A2DE3"
        }

        # 将dict转换为str
        zfpzfscz_send_data_str = json.dumps(zfpzfscz_send_data)
        try:
            zfpzfscz_send_start = time.time()  # 开始时间
            zfpzfscz_send_res = requests.post(zfpzfscz_send_url,
                                                       headers=zfpzfscz_send_headers,
                                                       data=zfpzfscz_send_data_str)
            zfpzfscz_send_res_json = zfpzfscz_send_res.json()
            zfpzfscz_send_end = time.time()  # 结束时间
            zfpzfscz_send_res_time = zfpzfscz_send_end - zfpzfscz_send_start
            zfpzfscz_send_res_time_ms = zfpzfscz_send_res_time * 1000
            print("\n")
            print(f"响应时间：{zfpzfscz_send_res_time_ms}毫秒")
            # print(zfpzfscz_send_res.text)

            logss.logger.info(
                "请求参数：{}，{}，{}".format(zfpzfscz_send_url, zfpzfscz_send_data_str,
                                       zfpzfscz_send_headers))
            logss.logger.info("返回结果：{}".format(zfpzfscz_send_res.text))
            ###断言
            response_rscode = zfpzfscz_send_res_json.get('rscode')
            response_result = zfpzfscz_send_res_json.get('result')

            # pytest.assume(zblr_loadTableDatas_res.status_code == 200)
            # pytest.assume(response_rscode == 200)
            # pytest.assume(response_result == "请求成功")

            assert zfpzfscz_send_res.status_code == 200
            assert response_rscode == 200
            assert response_result == "请求成功"

        except AssertionError as e:
            # print(f"请求失败：{e}")
            logss.logger.error("断言失败：%s", e)
            raise e  # 主动抛出异常，不写则捕获异常





if __name__ == '__main__':

    pytest.main()
