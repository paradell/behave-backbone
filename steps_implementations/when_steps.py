from behave import *


@when('the user tries to get the repositories of {user:w} user')
def get_user_repositories(context, user):
    # make a GET call to https://api.github.com/users/paradell/repos
    context.response = context.api.get_repositories(user=user)


@when('the user accesses into its own profile')
def get_own_profile(context):
    # make a GET call to https://api.github.com/user
    context.response = context.api.get_own_profile(user=context.user,
                                                   token=context.token)


@when('the user defines a new {privacy:w} repository details for personal use')
def define_new_repository_details(context, privacy):
    context.repo_details = dict()
    context.repo_details['name'] = 'test_repo'
    context.repo_details['private'] = True if privacy == 'private' else False
    context.repo_details['description'] = f'This is a {privacy} repo for test purposes'


@when('the user creates a new repository')
def create_repository(context):
    context.response = context.api.create_repository(repository_details=context.repo_details)
