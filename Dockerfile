###
# To manually start your image:
# Make sure you create the folders suites, scrips and reports
# docker run --rm -ti --network=host -v "$PWD/output:/output" -v "$PWD/suites:/suites" -v "$PWD/scripts:/scripts" -v "$PWD/reports:/reports"  robot  bash
#
# Or using docer-compose (see listing below):
# docker-compose up
# docker-compose down
###

FROM python:3.6

LABEL name="Docker build"

MAINTAINER "cuong.buiviet"

RUN apt-get update \
    && apt-get install -y xvfb wget ca-certificates fonts-liberation libasound2 libatk-bridge2.0-0 libatk1.0-0 \
       libatspi2.0-0 libcups2 libdbus-1-3 libgbm1 libgtk-3-0 libnspr4 libnss3 \
       libxcomposite1 libxkbcommon0 libxrandr2 xdg-utils ntpdate openssl

RUN python3 -m pip install --upgrade pip

COPY requirements.txt /tmp/requirements.txt
RUN  pip3 install -r /tmp/requirements.txt


CMD ["/scripts/run.sh"]