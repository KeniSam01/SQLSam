# -*- coding: UTF-8 -*-

import re, requests, time, subprocess, argparse
from datetime import datetime

def clear():
    subprocess.call('clear', shell=True)

def banner():
    time.sleep(1)
    print '\033[32m''''
     _______.  ______       __           _______.     ___      .___  ___. 
    /       | /  __  \     |  |         /       |    /   \     |   \/   | 
   |   (----`|  |  |  |    |  |        |   (----`   /  ^  \    |  \  /  | 
    \   \    |  |  |  |    |  |         \   \      /  /_\  \   |  |\/|  | 
.----)   |   |  `--'  '--. |  `----..----)   |    /  _____  \  |  |  |  | 
|_______/     \_____\_____\|_______||_______/    /__/     \__\ |__|  |__|  ''''\033[0;0m'"\n"

def escopo():
    time.sleep(1)
    print '\033[32m' + hour() + "[INFO] Testing conection with website"
    time.sleep(1)
    print hour() + "[INFO] Waiting for website response"
    time.sleep(2)
    print hour() + "[INFO] Presenting result: \n"'\033[0;0m'
    time.sleep(1)

def sqlerror():
    time.sleep(1)
    print '\033[32m' + hour() + '[INFO] Link: ' + site
    time.sleep(1)
    print hour() + "[INFO] MYSQL Error: SQL Error: You have an error in your SQL syntax"
    time.sleep(1)
    print hour() + "[INFO] Method: GET"'\033[0;0m'
    time.sleep(1)
    print hour() + "[INFO] Scan completed\n"'\033[0;0m'

def odbc():
    time.sleep(1)
    print '\033[32m' + hour(), '[INFO] Link: ' + site
    time.sleep(1)
    print hour(), "[INFO] Oracle Error: [MySQL][ODBC 5.1 Driver][mysqld-4.1.22-community-nt-log]You have an error in your SQL syntax"
    time.sleep(1)
    print hour(), "[INFO] Method: GET"'\033[0;0m'
    time.sleep(1)
    print hour(), "[INFO] Scan completed\n"'\033[0;0m'

def mysql_fatch_array():
    time.sleep(1)
    print '\033[32m' + hour(), '[INFO] Link: ' + site
    time.sleep(1)
    print hour(), "[INFO] MYSQL Error: mysql_fetch_array()"
    time.sleep(1)
    print hour(), "[INFO] Method: GET"
    time.sleep(1)
    print hour(), "[INFO] Scan completed\n"'\033[0;0m'

def your_sql():
    time.sleep(1)
    print '\033[32m' + hour(), '[INFO] Link: ' + site
    time.sleep(1)
    print hour(), '[INFO] MYSQL or Oracle Error: You have an error in your SQL syntax'
    time.sleep(1)
    print hour(), '[INFO] Method: GET'
    time.sleep(1)
    print hour(), "[INFO] Scan completed\n"'\033[0;0m'

def mysql_query():
    time.sleep(1)
    print '\033[32m' + hour(), '[INFO] Link: ' + site
    time.sleep(1)
    print hour(), '[INFO] MYSQL Error: Warning: mysql_query()'
    time.sleep(1)
    print hour(), '[INFO] Method: GET'
    time.sleep(1)
    print hour(), "[INFO] Scan completed\n"'\033[0;0m'

def mysql_fetch_object():
    time.sleep(1)
    print '\033[32m' + hour(), '[INFO] Link: ' + site
    time.sleep(1)
    print hour(), '[INFO] MYSQL Error: Warning: mysql_fetch_object()'
    time.sleep(1)
    print hour(), '[INFO] Method: GET'
    time.sleep(1)
    print hour(), "[INFO] Scan completed\n"'\033[0;0m'

def query_failed():
    time.sleep(1)
    print '\033[32m' + hour(), '[INFO] Link: ' + site
    time.sleep(1)
    print hour(), '[INFO] MYSQL Error: Query failed : You have an error in your SQL syntax'
    time.sleep(1)
    print hour(), '[INFO] Method: GET'
    time.sleep(1)
    print hour(), "[INFO] Scan completed\n"'\033[0;0m'

def include():
    time.sleep(1)
    print '\033[32m' + hour(), '[INFO] Link: ' + site
    time.sleep(1)
    print hour(), '[INFO] MYSQL Error: Warning: include() [function.include]'
    time.sleep(1)
    print hour(), '[INFO] Method: GET'
    time.sleep(1)
    print hour(), "[INFO] Scan completed\n"'\033[0;0m'

def mysql_num_rows():
    time.sleep(1)
    print '\033[32m' + hour(), "[INFO] Link: " + site
    time.sleep(1)
    print hour(), '[INFO] MYSQL Error: mysql_num_rows()'
    time.sleep(1)
    print hour(), '[INFO] Method: GET'
    time.sleep(1)
    print hour(), "[INFO] Scan completed\n"'\033[0;0m'

def database_query_failed():
    time.sleep(1)
    print '\033[32m' + hour(), "[INFO] Link: " + site
    time.sleep(1)
    print hour(), '[INFO] MYSQL Error: Database Query Failed'
    time.sleep(1)
    print hour(), '[INFO] Method: GET'
    time.sleep(1)
    print hour(), "[INFO] Scan completed\n"'\033[0;0m'

def mysql_fetch_assoc():
    time.sleep(1)
    print '\033[32m' + hour(), "[INFO] Link: " + site
    time.sleep(1)
    print hour(), '[INFO] MYSQL Error: mysql_fetch_assoc()'
    time.sleep(1)
    print hour(), '[INFO] Method: GET'
    time.sleep(1)
    print hour(), "[INFO] Scan completed\n"'\033[0;0m'

def mysql_free_result():
    time.sleep(1)
    print '\033[32m' + hour(), "[INFO] Link: " + site
    time.sleep(1)
    print hour(), '[INFO] MYSQL Error: mysql_free_result()'
    time.sleep(1)
    print hour(), '[INFO] Method: GET'
    time.sleep(1)
    print hour(), "[INFO] Scan completed\n"'\033[0;0m'

def select_from_where_id():
    time.sleep(1)
    print '\033[32m' + hour(), "[INFO] Link: " + site
    time.sleep(1)
    print hour(), '[INFO] MYSQL Error: Query failed (SELECT * FROM WHERE id = )'
    time.sleep(1)
    print hour(), '[INFO] Method: GET'
    time.sleep(1)
    print hour(), "[INFO] Scan completed\n"'\033[0;0m'

def not_vul():
    time.sleep(1)
    print '\033[31m' + hour() + '[INFO] Link: ' + site
    time.sleep(1)
    print hour() + '[INFO] Non-Vulnerable Site'
    time.sleep(1)
    print hour() + "[INFO] Scan completed\n"'\033[0;0m'

def hour():
    now = datetime.now()
    return "["+str(now.hour) + ":" + str(now.minute)+"]"


parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", dest="url",help="Link the website", nargs=1)

args = parser.parse_args()

clear()

if args.url:
    try:
        site = args.url[0]

        if not 'http://' in site:
            url_correct = 'http://'+site

        elif not 'https://' in site:
            url_correct = 'https://'+site

        padrao = re.search(r'([\w:/\._-]+\?[\w_-]+=[\w_-]+)', url_correct)

        injecao = padrao.groups()[0] + "\'"

        header = {
            'user-agent': 'Googlebot'
                          'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/55.0.2883.87 Safari/537.36'
                          'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/51.0.2704.103 Safari/537.36'
                          'Mozilla/5.0 (Windows NT 6.1) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/55.0.2883.87 Safari/537.36'
                          'Mozilla/5.0 (Windows NT 6.1; rv:45.0)'
                          'Gecko/20100101 Firefox/45.0'
        }

        req = requests.get(injecao, headers=header)

        html = req.text
    except AttributeError:
        banner()
        time.sleep(1)
        print '\033[32m\n' + hour() + "[INFO] Invalid site, please try again\n"'\033[0;0m'
        exit()

    banner()

    if 'SQL Error' in html:
        escopo()
        sqlerror()

    elif '[MySQL][ODBC 5.1 Driver][mysqld-4.1.22-community-nt-log]You have an error in your SQL syntax' in html:
        escopo()
        odbc()

    elif 'mysql_fetch_array()' in html:
        escopo()
        mysql_fatch_array()

    elif 'You have an error in your SQL syntax' in html:
        escopo()
        your_sql()

    elif 'mysql_query()' in html:
        escopo()
        mysql_query()


    elif 'mysql_fetch_object()' in html:
        escopo()
        mysql_fetch_object()


    elif 'Query failed:' in html:
        escopo()
        query_failed()


    elif 'Warning include() [function.include]' in html:
        escopo()
        include()


    elif 'mysql_num_rows()' in html:
        escopo()
        mysql_num_rows()


    elif 'Database Query Failed' in html:
        escopo()
        database_query_failed()


    elif 'mysql_fetch_assoc()' in html:
        escopo()
        mysql_fetch_assoc()

    elif 'mysql_free_result()' in html:
        escopo()
        mysql_free_result()


    elif 'Query failed (SELECT * FROM WHERE id = )' in html:
        escopo()
        select_from_where_id()

    else:
        escopo()
        not_vul()
