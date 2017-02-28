var angular = require('angular');
var moment = require('moment');
require('moment-timezone');

module.exports = angular
    .module('dateTimeExample', [
        require('webui-core').name,
        require('webui-core/modules/datetime').name
    ])
    .controller('AppController', AppController);

AppController.$inject = ['$interval', '$scope', '$timeout', 'currentUser'];

function AppController($interval, $scope, $timeout, currentUser) {

    var _this = this;
    var _filters = require('../datetime.filters');
    var _locales = require('../datetime.locales');

    this.date = new Date('02/29/2016 3:03:50 PM CST');
    this.filters = _filters;
    this.locales = _locales;
    this.userPrefs = currentUser.preferences;
    this.timezones = moment.tz.names();
    this.relative = _relativeDates();

    /**
     * Toggling the user preferences isn't cause for re-rendering the
     * filters. This is a brute force means of forcing the tables to
     * re-render.  In the wild this won't be necessary because the
     * user preferences will be in a separate page/view.
     */
    this.refreshDates = function () {
        _this.date = new Date('02/29/2016 3:03:50 PM CST');
        $timeout(function() {
            _this.filters = [];
            _this.relative = [];
        });
        $timeout(function() {
            _this.filters = _filters;
            _this.relative = _relativeDates();
        });
    };

    function _relativeDates() {
        return [
            moment().add(3, 'm'),
            moment().add(3, 'h'),
            moment().add(3, 'd'),
            moment().add(1, 'M'),
            moment().subtract(10, 'm'),
            moment().subtract(12, 'h'),
            moment().subtract(6, 'd'),
            moment().subtract(2, 'M')
        ];
    }

}
