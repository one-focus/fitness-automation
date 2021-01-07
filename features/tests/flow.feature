# Created by kardash at 12/19/20
Feature: flow
  # Enter feature description here

  @validation
  Scenario Outline: create order
    Given обнулить таймер
    When открываю <page_name> страницу
    When считаю время загрузки "home"
    When перехожу на страницу cart
    When считаю время загрузки "cart"
    When перехожу на страницу <bank>
    When считаю время загрузки "payment_before"
    When ввожу карту <card>
    Then проверяю наличие элемента <type>
    When считаю время загрузки "payment_after"
    When отсылаю результат в гугл таблицу

    Examples:
      | page_name             | bank          | card      | type            |
      | antizhir365.ru        | alfabank      | alfa card | 3d secure page  |
      | gym-face.ru           | cloudpayments | real card | continue button |
      | minuszhir.com         | alfabank      | alfa card | 3d secure page  |
      | myslimbody.ru         | cloudpayments | real card | continue button |
      | silaosanki.ru         | cloudpayments | real card | continue button |
      | shpagat7.ru           | cloudpayments | real card | continue button |
      | twerk-twerk.ru        | cloudpayments | real card | continue button |
      | zhiry-net.ru          | cloudpayments | real card | continue button |
      | fitsbody.life/promo   | cloudpayments | real card | continue button |
      | fitsbody.life/agpromo | alfabank      | alfa card | 3d secure page  |
