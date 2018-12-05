CMD="flask run"

case "$1" in
    dev)
        source venv/bin/activate
        export FLASK_ENV=development
        $CMD --host=0.0.0.0 --port=8015
        ;;
#    disable)
#        stop_service
#        $CMD disable $SERVICE
#        $CMD disable $SOCKET
#        ;;
#    start)
#        start_service
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
        echo "Usage: $NAME {dev|restart}" >&2
        exit 3
esac

flask run
