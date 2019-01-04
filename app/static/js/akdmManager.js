var app = angular.module('akdmManager', ['ngAnimate']);

// avoid clashes with jinja2
app.config(['$interpolateProvider', function($interpolateProvider) {
  $interpolateProvider.startSymbol('{a');
    $interpolateProvider.endSymbol('a}');
}]);

app.controller("rootController", function($scope, $http) {

    $scope.cur_date = new Date();

    $scope.ui = {
        showLoadingVeil: true
    };


    $scope.apiGET = function(endpoint, token) {
        // returns a promise!

        var req_url = $scope.api_url + endpoint;

        var req = {
            method: 'GET',
            url: $scope.api_url + endpoint,
            headers: {
                'Content-Type': undefined,
                'Authorization': $scope.access_token
                },
            data: { test: 'test' }
        }

		console.warn(req_url);

        return $http(req)

    };

    $scope.initAPI = function(url) {

        // set it
        $scope.api_url = url;
        
        // get it
        console.time($scope.api_url + 'stat');
        $scope.apiGET("stat").then(
            function successCallback(response) {
                $scope.api = response.data.meta.api;
                $scope.api.url = $scope.api_url;
                console.log("API version " + $scope.api.version + " responding at " + $scope.api.url);
                console.timeEnd($scope.api_url + 'stat')
            }, function errorCallback(response) {
                console.error(response);
                console.timeEnd($scope.api_url + 'stat')
                return undefined;
            }
        );
    };


    $scope.initSession = function(user_id) {
        $scope.user_id = user_id;
        $scope.access_token = getCookie("akdm_token");

        console.time($scope.api_url + "user/get/" + $scope.user_id);
        $scope.apiGET('user/get/' + $scope.user_id).then(
            function successCallback(response) {
                $scope.user = response.data.user;
        		console.timeEnd($scope.api_url + "user/get/" + $scope.user_id);
            }, function errorCallback(response) {
                console.error(response);
        		console.timeEnd($scope.api_url + "user/get/" + $scope.user_id);
            }        
        );


    };

}) // rootController


