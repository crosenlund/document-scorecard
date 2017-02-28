
var controller = require('./message.ctrl');
var template = require('./message.tmpl.html!text');

module.exports = function () {
    return {
        scope: {},
        restrict: 'E',
        transclude: true,
        template: template,
        controllerAs: 'ctrl',
        controller: controller
    };
};
