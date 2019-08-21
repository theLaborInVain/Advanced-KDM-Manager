# [https://a.kdm-manager.com](https://a.kdm-manager.com)
* Webapp: [Flask](http://flask.pocoo.org/) + [AngularJS](https://angularjs.org/) (1.754)
* Webserver: [NGINX](https://www.nginx.com/) + [Gunicorn](http://gunicorn.org/)

## Introduction 
[https://a.kdm-manager.com](https://a.kdm-manager.com), also known as Advanced
KDM-Manager, is an Interactive campaign manager for *Monster* by
[Kingdom Death](https://kingdomdeath.com). It replaces Timothy O'Connell's
 [KDM Manager](https://github.com/toconnell/kdm-manager).


**Neither the [https://a.kdm-manager.com](https://a.kdm-manager.com) service nor
any of the software utilized by that service (including the API at 
[https://api.kdm-manager.com](https://api.kdm-manager.com) are developed,
authorized in any other way supported by or affiliated with Kingdom Death or
 Adam Poots Games, LLC.**

Both the Manager and the API are totally independent, fan-maintained projects.

For more information, please refer to
[the 'About' section of the project's development blog](http://kdm-manager.blogspot.com/p/credits-and-acknowledgements.html).



# Setup
**Important!** This is simply a web application. In order to work with user
data you will need a KDM API key.

Install and start an instance of the dev server:

## 1.) Install

First, install base/background dependencies:

    # apt-get -y update
    # apt-get -y install python3 python3-venv python3-dev supervisor nginx git

Then, clone the repo down to your home dir (or wherever) and find the
`install.sh` file in the root of the project directory.

Important! `install.sh` is not executable by default. Do not execute it
directly!

Instead, do this to install the webapp:

    $ source install.sh

## 2.) Add your API key
Create a file in the project root directory called `private.cfg`. Update the file:

    [api]
    key = YOUR_SECRET_API_KEY

The server will run without an API key, though the application will mostly fail
once you start clicking buttons.

Check the documentation for [the KDM API](https://github.com/toconnell/kdm-manager)
for more information on how to setup an API server and make your own key, or how
to get a key to the production instance of the KDM API.

## 3.) Run the dev server
    $ ./server.sh dev
