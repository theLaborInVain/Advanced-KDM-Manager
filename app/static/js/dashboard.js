app.controller("dashboardController", function($scope) {

    $scope.ui = {
        showLoadingVeil: true,
        showProfileModal: false,
    };

    $scope.ui.showLoadingVeil = false;

    $scope.loadUserDashboard = function() {
        // gets the user dashboard from the API, sets it to $scope.user.dashboard

	    console.time($scope.api_url + "user/dashboard/" + $scope.user_id);
        $scope.apiGET('user/dashboard/' + $scope.user_id).then(
            function successCallback(response) {
                $scope.user.dashboard = response.data.dashboard;
                console.timeEnd($scope.api_url + "user/dashboard/" + $scope.user_id);
            }, function errorCallback(response) {
                console.error(response);
                console.timeEnd($scope.api_url + "user/dashboard/" + $scope.user_id);
            }
        );


    };

}) // dashboardController
