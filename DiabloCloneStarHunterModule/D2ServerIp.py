# -*- coding: utf-8 -*-

import psutil


def getServerIpList():
    serverIpList = []
    connections = psutil.net_connections()
    cache = {}
    for conn in connections:
        if conn.pid in cache:
            (name, key) = cache[conn.pid]
        else:
            try:
                proc = psutil.Process(conn.pid)
                if len(proc.cmdline()) == 0:
                    continue

                name = proc.name()
                key = proc.cmdline()[0]
                cache[conn.pid] = (name, key)
            except Exception as e:
                print(e)
                break

        if name != 'D2R.exe':
            continue

        if conn.status != 'ESTABLISHED':
            continue

        if not conn.raddr:
            continue

        (ip, port) = conn.raddr
        if ip == '127.0.0.1':
            continue

        if port != 443:
            continue

        if ip in serverIpList:
            continue

        serverIpList.append(ip)

    return serverIpList


def getClientIpList():
    return [
        '24.105.29.76', '34.117.122.6',
        '37.244.28.80', '37.244.28.180', '37.244.54.10',
        '137.221.106.88', '137.221.106.188', '137.221.105.152',
        '117.52.35.45', '117.52.35.79', '117.52.35.179'
    ]


def getGameIpList(serverIpList):
    clientIpList = getClientIpList()
    gameIpList = []
    for ip in serverIpList:
        if ip in clientIpList:
            continue

        if (ip.startswith('34.')
                or ip.startswith('35.')
                or ip.startswith('104.')
                or ip.startswith('158.')
                or ip.startswith('37.')):
            if ip not in gameIpList:
                gameIpList.append(ip)

    return gameIpList


def getGameRegion(serverIpList):
    if len(serverIpList) < 1:
        return 'N/A'

    # IP 확인
    if '117.52.35.45' in serverIpList:
        return '아시아(45)'
    elif '117.52.35.79' in serverIpList:
        return '아시아(79)'
    elif '117.52.35.179' in serverIpList:
        return '아시아(179)'
    elif '137.221.106.88' in serverIpList:
        return '아메리카(88)'
    elif '137.221.106.188' in serverIpList:
        return '아메리카(188)'
    elif '137.221.105.152' in serverIpList:
        return '아메리카(152)'
    elif '37.244.28.80' in serverIpList:
        return '유럽(80)'
    elif '37.244.28.180' in serverIpList:
        return '유럽(180)'
    elif '37.244.54.10' in serverIpList:
        return '유럽(10)'
    else:
        return '알수없음'


def isFindGameIp(targetIp, gameIpList):
    if not targetIp:
        return False

    ips = targetIp.split(',')
    for ip in ips:
        if ip.strip() in gameIpList:
            return True

    return False


def getGameFindResult(targetIp, serverIpList, gameIpList, isStayMode=False):
    if len(serverIpList) == 0:
        return '디아블로 서버를 찾을 수 없습니다.'

    if len(gameIpList) == 0:
        return '게임방 IP를 찾을 수 없습니다.'

    ips = ', '.join(gameIpList)

    if isStayMode:
        return ips + '(지킴이 모드)'

    if not targetIp:
        return ips

    isFind = isFindGameIp(targetIp, gameIpList)
    if isFind:
        return ips + ' - ★☆★☆ OK ☆★☆★'
    else:
        return ips + ' - FAIL!'
