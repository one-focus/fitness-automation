# Created by kardash at 12/19/20
Feature: fitness-online.ru.com
  # Enter feature description here

  @validation
  Scenario Outline: Email
    Given clear time
    When open <page_name> page
    When clear time
    When go to confirmation page
    When calculate time for 'confirmation'
    When go to cloudpayments page
    When enter <card> details
    Then I see <type> element
    When calculate time for 'cloudpayments'

    Examples:
      | page_name      | card      | type          |
      | f.gum24.online | fake card | cancel button |
