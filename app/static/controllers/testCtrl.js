angular.module("myApp").controller("testCtrl", testCtrl);

testCtrl.$inject = ["$scope", "scenariosFactory", "feedbackService", "$uibModal"];
function testCtrl($scope, scenariosFactory, feedbackService, $uibModal) {
    //initiate local variables for tableCtrl
    $scope.scenarios = [];
    $scope.selectedScenario = [];
    $scope.scenariosTestList = [];
    $scope.scenarioFilter = {filter: ''};
    $scope.fileUploaded = false;
    $scope.reverse = true;
    $scope.fd = new FormData();
    $scope.menuOpen = '';

    //hide buttons and columns for this view
    $scope.hideRemove = true;
    $scope.hideCopy = true;
    $scope.hideEdit = true;
    $scope.hideAddField = true;
    $scope.hideAddGroup = true;
    $scope.hideRightSearch = true;
    $scope.hideCreate = true;
    $scope.hideSchema = true;
    $scope.hideFieldsView = true;
    $scope.hideFieldsTable = true;
    $scope.hideFieldsTextarea = true;
    $scope.hideCheckBox = true;

    //Initially loads the table of scenarios
    scenariosFactory.getScenarioList().success(function (data) {
        $scope.scenarios = data;
        console.log(data);

    });

    $scope.openModal = function () {
        var modalInstance = $uibModal.open({
            templateUrl: "views/modals/fileuploadModal.tpl.html?bust=" + Math.random().toString(36).slice(2),
            controller: 'modalCtrl',
            resolve: {
                scenario: function () {
                    return '';
                }, action: function () {
                    return '';
                }, schemas: function () {
                    return '';
                }
            }
        })
            .result.then(function (result) { //this happens when the modal is closed, not dismissed
                angular.forEach(result.file, function (file) {
                    $scope.fd.append('file', file);
                    $scope.fileUploaded = true;
                });
            });
    };

    $scope.compareAndDownload = function (validateData, validateSchema) {
        //add list of scenarios in the testList for the db call
        console.log($scope.scenariosTestList);
        var jsonData = (JSON.stringify({
            testList: $scope.testList,
            validateData: validateData,
            validateSchema: validateSchema
        }));
        $scope.fd.append("data", jsonData);

        scenariosFactory.compareAndDownload($scope.fd).success(function (data, status, headers, config) {
            console.log(headers);
            var blob = new Blob([data], {type: "attachment;charset=utf-8"});
            console.log(headers("Content-Disposition"));
            var fileDownload = angular.element('<a></a>');
            var fileName = headers("Content-Disposition").split(';')[1].trim().split('=')[1];
            fileName = fileName.replace(/"/g, '');
            fileDownload.attr('href', window.URL.createObjectURL(blob));
            fileDownload.attr('download', fileName);
            fileDownload[0].click();

            // we have to clear this data after the test is run so old data is not used next time
            $scope.fd = new FormData();
            $scope.fileUploaded = false;
        });
    };

    $scope.downloadScenario = function (scenario) {
        var scenarioName = (JSON.stringify({
            name: scenario.name,
            id: scenario.scenId,
            schema: scenario.schema
        }));
        scenariosFactory.downloadScenario(scenarioName).success(function (data) {
            var blob = new Blob([data], {type: "attachment;charset=utf-8"});
            var fileDownload = angular.element('<a></a>');
            // var fileName = data.fileName;
            fileDownload.attr('href', window.URL.createObjectURL(blob));
            fileDownload.attr('download', scenario.name + '.txt');
            fileDownload[0].click();
        });
    };

    //sets column filters for the scenario table
    $scope.checkSort = function (column) {
        if (column == $scope.sortColumn) {
            $scope.reverse = !$scope.reverse;
        } else if (column != $scope.sortColumn) {
            $scope.sortColumn = column;
            $scope.reverse = true;
        }
    };

    //track selected scenario row and get list of fields to build field table from
    $scope.setSelectedScenario = function (scen) {
        if ($scope.selectedScenario.name != scen.name) {
            $scope.selectedScenario.isChecked = false; //remove old checkbox
            $scope.selectedScenario = scen;
            $scope.selectedScenario.isChecked = true; //add new checkbox
        } else {//row is unselected so empty selectedScenario and remove checkbox check
            $scope.selectedScenario = [];
            scen.isChecked = false;
        }
    };

    //track which items menu button is open - only one should be open at a time
    $scope.openMenu = function (name) {
        if ($scope.menuOpen != name) {
            $scope.menuOpen = name;
        } else {//menuOpen == name, so close the menu without opening another
            $scope.menuOpen = '';
        }
    };

    $scope.addToList = function (scenario) {
        //make sure a scenario is selected
        if (scenario != null) {
            //check if the selected scenario is already in the test list, if not add to it. If it is then ignore
            if (!$scope.scenariosTestList.some(function (e) {
                    return e.name == scenario.name
                })) {
                //add the selected scenario to the scenario test list, automatically updates the table
                $scope.scenariosTestList.push(scenario);
            }
            $scope.updateTestList();
        }
    };

    //removed the selected scenario in the test list by finding its position in the array and splicing it out
    $scope.removedFromList = function (scenario) {
        var position = -1;
        //find position of selected scenario in the array, if present
        $scope.scenariosTestList.some(function (entry, i) {
            if (entry.name == scenario.name) {
                position = i;
            }
        });
        //if selected scenario is present in array, remove it
        if (position != -1) {
            $scope.scenariosTestList.splice(position, 1);
        }
        $scope.updateTestList();
    };

    $scope.updateTestList = function () {
        var stringList = '';
        $scope.testList = '';
        $scope.scenariosTestList.some(function (entry, i) {
            if (stringList == '') {//prevent a leading comma
                stringList = entry.name;
            } else {//already a value in stringList
                stringList = stringList + "," + entry.name;
            }
        });
        $scope.testList = stringList;
    }
}
