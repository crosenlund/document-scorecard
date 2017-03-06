angular.module("myApp").factory('xmlHelperFactory', ['$http', function ($http) {

    return {
        modifyAttributes: function (data) {
            return $http.post("modify_attributes", data,
                {
                    headers: {
                        'Content-Type': undefined
                    }
                }
            )
        }
    };
}]);
