# MSDNSScan

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

```-a, --all - runs all checks```

 ```-dn, --dns - checks DNS records```
 
 ```-z, --zone - checks Zone Transfer records```

 ```-e, --email - checks Email records (DMARC, SPF, and DKIM)```
 
 ```-s, --subdom - checks for subdomains```
  
 ```-w, --wordlist - uses user input wordlist instead of default```
 
 ```-wl, --weblist - use a raw.githubusercontent.com wordlist for subdomains```

 ```-tx, --test - write results of subdomain scan to a text file```

 ```-md, --markdown - write results of subdomain scan to a markdown file for use with Xmind```

 ```-il, --input - check subdomain against a list of IP addresses```

 ```-c, --concurrent (requests) - Number of concurrent requests to run. Defaults to 10. Anything greater than 10 can be unstable```

And that's it!
