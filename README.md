# MayorSecDNSScan

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/M4M03Q2JN)

<p align="left">
  <img src="https://github.com/dievus/msdnsscan/blob/main/images/example.png" />
</p>

MSDNSScan is used to identify DNS records for target domains and check for zone transfers. There really isn't much special about it, and it's a lot like other tools you see installed on Kali. The goal is to implement some custom tooling into a "MayorSec Toolkit" to be released sometime in the future.

## Usage
Installing MSDNSScan

```git clone https://github.com/dievus/msdnsscan.git```

Change directories to msdnsscan and run:

```pip3 install -r requirements.txt```

This will run the install script to add necessary dependencies to your system.

```python3 msdnsscan.py <domain>```

And that's it!
