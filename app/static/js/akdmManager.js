var app = angular.module('akdmManager', ['ngAnimate']);

app.controller("rootController", function($scope, $http) {

    $scope.ui = {
        showLoadingVeil: true
    };


    $scope.apiGET = function(endpoint) {
        // returns a promise!

        var req_url = $scope.api_url + endpoint;

        var req = {
            method: 'GET',
            url: $scope.api_url + endpoint,
            headers: {
                'Content-Type': undefined
                },
            data: { test: 'test' }
        }

        return $http(req)

    };

    $scope.initAPI = function(url, port) {
//        console.warn("API: " + api_url + ":" + api_port);

        // build the root scope API url based on input vars
        var api_url = url;
        if (port === parseInt(port, 10)) {
            api_url = url + ":" + port
        };

        $scope.api_url = "https://" + api_url + "/"
        
        // now
        console.time("initAPI");
        $scope.apiGET("stat").then(
            function successCallback(response) {
                $scope.api = response.data.meta.api;
                $scope.api.url = $scope.api_url;
                $scope.api.port = port;
                console.log("API version " + $scope.api.version + " responding at " + $scope.api.url);
                console.timeEnd("initAPI")
            }, function errorCallback(response) {
                console.error('GET ' + req_url);
                console.error(response);
                console.timeEnd("initAPI");
                return undefined;
            }
        );
    };



}) // rootController


