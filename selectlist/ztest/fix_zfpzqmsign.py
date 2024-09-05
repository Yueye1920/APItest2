import base64
import json
import xmltodict
import xml.etree.ElementTree

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


zfpzqm_sign_url = base_url + '/payfront/pay-voucher-service/v3/payvoucherbill/action/sign'
zfpzqm_sign_headers = {"Content-Type": "application/json",
                                   "tokenid": tokenids}

global zfsqlrdw_pay_cert_id
zfsqlrdw_pay_cert_id='66D1EF1B00C5432783A34719F7FC20C6'
global zfsqlrdw_pay_cert_no
zfsqlrdw_pay_cert_no='W002418000209'
global zfsqlrdw_pay_app_id
zfsqlrdw_pay_app_id='B6A95AC9AF4F4691997FE569D9ABDFCF'
global zfsqlrdw_pay_app_no
zfsqlrdw_pay_app_no='SQW002418000153'

zfpzqm_sign_data = {
    "vt_code": "5214",
    "vouchers": "<?xml version=\"1.0\" encoding=\"GBK\" ?>\n<MOF>\n    <VoucherCount>1</VoucherCount>\n    <VoucherBody VoucherNo=\"pay_cert_no\" AdmDivCode=\"420000\" StYear=\"2024\" VtCode=\"5214\">\n        <VoucherFlag>0</VoucherFlag>\n        <Voucher>PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iR0JLIj8+Cgo8Vm91Y2hlcj4KICA8SWQ+MDBFRkI3Rjk0RUYzNDlBMjg5Q0RCRDFFQzBDRjI1Q0M8L0lkPgogIDxBZG1EaXZDb2RlPjQyMDAwMDwvQWRtRGl2Q29kZT4KICA8U3RZZWFyPjIwMjQ8L1N0WWVhcj4KICA8VnRDb2RlPjUyMTQ8L1Z0Q29kZT4KICA8Vm91RGF0ZT4yMDI0MDUxMDwvVm91RGF0ZT4KICA8Vm91Y2hlck5vPlcwMDI0MTgwMDAyMTE8L1ZvdWNoZXJObz4KICA8QmlsbE5vPlNRVzAwMjQxODAwMDE1NTwvQmlsbE5vPgogIDxGdW5kVHlwZUNvZGU+MTExMTE8L0Z1bmRUeXBlQ29kZT4KICA8RnVuZFR5cGVOYW1lPr6tt9Gypr/usrnW+jwvRnVuZFR5cGVOYW1lPgogIDxCZ3RUeXBlQ29kZT4xMTwvQmd0VHlwZUNvZGU+CiAgPEJndFR5cGVOYW1lPtSksqbWuLHqPC9CZ3RUeXBlTmFtZT4KICA8UGF5VHlwZUNvZGU+MTwvUGF5VHlwZUNvZGU+CiAgPFBheVR5cGVOYW1lPrn6v+K8r9bQ1qe4tjwvUGF5VHlwZU5hbWU+CiAgPFByb0NhdENvZGU+PC9Qcm9DYXRDb2RlPgogIDxQcm9DYXROYW1lPjwvUHJvQ2F0TmFtZT4KICA8TU9GRGVwQ29kZT4wOTwvTU9GRGVwQ29kZT4KICA8TU9GRGVwTmFtZT7FqdK1tKY8L01PRkRlcE5hbWU+CiAgPFN1cERlcENvZGU+MjE5PC9TdXBEZXBDb2RlPgogIDxTdXBEZXBOYW1lPrr+sbHKocWp0rXFqbTlzPw8L1N1cERlcE5hbWU+CiAgPEFnZW5jeUNvZGU+MjE5MDExPC9BZ2VuY3lDb2RlPgogIDxBZ2VuY3lOYW1lPrr+sbHKobn7suiw7LmrytI8L0FnZW5jeU5hbWU+CiAgPEV4cEZ1bmNDb2RlPjIwMTAxMDE8L0V4cEZ1bmNDb2RlPgogIDxFeHBGdW5jTmFtZT7Q0NX+1MvQ0DwvRXhwRnVuY05hbWU+CiAgPEV4cEZ1bmNDb2RlMT4yMDE8L0V4cEZ1bmNDb2RlMT4KICA8RXhwRnVuY05hbWUxPtK7sOO5q7myt/7O8dans/Y8L0V4cEZ1bmNOYW1lMT4KICA8RXhwRnVuY0NvZGUyPjAxPC9FeHBGdW5jQ29kZTI+CiAgPEV4cEZ1bmNOYW1lMj7Iy7TzysLO8TwvRXhwRnVuY05hbWUyPgogIDxFeHBGdW5jQ29kZTM+MDE8L0V4cEZ1bmNDb2RlMz4KICA8RXhwRnVuY05hbWUzPtDQ1f7Uy9DQPC9FeHBGdW5jTmFtZTM+CiAgPEdvdkV4cEVjb0NvZGU+PC9Hb3ZFeHBFY29Db2RlPgogIDxHb3ZFeHBFY29OYW1lPjwvR292RXhwRWNvTmFtZT4KICA8RGVwRXhwRWNvQ29kZT4zMDEwMTwvRGVwRXhwRWNvQ29kZT4KICA8RGVwRXhwRWNvTmFtZT67+bG+uaTXyjwvRGVwRXhwRWNvTmFtZT4KICA8RGVwUHJvQ29kZT40MjAwMDAyNDIxOVAwMDcwMDAwNTE8L0RlcFByb0NvZGU+CiAgPERlcFByb05hbWU+MjE5MDEx1rix6rncwO0xNTEyPC9EZXBQcm9OYW1lPgogIDxTZXRNb2RlQ29kZT4xPC9TZXRNb2RlQ29kZT4KICA8U2V0TW9kZU5hbWU+tefX09eq1cvWp7i2PC9TZXRNb2RlTmFtZT4KICA8UGF5QmFua0NvZGU+MTAyNTIxMDAwMzM1PC9QYXlCYW5rQ29kZT4KICA8UGF5QmFua05hbWU+1tC5+rmkyczS+NDQzuS6usrQzuTn88K31qfQ0DwvUGF5QmFua05hbWU+CiAgPENsZWFyQmFua0NvZGU+PC9DbGVhckJhbmtDb2RlPgogIDxDbGVhckJhbmtOYW1lPjwvQ2xlYXJCYW5rTmFtZT4KICA8Q2xlYXJBY2N0Tm8+PC9DbGVhckFjY3RObz4KICA8Q2xlYXJBY2N0TmFtZT48L0NsZWFyQWNjdE5hbWU+CiAgPENsZWFyQWNjdEJhbmtOYW1lPjwvQ2xlYXJBY2N0QmFua05hbWU+CiAgPFBheWVlQWNjdE5vPjMyMDIwMTA2MTkxMDAxNDg3OTc8L1BheWVlQWNjdE5vPgogIDxQYXllZUFjY3ROYW1lPrr+sbG2psGmuuO9qMno09DP3rmry748L1BheWVlQWNjdE5hbWU+CiAgPFBheWVlQWNjdEJhbmtOYW1lPrmkyczS+NDQzuS6ur/VuNvWp9DQPC9QYXllZUFjY3RCYW5rTmFtZT4KICA8UGF5ZWVBY2N0QmFua05vPjwvUGF5ZWVBY2N0QmFua05vPgogIDxQYXlBY2N0Tm8+MzIwMjAwNjAwOTIwMDAwOTIwMzwvUGF5QWNjdE5vPgogIDxQYXlBY2N0TmFtZT66/rGxyqG5+7LosOy5q8rSPC9QYXlBY2N0TmFtZT4KICA8UGF5QWNjdEJhbmtOYW1lPtbQufq5pMnM0vjQ0M7kurrK0M7k5/PCt9an0NA8L1BheUFjY3RCYW5rTmFtZT4KICA8UGF5U3VtbWFyeUNvZGU+PC9QYXlTdW1tYXJ5Q29kZT4KICA8UGF5U3VtbWFyeU5hbWU+1qe4tsH3s8w8L1BheVN1bW1hcnlOYW1lPgogIDxQYXlBbXQ+Mi4wMDwvUGF5QW10PgogIDxCdXNpbmVzc1R5cGVDb2RlPjE8L0J1c2luZXNzVHlwZUNvZGU+CiAgPEJ1c2luZXNzVHlwZU5hbWU+xtXNqNK1zvE8L0J1c2luZXNzVHlwZU5hbWU+CiAgPFRheEJpbGxObz48L1RheEJpbGxObz4KICA8VGF4YXllcklEPjwvVGF4YXllcklEPgogIDxUYXhPcmdDb2RlPjwvVGF4T3JnQ29kZT4KICA8R292UHJvY3VyZW1lbnRJRD48L0dvdlByb2N1cmVtZW50SUQ+CiAgPENoZWNrTm8+PC9DaGVja05vPgogIDxQYXlDb2RlPjwvUGF5Q29kZT4KICA8Rm9yZWlnbkFtdD4wPC9Gb3JlaWduQW10PgogIDxDdXJyZW5jeUNvZGU+Q05ZPC9DdXJyZW5jeUNvZGU+CiAgPEVzdFJhdD48L0VzdFJhdD4KICA8QW10VW5pdD48L0FtdFVuaXQ+CiAgPFhQYXlEYXRlPjwvWFBheURhdGU+CiAgPFhBZ2VudEJ1c2luZXNzTm8+PC9YQWdlbnRCdXNpbmVzc05vPgogIDxYQ2hlY2tObz48L1hDaGVja05vPgogIDxYUGF5QW10PjA8L1hQYXlBbXQ+CiAgPFhQYXllZUFjY3RCYW5rTmFtZT48L1hQYXllZUFjY3RCYW5rTmFtZT4KICA8WFBheWVlQWNjdE5vPjwvWFBheWVlQWNjdE5vPgogIDxYUGF5ZWVBY2N0TmFtZT48L1hQYXllZUFjY3ROYW1lPgogIDxIb2xkMT4xMjwvSG9sZDE+CiAgPEhvbGQyPjwvSG9sZDI+CiAgPERldGFpbExpc3Q+CiAgICA8RGV0YWlsPgogICAgICA8SWQ+NTAzNEVCQzkwMUIzNDhFMThEQkEzQTQxODk1ODI2OEQ8L0lkPgogICAgICA8Vm91Y2hlckJpbGxJZD4wMEVGQjdGOTRFRjM0OUEyODlDREJEMUVDMENGMjVDQzwvVm91Y2hlckJpbGxJZD4KICAgICAgPFZvdWNoZXJCaWxsTm8+VzAwMjQxODAwMDIxMTwvVm91Y2hlckJpbGxObz4KICAgICAgPFZvdWNoZXJEZXRhaWxObz5TUVcwMDI0MTgwMDAxNTU8L1ZvdWNoZXJEZXRhaWxObz4KICAgICAgPEZ1bmRUeXBlQ29kZT4xMTExMTwvRnVuZFR5cGVDb2RlPgogICAgICA8RnVuZFR5cGVOYW1lPr6tt9Gypr/usrnW+jwvRnVuZFR5cGVOYW1lPgogICAgICA8Qmd0VHlwZUNvZGU+MTE8L0JndFR5cGVDb2RlPgogICAgICA8Qmd0VHlwZU5hbWU+1KSypta4seo8L0JndFR5cGVOYW1lPgogICAgICA8UHJvQ2F0Q29kZT48L1Byb0NhdENvZGU+CiAgICAgIDxQcm9DYXROYW1lPjwvUHJvQ2F0TmFtZT4KICAgICAgPFBheUtpbmRDb2RlPjwvUGF5S2luZENvZGU+CiAgICAgIDxQYXlLaW5kTmFtZT48L1BheUtpbmROYW1lPgogICAgICA8TU9GRGVwQ29kZT48L01PRkRlcENvZGU+CiAgICAgIDxNT0ZEZXBOYW1lPjwvTU9GRGVwTmFtZT4KICAgICAgPFN1cERlcENvZGU+MjE5PC9TdXBEZXBDb2RlPgogICAgICA8U3VwRGVwTmFtZT66/rGxyqHFqdK1xam05cz8PC9TdXBEZXBOYW1lPgogICAgICA8QWdlbmN5Q29kZT4yMTkwMTE8L0FnZW5jeUNvZGU+CiAgICAgIDxBZ2VuY3lOYW1lPrr+sbHKobn7suiw7LmrytI8L0FnZW5jeU5hbWU+CiAgICAgIDxFeHBGdW5jQ29kZT4yMDEwMTAxPC9FeHBGdW5jQ29kZT4KICAgICAgPEV4cEZ1bmNOYW1lPtDQ1f7Uy9DQPC9FeHBGdW5jTmFtZT4KICAgICAgPEdvdkV4cEVjb0NvZGU+PC9Hb3ZFeHBFY29Db2RlPgogICAgICA8R292RXhwRWNvTmFtZT48L0dvdkV4cEVjb05hbWU+CiAgICAgIDxEZXBFeHBFY29Db2RlPjwvRGVwRXhwRWNvQ29kZT4KICAgICAgPERlcEV4cEVjb05hbWU+PC9EZXBFeHBFY29OYW1lPgogICAgICA8RGVwUHJvQ29kZT48L0RlcFByb0NvZGU+CiAgICAgIDxEZXBQcm9OYW1lPjwvRGVwUHJvTmFtZT4KICAgICAgPFBheWVlQWNjdE5vPjMyMDIwMTA2MTkxMDAxNDg3OTc8L1BheWVlQWNjdE5vPgogICAgICA8UGF5ZWVBY2N0TmFtZT66/rGxtqbBprrjvajJ6NPQz965q8u+PC9QYXllZUFjY3ROYW1lPgogICAgICA8UGF5ZWVBY2N0QmFua05hbWU+uaTJzNL40NDO5Lq6v9W429an0NA8L1BheWVlQWNjdEJhbmtOYW1lPgogICAgICA8UGF5ZWVBY2N0QmFua05vPjwvUGF5ZWVBY2N0QmFua05vPgogICAgICA8VHJhY2tpbmdJRD48L1RyYWNraW5nSUQ+CiAgICAgIDxQYXlBbXQ+Mi4wMDwvUGF5QW10PgogICAgICA8UmVtYXJrPjwvUmVtYXJrPgogICAgICA8Rm9yZWlnbkFtdD4wPC9Gb3JlaWduQW10PgogICAgICA8Q3VycmVuY3lDb2RlPkNOWTwvQ3VycmVuY3lDb2RlPgogICAgICA8RXN0UmF0PjwvRXN0UmF0PgogICAgICA8UmVjZWl2ZXJDb2RlPjwvUmVjZWl2ZXJDb2RlPgogICAgICA8QW10VW5pdD48L0FtdFVuaXQ+CiAgICAgIDxYUGF5RGF0ZT48L1hQYXlEYXRlPgogICAgICA8WEFnZW50QnVzaW5lc3NObz48L1hBZ2VudEJ1c2luZXNzTm8+CiAgICAgIDxYQ2hlY2tObz48L1hDaGVja05vPgogICAgICA8WFBheUFtdD48L1hQYXlBbXQ+CiAgICAgIDxYQWRkV29yZD48L1hBZGRXb3JkPgogICAgICA8WFBheWVlQWNjdEJhbmtOYW1lPjwvWFBheWVlQWNjdEJhbmtOYW1lPgogICAgICA8WFBheWVlQWNjdE5vPjwvWFBheWVlQWNjdE5vPgogICAgICA8WFBheWVlQWNjdE5hbWU+PC9YUGF5ZWVBY2N0TmFtZT4KICAgICAgPEhvbGQxPjwvSG9sZDE+CiAgICAgIDxIb2xkMj48L0hvbGQyPgogICAgICA8SG9sZDM+PC9Ib2xkMz4KICAgICAgPEhvbGQ0PjwvSG9sZDQ+CiAgICA8L0RldGFpbD4KICA8L0RldGFpbExpc3Q+CjwvVm91Y2hlcj4K</Voucher>\n        <SignStampList />\n        <SignatureList>\n            <Signature No=\"cz_dwfz\" SN=\"3f38e4aaee0c2acb\">MIIFlgYJKoZIhvcNAQcCoIIFhzCCBYMCAQExCzAJBgUrDgMCGgUAMAsGCSqGSIb3DQEHAaCCBGQwggRgMIIDSKADAgECAgg/OOSq7gwqyzANBgkqhkiG9w0BAQUFADBKMQswCQYDVQQGEwJDTjEMMAoGA1UEChMDTU9GMS0wKwYDVQQDEyRQcml2YXRlIENlcnRpZmljYXRlIEF1dGhvcml0eSBPZiBNT0YwHhcNMjEwODE2MTc0NjI4WhcNMjkxMTAyMTc0NjI4WjCBkzELMAkGA1UEBhMCQ04xDDAKBgNVBAoMA01PRjELMAkGA1UECgwCMDExCzAJBgNVBAgMAjQyMQswCQYDVQQHDAIwNjELMAkGA1UEBwwCMDAxCzAJBgNVBAsMAjA0MRswGQYDVQQMDBI0MjA2MDAxOTgzMDEwNDI1NjMxGDAWBgNVBAMMD+ilhOmYs+W4guacrOe6pzCBnzANBgkqhkiG9w0BAQEFAAOBjQAwgYkCgYEAzeXNBTvF+1Xr0WkTpYYso8c9Z6QbKPVTJyS7GLRnjaxPuF95UEMXZYKPSQLlLxMCwPg9pIPwysZgKsJfPnuMbgg6L0y6Id0lcjsLCtUO5Z5XdJwj3FglQcVb4TQzkpyktN36u8rKiEs5MHq+IGFpB4HM8VJhZK0DXkMHR+lZ5zECAwEAAaOCAYIwggF+MB8GA1UdIwQYMBaAFJb4S7KJrQAb2Qm/dCDwB+CLzQtbMB0GA1UdDgQWBBSdMb2OF61MoZaAfnn1mN9mYCfJIjALBgNVHQ8EBAMCA8gwgfEGA1UdHwSB6TCB5jBCoECgPqQ8MDoxCzAJBgNVBAYTAmNuMQwwCgYDVQQKDANtb2YxDDAKBgNVBAsMA0NSTDEPMA0GA1UEAwwGY3JsNDEzMCagJKAihiBodHRwOi8vY3JsLmNhLm1vZi9jcmwvY3JsNDEzLmNybDB4oHagdIZybGRhcDovL2xkYXAuY2EubW9mOjM4OS9DTj1jcmw0MTMsT1U9Q1JMLG89bW9mLGM9Y24/Y2VydGlmaWNhdGVSZXZvY2F0aW9uTGlzdD9iYXNlP29iamVjdGNsYXNzPWNSTERpc3RyaWJ1dGlvblBvaW50MDsGA1UdJQQ0MDIGCCsGAQUFBwMCBggrBgEFBQcDAwYIKwYBBQUHAwQGCCsGAQUFBwMIBggrBgEFBQcDCTANBgkqhkiG9w0BAQUFAAOCAQEAHLam+IAmxRAFOjcF+utB+TLsQLwpqaHjj5AlYstJeSBZLLAkypwVaPEcqK7WSczeQzOhOX4LhNon9xCdY+fmYBEG99tsQfC7FhO7dDODmKwwjOYco6ZxsVWEU/SWoMrYgcD/VIFlbFeQjPGYR+JDfkif7oRWp1EAotmyglss5p4tgyq17HjXkXMhKzcp6IT3maW1ZM0/8+LtXu8PMj47N5IFcb0kKDuVrCZQvFJxwGFz7aXxn5vumIBv4vfc579rWinsotw9BVMH7zcjbkV8zYyNq6j46VE9vWJ6WuKQd8pzkHulxuTWfY4Q4yQRLWo1txXW+RC+YNelE2e7Qkw84jGB+zCB+AIBATBWMEoxCzAJBgNVBAYTAkNOMQwwCgYDVQQKEwNNT0YxLTArBgNVBAMTJFByaXZhdGUgQ2VydGlmaWNhdGUgQXV0aG9yaXR5IE9mIE1PRgIIPzjkqu4MKsswCQYFKw4DAhoFADANBgkqhkiG9w0BAQEFAASBgCTAuFvxZq1g/medc2WDEmRIiNbfmclN73RAv0Y0GdefuZC3sEyMJhPtjL6y3isBdaj2oPyxKElxtT7JLPmcT8odnvl0CkYs62epaDdiV4Nk8iXXKcXAHgQ0ZVW1KJ6wU4MsJpceIxRsRRR9sLu6ZHoXG1UCvjuJgXSAbEyesHcs</Signature>\n        </SignatureList>\n    </VoucherBody>\n</MOF>\n",
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

# print(type(zfpzqm_sign_data))
# print(zfpzqm_sign_data)

# 提取data中的xml报文内容
zfsqlrdw_xml = zfpzqm_sign_data.get("vouchers")
# print(zfsqlrdw_xml)
# 将xml报文解析为dict字典
data_dict = xmltodict.parse(zfsqlrdw_xml)
# print(data_dict)
# 提取字典中voucherno
voucherno=data_dict['MOF']['VoucherBody']['@VoucherNo']
print(voucherno)

# 将字典中的voucherno修改为全部变量pay_cert_no
data_dict['MOF']['VoucherBody']['@VoucherNo']=zfsqlrdw_pay_cert_no
# 将修改后字典转换为xml数据


voucherxml=data_dict['MOF']['VoucherBody']['Voucher']
# print(voucherxml)



if (len(voucherxml) % 3 == 1):
    voucherxml += "=="
    base64_xml = base64.b64decode(voucherxml)
    decoded_gbk_string = base64_xml.decode("GBK")
elif (len(voucherxml) % 3 == 2):
    voucherxml += "="
    base64_xml = base64.b64decode(voucherxml)
    decoded_gbk_string = base64_xml.decode("GBK")

elif (len(voucherxml) % 4 == 1):
    voucherxml += "==="
    base64_xml = base64.b64decode(voucherxml)
    decoded_gbk_string = base64_xml.decode("GBK")
elif (len(voucherxml) % 4 == 2):
    voucherxml += "=="
    base64_xml = base64.b64decode(voucherxml)
    decoded_gbk_string = base64_xml.decode("GBK")



# base64_xml = base64.b64decode(xml_fix)
# decoded_utf8_string = base64_xml.decode("utf-8")

print(decoded_gbk_string)

zfsqlrdw_xml_fix=decoded_gbk_string

# 将xml报文解析为dict字典
xml_data_dict = xmltodict.parse(zfsqlrdw_xml_fix)
print(xml_data_dict)


xml_data_dict['Voucher']['Id']=zfsqlrdw_pay_cert_id
xml_data_dict['Voucher']['VoucherNo']=zfsqlrdw_pay_cert_no
xml_data_dict['Voucher']['BillNo']=zfsqlrdw_pay_app_no
xml_data_dict['Voucher']['DetailList']['Detail']['Id']=zfsqlrdw_pay_app_id
xml_data_dict['Voucher']['DetailList']['Detail']['VoucherBillId']=zfsqlrdw_pay_cert_id
xml_data_dict['Voucher']['DetailList']['Detail']['VoucherBillNo']=zfsqlrdw_pay_cert_no
xml_data_dict['Voucher']['DetailList']['Detail']['VoucherDetailNo']=zfsqlrdw_pay_app_no

xml_voucher=xml_data_dict['Voucher']
# print(xml_voucher)

# 将修改后字典转换为xml数据
zfsqlrdw_xmls = xmltodict.unparse(xml_data_dict,pretty=True,encoding='GBK')
# print(zfsqlrdw_xmls)

# 将xml转换为base64编码
xml_gbk=zfsqlrdw_xmls.encode('utf-8')
fix_base64_xml =base64.b64encode(xml_gbk).decode('utf-8')

# 更新voucherxml
data_dict['MOF']['VoucherBody']['Voucher']=fix_base64_xml

# 将修改后字典转换为xml数据
zfsqlrdw_xmls = xmltodict.unparse(data_dict,pretty=True,encoding='GBK')
# print(zfsqlrdw_xmls)

# 将data修改
zfpzqm_sign_data_fix = {
    "vt_code": "5214",
    "vouchers": zfsqlrdw_xmls ,
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

print(zfpzqm_sign_data_fix)

# 使用修改后的data进行转为str
zfpzqm_sign_data_str = json.dumps(zfpzqm_sign_data_fix)

zfpzqm_sign_res = requests.post(zfpzqm_sign_url,
                                headers=zfpzqm_sign_headers,
                                data=zfpzqm_sign_data_str)
zfpzqm_sign_res_json = zfpzqm_sign_res.json()

print(zfpzqm_sign_res)
print(zfpzqm_sign_res_json)