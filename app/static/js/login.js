app.controller("loginController", function($scope) {

    $scope.scratch = {
        showAboutModal: false,
        showHelpModal: false,
        showLoginFormPanel: true
    };

    $scope.showSignupForm = function() {
        console.warn("showing Signup form!")
    };


    $scope.ui.showLoadingVeil = false;

}) // loginController
