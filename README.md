# crtsh.py
A Python utility to scrape subdomains from https://crt.sh.

### Installation
```shell
git clone https://github.com/YashGoti/crtsh.py.git
cd crtsh.py
python3 crtsh.py -h
```

If you want to use crtsh from anywhere:

```shell
git clone https://github.com/YashGoti/crtsh.py.git
cd crtsh.py
mv crtsh.py crtsh
chmod +x crtsh
cp crtsh /usr/bin/
```

### Options
|Flags||Description|
|-|-|-|
|-h|--help|Show this help message and exit|
|-d DOMAIN|--domain DOMAIN|Specify target domain to get subdomains from crt.sh|
|-o FILENAME|--output FILENAME|Specify file to direct output to|
|-r|--recursive|Do recursive search for subdomains|
|-w|--wildcard|Include wildcard in output|

### Usage
```shell
python3 crtsh.py -d example.com
python3 crtsh.py -d example.com -w
python3 crtsh.py -d example.com -r
python3 crtsh.py -d example.com -r -w
python3 crtsh.py -d example.com -r -w -o output.txt
```
