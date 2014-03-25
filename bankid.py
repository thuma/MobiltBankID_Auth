# -*- coding: utf-8 -*-
import sys
import tornado.httpclient
from bs4 import BeautifulSoup

pno = sys.argv[1]

http_client = tornado.httpclient.HTTPClient()
request = tornado.httpclient.HTTPRequest("https://test.bankid.com/Mobile", method='GET', validate_cert=0)
try:
    response = http_client.fetch(request)
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

print 'Kakor hämtade -> Söker'

headers = tornado.httputil.HTTPHeaders({"Cookie": allakakor[0]+';LanguageCookie=sv;'+allakakor[2]+';'+allakakor[3]})

request = tornado.httpclient.HTTPRequest("https://test.bankid.com/Authentication/Step1", method='POST',headers =headers , body='CenturyBreak=2001&Personnummer='+pno, validate_cert=0)
http_client = tornado.httpclient.HTTPClient()
try:
    response = http_client.fetch(request)
except tornado.httpclient.HTTPError as e:
    print "Error:", e
    
html_doc = BeautifulSoup(response.body)
http_client.close()

orderRef =  "orderRef="+html_doc.find(id="orderRef")['value']
reqtok =  "__RequestVerificationToken="+html_doc.find(id="nextStepForm").findChildren()[0]['value']

print 'Sök startad -> order ref hämtad -> Väntar'

print orderRef + reqtok
headers = tornado.httputil.HTTPHeaders({"Cookie": allakakor[0]+';LanguageCookie=sv;'+allakakor[2]+';'+allakakor[3]})

request = tornado.httpclient.HTTPRequest("https://test.bankid.com/Authentication/Step2RpCall", method='POST', body = orderRef, headers=headers, validate_cert=0,request_timeout=150)
http_client = tornado.httpclient.HTTPClient()
try:
    response = http_client.fetch(request)
except tornado.httpclient.HTTPError as e:
    print "Error:", e
    
http_client.close()

print 'Användaren inloggad'

headers = tornado.httputil.HTTPHeaders({"Cookie": allakakor[0]+';LanguageCookie=sv;'+allakakor[2]+';'+allakakor[3]})

request = tornado.httpclient.HTTPRequest("https://test.bankid.com/Authentication/Step3", method='POST', body = orderRef +'&'+reqtok, headers=headers, validate_cert=0)
http_client = tornado.httpclient.HTTPClient()
try:
    response = http_client.fetch(request)
except tornado.httpclient.HTTPError as e:
    print "Error:", e
http_client.close()

print 'Användaren autentiserar'

request = tornado.httpclient.HTTPRequest("https://test.bankid.com/Authentication/Step3RpCall", method='POST',body = orderRef, headers=headers, validate_cert=0,request_timeout=150)
http_client = tornado.httpclient.HTTPClient()
try:
    response = http_client.fetch(request)
except tornado.httpclient.HTTPError as e:
    print "Error:", e
http_client.close()

print 'Väntar'

request = tornado.httpclient.HTTPRequest("https://test.bankid.com/Authentication/Step4", method='POST',body = orderRef, headers=headers, validate_cert=0)
http_client = tornado.httpclient.HTTPClient()
try:
    response = http_client.fetch(request)
except tornado.httpclient.HTTPError as e:
    print "Error:", e

html_doc = BeautifulSoup(response.body)
part1 = html_doc.find(id="MainBody")
part1 = part1.find_all('h2')

print part1[0].get_text()
http_client.close()


