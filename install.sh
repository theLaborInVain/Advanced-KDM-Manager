#!/bin/bash

INSTALL_DIR=`pwd`
PRODUCTION_PORT=8015


#
#   DO NOT execute this file directly; always source it!
#


#
#   first, set up the virtual env
#

python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
deactivate


#
#   write the akdm-manager.nginx.conf file
#

NGINX="deploy/akdm-manager.nginx.conf"
LOC_STUB1="\tlocation / {\n\t\tproxy_set_header\tX-Real-IP $remote_addr;\n\t\tproxy_set_header\tHost\t$http_host;\n\t\tproxy_pass\thttp://127.0.0.1:$PRODUCTION_PORT;\n\t}"

# start the file from the stub; cat the root location
cp deploy/nginx_stub $NGINX
echo -e $LOC_STUB1 >> $NGINX

# now write the media dir location
echo -e "\n\tlocation /static {" >> $NGINX
echo -e "\t\troot\t$INSTALL_DIR/app/static;" >> $NGINX
echo -e "\t\tautoindex\ton;" >> $NGINX
echo -e "\t}" >> $NGINX

# close the whole file
echo -e "}" >> $NGINX


#
#   write the supervisor files
#

# akdm-manager.supervisor.conf

# supervisor start.sh
START="deploy/start.sh"
echo -e "#!/bin/bash\n" > $START
echo "pushd $INSTALL_DIR" >> $START
echo -e "source venv/bin/activate\nexport FLASK_ENV=production\nexport API_URL=api.thewatcher.io" >> $START
echo -e "$INSTALL_DIR/venv/bin/gunicorn -b localhost:8015 -w 4 app:akdm" >> $START


# finally, root needs to:
# 1.) make a symlink in /etc/supervisor/conf.d/ to the akdm-manager.supervisor.conf file
# 2.) make a symlink in /etc/nginx/conf.d/sites-enabled to the akdm-manager.nginx.conf file
