import base64
voucherxml="MIIFlgYJKoZIhvcNAQcCoIIFhzCCBYMCAQExCzAJBgUrDgMCGgUAMAsGCSqGSIb3DQEHAaCCBGQwggRgMIIDSKADAgECAgg/OOSq7gwqyzANBgkqhkiG9w0BAQUFADBKMQswCQYDVQQGEwJDTjEMMAoGA1UEChMDTU9GMS0wKwYDVQQDEyRQcml2YXRlIENlcnRpZmljYXRlIEF1dGhvcml0eSBPZiBNT0YwHhcNMjEwODE2MTc0NjI4WhcNMjkxMTAyMTc0NjI4WjCBkzELMAkGA1UEBhMCQ04xDDAKBgNVBAoMA01PRjELMAkGA1UECgwCMDExCzAJBgNVBAgMAjQyMQswCQYDVQQHDAIwNjELMAkGA1UEBwwCMDAxCzAJBgNVBAsMAjA0MRswGQYDVQQMDBI0MjA2MDAxOTgzMDEwNDI1NjMxGDAWBgNVBAMMD+ilhOmYs+W4guacrOe6pzCBnzANBgkqhkiG9w0BAQEFAAOBjQAwgYkCgYEAzeXNBTvF+1Xr0WkTpYYso8c9Z6QbKPVTJyS7GLRnjaxPuF95UEMXZYKPSQLlLxMCwPg9pIPwysZgKsJfPnuMbgg6L0y6Id0lcjsLCtUO5Z5XdJwj3FglQcVb4TQzkpyktN36u8rKiEs5MHq+IGFpB4HM8VJhZK0DXkMHR+lZ5zECAwEAAaOCAYIwggF+MB8GA1UdIwQYMBaAFJb4S7KJrQAb2Qm/dCDwB+CLzQtbMB0GA1UdDgQWBBSdMb2OF61MoZaAfnn1mN9mYCfJIjALBgNVHQ8EBAMCA8gwgfEGA1UdHwSB6TCB5jBCoECgPqQ8MDoxCzAJBgNVBAYTAmNuMQwwCgYDVQQKDANtb2YxDDAKBgNVBAsMA0NSTDEPMA0GA1UEAwwGY3JsNDEzMCagJKAihiBodHRwOi8vY3JsLmNhLm1vZi9jcmwvY3JsNDEzLmNybDB4oHagdIZybGRhcDovL2xkYXAuY2EubW9mOjM4OS9DTj1jcmw0MTMsT1U9Q1JMLG89bW9mLGM9Y24/Y2VydGlmaWNhdGVSZXZvY2F0aW9uTGlzdD9iYXNlP29iamVjdGNsYXNzPWNSTERpc3RyaWJ1dGlvblBvaW50MDsGA1UdJQQ0MDIGCCsGAQUFBwMCBggrBgEFBQcDAwYIKwYBBQUHAwQGCCsGAQUFBwMIBggrBgEFBQcDCTANBgkqhkiG9w0BAQUFAAOCAQEAHLam+IAmxRAFOjcF+utB+TLsQLwpqaHjj5AlYstJeSBZLLAkypwVaPEcqK7WSczeQzOhOX4LhNon9xCdY+fmYBEG99tsQfC7FhO7dDODmKwwjOYco6ZxsVWEU/SWoMrYgcD/VIFlbFeQjPGYR+JDfkif7oRWp1EAotmyglss5p4tgyq17HjXkXMhKzcp6IT3maW1ZM0/8+LtXu8PMj47N5IFcb0kKDuVrCZQvFJxwGFz7aXxn5vumIBv4vfc579rWinsotw9BVMH7zcjbkV8zYyNq6j46VE9vWJ6WuKQd8pzkHulxuTWfY4Q4yQRLWo1txXW+RC+YNelE2e7Qkw84jGB+zCB+AIBATBWMEoxCzAJBgNVBAYTAkNOMQwwCgYDVQQKEwNNT0YxLTArBgNVBAMTJFByaXZhdGUgQ2VydGlmaWNhdGUgQXV0aG9yaXR5IE9mIE1PRgIIPzjkqu4MKsswCQYFKw4DAhoFADANBgkqhkiG9w0BAQEFAASBgCTAuFvxZq1g/medc2WDEmRIiNbfmclN73RAv0Y0GdefuZC3sEyMJhPtjL6y3isBdaj2oPyxKElxtT7JLPmcT8odnvl0CkYs62epaDdiV4Nk8iXXKcXAHgQ0ZVW1KJ6wU4MsJpceIxRsRRR9sLu6ZHoXG1UCvjuJgXSAbEyesHcs"


if (len(voucherxml) % 3 == 1):
    voucherxml += "=="
    base64_xml = base64.b64decode(voucherxml)
    decoded_gbk_string = base64_xml.decode("utf-8")
    print(decoded_gbk_string)
elif (len(voucherxml) % 3 == 2):
    voucherxml += "="
    base64_xml = base64.b64decode(voucherxml)
    decoded_gbk_string = base64_xml.decode("utf-8")
    print(decoded_gbk_string)

elif (len(voucherxml) % 4 == 1):
    voucherxml += "==="
    base64_xml = base64.b64decode(voucherxml)
    decoded_gbk_string = base64_xml.decode("utf-8")
    print(decoded_gbk_string)
elif (len(voucherxml) % 4 == 2):
    voucherxml += "=="
    base64_xml = base64.b64decode(voucherxml)
    decoded_gbk_string = base64_xml.decode("utf-8")
    print(decoded_gbk_string)
else:
    base64_xml = base64.b64decode(voucherxml)
    decoded_gbk_string = base64_xml.decode("utf-8")
    print(decoded_gbk_string)
