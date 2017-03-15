//This controller is used for scenario and esp modals so variable 'scenario' will pass the groups and fields to manipulate as well
angular.module('myApp').controller('modalCtrl', ['$scope', '$modalInstance', '$filter', '$state', 'scenario', 'action', 'schemas',
    function ($scope, $modalInstance, $filter, $state, scenario, action, schemas) {
        $scope.newScenario = angular.copy(scenario);
        $scope.scenario = scenario;
        $scope.schemas = schemas;
        //holds the options for the drop down menus
        $scope.allData = [
            {id: 810, docType: '810', rootName: 'Invoice'},
            {id: 846, docType: '846', rootName: 'ItemRegistry'},
            {id: 850, docType: '850', rootName: 'Order'},
            {id: 855, docType: '855', rootName: 'OrderAck'},
            {id: 856, docType: '856', rootName: 'Shipment'},
            {id: 860, docType: '860', rootName: 'OrderChange'},
            {id: 0, docType: 'Other', rootName: ''}
        ];
        // when editing a scenario, set the docType drop down to existing docType

        //an empty set to create the one line to use for the 'allData' set
        $scope.data = [
            {id: 1, docType: '', rootName: ''}
        ];
        if ($scope.newScenario.doctype) {
            $scope.data = $filter("filter")($scope.allData, {docType: $scope.newScenario.doctype});
        }

        $scope.fulfillmentTypeOptions = ['Bulk Import', 'Cross Dock', 'Drop Ship', 'Multi Store', 'Multiple', 'Vendor Managed Inventory'];

        console.log(schemas);
        console.log($scope.scenario);

        $scope.closeModal = function () {
            if ($scope.newScenario.data) {
                $scope.newScenario.doctype = $scope.newScenario.data.docType;
            }
            $modalInstance.close({scenario: $scope.newScenario, file: $scope.files, action: action});
        };

        $scope.cancelModal = function () {
            $modalInstance.dismiss();
        };

    }
]);
