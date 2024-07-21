*** Keywords ***
Open Example Page
    [Arguments]    ${url}
    Open Browser    ${url}    chrome
    Maximize Browser Window

Verify Page Title
    Title Should Be    百度一下，你就知道