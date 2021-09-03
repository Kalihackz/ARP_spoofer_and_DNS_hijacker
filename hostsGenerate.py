import sys

hosts = '''{hosts_ip} *'''

def config_hosts(hosts_ip="0.0.0.0"):
    file='hosts.txt' 
    with open(file, 'w') as f:
        f.write(hosts.format(hosts_ip=hosts_ip))

config_hosts(sys.argv[1])
