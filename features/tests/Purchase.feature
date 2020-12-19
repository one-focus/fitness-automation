# Created by kardash at 12/19/20
Feature: Purchase
  # Enter feature description here

  Scenario: Email
    Given I open home page
    When I scroll down
    And I click on activate button
    And I click on email field
    And I type "random" in email field
    And I click on next button
    Then I am on confirmation page
    When I click on confirm checkbox
    And I click on continue button
    And I click on pay button