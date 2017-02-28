/**
 * Created by aivakhnenko on 12/31/2015.
 */
(function () {
    'use strict';

    var angular = require('angular');

    require('angular-ui-router');
    require('angular-foundation');
    require('./page-nav.min.css!');

    var service = require('./page-nav.service');
    var directive = require('./page-nav.directive');

    var ngDependecies = [
        'mm.foundation.offcanvas',
        'ui.router'
    ];

    module.exports = angular.module('spsui.pagenav', ngDependecies)
        .directive('spsuiPageNav', directive)
        .factory('pageNavService', service);


})();
