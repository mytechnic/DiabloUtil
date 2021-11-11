import os

import yaml


class D2Config(object):
    config = {}
    configFile = None

    def __init__(self, programId):
        self.configFile = programId + 'Config.yaml'
        if os.path.isfile(self.configFile + 'Config.yaml'):
            self.loadConfig()

    def get(self, key):
        return self.config[key]

    def put(self, key, value):
        self.config[key] = value
        if key == 'config':
            self.saveConfig()

    def getConfig(self, key):
        if 'config' not in self.config:
            self.config['config'] = {}

        if 'config' not in self.config['config']:
            self.config['config'][key] = ''

        return self.config['config'][key]

    def setConfig(self, key, value):
        self.config['config'][key] = value
        self.saveConfig()

    def loadConfig(self):
        with open(self.configFile) as f:
            self.config['config'] = yaml.load(f, Loader=yaml.FullLoader)

    def saveConfig(self):
        with open(self.configFile, 'w') as f:
            yaml.dump(self.config['config'], f)
