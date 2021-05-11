import os
import requests
from .config_util import BDD_config


class GitHubApiClient(object):
    """
    Define all API calls in this class using requests
    """

    def __init__(self, env='PRO'):
        self.config = BDD_config().get_config_map()
        self.env = env
        self.token = os.environ['GITHUB_TOKEN']


    @property
    def user(self):
        return self.config[self.env]['user']
    
    @property
    def url(self):
        return self.config[self.env]['url']

    @property
    def headers(self):
        return {'Accept': self.config[self.env]['version']}

    def basic_auth(self, user=None, token=None):
        return (user if user is not None else self.user,
                token if token is not None else self.token)

    def get_repositories(self, user, **kwargs):
        """
        Get from GitHub the public information of the repositories of a user)
        """
        return requests.get(url=self.url + '/users/'+user+'/repos',
                            headers=self.headers)

    def get_own_profile(self, user=None, token=None):
        """
        Get from Github the own user's information
        """
        return requests.get(url=self.url + '/user',
                            headers=self.headers,
                            auth=self.basic_auth(user=user,
                                                 token=token))

    def create_repository(self, repository_details):
        """
        Creates a new repository based on the configuration details stored in repository_details dict
        """

        return requests.post(url=self.url + '/user/repos',
                             headers=self.headers,
                             auth=self.basic_auth(),
                             json=repository_details)

    def delete_repository(self, repository_name):
        """
        Deletes the {repository_details} repository
        """

        return requests.delete(url=self.url + '/repos/'+ self.user + '/' + repository_name,
                             headers=self.headers,
                             auth=self.basic_auth())
