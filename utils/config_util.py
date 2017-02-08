from ConfigParser import ConfigParser


class BDD_config(object):
    """
    Import settings from settings.cfg file to use it in BDD tests
    """

    def __init__(self):
        self.config = ConfigParser()
        self.config.read('settings.cfg')

    def get_config_map(self):
        dict = {}
        sections = self.config.sections()

        for section in sections:
            dict[section] = {}
            options = self.config.options(section)
            for option in options:
                dict[section][option] = self.config.get(section, option)

        return dict
