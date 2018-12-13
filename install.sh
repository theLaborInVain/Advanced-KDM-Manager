#!/bin/bash

INSTALL_DIR=`pwd`
PRODUCTION_PORT=8015


#
#   DO NOT execute this file directly; always source it!
#

#python3 -m venv venv
#source ./venv/bin/activate
#pip install -r requirements.txt
#deactivate


#
#   write the production nginx config
#

NGINX="nginx/production"
LOC_STUB1="\tlocation / {\n\t\tproxy_set_header\tX-Real-IP $remote_addr;\n\t\tproxy_set_header\tHost\t$http_host;\n\t\tproxy_pass\thttp://127.0.0.1:$PRODUCTION_PORT;\n\t}"

# start the file from the stub; cat the root location
cp nginx/stub $NGINX
echo -e $LOC_STUB1 >> $NGINX

# now write the media dir location
echo -e "\n\tlocation /static {" >> $NGINX
echo -e "\t\troot\t$INSTALL_DIR/app/static;" >> $NGINX
echo -e "\t\tautoindex\ton;" >> $NGINX
echo -e "\t}" >> $NGINX

# close the whole file
echo -e "}" >> $NGINX

#cat $NGINX

