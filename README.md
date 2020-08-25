# crtsh.py
A Python utility to fetch or would say scrap subdomains from https://crt.sh

### Requirements
```
argparse
requests
json
```

### Installation
```
git clone https://github.com/YashGoti/crtsh.py.git
cd crtsh.py
python3 crtsh.py -h
```
* if you want to use crtsh from anywhere try below installation guide
```
git clone https://github.com/YashGoti/crtsh.py.git
cd crtsh.py
mv crtsh.py crtsh
chmod +x crtsh
cp crtsh /usr/bin/
```

### Options
|Flags||Description|
|-|-|-|
|-h|--help|show this help message and exit|
|-d DOMAIN|--domain DOMAIN|Specify Target Domain to get subdomains from crt.sh|
|-r|--recursive|Do recursive search for subdomains|
|-w|--wildcard|Include wildcard in output|

### Usage
```
python3 crtsh.py -d example.com
python3 crtsh.py -d example.com -w
python3 crtsh.py -d example.com -r
python3 crtsh.py -d example.com -r -w
```
