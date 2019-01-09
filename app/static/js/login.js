app.controller("loginController", function($scope) {

    $scope.ui = {
        showLoadingVeil: true,
        showAboutModal: false,
        showSignupModal: false,
        showHelpModal: false,
        showResetPasswordPanel: true,
        showResetPasswordLoader: false,
        showResetPasswordReset: false,
        showCloseResetPasswordButton: true,
    };

	$scope.reset_pw = {};
    $scope.resetPassword = function() {

		var endpoint = 'reset_password/request_code'
        data = {
            'username': $scope.reset_pw.email,
            'app_url': 'https://a.kdm-manager.com/reset_password'
        }

        console.time($scope.api_url + endpoint);
        $scope.apiPOST(endpoint, data).then(
            function successCallback(response) {
				$scope.ui.showCloseResetPasswordButton = false;
				$scope.ui.showResetPasswordLoader = false;
				$scope.ui.showResetPasswordResult = true;
                $scope.reset_pw.response = response;
                $scope.reset_pw.response.data = 'Email sent! Please close this window and follow the instructions in the email to complete your password reset!'
                console.timeEnd($scope.api_url + endpoint)
            }, function errorCallback(response) {
				$scope.ui.showResetPasswordLoader = false;
				$scope.ui.showResetPasswordResult = true;
				$scope.ui.showResetPasswordReset = true;
                console.error(response);
				$scope.reset_pw.response = response
                console.timeEnd($scope.api_url + endpoint)
            }
        );

    };

    $scope.resetPasswordForm = function () {
        $scope.reset_pw.email = undefined; 
    	$scope.ui.showResetPasswordPanel = true;
    	$scope.ui.showResetPasswordResult = false;
		$scope.ui.showResetPasswordReset = false;
    }



    $scope.ui.showLoadingVeil = false;

}) // loginController
