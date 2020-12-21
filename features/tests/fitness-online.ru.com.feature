# Created by kardash at 12/19/20
Feature: fitness-online.ru.com
  # Enter feature description here

  @validation
  Scenario: Email
    Given clear time
    When open fitness-online.ru.com page
    When calculate time for 'home'
    When go to confirmation page
    When calculate time for 'confirmation'
    When go to cloudpayments page
    When calculate time for 'payment'
    When enter real card details
    Then I see 3d secure element
    When calculate time for 'cloudpayments'
    When wait for "1" sec
