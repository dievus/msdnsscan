import dns.resolver
import sys
from colorama import Fore, Style, init


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
            print(success + f'\n{records} records found')
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

    print(f'\n[info] DNS enumeration for {domain} completed.\n')


if __name__ == "__main__":
    try:
        init()
        style()
        banner()
        main()
    except KeyboardInterrupt:
        print(
            info + f'\n[warn] You either fat fingered this, or meant to do it. Either way, goodbye!\n')
        quit()
