var app = angular.module('akdmLogin', []);

app.controller("rootController", function($scope) {
    console.warn('rootController initialized!')
}) // rootController

app.controller("loginController", function($scope) {

    $scope.showSignupForm = function() {
        console.warn("showing Signup form!")
    };

    $scope.showLoginForm = function() {
        showHide("loginLoginButton");
        showHide("loginSignupButton");
        showHide("loginLoginFormPanel");
        document.getElementById("username").focus();
    };


}) // loginController
