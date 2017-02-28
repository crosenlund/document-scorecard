
var controller = require('./container.ctrl');

module.exports = function () {
    return {
        scope: {},
        restrict: 'E',
        transclude: true,
        controllerAs: 'ctrl',
        controller: controller,
        template: '<ng-transclude></ng-transclude>'
    };
};
