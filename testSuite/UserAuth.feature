Feature: To access some of the github API resources, a github user have to be authenticated into github service
  As a Github user
  I want to get authenticated into github API services
  In order to get access to restricted github API actions


  Scenario: A Github user with the correct token is able to authenticate into Github API
    Given a registered github user
    And the user has a correct authentication token
    When the user accesses into its own profile
    Then the api response is a 200 code

  Scenario: A Github user with an incorrect token is not able to authenticate into Github API
    Given a registered github user
    And the user has a correct authentication token
    When the user accesses into its own profile
    Then the api response is a 401 code
