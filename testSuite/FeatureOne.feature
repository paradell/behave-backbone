Feature: To test a basic API, a user will get the repositories of paradell user in GitHub
  As a GitHub visitor
  I want to get the repositories of a GitHub user
  In order to get the information of each repository

  Scenario: a user can retrieve the repository list of a GitHub user
    Given a user not registered in GitHub
    When the user tries to get the repositories of paradell user
    Then the api response is a 200 code
    And the response includes a list with all user repositories

  Scenario: a user can get information of each repository of a GitHub user
    Given a user not registered in GitHub
    When the user tries to get the repositories of paradell user
    Then each repository includes all information
