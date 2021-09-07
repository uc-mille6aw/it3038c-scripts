#!/bin/bash
# This script downloads covid data and displays it

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
TODAY=$(date)
NEGATIVE=$(echo $DATA | jq '.[0].negative')
PENDING=$(echo $DATA | jq '.[0].pending')
TOTALTESTRESULTS=$(echo $DATA | jq '.[0].totalTestResults')

echo "On $TODAY, there were $POSITIVE positive COVID cases, $NEGATIVE negative Covid cases, $PENDING pending cases, and $TOTALTESTRESULTS total test results."
