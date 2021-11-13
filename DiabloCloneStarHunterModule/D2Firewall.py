import subprocess

GAME_IP_PREFIX_LIST = (34, 35, 104, 158)


def getFirewallName(targetIp, firewallClass='B'):
    if not targetIp:
        return ''

    z = targetIp.split('.')
    o1 = int(z[0])
    o2 = int(z[1])

    if firewallClass == 'B':
        return '스타 우버디아 (' + str(o1) + '.' + str(o2) + '.x.x)'
    else:
        return '스타 우버디아 (' + str(o1) + '.x.x.x)'


def getFirewallIpList(targetIp, firewallClass='B'):
    if not targetIp:
        return []

    z = targetIp.split('.')
    o1 = int(z[0])
    o2 = int(z[1])

    firewallIpList = []
    for g1 in GAME_IP_PREFIX_LIST:
        if o1 == g1:
            if firewallClass == 'B':
                firewallIpList.append(str(g1) + '.1.1.1-' + str(g1) + '.' + str(o2 - 1) + '.255.255')
                firewallIpList.append(str(g1) + '.' + str(o2 + 1) + '.1.1-' + str(g1) + '.255.255.255')
        elif g1 == 34:
            firewallIpList.append('34.1.1.1-' + '34.117.122.5')
            firewallIpList.append('34.117.122.7-' + '34.255.255.255')
        else:
            firewallIpList.append(str(g1) + '.1.1.1-' + str(g1) + '.255.255.255')
    return firewallIpList


def setFirewall(targetIp, program, firewallIpList):
    name = getFirewallName(targetIp)
    remoteip = ','.join(firewallIpList)

    cmd = ['netsh', 'advfirewall', 'firewall', 'add', 'rule', 'name=' + name, 'dir=out',
           'program=' + program, 'remoteip=' + remoteip, 'action=block', 'enable=yes']
    res = subprocess.run(cmd, stdout=subprocess.PIPE, text=True)
    if res.returncode == 0:
        return True
    else:
        return False


def clearFirewall():
    data = subprocess.run(['netsh', 'advfirewall', 'firewall', 'show', 'rule', 'name=all', 'dir=out'],
                          stdout=subprocess.PIPE, text=True)
    arr = data.stdout.split("\n")

    for text in arr:
        if text.find('스타 우버디아 (') == -1:
            continue

        z = text.split('규칙 이름:')
        name = z[1].strip()
        res = subprocess.run(['netsh', 'advfirewall', 'firewall', 'delete', 'rule', 'name=', name],
                             stdout=subprocess.PIPE, text=True)
        if res.returncode != 0:
            return False

    return True
