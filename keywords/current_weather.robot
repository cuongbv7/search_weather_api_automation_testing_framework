*** Settings ***
Resource        ./import_keywords.robot
Library           ../common/requestsKeywords.py
Library           ../common/distanceCalculator.py
Library           String

*** Keywords ***

Current weather data - Failure cases
    [Arguments]     ${city}         ${state_code}       ${appid}       ${expected_status_code}        ${expected_msg}
    ${q}=       Strip String	     ${city},${state_code}    mode=both     characters=,
    ${params}=      catenate    SEPARATOR=      q=${q}       &      appid=${appid}
    ${response}=    GET     ${weather_api}      ${params}
    status should be    ${expected_status_code}
    should be equal as strings      ${response.json()['message']}       ${expected_msg}


Current weather data - Success cases
    [Arguments]     ${city}         ${state_code}       ${country_code}     ${longtitude}   ${latitude}     ${timeZone}     ${cityId}
    ${q}=       Strip String	     ${city},${state_code}    mode=both     characters=,
    ${params}=      catenate    SEPARATOR=      q=${q}       &      appid=${appid}
    ${response}=    GET     ${weather_api}      ${params}
    status should be    ${success_code}
    verify response body    ${response.json()}      ${country_code}     ${longtitude}     ${latitude}     ${timeZone}     ${cityId}


Verify response body
    [Arguments]         ${response}         ${country_code}       ${longtitude}     ${latitude}     ${timeZone}     ${cityId}
    should be equal as strings      ${response['sys']['country']}           ${country_code}
    should be equal as strings      '${response['timezone']}'               '${timeZone}'
    should be equal as strings      '${response['id']}'                     '${cityId}'
    coordinate should be accurate within expected value     ${longtitude}     ${latitude}     ${response['coord']['lon']}  ${response['coord']['lat']}    0

    should not be empty     '${response['weather'][0]['id']}'
    should not be empty     ${response['weather'][0]['main']}
    should not be empty     ${response['weather'][0]['description']}
    should not be empty     ${response['weather'][0]['icon']}

    should not be empty     ${response['base']}

    should not be empty     '${response['main']['temp']}'
    should not be empty     '${response['main']['feels_like']}'
    should not be empty     '${response['main']['temp_min']}'
    should not be empty     '${response['main']['temp_max']}'
    should not be empty     '${response['main']['pressure']}'
    should not be empty     '${response['main']['humidity']}'

    should not be empty     '${response['visibility']}'
    should not be empty     '${response['wind']['speed']}'
    should not be empty     '${response['wind']['deg']}'
    should not be empty     '${response['clouds']['all']}'

    should not be empty     '${response['dt']}'
    should not be empty     '${response['sys']['type']}'
    should not be empty     '${response['sys']['id']}'
    should not be empty     '${response['sys']['sunrise']}'
    should not be empty     '${response['sys']['sunset']}'

    should not be empty     '${response['cod']}'



