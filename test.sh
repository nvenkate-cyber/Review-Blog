#!/usr/bin/env bash

declare -A C    # Colors
C[W]="\033[0m"  # White
C[R]="\033[31;1m" # Red
C[G]="\033[32;1m" # Green
C[B]="\033[34;1m" # Blue

function generate_credential()
{
    local USER=`tr -dc A-Za-z0-9 </dev/urandom | head -c 13`
    local PASSWD=`tr -dc A-Za-z0-9 </dev/urandom | head -c 13`
    printf "username=$USER&password=$PASSWD\n"
}

function head_status()
{
    sed -n '1p' $@ | cut -d' ' -f2
}

function get_status()
{
    curl -I -s "$@" | head_status
}

function post_status()
{
    curl -s -D - -X POST -d "$2" "$1" | head_status
}

function test_endpoint()
{
    local URL="$1"
    local ENDP="$2"
    if [[ "$3" == "GET" ]]
    then
        local GET="$3"
    else
        local POST="$3"
    fi
    local EXPECTED="$4"
    local CREDS="$5"

    printf "${C[B]}URL:${C[W]} $URL\n"
    printf "${C[B]}ENDP:${C[W]} $ENDP\n"

    if [[ "$3" == "GET" ]]
    then
        local STATUS=`get_status "$URL$ENDP"`
    else
        local STATUS=`post_status "$URL$ENDP" "$CREDS"`
    fi

    if [[ -n "$GET" ]]
    then
        printf "${C[B]}GET:${C[W]} $STATUS "
    else
        printf "${C[B]}POST:${C[W]} $STATUS "
    fi

    if [[ "$STATUS" == "$EXPECTED" ]]
    then
        if [[ "$STATUS" == 200 ]] || [[ "$STATUS" == 301 ]] || [[ "$STATUS" == 303 ]]
        then
            printf "(${C[G]}expected success${C[W]})\n"
        else
            printf "(${C[G]}expected fail${C[W]})\n"
        fi
    else
        if [[ "$STATUS" == 200 ]] || [[ "$STATUS" == 301 ]] || [[ "$STATUS" == 303 ]]
        then
            printf "(${C[R]}unexpected success${C[W]}:$EXPECTED)\n"
        else
            printf "(${C[R]}unexpected fail${C[W]}:$EXPECTED)\n"
        fi
        printf "(${C[R]}fail${C[W]})\n"
    fi
    [[ -n "GET" ]] && printf "; with CREDENTIALS=\"$CREDS\"\n"

    if [[ "$STATUS" == "$EXPECTED" ]]
    then
        printf "0\n"
    else
        printf "1\n"
    fi
}

CREDENTIALS=`generate_credential`
MOCK_CREDENTIALS="username=user&password=password"

URL='https://review-blog.duckdns.org'
ENDPOINTS=(\
"/         : GET  : 200 : $CREDENTIALS"
"/health   : GET  : 200 : $CREDENTIALS"
"/register : GET  : 200 : $CREDENTIALS"
"/register : POST : 200 : $CREDENTIALS"
"/register : GET  : 200 : $CREDENTIALS"
"/register : POST : 418 : $CREDENTIALS"
"/login    : GET  : 200 : $CREDENTIALS"
"/login    : POST : 200 : $CREDENTIALS"
"/login    : POST : 418 : $MOCK_CREDENTIALS"
"/random   : GET  : 404 : $MOCK_CREDENTIALS"
"/random   : POST : 404 : $MOCK_CREDENTIALS")

for ENDP in "${ENDPOINTS[@]}"
do
    RESULT="$(test_endpoint "$URL" `printf "$ENDP" | tr ':' ' '`)"
    SUCCESS="`printf "$RESULT" | sed -n '$p'`"
    if [[ "$SUCCESS" == "1" ]]
    then
        ERROR="1"
    fi
    printf "$RESULT" | sed -n '1,3p'
    echo
done

exit $ERROR
