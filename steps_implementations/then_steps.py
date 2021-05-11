from behave import *
from pyshould import should


@then('the api response is a {code} code')
def check_http_response_code(context, code):
    # Check if the response has the correct HTTP response status code
    context.response.status_code | should.be_equal(int(code))


@then('the response includes a list with all user repositories')
def check_user_repository_list(context):
    # Check that the json returned by the API is correct
    repositories = context.response.json()

    # Check that the user has more than one repository
    repositories | should.be_a_list()
    len(repositories) | should.be_more(0)


@then('each repository includes all information')
def check_repository_details(context):
    repositories = context.response.json()

    for repository in repositories:
        repository | should.have_entries({
            "id": should.be_an_integer(),
            "name": should.be_a_string(),
            "full_name": should.be_a_string(),
            "owner": {
              "login": should.be_a_string(),
              "id": should.be_an_integer(),
              "avatar_url": should.be_a_string(),
              "gravatar_id": should.be_a_string(),
              "url": should.be_a_string(),
              "html_url": should.be_a_string(),
              "followers_url": should.be_a_string(),
              "following_url": should.be_a_string(),
              "gists_url": should.be_a_string(),
              "starred_url": should.be_a_string(),
              "subscriptions_url": should.be_a_string(),
              "organizations_url": should.be_a_string(),
              "repos_url": should.be_a_string(),
              "events_url": should.be_a_string(),
              "received_events_url": should.be_a_string(),
              "type": should.be_a_string(),
              "site_admin": should.be_a_bool()
            },
            "private": should.be_a_bool(),
            "html_url": should.be_a_string(),
            "description": should.be_a_string(),
            "fork": should.be_a_bool(),
            "url": should.be_a_string(),
            "forks_url": should.be_a_string(),
            "keys_url": should.be_a_string(),
            "collaborators_url": should.be_a_string(),
            "teams_url": should.be_a_string(),
            "hooks_url": should.be_a_string(),
            "issue_events_url": should.be_a_string(),
            "events_url": should.be_a_string(),
            "assignees_url": should.be_a_string(),
            "branches_url": should.be_a_string(),
            "tags_url": should.be_a_string(),
            "blobs_url": should.be_a_string(),
            "git_tags_url": should.be_a_string(),
            "git_refs_url": should.be_a_string(),
            "trees_url": should.be_a_string(),
            "statuses_url": should.be_a_string(),
            "languages_url": should.be_a_string(),
            "stargazers_url": should.be_a_string(),
            "contributors_url": should.be_a_string(),
            "subscribers_url": should.be_a_string(),
            "subscription_url": should.be_a_string(),
            "commits_url": should.be_a_string(),
            "git_commits_url": should.be_a_string(),
            "comments_url": should.be_a_string(),
            "issue_comment_url": should.be_a_string(),
            "contents_url": should.be_a_string(),
            "compare_url": should.be_a_string(),
            "merges_url": should.be_a_string(),
            "archive_url": should.be_a_string(),
            "downloads_url": should.be_a_string(),
            "issues_url": should.be_a_string(),
            "pulls_url": should.be_a_string(),
            "milestones_url": should.be_a_string(),
            "notifications_url": should.be_a_string(),
            "labels_url": should.be_a_string(),
            "releases_url": should.be_a_string(),
            "deployments_url": should.be_a_string(),
            "created_at": should.be_a_string(),
            "updated_at": should.be_a_string(),
            "pushed_at": should.be_a_string(),
            "git_url": should.be_a_string(),
            "ssh_url": should.be_a_string(),
            "clone_url": should.be_a_string(),
            "svn_url": should.be_a_string(),
            "homepage": should.be_a_string.or_be_none(),
            "size": should.be_an_integer(),
            "stargazers_count": should.be_an_integer(),
            "watchers_count": should.be_an_integer(),
            "language": should.be_a_string.or_be_none(),
            "has_issues": should.be_a_bool(),
            "has_downloads": should.be_a_bool(),
            "has_wiki": should.be_a_bool(),
            "has_pages": should.be_a_bool(),
            "forks_count": should.be_an_integer(),
            "mirror_url": should.be_a_string.or_be_none(),
            "open_issues_count": should.be_an_integer(),
            "forks": should.be_an_integer(),
            "open_issues": should.be_an_integer(),
            "watchers": should.be_an_integer(),
            "default_branch": should.be_a_string()
          })


@then('the repository creation response shows the correct details')
def check_create_repository_response_details(context):
    create_repository = context.response.json()

    create_repository['name'] | should.be_equal(context.repo_details['name'])
    create_repository['description'] | should.be_equal(context.repo_details['description'])
    create_repository['private'] | should.be_equal(context.repo_details['private'])
