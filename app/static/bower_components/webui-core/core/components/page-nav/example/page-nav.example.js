var angular = require('angular');

require('/core/all');

var DemoController = require('./page-nav.example.ctrl');

module.exports = angular
    .module('PageNavExample', ['webui-core'])
    .config(function ($stateProvider) {
        $stateProvider
            .state('overview', {
                url: '/',
                templateUrl: 'views/overview.html',
                data: {
                    title: 'Overview'
                }
            })
            .state('dashboard', {
                url: '/dashboard/',
                templateUrl: 'views/dashboard.html',
                controller: 'PageNavExampleCtrl',
                controllerAs: 'ctrl'
            })
            .state('favorites', {
                url: '/favorites/',
                templateUrl: 'views/favorites.html',
                data: {
                    title: 'Favorites'
                }
            })
            .state('people', {
                url: '/people/',
                templateUrl: 'views/people.html',
                data: {
                    title: 'People'
                }
            })
            .state('applications', {
                url: '/applications/',
                templateUrl: 'views/applications.html',
                data: {
                    title: 'Applications'
                }
            });

    })
    .run(['$state', function ($state) {
        $state.transitionTo('overview');
    }])
    .controller('PageNavExampleCtrl', DemoController);
