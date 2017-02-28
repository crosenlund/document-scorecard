/**
 * Created by aivakhnenko on 12/31/2015.
 */
(function () {
    'use strict';

    var angular = require('angular');

    module.exports = function pageNavService() {

        /*jshint validthis:true */
        var vm = this;

        vm.items = [];

        return {
            setItems: setItems,
            addItem: addItem,
            removeItem: removeItem
        };

        function setItems(items) {
            if (!items) {
                throw new Error('navigation items collection should be specified');
            }

            return (vm.items = items);
        }

        function addItem(value) {

            if (!value) {
                throw new Error('navigation menu item should be specified in order added to navigation');
            }

            if (angular.isArray(value)) {
                angular.forEach(value, function (item) {
                    vm.items.push(item);
                });
            } else {
                vm.items.push(value);
            }
        }

        function removeItem(value) {

            if (!value && value !== 0) {
                throw new Error('item index or actual navigation menu item should be specified in order to be deleted');
            }

            var index = -1;

            if (angular.isNumber(value)) {
                if (vm.items.length <= value || value < 0) {
                    throw new Error('item index out of menu items collection range');
                }

                index = value;
            } else {
                for (var i = 0, count = vm.items.length; i < count; i++) {
                    if ((value.state && value.state === vm.items[i].state) || (value.url && value.url === vm.items[i].url)) {
                        index = i;
                        break;
                    }
                }
            }

            if (index === -1) {
                throw new Error('unable to find specified item in menu items collection');
            }

            vm.items.splice(value, 1);
        }
    };

})();
