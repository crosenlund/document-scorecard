/**
 * Created by aivakhnenko on 12/31/2015.
 */
(function () {
    'use strict';

    module.exports = spsuiPageNavDirective;

    spsuiPageNavDirective.$inject = ['pageNavService'];

    function spsuiPageNavDirective(pageNavigationService) {

        return {
            restrict: 'E',
            transclude: true,

            scope: {},

            bindToController: {
                titleState: '@',
                logoImageUrl: '@',
                title: '@',
                items: '='
            },

            link: link,
            controller: controller,
            controllerAs: 'vm',

            template: require('./page-nav.tpl.html!text')
        };

        function link(scope, el, attr) {
            if (attr.logoImageUrl) {
                var applicationTitleLink = el.find('h1 a');
                applicationTitleLink.css('background-image', 'url(' + attr.logoImageUrl + ')');
                applicationTitleLink.addClass('application-logo');
            }
        }

        function controller() {

            /*jshint validthis:true */
            var vm = this;

            if (!vm.titleState && vm.items && vm.items.length > 0) {
                vm.titleState = vm.items[0].state;
            }

            pageNavigationService.setItems(vm.items);
        }
    }
})();
