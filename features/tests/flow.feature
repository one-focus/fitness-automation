# Created by kardash at 12/19/20
Feature: flow
  # Enter feature description here

  @validation
  Scenario Outline: create order
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
      | page_name             | bank          | card      | type           |
      | shpagat7.ru           | cloudpayments | fake card | cancel button  |
      | myslimbody.ru         | cloudpayments | fake card | cancel button  |
      | twerk-twerk.ru        | cloudpayments | fake card | cancel button  |
      | silaosanki.ru         | cloudpayments | fake card | cancel button  |
      | minuszhir.com         | alfabank      | alfa card | 3d secure page |
      | fitness-online.ru.com | cloudpayments | fake card | cancel button  |
      | f.gum24.online        | cloudpayments | fake card | cancel button  |
      | zhiry-net.ru          | cloudpayments | fake card | cancel button  |
      | antizhir365.ru        | alfabank      | alfa card | 3d secure page |
#      | fitness-online.ru.com | cloudpayments | real card | 3d secure widget |
#      | f.gum24.online        | cloudpayments | real card | 3d secure widget |
#      | zhiry-net.ru          | cloudpayments | real card | 3d secure widget |