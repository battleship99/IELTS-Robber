#coding=utf-8

Month='2015-08%2C2015-09'

# 11: Beijing
# 44: Guangdong
Province='11' 

UID='<Your UID>'


sessiondict={}
sessiondict['BIGipServerhw_ielts_internal_pool']='<...>'
sessiondict['JSESSIONID']='<...>'
sessiondict['_ga']='<...>'
# Configure your cookie here

sessiondict['domain_name_edu']='ielts.etest.edu.cn'
sessiondict['domain_name_net']='ielts.etest.net.cn'
sessiondict['domain_port_http']='80'
sessiondict['domain_port_https']='443'
sessiondict['locale']='zh_CN'

import requests

def getHtml(url):
	user_agent = ( 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko/20100101 Firefox/22.0' ) 
	global sessiondict
	global Month
	global UID
	global Province 
	session = requests.session() 
	session.headers['User-Agent'] = user_agent 
	session.headers["Connection"] ="close" 
	session.cookies.update(sessiondict)
	r=session.get(url)
	return r.content

def main():
	html = getHtml("http://ielts.etest.edu.cn/myHome/%s/queryTestSeats?queryMonths=%s&queryProvinces=%s&neeaAppId=&productId=IELTSPBT"%(UID,Month,Province))
	html=html.replace('null','None')
	a=eval(html)
	for each in a:
		for i in a[each]:
			if i['optStatusEn']=="No Seat":
				print '\033[1;37;41m ',i['optStatusEn'],' \033[0m-',i['adminDate'],'-',i['centerNameEn']
			else:
				print '\033[1;37;42m',i['optStatusEn'],'\033[0m-',i['adminDate'],'-',i['centerNameEn']
main()