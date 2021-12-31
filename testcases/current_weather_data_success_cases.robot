*** Settings ***
Documentation       Data driven test for positive cases with value read from csv file


Resource        ${CURDIR}/../keywords/import_keywords.robot
Resource        ${CURDIR}/../resources/import_resources.robot


*** Variables ***

${csv_file}     ${CURDIR}/../resources/data_test/data_driven.csv

*** Test Cases ***

Success cases - Get weather data
    @{data}=    GET DATA FROM CSV    ${csv_file}

    FOR    ${row}    IN    @{data}
        ${city}=            set variable    ${row[0]}
        ${state_code}=      set variable    ${row[1]}
        ${country_code}=    set variable    ${row[2]}
        ${longtitude}=      set variable    ${row[3]}
        ${latitude}=        set variable    ${row[4]}
        ${timeZone}=        set variable    ${row[5]}
        ${cityId}=          set variable    ${row[6]}
        Current weather data - Success cases     ${city}    ${state_code}   ${country_code}     ${longtitude}   ${latitude}     ${timeZone}     ${cityId}
    END