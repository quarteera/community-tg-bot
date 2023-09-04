FROM python:3.10.12 as build

MAINTAINER quarteera

WORKDIR /community-tg-bot

#ENV GROUP_UID $GROUP_UID
#ENV USER_UID $USER_UID
#ENV PIP_NO_CACHE_DIR off
#ENV PIP_DISABLE_PIP_VERSION_CHECK on

COPY ..
RUN pip3 install -r /src/requirements.txt
CMD python3 /src/main.py

#ONBUILD COPY $FOLDER/requirements.txt   /config/
#ONBUILD RUN pip3 install -r /config/requirements.txt