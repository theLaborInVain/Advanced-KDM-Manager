from app import akdm, routes, models

if __name__ == '__main__':
    akdm.run(host="0.0.0.0", port=8015, ssl_context='adhoc')
