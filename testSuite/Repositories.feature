Feature: a user with authorized access to github API is able to manage its own repositories
  As a Github user
  I want to manage my repositories
  In order to have control on the code I upload to Github service

  Scenario: a github user is able to create a new public repository for its personal use
    Given a registered github user
    When the user defines a new public repository details for personal use
    And the user creates a new repository
    Then the api response is a 200 code

  @skip
  Scenario: a github user is able to create a new private repository for its personal use
    Given a registered github user
    When the user defines a new private repository details for personal use
    And the user creates a new repository
    Then the api response is a 200 code

  @skip
  Scenario: a github user is able to create a new public repository for its organization
    Given a registered github user
    When the user defines a new public repository details for an organization.
    And the user creates a new repository
    Then the api response is a 200 code


  @skip
  Scenario: a github user is able to create a new private repository for its organization
    Given a registered github user
    When the user defines a new private repository details for an organization.
    And the user creates a new repository
    Then the api response is a 200 code