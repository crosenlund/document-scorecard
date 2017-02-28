var items = [
    {state: 'overview', name: 'Overview'},
    {state: 'dashboard', name: 'Dashboard'},
    {state: 'favorites', name: 'Favorites'},
    {state: 'people', name: 'People'},
    {url: 'http://www.google.com', name: 'Google'}
];

module.exports = PageNavExample;

PageNavExample.$inject = ['pageNavService'];

function PageNavExample(pageNavService) {

    /*jshint validthis:true */
    var vm = this;

    vm.navItems = items;

    vm.addItem = function (item) {

        pageNavService.addItem(item);

        vm.item = null;
    };

    vm.removeItem = pageNavService.removeItem;
}
