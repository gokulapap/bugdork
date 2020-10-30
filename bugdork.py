from prettytable import PrettyTable
import webbrowser
from os import system
from time import sleep

dict = {
'1':'site:{} intitle:index.of',
'2':'site:{} ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ini',
'3':'site:{} ext:sql | ext:dbf | ext:mdb',
'4':'site:{} inurl:wp- | inurl:wp-content | inurl:plugins | inurl:uploads | inurl:themes | inurl:download',
'5':'site:{} ext:log',
'6':'site:{} ext:bkf | ext:bkp | ext:bak | ext:old | ext:backup',
'7':'site:{} inurl:login',
'8':'site:{} intext:"sql syntax near" | intext:"syntax error has occurred" | intext:"incorrect syntax near" | intext:"unexpected end of SQL command" | intext:"Warning: mysql_connect()" | intext:"Warning: mysql_query()" | intext:"Warning: pg_connect()"',
'9':'site:{} ext:doc | ext:docx | ext:odt | ext:pdf | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv',
'10':'site:{} ext:php intitle:phpinfo "published by the PHP Group"',
'11':'https://mxtoolbox.com/SuperTool.aspx?action=mx%3a{}&run=toolpage',
'12':'site:{} inurl:redir | inurl:url | inurl:redirect | inurl:return | inurl:src=http | inurl:r=http',
'13':'site:*.{}',
'14':'{}/robots.txt',
'15':'{}/crossdomain.xml',
'16':'https://crt.sh/?q=%25.{}',
'17':'https://threatcrowd.org/domain.php?domain={}',
'18':'site:{} inurl:"/phpinfo.php" | inurl:".htaccess" | inurl:"/.git" {} -github'
}

system('toilet -f slant Bug hunter tool')
print('                                  BY GOKUL\n')
print("= = = = = = = = = = = = = Enter options to select = = = = = = = = = = = = = = ")
system('echo')
print('1)  Check Directory listing')
print('2)  Check Exposed config files')
print('3)  Check Exposed database files')
print('4)  Check whether wordpress or not')
print('5)  Check Exposed log files')
print('6)  Check Backup and old files')
print('7)  Find login pages')
print('8)  Check SQL Errors')
print('9)  Check Publicly Exposed documents')
print('10) Check phpinfo')
print('11) Check DMARC misconfiguration')
print('12) Check Open redirects')
print('13) Find Subdomains')
print('14) Find Robots txt file')
print('15) Test CrossDomain')
print('16) Check in crt.sh')
print('17) Check in threatcrowd')
print('18) Check Exposed sensitive files')
system('echo')

url = input("[+] Enter domain name without (http/https://www) [Eg.domain.com] : ")
opt = input("[+] Select the Option you want to scan : ")

system('echo')
print('[!] Note: If the website doesnt have that Vulnerabilty then the Browser will not show results')
system('echo')
t = PrettyTable()
t.field_names = ['Domain Name','Option selected']
t.add_row([url,opt])
print(t)

address = ['11','14','15','16','17']

if opt in address:
 url1 = 'https://www.'+dict[opt].format(url)
 sleep(3)
 webbrowser.open(url1)
else:
 url2 = 'https://www.google.com/search?q='+dict[opt].format(url)
 sleep(3)
 webbrowser.open(url2)
