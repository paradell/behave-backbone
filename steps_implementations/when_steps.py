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


@step('the user creates a new repository')
def create_repository(context):
    context.response = context.api.create_repository(repository_details=context.repo_details)


@when('the user deletes one of its repositories')
def delete_repository(context):
    context.response = context.api.delete_repository(repository_name=context.repo_details['name'])