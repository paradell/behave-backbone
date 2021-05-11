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
    pass

@given('the user has an incorrect authentication token')
def user_with_incorrect_token(context):
    context.token = 'incorrect_token'
