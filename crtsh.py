#!/usr/bin/env python
import sys, argparse, requests, json

def parser_error(errmsg):
    print("Usage: python3 " + sys.argv[0] + " [Options] use -h for help")
    print("Error: " + errmsg)
    sys.exit()

def parse_args():    
    parser = argparse.ArgumentParser(epilog='\tExample: \r\npython3 ' + sys.argv[0] + " -d google.com")
    parser.error = parser_error
    parser._optionals.title = "OPTIONS"
    parser.add_argument('-d', '--domain', help='Domain for get subdomains from crt.sh', required=True)
    parser.add_argument('-w', '--wildcard', help='Include wildcard in output', action='store_true', required=False)
    parser.add_argument('-r', '--recursive', help='Include recursive subdomain in output', action='store_true', required=False)
    return parser.parse_args()

BASE_URL = "https://crt.sh/?q={}&output=json"
subdomains = set()
s = set()
wildcardsubdomains = set()
ws = set()

def crtsh(domain):
    response = requests.get(BASE_URL.format(domain), timeout=50)
    if response.ok:
        try:
            content = response.content.decode('UTF-8')
            jsondata = json.loads(content)            
            for i in range(len(jsondata)):
                name_value = jsondata[i]['name_value']
                if name_value.find('\n'):
                    subname_value = name_value.split('\n')
                    for subname_value in subname_value:
                        if subname_value.find('*'):
                            if subname_value not in subdomains:
                                subdomains.add(subname_value)
                        else:
                            if subname_value not in wildcardsubdomains:
                                wildcardsubdomains.add(subname_value)
                else:
                    print("`0_0`")
        except Exception as error:
            print(error)
    else:
        print("`0_0`")

if __name__ == "__main__":    
    args = parse_args()

    crtsh(args.domain)

    if args.domain:        
        for subdomain in subdomains:
            if subdomain not in s:
                s.add(subdomain)

    if args.wildcard:
        for wildcardsubdomain in wildcardsubdomains:
            if wildcardsubdomain not in ws:
                ws.add(wildcardsubdomain)
        for wildcardsubdomain in ws:
            print(wildcardsubdomain)

    if args.recursive:
        for wildcardsubdomain in wildcardsubdomains:
            wildcardsubdomain = wildcardsubdomain.replace('*.', '%25.')
            crtsh(wildcardsubdomain)

    for subdomain in s:
        print(subdomain)
