from behave import *


@when('the user tries to get the repositories of {user:w} user')
def get_user_repositories(context, user):
    # make a GET call to https://api.github.com/users/paradell/repos
    context.response = context.api.get_repositories(user=user)
