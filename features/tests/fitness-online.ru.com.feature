# Created by kardash at 12/19/20
Feature: fitness-online.ru.com
  # Enter feature description here

  @validation
  Scenario Outline: Email
    Given clear time
    When open <page_name> page
    When calculate time for 'home'
    When go to confirmation page
    When calculate time for 'confirmation'
    When go to cloudpayments page
    When calculate time for 'payment'
    When enter fake card details
    Then I see cancel button element
    When calculate time for 'cloudpayments'

    Examples:
      | page_name             |
      | fitness-online.ru.com |
      | f.gum24.online        |
