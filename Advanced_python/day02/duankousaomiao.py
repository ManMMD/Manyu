# _*_coding:utf8-
import optparse
import socket
from socket import gethostbyaddr,gethostbyname

def connScan(tgtHost,tgtPort):
    try:
        connSkt = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        connSkt.connect((tgtHost,tgtPort))
        connSkt.send('ViolentPython\r\n')
        results = connSkt.recv(100)
        print '[+]%d/tcp open' % tgtPort
        print '[+] '+str(results)
        connSkt.close()
    except:
        print '[-]%d/tcp closed' % tgtPort

def portScan(tgtHost,tgtPorts):
    try:
        tgtIp=gethostbyname(tgtHost)
        print '[+] hostname ipv4 is :'+str(tgtIp)
    except:
        print '[-] Cannot resolve \'%s\': Unkonwn host' % tgtHost

    try:
        tgtName= gethostbyaddr(tgtIp)
        print '[+] Scan Results for: ' + tgtName[0]
    except:
        print '[+] Scan Results for: ' + tgtIp
    socket.setdefaulttimeout(1)
    
    for tgtPort in tgtPorts:
        print 'Scanning port '+ tgtPort
        connScan(tgtHost,int(tgtPort))

def main():
    parser = optparse.OptionParser('usage %prog -H' + ' <target host> -p <target port>')

    parser.add_option('-H',dest = 'tgtHost',type='string', help='host and address')
    parser.add_option('-p',dest = 'tgtPort',type='string', help='port')

    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPort = options.tgtPort.split(',')

    if (tgtHost == None) and (tgtPort == None):
        print parser.usage
        exit(0)
    else:
        portScan(tgtHost,tgtPort)

if __name__ == '__main__':
    main()
