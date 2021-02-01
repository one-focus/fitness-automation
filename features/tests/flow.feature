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
    When отсылаю результат в гугл таблицу

    Examples:
      | page_name             | bank          |
      | antizhir365.ru        | alfabank      |
      | gym-face.ru           | cloudpayments |
      | minuszhir.com         | alfabank      |
      | myslimbody.ru         | cloudpayments |
      | silaosanki.ru         | cloudpayments |
      | shpagat7.ru           | cloudpayments |
      | twerk-twerk.ru        | cloudpayments |
      | zhiry-net.ru          | cloudpayments |
#      | fitsbody.life/promo   | cloudpayments | real card | 3d secure widget |
#      | fitsbody.life/agpromo | alfabank      | alfa card | 3d secure page   |
