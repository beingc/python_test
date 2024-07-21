*** Settings ***
Library    SeleniumLibrary
Resource   ../resources/keywords.robot

*** Variables ***
${URL}    https://www.baidu.com

*** Test Cases ***
Test Example Page Title
    Open Browser    ${URL}    chrome
    Verify Page Title
    Close Browser