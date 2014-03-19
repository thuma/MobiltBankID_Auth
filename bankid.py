import tornado.httpclient

http_client = tornado.httpclient.HTTPClient()
try:
    response = http_client.fetch("https://test.bankid.com/Mobile")
    kaka = response.headers['Set-Cookie']
except tornado.httpclient.HTTPError as e:
    print "Error:", e
http_client.close()


print kaka
kakor = kaka.split(',')

allakakor = []

for i in kakor:
	if(i.split(';')[0][0] != ' '):
		allakakor.append(i.split(';')[0])

print allakakor

request = tornado.httpclient.HTTPRequest("https://test.bankid.com/Authentication/Step1", method='POST', headers='Cookie:'+allakakor[0]+';'+allakakor[1]+';'+allakakor[2]+';'+allakakor[3], body='CenturyBreak=2001&Personnummer=198303234655')

http_client = tornado.httpclient.HTTPClient()
try:
    response = http_client.fetch(request)
except tornado.httpclient.HTTPError as e:
    print "Error:", e

http_client.close()
'''Cookies:
https://test.bankid.com/Mobile

Pno:
curl 'https://test.bankid.com/Authentication/Step1' 
-H 'Cookie: ASP.NET_SessionId=lawgyt0ykjm55eyygtjdl5xp; LanguageCookie=sv; __RequestVerificationToken=4P1JvWs1ejiEyDi32QluJdRRtH-FgMQ7sJxUiOolhezR7LvkUY24wX8UkXdxDNYmo5z5p9L9ZF1KrIBtGybXseLMEAph86k1sxsufWob69iYQo8yyr71Klpy1yE2tYbxqbVaqAI4Rzze1tdM9kq8Dw2; DisplaySettings=F7=OK' 
-H 'Origin: https://test.bankid.com' 
-H 'Accept-Encoding: gzip,deflate,sdch' 
-H 'Accept-Language: sv-SE,sv;q=0.8,en-US;q=0.6,en;q=0.4' 
-H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/32.0.1700.107 Chrome/32.0.1700.107 Safari/537.36' 
-H 'Content-Type: application/x-www-form-urlencoded' 
 --data 'CenturyBreak=2001&Personnummer=198303234655'

curl 'https://test.bankid.com/Authentication/Step2RpCall' -H 'Accept: */*' 
-H 'Referer: https://test.bankid.com/Authentication/Step1' 
-H 'Origin: https://test.bankid.com' 
-H 'X-Requested-With: XMLHttpRequest' 
-H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/32.0.1700.107 Chrome/32.0.1700.107 Safari/537.36' 
-H 'Content-Type: application/x-www-form-urlencoded' 
--data 'orderRef=7c8174ff-ea0d-4542-9227-5813bfb3f084' --compressed

curl 'https://test.bankid.com/Authentication/Step3' 
-H 'Cookie: ASP.NET_SessionId=twqr3xam4y1ive0fuyyjzxvp; LanguageCookie=sv; __RequestVerificationToken=bxzuSvnHmoHmA1Huxem-SHx-yUHTdG-g8boMVl-OTvuhSZNYAunfrRABPBWWBQdwV5AQc6DYv5wFe51BCkEY0qZPttWq-EIfVqGIDLqHhjJz0BU-vsnC-FLQV9I_qI7pvN1mzDFTEF14FgtVcrSIyw2; DisplaySettings=' 
-H 'Origin: https://test.bankid.com' 
-H 'Accept-Encoding: gzip,deflate,sdch' 
-H 'Accept-Language: sv-SE,sv;q=0.8,en-US;q=0.6,en;q=0.4' 
-H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/32.0.1700.107 Chrome/32.0.1700.107 Safari/537.36' 
-H 'Content-Type: application/x-www-form-urlencoded' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' 
-H 'Cache-Control: max-age=0' 
-H 'Referer: https://test.bankid.com/Authentication/Step1' 
-H 'Connection: keep-alive' 
--data '__RequestVerificationToken=ymjX8g1-AHdoDMsnTQJmpNmoYB9PDJ2e2GmoAqlSz7zGwiuWPEqQf-Fv90S7b7QusQKvn-psd9DEtcrjnlSZgCcPFgW1DwSkOa5KrvzyqOFLdPXao0z2qutYjbx3G1ygsQrjzI2Lt-PbS-ry5fjcTnYeSRTrWFCRCD08w4IWUPU1&orderRef=7c8174ff-ea0d-4542-9227-5813bfb3f084' --compressed

curl 'https://test.bankid.com/Authentication/Step3RpCall' 
-H 'Accept: */*' 
-H 'Referer: https://test.bankid.com/Authentication/Step3' 
-H 'Origin: https://test.bankid.com' 
-H 'X-Requested-With: XMLHttpRequest' 
-H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/32.0.1700.107 Chrome/32.0.1700.107 Safari/537.36' 
-H 'Content-Type: application/x-www-form-urlencoded' 
--data 'orderRef=7c8174ff-ea0d-4542-9227-5813bfb3f084' --compressed

curl 'https://test.bankid.com/Authentication/Step4' 
-H 'Cookie: ASP.NET_SessionId=twqr3xam4y1ive0fuyyjzxvp; LanguageCookie=sv; __RequestVerificationToken=bxzuSvnHmoHmA1Huxem-SHx-yUHTdG-g8boMVl-OTvuhSZNYAunfrRABPBWWBQdwV5AQc6DYv5wFe51BCkEY0qZPttWq-EIfVqGIDLqHhjJz0BU-vsnC-FLQV9I_qI7pvN1mzDFTEF14FgtVcrSIyw2; DisplaySettings=' 
-H 'Origin: https://test.bankid.com' 
-H 'Accept-Encoding: gzip,deflate,sdch' 
-H 'Accept-Language: sv-SE,sv;q=0.8,en-US;q=0.6,en;q=0.4' 
-H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/32.0.1700.107 Chrome/32.0.1700.107 Safari/537.36' 
-H 'Content-Type: application/x-www-form-urlencoded' 
-H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' 
-H 'Cache-Control: max-age=0' 
-H 'Referer: https://test.bankid.com/Authentication/Step3' 
-H 'Connection: keep-alive' 
--data 'orderRef=7c8174ff-ea0d-4542-9227-5813bfb3f084' --compressed'''



