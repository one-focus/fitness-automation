# Created by kardash at 12/19/20
Feature: test
  # Enter feature description here

  @test
  Scenario Outline: test
    Given обнулить таймер
    When открываю <page_name> страницу
    When перехожу на страницу cart
    When считаю время загрузки "cart"
    When перехожу на страницу <bank>
    When ввожу карту <card>
    Then проверяю наличие элемента <type>

    Examples:
      | page_name      | bank          | card      | type             |
      | minuszhir.com  | alfabank      | alfa card | 3d secure page   |
