#!/bin/bash
source .env
lftp -u $VOXEO_USER,$VOXEO_PASSWORD -e "cd www/$VOXEO_APP; mput *.xml; cd en; mput en/*.xml; cd ../fr; mput fr/*.xml; quit" ftp.voxeo.net
