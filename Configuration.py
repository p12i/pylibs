import ConfigParser


class Configuration(object):
    class __impl:
        def __init__(self, path=None):
            self.config = ConfigParser.ConfigParser()
            if path:
                self.config.read(path)
            self.globals = {}

    __instance = None

    def __init__(self, path=None):
        if not (Configuration.__instance or path):
            raise RuntimeError('No instance of class configuration and no'
                               + ' config file path given.')
        elif not Configuration.__instance:
            Configuration.__instance = Configuration.__impl(path)

    @staticmethod
    def getInstance():
        return Configuration.__instance.config

    @staticmethod
    def setup(configuration):
        if not Configuration.__instance:
            Configuration.__instance = Configuration.__impl(configuration)
        return Configuration.__instance.config

    @staticmethod
    def registerGlobal(name, value):
        Configuration.__instance.globals[name] = value

    @staticmethod
    def getGlobal(name):
        return Configuration.__instance.globals.get(name)

    @staticmethod
    def defaults(name):
        return Configuration.__instance.config.defaults.get(name)

    @staticmethod
    def get(section, name=None, **kwargs):
        try:
            if name:
                var = Configuration.__instance.config.get(section, name)
            else:
                var = Configuration.defaults(section)
            if var and (len(var.split("\n")) >= 2):
                tvars = []
                for v in var.split("\n"):
                    if v and v != "":
                        tvars.append(v)
                var = tvars
            return var
        except ConfigParser.Error:
            return kwargs.get('default')

    @staticmethod
    def check(name, section=None):
        val = Configuration.get(name, section)
        if val and val.lower() in ['true', 'on', 1]:
            return True
        else:
            return False
