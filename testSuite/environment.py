from utils.api_utils import GitHubApiClient


def before_all(context):
    env = context.config.userdata.get("env", "PRO")
    context.api = GitHubApiClient(env=env)
