Feature: internet-storm-center-status-report
  Scenario Outline: Current SANS Internet Storm Center threat condition report
    Given an English speaking user
     When the user says "what is the current internet storm center condition"
     Then "internet-storm-center-status-report-skill" should reply with dialog from "report.status.center.storm.internet.dialog"
      And mycroft reply should contain <Color>
    Examples: Threat Condition Colors
      | Color  |
      | green  |
      | yellow |
      | red    |
