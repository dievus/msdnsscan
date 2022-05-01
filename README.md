# MayorSecDNSScan

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/M4M03Q2JN)

<p align="left">
  <img src="https://github.com/dievus/msdnsscan/blob/main/images/msdnsscan.png" />
</p>

MSDNSScan is used to identify DNS records for target domains, check for zone transfers and conduct subdomain enumeration. There really isn't much special about it, and it's a lot like other tools you see installed on Kali. The goal is to implement some custom tooling into a "MayorSec Toolkit" to be released sometime in the future.

## Usage
Installing MSDNSScan

```git clone https://github.com/dievus/msdnsscan.git```

Change directories to msdnsscan and run:

```pip3 install -r requirements.txt```

This will run the install script to add necessary dependencies to your system.

```python3 msdnsscan.py -d <domain> <options>```

Options include:
 ```-dn, --dns - checks DNS records```
 
 ```-z, --zone - checks Zone Transfer records```
 
 ```-s, --subdom - checks for subdomains```
 
 ```-a, --all - runs all checks```
 
 ```-w, --wordlist - uses user input wordlist instead of default```
 
 ```-wr, --write = writes valid subdomains to a text file```

And that's it!
