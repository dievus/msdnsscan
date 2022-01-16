import dns.resolver
import dns.zone
import sys
from colorama import Fore, Style, init
import os


def style():
    global success, info, fail
    success, info, fail = Fore.GREEN + Style.BRIGHT, Fore.YELLOW + \
        Style.BRIGHT, Fore.RED + Style.BRIGHT


record_types = ['A', 'AAAA', 'NS', 'CNAME', 'MX', 'PTR', 'SOA', 'SRV',
                'TXT', 'DNSKEY', 'DNSKEYNSEC', 'NSEC3', 'NSEC3PARAM', 'RRSIG']


def banner():
    print(Fore.YELLOW + Style.BRIGHT + "")
    print('███╗   ███╗███████╗██████╗ ███╗   ██╗███████╗███████╗ ██████╗ █████╗ ███╗   ██╗')
    print('████╗ ████║██╔════╝██╔══██╗████╗  ██║██╔════╝██╔════╝██╔════╝██╔══██╗████╗  ██║')
    print('██╔████╔██║███████╗██║  ██║██╔██╗ ██║███████╗███████╗██║     ███████║██╔██╗ ██║')
    print('██║╚██╔╝██║╚════██║██║  ██║██║╚██╗██║╚════██║╚════██║██║     ██╔══██║██║╚██╗██║')
    print('██║ ╚═╝ ██║███████║██████╔╝██║ ╚████║███████║███████║╚██████╗██║  ██║██║ ╚████║')
    print('╚═╝     ╚═╝╚══════╝╚═════╝ ╚═╝  ╚═══╝╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝\n')
    print('                                   Version 1.0.0                                 ')
    print('                               A project by The Mayor                            ')
    print('                       python3 msdnsscan.py <domain> to start                  \n' + Style.RESET_ALL)
    print("-" * 79)


ns_servers = []
def main():
    try:
        domain = sys.argv[1]
    except IndexError:
        print(
            fail + f'\n[warn] You did not enter a domain. Syntax is python3 msdnsscan.py <domain>.')
        quit()
    for records in record_types:
        try:
            answers = dns.resolver.resolve(domain, records)
            print(info + f'\n{records} Records')
            print('-' * 50)
            for server in answers:
                print(success + server.to_text())
        except dns.resolver.NXDOMAIN:
            print(fail + f'\n[warn] {domain} domain does not exist.\n')
            quit()
        except dns.resolver.NoAnswer:
            print(info + f'\n[info] No {records} records found.')
        except dns.rdatatype.UnknownRdatatype:
            pass
        except dns.resolver.NoNameservers:
            pass


def zone_transfer(address):
    name_server = dns.resolver.resolve(address, 'NS')
    print(
        info + f'\n[info] Testing discovered name servers for zone transfers. This may take a minute.')
    for server in name_server:
        #print(info + f'Found Name Server: {server}')
        ip_value = dns.resolver.resolve(server.target, 'A')
        for ip_addr in ip_value:
            try:
                z_transfer = dns.zone.from_xfr(dns.query.xfr(str(ip_addr), address))
                print(
                    info + f'\nZone transfer records for {server} at {ip_addr}')
                print('-' * 60)
                for z_host in z_transfer:
                    print(success + z_host.to_text())
            except dns.xfr.TransferError:
                print(info + f'\n[info] Zone Transfer refused for {server}')
                pass
            except TimeoutError:
                print(info + f'\n[info] Zone Transfer refused for {server}')
                pass


if __name__ == "__main__":
    try:
        init()
        style()
        banner()
        main()
        domain = sys.argv[1]
        zone_transfer(domain)
        print(info + f'\n[info] DNS enumeration for {domain} completed.\n')
    except KeyboardInterrupt:
        print(
            info + f'\n[warn] You either fat fingered this, or meant to do it. Either way, goodbye!\n')
        quit()
