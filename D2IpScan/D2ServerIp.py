# -*- coding: utf-8 -*-
import winsound

import psutil


def getServerIpList():
    serverIpList = []
    for conn in psutil.net_connections():
        if psutil.Process(conn.pid).name() != 'D2R.exe':
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


def getGameIpList(serverIpList):
    gameIpList = []
    for ip in serverIpList:
        if (ip == '24.105.29.76'
                # 유럽
                or ip == '37.244.28.80'
                or ip == '104.76.67.204'
                # 아메리카
                or ip == '34.117.122.6'
                or ip == '137.221.106.88'):
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
    if '117.52.35.79' in serverIpList:
        return '아시아(79)'
    elif '117.52.35.179' in serverIpList:
        return '아시아(179)'
    elif '137.221.106.88' in serverIpList:
        return '아메리카'
    elif '37.244.28.80' in serverIpList:
        return '유럽'
    else:
        return 'None'


def isFindGameIp(targetIp, gameIpList):
    if not targetIp:
        return False

    return targetIp.strip() in gameIpList


def getGameFindResult(targetIp, gameIpList):
    if len(gameIpList) == 0:
        return '게임 아이피를 찾을 수 없습니다.'

    ips = ', '.join(gameIpList)

    if not targetIp:
        return ips

    isFind = isFindGameIp(targetIp, gameIpList)
    if isFind:
        winsound.PlaySound("SystemHand", winsound.SND_ASYNC | winsound.SND_ALIAS)
        return ips + ' - ★☆★☆ OK ☆★☆★'
    else:
        return ips + ' - FAIL!'
