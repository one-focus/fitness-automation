# Created by kardash at 12/19/20
Feature: fitness-online.ru.com
  # Enter feature description here

  @validation
  Scenario Outline: cloudpayments
    Given clear time
    When open <page_name> page
    When calculate time for "home"
    When go to confirmation page
    When calculate time for "confirmation"
    When go to <bank> page
    When calculate time for "payment_before"
    When enter <card> details
    Then I see <type> element
    When calculate time for "payment_after"
    When send results to google sheet

    Examples:
      | page_name             | bank          | card      | type          |
#      | antizhir365.ru        | alfabank      | alfa card | 3d page       |
#      | fitness-online.ru.com | cloudpayments | fake card | cancel button |
#      | f.gum24.online        | cloudpayments | fake card | cancel button |
      | zhiry-net.ru          | cloudpayments | fake card | cancel button |