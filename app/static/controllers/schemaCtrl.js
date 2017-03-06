//This controller is used for creating and maintaining the tools schemas
angular.module('myApp').controller('schemaCtrl', ['$scope', '$modalInstance', '$state', 'schemas',
    function ($scope, $modalInstance, $state, schemas) {
        // puts the existing schemas into the modal popup
        $scope.schemas = schemas;

        $scope.addSchema = function () {
            $modalInstance.close({
                schema: $scope.schema.docType + "-" + $scope.schema.version,
                file: $scope.files,
                action: 'add'
            });
        };

        $scope.deleteSchema = function () {
            $modalInstance.close({delete: $scope.schema.delete, action: 'delete'});
        };

        $scope.cancelModal = function () {
            $modalInstance.dismiss();
        };
    }
]);
