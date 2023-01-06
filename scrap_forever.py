import requests
import re
import argparse
from sys import argv
import urllib3



urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)




parser=argparse.ArgumentParser (description='Requests.')
parser.add_argument ('-t', dest='scrap_url', help='https://site.com.br', required=True)
parser.add_argument ('-o', '--output', type=argparse.FileType(mode='w'), dest='scrap_out', help='Salva data.', required=True)
parser.add_argument ('-p', '--proxy',  dest='scrap_proxy', help='-p http://127.0.0.1:8080', required=False)
parser.add_argument ('-a', '--auth',  dest='scrap_auth', help='-a Besic aqsdiqjewqd==', required=False)
parser.add_argument ('-c', '--cookie',  dest='scrap_cookie', help='-c PHPSESSION=cookie', required=False)
parser.add_argument ('--user-agent',  dest='scrap_user_agent', help='--user-agent Mozilla/5.0', required=False)

args=parser.parse_args()



if not len(argv) > 1:
       print(''' 
       python3 forever_scrap.py -h/--help

        -t Target to web scraping (Ex. -t https://site.com)
        -o output file (Ex. -o output.txt )
        -p/--proxy set proxy to request (Ex. -p http://127.0.0.1:8080)
        -c/--cookie set cookie (Ex. -c Authorization: aqsdiqjewqd==)

        
        Usage:
        
        ./forever_scrap.py -t site.com -o output.txt
       ''')

#global List of Results
global_url = []

#url base request
first_url = args.scrap_url

#request and return html
def resq_urls(url_x):
    headers = {
        'authorization': f'{args.scrap_auth}',
        'cookie': f'{args.scrap_cookie}',
        'user-agent': f'{args.scrap_user_agent}'
    }
    if args.scrap_proxy is None:

        response = requests.get(url_x, verify=False, headers=headers)
        return(response.text)

    elif args.scrap_proxy is not None:
        proxy = {'http': f'{args.scrap_proxy}','https': f'{args.scrap_proxy}'}
        response = requests.get(url_x, proxies=proxy, verify=False, headers=headers)
        return (response.text)


#Def find URL in pag
def find_url(response_x):
    comp = re.compile("https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)")
    x = re.findall(comp, response_x)

    for list in x:
        if first_url in list:
            if list not in global_url:
                global_url.append(list)
            else:
                pass
        else:
            pass

#Def get HREF
def find_href(response_x):
    comp_href = re.compile(r'href=[\'"]?([^\'" >]+)')
    x = re.findall(comp_href, response_x)

    for list in x:
            if f'{first_url}/{list}' not in global_url:
                if 'http' in f'{list}':
                    if first_url not in list:
                        pass
                    else:
                        global_url.append(f'{list}')

                elif 'https' in f'{list}':
                    if first_url not in list:
                        pass
                    else:
                        global_url.append(f'{list}')

                elif '/' in f'{first_url}/{list}':
                    global_url.append(f'{first_url}/{list}')
            else:
                pass



#base first Request
resq_urls(first_url)
find_url(resq_urls(first_url))
find_href(resq_urls(first_url))


#Collect All Url in All Pages
n=0
try:
    while n < len(global_url):

            find_url(resq_urls(global_url[n]))
            find_href(resq_urls(global_url[n]))
            print(f'List URL: {global_url[n]}', end='\r', flush=True)
            args.scrap_out.write(global_url[n]+'\n')
            n+=1

except (KeyboardInterrupt):
    print('[-] STOP')


# tratar href que contain http e https.
#pensar em criar duas lista um com apenas o dominio e outra apenas com os possiveis falso positovos.


for out in global_url:
    print(out)
