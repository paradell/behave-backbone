import requests
from .config_util import BDD_config


class GitHubApiClient(object):
    """
    Define all API calls in this class using requests
    """

    def __init__(self, env='PRO'):
        self.config = BDD_config().get_config_map()
        self.env = env

    @property
    def url(self):
        return self.config[self.env]['url']

    @property
    def headers(self):
        return {'Accept': self.config[self.env]}

    def get_repositories(self, user, **kwargs):
        """
        Get from GitHub the public information of the repositories of a user)
        """
        return requests.get(self.url + '/users/'+user+'/repos')
