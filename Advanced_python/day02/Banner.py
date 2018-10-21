#coding=utf-8
import optparse
import socket
from socket import * #include any func or method
def connScan(tatHost,tgtPort):
    try:
        connSkt=socket(AF_INET,SOCK_STREAM) #Create TCP socket
        connSkt.connect((tgtHost,tgtPort)) #connect Socket
        connSkt.send=('ViolentPython\r\n') # Send spicy chicken information
        results=connSKt.recv(100) #s.serv(bufsize[,flag]),accept max data size
        print '[+]%d/tcp open'% tgtPort
        print '[+] '+str(results)
        connSkt.close()
    except:
        print '[-]%d/tcp closed'% tgtPort
def portScan (tgtHost,tgtPorts):
    try:
        tgtIP=gethostbyname(tgtHost)
    except:
        print "[-] Cannot reslove '%s': Unknown host"%tgtHost
        return
    try:
        tgtName= gethostbuaddr(tgtIP)
        print '\n[+] Scan Results for: '+tgtName[0]
    except:
        print '\n[+] Scan Results for:' +tgtIP
    setdefaulttimeout(1)
    for tgtPort in tatPorts:
        print 'Scanning port '+tgtPort
        connScan(tgtHost,int(tgtPort))
def main():
    parser = optparse.OptionParser("usage %prog -H"+"<target host> -p <target port>")
    parser.add_option('-H',dest='tgtHost',type='string',help='specify target host')
    parser.add_option('-p',dest='tgtPort',type='string',help='specify target port[s] separated by comma')
    (option,args)=parser.parse_args()
    tgtHost= option.tgtHost
    tgtPort= str(option.tgtPort).split(', ')
    if (tgtHost == None) | (tgtPort== None):
	    print '[-] You musy specify a targer host and port[s]'
	    exit(0)
    portScan(tgtHost,tgtPorts)

    if __name__ == '__main__':
        main()

