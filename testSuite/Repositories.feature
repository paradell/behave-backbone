Feature: a user with authorized access to github API is able to manage its own repositories
  As a Github user
  I want to manage my repositories
  In order to have control on the code I upload to Github service

  Scenario: a github user is able to create a new public repository for its personal use
    Given a registered github user
    When the user defines a new public repository details for personal use
    And the user creates a new repository
    Then the api response is a 201 code
    And the repository creation response shows the correct details

  @skip
  Scenario: a github user is able to create a new private repository for its personal use
    Given a registered github user
    When the user defines a new private repository details for personal use
    And the user creates a new repository
    Then the api response is a 201 code
    And the repository creation response shows the correct details

  @skip
  Scenario: a github user is able to create a new public repository for its organization
    Given a registered github user
    When the user defines a new public repository details for an organization.
    And the user creates a new repository
    Then the api response is a 201 code
    And the repository creation response shows the correct details


  @skip
  Scenario: a github user is able to create a new private repository for its organization
    Given a registered github user
    When the user defines a new private repository details for an organization.
    And the user creates a new repository
    Then the api response is a 201 code
    And the repository creation response shows the correct details

  @skip
  Scenario: a github user will not be able to create a new repository with a name already used for that purpose
    Given a registered github user
    When the user defines a new public repository details with a repeated name
    And the user creates a new repository
    Then the api response is a 422 code

  Scenario: a github user is able to delete a repository of its own creation
    Given a registered github user
    And the user defines a new private repository details for personal use
    And the user creates a new repository
    When the user deletes one of its repositories
    Then the api response is a 204 code