angular.module("myApp").controller("scenariosCtrl", scenariosCtrl);

scenariosCtrl.$inject = ["$scope", "scenariosFactory", "groupsFactory", "fieldsFactory", "schemasFactory", "feedbackService", "$uibModal"];
function scenariosCtrl($scope, scenariosFactory, groupsFactory, fieldsFactory, schemasFactory, feedbackService, $uibModal) {
    //initiate local variables for tableCtrl
    $scope.scenarios = [];
    $scope.currentScenario = [];
    $scope.selectedScenario = [];
    $scope.scenarioFilter = {filter: ''};
    $scope.fieldFilter = {filter: ''};
    $scope.reverse = false;
    $scope.closeRoot = false;
    $scope.expandedGroup = true;
    $scope.notEqual = false;
    $scope.menuOpen = '';

    //hide buttons and columns for this view
    $scope.hideTestButton = true;
    $scope.hideUpload = true;
    $scope.hideAddTest = true;
    $scope.hideTestTable = true;
    $scope.hideFieldsView = false;
    $scope.hideFieldsViewWindow = true;
    $scope.hideFieldsTextarea = true;
    $scope.hideExpandCollapse = true;
    $scope.expandAll = false;

    //Initially loads the table of scenarios
    scenariosFactory.getScenarioList().success(function (data) {
        $scope.scenarios = data;
    });


    schemasFactory.getSchemaList().success(function (data) {
        $scope.schemas = data;
    });

    //opens the scenario, group, and field modal windows and performs the confirmed action when it closes
    $scope.openModal = function (action, scenario) {
        var template = "";
        if (action == 'delete') {
            template = "views/modals/deleteScenarioModal.tpl.html?bust=" + Math.random().toString(36).slice(2);
        } else if (action == 'edit') {
            template = "views/modals/editScenarioModal.tpl.html?bust=" + Math.random().toString(36).slice(2);
        } else if (action == 'copy') {
            template = "views/modals/copyScenarioModal.tpl.html?bust=" + Math.random().toString(36).slice(2);
        } else if (action == 'create') {
            template = "views/modals/createScenarioModal.tpl.html?bust=" + Math.random().toString(36).slice(2);
        } else if (action == 'addGroup') {
            template = "views/modals/addGroupModal.tpl.html?bust=" + Math.random().toString(36).slice(2);
        } else if (action == 'editGroup') {
            template = "views/modals/editGroupModal.tpl.html?bust=" + Math.random().toString(36).slice(2);
        } else if (action == 'removeGroup') {
            template = "views/modals/removeGroupModal.tpl.html?bust=" + Math.random().toString(36).slice(2);
        } else if (action == 'addField') {
            template = "views/modals/addFieldModal.tpl.html?bust=" + Math.random().toString(36).slice(2);
        } else if (action == 'editField') {
            template = "views/modals/editFieldModal.tpl.html?bust=" + Math.random().toString(36).slice(2);
        } else if (action == 'removeField') {
            template = "views/modals/removeFieldModal.tpl.html?bust=" + Math.random().toString(36).slice(2);
        }

        if (template != "") {
            $uibModal.open({
                templateUrl: template,
                controller: 'modalCtrl',
                resolve: {
                    scenario: function () {
                        return scenario;
                    }, action: function () {
                        return action;
                    }, schemas: function () {
                        return $scope.schemas;
                    }
                }
            })
                .result.then(function (result) { //this happens when the modal is closed, not dismissed
                console.log(result.scenario);
                console.log($scope.selectedScenario.name);
                var jsonData = '';
                if (action.indexOf('Group') > -1) { //limits the jsonData being sent when performing an action for a group
                    jsonData = (JSON.stringify({
                        //----------SCENARIO-------------------------------
                        name: result.scenario.name,
                        scenID: result.scenario.scenId,
                        scenID2: $scope.selectedScenario.scenId, // this will be used to return any new json data to repopulate the scenario tree
                        //----------GROUP----------------------------------
                        groupName: result.scenario.groupName,
                        newGroupName: result.scenario.newGroupName,
                        groupID: result.scenario.groupId
                    }));
                } else if (action.indexOf('Field') > -1) { //limits the jsonData being sent when performing an action for a field
                    jsonData = (JSON.stringify({
                        //----------SCENARIO-------------------------------
                        scenID: result.scenario.scenId,
                        scenID2: $scope.selectedScenario.scenId,
                        //----------GROUP----------------------------------
                        groupName: result.scenario.groupName,
                        newGroupName: result.scenario.newGroupName,
                        groupID: result.scenario.groupId,
                        //----------FIELD----------------------------------
                        fieldName: result.scenario.name,
                        score: result.scenario.score,
                        data: result.scenario.data,
                        fieldID: result.scenario.fieldId,
                        notEqual: result.scenario.notEqual
                    }));
                } else { // gives all data in the jsonData object
                    jsonData = (JSON.stringify({
                        //----------SCENARIO-------------------------------
                        name: result.scenario.name,
                        schema: result.scenario.schema,
                        description: result.scenario.description,
                        docType: result.scenario.doctype,
                        fulfillmentType: result.scenario.fulfillmenttype,
                        rootName: result.scenario.rootname,
                        scenName: result.scenario.name,
                        oldScenName: $scope.selectedScenario.name,
                        oldRootName: $scope.selectedScenario.rootname,
                        oldSchema: $scope.selectedScenario.schema,
                        oldDescription: $scope.selectedScenario.description,
                        oldDocType: $scope.selectedScenario.doctype,
                        oldFulfillmentType: $scope.selectedScenario.fulfillmenttype,
                        scenID: result.scenario.scenId,
                        scenID2: $scope.selectedScenario.scenId
                    }));
                }

                //------------------------SCENARIOS-----------------------------------------
                if (result.action == 'copy') {
                    scenariosFactory.copyScenario(jsonData).success(function (data) {
                        $scope.scenarios = data;
                        feedbackService.addMessage('Scenario successfully copied', '200');
                    })
                        .error(function (result, status) {
                            feedbackService.addMessage(result, status);
                            console.log('error code: ' + status + '-' + result);
                        });
                } else if (result.action == 'edit') {
                    scenariosFactory.editScenario(jsonData).success(function (data) {
                        $scope.scenarios = data;
                        feedbackService.addMessage('Scenario successfully edited', '200');
                    })
                        .error(function (result, status) {
                            feedbackService.addMessage(result, status);
                            console.log('error code: ' + status + '-' + result);
                        });
                } else if (result.action == 'create') {
                    if (result.file == null) {
                        scenariosFactory.createScenario(jsonData).success(function (data) {
                            $scope.scenarios = data;
                            feedbackService.addMessage('A new empty scenario was created', '200');
                        })
                            .error(function (result, status) {
                                feedbackService.addMessage(result, status);
                                console.log('error code: ' + status + '-' + result);
                            });
                    } else {
                        var fd = new FormData();
                        angular.forEach(result.file, function (file) {
                            fd.append('file', file);
                        });
                        fd.append("data", jsonData);

                        scenariosFactory.createScenarioFromFile(fd).success(function (data) {
                            console.log(data);
                            $scope.scenarios = data;
                            feedbackService.addMessage('New scenario was created from the uploaded file', '200');
                        })
                            .error(function (result, status) {
                                feedbackService.addMessage(result, status);
                                console.log('error code: ' + status + '-' + result);
                            });
                    }
                } else if (result.action == 'delete') {
                    scenariosFactory.deleteScenario(jsonData).success(function (data) {
                        $scope.scenarios = data;
                        // empty fields table so it doesn't still show the deleted scenario
                        $scope.selectedScenario = '';
                        $scope.groups = '';
                        $scope.fields = '';
                        feedbackService.addMessage('Scenario successfully deleted', '200');
                    })
                        .error(function (result, status) {
                            feedbackService.addMessage(result, status);
                            console.log('error code: ' + status + '-' + result);
                        });
                }
                //------------------------GROUPS-----------------------------------------
                else if (result.action == 'addGroup') {
                    groupsFactory.addGroup(jsonData).success(function (data) {
                        $scope.currentScenario = data;
                        feedbackService.addMessage('Field successfully added', '200');
                    })
                        .error(function (result, status) {
                            feedbackService.addMessage(result, status);
                            console.log('error code: ' + status + '-' + result);
                        });
                } else if (result.action == 'editGroup') {
                    groupsFactory.editGroup(jsonData).success(function (data) {
                        $scope.currentScenario = data;
                        feedbackService.addMessage('Field successfully edited', '200');
                    })
                        .error(function (result, status) {
                            feedbackService.addMessage(result, status);
                            console.log('error code: ' + status + '-' + result);
                        });
                } else if (result.action == 'removeGroup') {
                    groupsFactory.removeGroup(jsonData).success(function (data) {
                        $scope.currentScenario = data;
                        feedbackService.addMessage('Field successfully removed', '200');
                    })
                        .error(function (result, status) {
                            feedbackService.addMessage(result, status);
                            console.log('error code: ' + status + '-' + result);
                        });
                }
                //------------------------FIELDS-----------------------------------------
                else if (result.action == 'addField') {
                    fieldsFactory.addField(jsonData).success(function (data) {
                        $scope.currentScenario = data;
                        feedbackService.addMessage('Field successfully added', '200');
                    })
                        .error(function (result, status) {
                            feedbackService.addMessage(result, status);
                            console.log('error code: ' + status + '-' + result);
                        });
                } else if (result.action == 'editField') {
                    fieldsFactory.editField(jsonData).success(function (data) {
                        $scope.currentScenario = data;
                        feedbackService.addMessage('Field successfully edited', '200');
                    })
                        .error(function (result, status) {
                            feedbackService.addMessage(result, status);
                            console.log('error code: ' + status + '-' + result);
                        });
                } else if (result.action == 'removeField') {
                    fieldsFactory.removeField(jsonData).success(function (data) {
                        $scope.currentScenario = data;
                        feedbackService.addMessage('Field successfully removed', '200');
                    })
                        .error(function (result, status) {
                            feedbackService.addMessage(result, status);
                            console.log('error code: ' + status + '-' + result);
                        });
                }
            });
        }
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

    //track selected scenario row and get list of fields to build fields table from
    $scope.setSelectedScenario = function (scen) {
        if ($scope.selectedScenario.name != scen.name) {
            $scope.selectedScenario.isChecked = false; //remove old checkbox
            $scope.selectedScenario = scen;
            $scope.selectedScenario.isChecked = true; //add new checkbox
        } else {//row is unselected so empty selectedScenario and remove checkbox check
            $scope.selectedScenario = [];
            scen.isChecked = false;
        }

        //get fields to populate fieldsTable
        if ($scope.selectedScenario != null && $scope.selectedScenario.name != null) {
            var jsonData = (JSON.stringify({
                scenID: $scope.selectedScenario.scenId
            }));
            if (!$scope.hideFieldsTable) {
                scenariosFactory.jsonScenario(jsonData).success(function (data) {
                    $scope.currentScenario = data;
                });
            } else if (!$scope.hideFieldsTextarea) {
                scenariosFactory.jsonScenario(jsonData).success(function (data) {
                    $scope.currentScenario = data;
                });
            }
        } else {
            $scope.currentScenario = []; // clears field table if no scenario is selected
        }
        console.log($scope.currentScenario);
    };

    //track which items menu button is open - only one should be open at a time
    $scope.openMenu = function (name) {
        if ($scope.menuOpen != name) {
            $scope.menuOpen = name;
        } else {//menuOpen == name, so close the menu without opening another
            $scope.menuOpen = '';
        }
    };

    //schema functionality--------------------------------------------------
    $scope.openSchemaModal = function () {
        template = "views/modals/schemaModal.tpl.html?bust=" + Math.random().toString(36).slice(2);

        if (template != "") {
            $uibModal.open({
                templateUrl: template,
                controller: 'schemaCtrl',
                resolve: {
                    schemas: function () {
                        return $scope.schemas;
                    }
                }
            }).result.then(function (result) { //this happens when the modal is closed, not dismissed

                if (result.action == 'add') {
                    var jsonData_addSchema = (JSON.stringify({
                        schema: result.schema
                    }));

                    if (result.file != null) {
                        var fd = new FormData();
                        angular.forEach(result.file, function (file) {
                            fd.append('file', file);
                        });
                        fd.append("data", jsonData_addSchema);

                        schemasFactory.addSchema(fd).success(function (data) {
                            $scope.schemas = data;
                            feedbackService.addMessage('Schema ' + result.schema + ' was added', '200');
                        })
                            .error(function (result, status) {
                                feedbackService.addMessage(result, status);
                            });
                    } else {//no file uploaded or other unforeseen error
                        feedbackService.addMessage('Unable to add schema', '400');
                    }
                } else if (result.action == 'delete') {
                    var jsonData_deleteSchema = (JSON.stringify({
                        delete: result.delete
                    }));
                    console.log(result.delete);

                    schemasFactory.deleteSchema(jsonData_deleteSchema).success(function (data) {
                        $scope.schemas = data;
                        feedbackService.addMessage('Schema ' + result.delete + " was successfully delete", '200');
                    })
                        .error(function (result, status) {
                            feedbackService.addMessage(result, status);
                        });
                }
            });
        }
    }
}

