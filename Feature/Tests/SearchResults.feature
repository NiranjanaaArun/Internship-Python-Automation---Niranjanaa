# Created by Admin at 14-12-2022
Feature: Search Results Page

  Scenario: Search results can be sorted by prices (low - high)

    Given Open search results page
    When Select sort by price, low to high
    Then Verify filter applied