angular.module("myApp").factory('scenariosFactory', ['$http', function ($http) {

    return {
        getScenarioList: function () {
            return $http.get("get_scenario_list")
        },
        createScenario: function (scenarioData) {
            return $http.post("create_scenario", scenarioData)
        },
        createScenarioFromFile: function (scenarioData) {
            return $http.post("upload_new_scenario", scenarioData, {
                headers: {
                    'Content-Type': undefined
                }
            })
        },
        deleteScenario: function (scenarioData) {
            return $http.post("delete_scenario", scenarioData)
        },
        copyScenario: function (scenarioData) {
            return $http.post("copy_scenario", scenarioData)
        },
        editScenario: function (scenarioData) {
            return $http.post("edit_scenario", scenarioData)
        },
        jsonScenario: function (scenarioData) {
            return $http.post("get_scenario_json", scenarioData)
        },
        downloadScenario: function (scenarioData) {
            return $http.post("get_scenario_xml", scenarioData)
        },
        compareAndDownload: function (scenarioData) {
            return $http.post("compare_download", scenarioData, {
                headers: {
                    'Content-Type': undefined
                }
            })
        }
    };
}]);
