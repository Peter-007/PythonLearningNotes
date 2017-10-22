# coding=utf-8

import paramiko

g_ssh = paramiko.SSHClient()
g_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def openSSH(ip,username,password):
    try:
        print('connecting ... %s' % ip)
        g_ssh.connect(ip,22,username,password)
    except:
        print('%s failed to connect.' % (ip))
        return False
    else:
        print('%s is connected.' % ip)
        return True

def exeCmd(strCmd, strException):
    try:
        stdin,stdout,stderr = g_ssh.exec_command(strCmd)
        strResult = str(stdout.read())
        print(strResult)
        i = strResult.find(strException)
        if i >= 0:
            return True
        else:
            return False

    except:
        print('Execute command error: %s' % strCmd)
        return False

def closeSSH():
    g_ssh.close()

def ssh_test():
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect('192.168.8.100',22,'pi','raspberry')
        stdin,stdout,stderr = ssh.exec_command('/sbin/ifconfig')
        for x in stdout.readlines():
            print(x.strip('\n'))
        stdin, stdout, stderr = ssh.exec_command( 'ls' )
        # print(stdin,stdout,stderr)
        #print(stdout.read())
        for x in stdout.readlines():
            print(x.strip('\n'))

    finally:
        ssh.close()

if __name__ == '__main__':
    openSSH('192.168.8.100','pi','raspberry')
    print(exeCmd('ls','ex') and exeCmd('ls', 'Public') and exeCmd('/sbin/ifconfig','8.200'))

    listResult = list(map(exeCmd,['ls','ls','/sbin/ifconfig'],['ex','public','192.168.8.100']))
    print(listResult)
    closeSSH()

