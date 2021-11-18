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


def getTargetIpToFirewallIpList(targetIp, firewallClass='B'):
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


def getRuleIpToFirewallIpList(rules):
    if not rules:
        return []

    z = rules.split("\n")
    firewallIpList = []
    for rule in z:
        rule = rule.strip()
        rule = rule.replace(' ', '')
        if not rule:
            continue

        firewallIpList.append(rule)

    return firewallIpList


def setFirewall(targetIp, programPath, firewallIpList):
    name = getFirewallName(targetIp)
    remoteip = ','.join(firewallIpList)

    cmd = ['netsh', 'advfirewall', 'firewall', 'add', 'rule', 'name=' + name + '', 'dir=out',
           'program=' + programPath + '', 'remoteip=' + remoteip, 'action=block', 'enable=yes']
    res = subprocess.run(cmd, stdout=subprocess.PIPE, text=True)
    if res.returncode == 0:
        return True
    else:
        return False


def delFirewall(programPath):
    cmd = ['netsh', 'advfirewall', 'firewall', 'show', 'rule', 'name=all', 'dir=out', 'verbose']
    data = subprocess.run(cmd, stdout=subprocess.PIPE, text=True)
    arr = data.stdout.split("\n")

    ruleList = []
    for text in arr:
        if text.find('규칙 이름:') >= 0:
            ruleList.append({})

        if len(ruleList) == 0:
            continue

        z = text.strip().split(':', maxsplit=1)
        if len(z) < 2:
            continue

        key = z[0].strip()
        val = z[1].strip()
        idx = len(ruleList) - 1
        ruleList[idx][key] = val

    for rule in ruleList:
        if '규칙 이름' in rule:
            name = rule['규칙 이름']
        else:
            name = ''
        if '프로그램' in rule:
            program = rule['프로그램']
        else:
            program = ''

        if name.find('스타 우버디아') == -1:
            continue

        if program != programPath:
            continue

        cmd = ['netsh', 'advfirewall', 'firewall', 'delete', 'rule', 'name=' + name + '', 'dir=out',
               'program=' + programPath + '']
        res = subprocess.run(cmd, stdout=subprocess.PIPE, text=True)
        if res.returncode != 0:
            return False, res.stderr

    return True, 'OK'
