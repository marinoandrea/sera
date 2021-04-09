#!/bin/bash
source .env
lftp -u $VOXEO_USER,$VOXEO_PASSWORD -e "cd www/$VOXEO_APP; mput *.xml; cd en; mput en/*.xml; cd audio; mput en/audio/*.wav; cd ../../fr; mput fr/*.xml; cd audio; mput fr/audio/*.wav; quit" ftp.voxeo.net
