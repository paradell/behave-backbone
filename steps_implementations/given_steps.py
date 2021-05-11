from behave import *


@given('a user not registered in GitHub')
def user_not_registered(context):
    # Set context user as a non existing one to override the one in configuration
    context.user = 'non_existing_user'

@given('a registered github user')
def user_registered(context):
    # Do not override the user name
    context.user = None

@given('the user has a correct authentication token')
def user_with_correct_token(context):
    # Do not override the user name
    context.token = None

@given('the user has an incorrect authentication token')
def user_with_incorrect_token(context):
    # Set context token as an incorrect one to override the one in configuration
    context.token = 'incorrect_token'


@given('the user defines a new {privacy:w} repository details for personal use')
def define_new_repository_details(context, privacy):
    context.repo_details = dict()
    context.repo_details['name'] = f'test_repo_{datetime.now().strftime("%Y%m%d%H%M%S")}'
    context.repo_details['private'] = True if privacy == 'private' else False
    context.repo_details['description'] = f'This is a {privacy} repo for test purposes'