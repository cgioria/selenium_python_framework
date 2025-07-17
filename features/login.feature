Feature: Login functionality
  As a user
  I want to login to the application
  So I can access secure areas

  Scenario: Successful login with valid credentials
    Given I am on the login page
    When I enter username "tomsmith" and password "SuperSecretPassword!"
    And I click the login button
    Then I should be redirected to the secure area

  Scenario: Failed login with invalid credentials
    Given I am on the login page
    When I enter username "invalid" and password "wrong"
    And I click the login button
    Then I should see an error message "Your username is invalid!"

  Scenario: Login with empty fields
    Given I am on the login page
    When I click the login button without entering credentials
    Then I should see an error message "Username is required"