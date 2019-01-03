var app = angular.module('akdmManager', ['ngAnimate']);

// avoid clashes with jinja2
app.config(['$interpolateProvider', function($interpolateProvider) {
  $interpolateProvider.startSymbol('{a');
    $interpolateProvider.endSymbol('a}');
}]);

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

    $scope.initAPI = function(url) {

        // set it
        $scope.api_url = url;
        
        // get it
        console.time("initAPI");
        $scope.apiGET("stat").then(
            function successCallback(response) {
                $scope.api = response.data.meta.api;
                $scope.api.url = $scope.api_url;
                console.log("API version " + $scope.api.version + " responding at " + $scope.api.url);
                console.timeEnd("initAPI")
            }, function errorCallback(response) {
                console.error(response);
                console.timeEnd("initAPI");
                return undefined;
            }
        );
    };



}) // rootController


