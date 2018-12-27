#!/usr/bin/env bash

DEV_API_URL=192.168.0.110
DEV_API_PORT=8013

#
#   This is how we spin up the virtual environment for the server to run in
#

start_venv() {
    echo -e "\nVirtual Envrionment:"

    # 1.) start the generic venv of the app
    source venv/bin/activate

    # 2.) export env variables for our server
    export FLASK_ENV=$1
    export API_URL=$2
    export API_PORT=$3

    # 3.) confirm to the CLI for the user
    PYTHON_PATH=`which python`
    PYTHON_VERS=`python --version`
    echo -e " * $PYTHON_PATH"
    echo -e " * Python $PYTHON_VERS"
    echo -e " * FLASK_ENV=$FLASK_ENV"
    echo -e " * API_URL=$API_URL"
    echo -e "\nPIP:"
    pip freeze $1 | while read x; do echo -e " * $x"; done
    echo -e
    echo -e "Flask server:"
}


#
#   Process CLI args
#

case "$1" in
    dev)
        start_venv development $DEV_API_URL $DEV_API_PORT
#        flask run --host=0.0.0.0 --port=8015
        python akdm.py
        ;;
#    start)
#        start_service
#   unicorn --certfile cert.pem --keyfile key.pem -b 0.0.0.0:8000 hello:app
#        ;;
#    stop)
#        stop_service
#        ;;
#    restart)
#        stop_service
#        start_service
#        ;;
#    status)
#        $CMD status $SERVICE
#        $CMD status $SOCKET
#        ;;
    *)
        echo "Usage: $NAME {dev|prod}" >&2
        exit 3
esac

