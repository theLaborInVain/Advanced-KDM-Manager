var app = angular.module('akdmLogin', []);

app.controller("rootController", function($scope) {
    console.warn('rootController initialized!')
}) // rootController

app.controller("loginController", function($scope) {

    $scope.showSignupForm = function() {
        showHide("loginLoginButton");
    };

    $scope.showLoginForm = function() {
        console.warn("showing login form!")
    };


}) // loginController
