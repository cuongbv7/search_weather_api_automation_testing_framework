#!/usr/bin/env bash

set -e
ENV="dev"


#run parallel test suites by pabot command, process = 2 mean run parallel 2 test suites
CMD="pabot --processes 2 -v env:$ENV -L TRACE  -e ignore --outputdir /reports /testcases/"
echo ${CMD}

``${CMD}``