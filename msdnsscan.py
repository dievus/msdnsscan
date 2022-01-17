import dns.resolver
import dns.zone
import sys
from colorama import Fore, Style, init
import requests


def style():
    global success, info, fail
    success, info, fail = Fore.GREEN + Style.BRIGHT, Fore.YELLOW + \
        Style.BRIGHT, Fore.RED + Style.BRIGHT


record_types = ['A', 'AAAA', 'NS', 'CNAME', 'MX', 'PTR', 'SOA', 'SRV',
                'TXT']
subdomains = ['a', 'acceptatie', 'access', 'accounting', 'accounts', 'ad', 'adm', 'admin', 'administrator', 'ads', 'adserver', 'affiliate', 'affiliates', 'agenda', 'alpha', 'alumni', 'analytics', 'ann', 'api', 'apollo', 'app', 'apps', 'ar', 'archive', 'art', 'assets', 'atlas', 'auth', 'auto', 'autoconfig', 'autodiscover', 'av', 'ayuda', 'b', 'b2b', 'backup', 'backups', 'banner', 'barracuda', 'bb', 'bbs', 'beta', 'biblioteca', 'billing', 'blackboard', 'blog', 'blogs', 'board', 'book', 'booking', 'bookings', 'broadcast-ip', 'bsd', 'bt', 'bug', 'bugs', 'business', 'c', 'ca', 'cache', 'cacti', 'cal', 'calendar', 'cam', 'careers', 'cart', 'cas', 'catalog', 'catalogo', 'catalogue', 'cc', 'cctv', 'cdn', 'cdn1', 'cdn2', 'chat', 'chimera', 'chronos', 'ci', 'cisco', 'citrix', 'classroom', 'client', 'clientes', 'clients', 'cloud', 'cloudflare-resolve-to', 'club', 'cms', 'cn', 'co', 'community', 'conference', 'config', 'connect', 'contact', 'contacts', 'content', 'control', 'controller', 'controlp', 'controlpanel', 'corp', 'corporate', 'correo', 'correoweb', 'cp', 'cpanel', 'crm', 'cs', 'css', 'customers', 'cvs', 'd', 'da', 'data', 'database', 'db', 'db1', 'db2', 'dbadmin', 'dbs', 'dc', 'de', 'default', 'demo', 'demo2', 'demon', 'demostration', 'descargas', 'design', 'desktop', 'dev', 'dev01', 'dev1', 'dev2', 'devel', 'developers', 'development', 'dialin', 'diana', 'direct', 'directory', 'dl', 'dmz', 'dns', 'dns1', 'dns2', 'dns3', 'dns4', 'doc', 'docs', 'domain', 'domain-controller', 'domainadmin', 'domaincontrol', 'domaincontroller', 'domaincontrolpanel', 'domainmanagement', 'domains', 'download', 'downloads', 'drupal', 'e', 'eaccess', 'echo', 'ecommerce', 'edu', 'ektron', 'elearning', 'email', 'en', 'eng', 'english', 'enterpriseenrollment', 'enterpriseregistration', 'erp', 'es', 'event', 'events', 'ex', 'example', 'examples', 'exchange', 'external', 'extranet', 'f', 'facebook', 'faq', 'fax', 'fb', 'feedback', 'feeds', 'file', 'files', 'fileserver', 'finance', 'firewall', 'folders', 'forms', 'foro', 'foros', 'forum', 'forums', 'foto', 'fr', 'free', 'freebsd', 'fs', 'ftp', 'ftp1', 'ftp2', 'ftpadmin', 'ftpd', 'fw', 'g', 'galeria', 'gallery', 'game', 'games', 'gate', 'gateway', 'gilford', 'gis', 'git', 'gmail', 'go', 'google', 'groups', 'groupwise', 'gu', 'guest', 'guia', 'guide', 'gw', 'health', 'help', 'helpdesk', 'hera', 'heracles', 'hercules', 'hermes', 'home', 'homer', 'host', 'host2', 'hosting', 'hotspot', 'hr', 'hypernova', 'i', 'id', 'idp', 'im', 'image', 'images', 'images1', 'images2', 'images3', 'images4', 'images5', 'images6', 'images7', 'images8', 'imail', 'imap', 'imap3', 'imap3d', 'imapd', 'imaps', 'img', 'img1', 'img2', 'img3', 'imgs', 'imogen', 'in', 'incoming', 'info', 'inmuebles', 'internal', 'interno', 'intra', 'intranet', 'io', 'ip', 'ip6', 'ipfixe', 'iphone', 'ipmi', 'ipsec', 'ipv4', 'ipv6', 'irc', 'ircd', 'is', 'isa', 'it', 'j', 'ja', 'jabber', 'jboss', 'jboss2', 'jira', 'job', 'jobs', 'jp', 'js', 'jupiter', 'k', 'kb', 'kerberos', 'l', 'la', 'lab', 'laboratories', 'laboratorio', 'laboratory', 'labs', 'ldap', 'legacy', 'lib', 'library', 'link', 'links', 'linux', 'lisa', 'list', 'lists', 'live', 'lms', 'local', 'localhost', 'log', 'loghost', 'login', 'logon', 'logs', 'london', 'loopback', 'love', 'lp', 'lync', 'lyncdiscover', 'm', 'm1', 'm2', 'magento', 'mail', 'mail01', 'mail1', 'mail2', 'mail3', 'mail4', 'mail5', 'mailadmin', 'mailbackup', 'mailbox', 'mailer', 'mailgate', 'mailhost', 'mailing', 'mailman', 'mailserver', 'main', 'manage', 'manager', 'mantis', 'map', 'maps', 'market', 'marketing', 'mars', 'master', 'math', 'mb', 'mc', 'mdm', 'media', 'meet', 'member', 'members', 'mercury', 'meta', 'meta01', 'meta02', 'meta03', 'meta1', 'meta2', 'meta3', 'miembros', 'mijn', 'minerva', 'mirror', 'ml', 'mm', 'mob', 'mobil', 'mobile', 'monitor', 'monitoring', 'moodle', 'movil', 'mrtg', 'ms', 'msoid', 'mssql', 'munin', 'music', 'mx', 'mx-a', 'mx-b', 'mx0', 'mx01', 'mx02', 'mx03', 'mx1', 'mx2', 'mx3', 'my', 'mysql', 'mysql2', 'n', 'nagios', 'nas', 'nat', 'nelson', 'neon', 'net', 'netmail', 'netscaler', 'network', 'network-ip', 'networks', 'new', 'newmail', 'news', 'newsgroups', 'newsite', 'newsletter', 'nl', 'noc', 'novell', 'ns', 'ns0', 'ns01', 'ns02', 'ns03', 'ns1', 'ns10', 'ns11', 'ns12', 'ns2', 'ns3', 'ns4', 'ns5', 'ns6', 'ns7', 'ns8', 'nt', 'ntp', 'ntp1', 'o', 'oa', 'office', 'office2', 'old', 'oldmail', 'oldsite', 'oldwww', 'on', 'online', 'op', 'openbsd', 'operation', 'operations', 'ops', 'ora', 'oracle', 'origin', 'orion', 'os', 'osx', 'ou', 'outgoing', 'outlook', 'owa', 'ox', 'p', 'painel', 'panel', 'partner', 'partners', 'pay', 'payment', 'payments', 'pbx', 'pcanywhere', 'pda', 'pegasus', 'pendrell', 'personal', 'pgsql', 'phoenix', 'photo', 'photos', 'php', 'phpmyadmin', 'pm', 'pma', 'poczta', 'pop', 'pop3', 'portal', 'portfolio', 'post', 'postgres', 'postgresql', 'postman', 'postmaster', 'pp', 'ppp', 'pr', 'pre-prod', 'pre-production', 'preprod', 'press', 'preview', 'private', 'pro', 'prod', 'production', 'project', 'projects', 'promo', 'proxy', 'prueba', 'pruebas', 'pt', 'pub', 'public', 'q', 'qa', 'r', 'ra', 'radio', 'radius', 'ras', 'rdp', 'redirect', 'redmine', 'register', 'relay', 'remote', 'remote2', 'repo', 'report', 'reports', 'repos', 'research', 'resources', 'restricted', 'reviews', 'robinhood', 'root', 'router', 'rss', 'rt', 'rtmp', 'ru', 's', 's1', 's2', 's3', 's4', 'sa', 'sales', 'sample', 'samples', 'sandbox', 'sc', 'search', 'secure', 'security', 'seo', 'server', 'server1', 'server2', 'service', 'services', 'sftp', 'share', 'sharepoint', 'shell', 'shop', 'shopping', 'signup', 'sip', 'site', 'siteadmin', 'sitebuilder', 'sites', 'skype', 'sms', 'smtp', 'smtp1', 'smtp2', 'smtp3', 'snmp', 'social', 'software', 'solaris', 'soporte', 'sp', 'spam', 'speedtest', 'sport', 'sports', 'sql', 'sqlserver', 'squirrel', 'squirrelmail', 'ssh', 'ssl', 'sslvpn', 'sso', 'st', 'staff', 'stage', 'staging', 'start', 'stat', 'static', 'static1', 'static2', 'stats', 'status', 'storage', 'store', 'stream', 'streaming', 'student', 'sun', 'support', 'survey', 'sv', 'svn', 't', 'team', 'tech', 'telewerk', 'telework', 'temp', 'test', 'test1', 'test2', 'test3', 'testing', 'testsite', 'testweb', 'tfs', 'tftp', 'thumbs', 'ticket', 'tickets', 'time', 'tools', 'trac', 'track', 'tracker', 'tracking', 'train', 'training', 'travel', 'ts', 'tunnel', 'tutorials', 'tv', 'tw', 'u', 'uat', 'uk', 'unix', 'up', 'update', 'upload', 'uploads', 'us', 'user', 'users', 'v', 'v2', 'vc', 'ventas', 'video', 'videos', 'vip', 'virtual', 'vista', 'vle', 'vm', 'vms', 'vmware', 'vnc', 'vod', 'voip', 'vpn', 'vpn1', 'vpn2', 'vpn3', 'vps', 'vps1', 'vps2', 'w', 'w3', 'wap', 'wc', 'web', 'web0', 'web01', 'web02', 'web03', 'web1', 'web2', 'web3', 'web4', 'web5', 'webadmin', 'webcam', 'webconf', 'webct', 'webdb', 'webdisk', 'weblog', 'webmail', 'webmail2', 'webmaster', 'webmin', 'webservices', 'webstats', 'webstore', 'whm', 'wifi', 'wiki', 'win', 'win32', 'windows', 'wordpress', 'work', 'wp', 'ws', 'wsus', 'ww', 'ww0', 'ww01', 'ww02', 'ww03', 'ww1', 'ww2', 'ww3', 'www', 'www-test', 'www0', 'www01', 'www02', 'www03', 'www1', 'www2', 'www3', 'www4', 'www5', 'www6', 'www7', 'wwwm', 'wwwold', 'wwww', 'x', 'xml', 'zabbix', 'zeus', 'zimbra']


def banner():
    print(Fore.YELLOW + Style.BRIGHT + "")
    print('███╗   ███╗███████╗██████╗ ███╗   ██╗███████╗███████╗ ██████╗ █████╗ ███╗   ██╗')
    print('████╗ ████║██╔════╝██╔══██╗████╗  ██║██╔════╝██╔════╝██╔════╝██╔══██╗████╗  ██║')
    print('██╔████╔██║███████╗██║  ██║██╔██╗ ██║███████╗███████╗██║     ███████║██╔██╗ ██║')
    print('██║╚██╔╝██║╚════██║██║  ██║██║╚██╗██║╚════██║╚════██║██║     ██╔══██║██║╚██╗██║')
    print('██║ ╚═╝ ██║███████║██████╔╝██║ ╚████║███████║███████║╚██████╗██║  ██║██║ ╚████║')
    print('╚═╝     ╚═╝╚══════╝╚═════╝ ╚═╝  ╚═══╝╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝\n')
    print('                                   Version 1.0.1                                 ')
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
        except dns.resolver.NoAnswer:
            pass
        except Exception:
            pass


def zone_transfer(address):
    name_server = dns.resolver.resolve(address, 'NS')
    print(
        info + f'\n[info] Testing name servers for zone transfers. This may take a minute.')
    for server in name_server:
        #print(info + f'Found Name Server: {server}')
        ip_value = dns.resolver.resolve(server.target, 'A')
        for ip_addr in ip_value:
            try:
                z_transfer = dns.zone.from_xfr(
                    dns.query.xfr(str(ip_addr), address))
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
            except dns.resolver.NoAnswer:
                pass
            except Exception:
                pass

def subdom_finder():
    sub_counter = 0
    subdomain_store = []
    print(info + f'\n[info] Checking for subdomains. This may take a minute.\n')
    for subdoms in subdomains:
        url = f'http://{subdoms}.{domain}'
        url_secure = f'https://{subdoms}.{domain}'
        try:
            requests.get(url)
            subdomain_store.append(subdoms)
            ip_value = dns.resolver.resolve(f'{subdoms}.{domain}', 'A')        
            for ip_addr in ip_value:
                print(success + f'{subdoms}.{domain} - {ip_addr}')    
            sub_counter = sub_counter + 1
            exists = subdoms in subdomain_store
            if exists != True:
                requests.get(url_secure)
                subdomain_store.append(subdoms)
                ip_value = dns.resolver.resolve(f'{subdoms}.{domain}', 'A')        
                for ip_addr in ip_value:
                    print(success + f'{subdoms}.{domain} - {ip_addr}')                 
                    sub_counter = sub_counter + 1
        except requests.ConnectionError:
            pass    

if __name__ == "__main__":
    try:
        init()
        style()
        banner()
        main()
        domain = sys.argv[1]
        zone_transfer(domain)
        subdom_finder()
        print(info + f'\n[info] DNS enumeration for {domain} completed.\n')
    except KeyboardInterrupt:
        print(
            info + f'\n[warn] You either fat fingered this, or meant to do it. Either way, goodbye!\n')
        quit()
