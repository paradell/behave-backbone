from utils.api_utils import GitHubApiClient


def before_all(context):
    context.api = GitHubApiClient()
