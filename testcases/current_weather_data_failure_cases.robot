*** Settings ***
Documentation       Data driven test for negative cases

Resource        ../keywords/import_keywords.robot
Resource        ../resources/import_resources.robot

Test Template       Current weather data - Failure cases

*** Test Cases ***
TC_001 - Empty city param          ${EMPTY}             US-AK          ${appid}                 ${notfound_code}            city not found
TC_002 - Invalid city               Anc                 US-AK          ${appid}                 ${notfound_code}            city not found
TC_003 - Invalid state code         Anchorage           AK             ${appid}                 ${notfound_code}            city not found
TC_004 - Invalid app id             Anchorage           US-AK          ${invalid_appID}         ${unauthorized_code}        Invalid API key. Please see http://openweathermap.org/faq#error401 for more info.

