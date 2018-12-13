app.controller("loginController", function($scope) {

    $scope.ui = {
        showLoadingVeil: true,
        showAboutModal: false,
        showSignupModal: false,
        showHelpModal: false,
    };

    $scope.showSignupForm = function() {
        console.warn("showing Signup form!")
    };


    $scope.ui.showLoadingVeil = false;

}) // loginController
