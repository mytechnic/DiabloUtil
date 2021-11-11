GAME_IP_PREFIX_LIST = (34, 35, 104, 158)


def getFirewallName(targetIp, is2Octet=True):
    if not targetIp:
        return ''

    z = targetIp.split('.')
    o1 = int(z[0])
    o2 = int(z[1])

    if is2Octet:
        return '스타 우버디아 (' + str(o1) + '.' + str(o2) + '.x.x)'
    else:
        return '스타 우버디아 (' + str(o1) + '.x.x.x)'


def getFirewallIpList(targetIp, is2Octet=True):
    if not targetIp:
        return []

    z = targetIp.split('.')
    o1 = int(z[0])
    o2 = int(z[1])

    firewallIpList = []
    for g1 in GAME_IP_PREFIX_LIST:
        if o1 == g1:
            if is2Octet:
                firewallIpList.append(str(g1) + '.1.1.1-' + str(g1) + '.' + str(o2 - 1) + '.255.255')
                firewallIpList.append(str(g1) + '.' + str(o2 + 1) + '.1.1-' + str(g1) + '.255.255.255')
            else:
                firewallIpList.append(str(g1) + '.1.1.1-' + str(g1) + '.255.255.255')
        else:
            firewallIpList.append(str(g1) + '.1.1.1-' + str(g1) + '.255.255.255')

    return firewallIpList
