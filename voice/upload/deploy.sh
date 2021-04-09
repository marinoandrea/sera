#!/bin/bash
source .env

ftp_script="cd www/$VOXEO_APP; put index.xml; rm -rf en; mkdir en; cd en; mput en/*.xml; mkdir audio; cd audio; mput en/audio/*.wav; cd ../..; rm -rf fr; mkdir fr; cd fr; mput fr/*.xml; mkdir audio; cd audio; mput fr/audio/*.wav; quit;"
lftp -u $VOXEO_USER,$VOXEO_PASSWORD -e "$ftp_script" ftp.voxeo.net
