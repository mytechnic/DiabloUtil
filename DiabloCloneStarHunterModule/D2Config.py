import os

import yaml


class D2Config(object):
    config = {}
    configFile = None

    def __init__(self, programId):
        self.configFile = programId + 'Config.yaml'
        if os.path.isfile(self.configFile):
            self.loadConfig()

    def getAll(self):
        return self.config

    def get(self, key):
        if key in self.config:
            return self.config[key]
        else:
            return None

    def set(self, key, value):
        self.config[key] = value

    def getConfig(self, key):
        if 'config' not in self.config:
            self.config['config'] = {}

        if key not in self.config['config']:
            self.config['config'][key] = ''

        return self.config['config'][key]

    def setConfig(self, key, value):
        self.config['config'][key] = value

    def loadConfig(self):
        with open(self.configFile, encoding='UTF8') as f:
            self.config = {'config': yaml.load(f, Loader=yaml.FullLoader)}

    def saveConfig(self):
        with open(self.configFile, 'w', encoding='UTF8') as f:
            yaml.dump(self.config['config'], f)
