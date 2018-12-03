from app import akdm

@akdm.route('/')
@akdm.route('/index')
def index():
    return "Hello, World!"
