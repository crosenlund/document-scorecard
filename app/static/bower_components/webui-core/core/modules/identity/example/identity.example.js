var angular = require('angular');

module.exports = angular
    .module('identityExample', [require('webui-core').name])
    .controller('AppController', AppController)
    .config(function (identityServiceProvider) {

        // You can set the identity environment during the config
        // phase using the identityServiceProvider.setEnv() method.

        identityServiceProvider.setEnv('prod');
    });

AppController.$inject = ['$scope', '$http', 'tokenService', 'identityService'];

function AppController($scope, $http, tokenService, identityService) {

    var _this = this;

    this.result = {};
    this.waiting = false;
    this.env = identityService.getEnv();
    this.token = tokenService.token;
    this.setEnv = identityService.setEnv;

    $scope.$watch(function(){

        // This isn't necessary for using Identity Service,
        // it just keeps our form up to date with the env
        // settings as they change.

        return identityService.getEnv();

    }, function(newVal){
        _this.env = newVal;
    });

    this.whoami = function(token) {

        _this.waiting = true;
        _this.result = {};

        identityService.whoami(token).then(function(result) {

            _this.result.success = result;
            console.log(result);

        }).catch(function(err){

            _this.result.error = err;
            console.warn(err);

        }).finally(function(){

            _this.waiting = false;

        });

    };

}
