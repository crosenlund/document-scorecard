//This controller is used for modifying attributes and the XML Helper functions
angular.module('myApp').controller('xmlHelperCtrl', ['$scope', '$modalInstance', '$state',
    function ($scope, $modalInstance, $state) {

        $scope.modifyAttributes = function () {
            $modalInstance.close({score: $scope.xmlHelper.score, file: $scope.files});
        };

        $scope.cancelModal = function () {
            $modalInstance.dismiss();
        };
    }
]);
