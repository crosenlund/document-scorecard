// http://plnkr.co/edit/ybYmHtFavHnN1oD8vsuw?p=preview
// http://stackoverflow.com/questions/14574365/angularjs-dropdown-directive-hide-when-clicking-outside

angular.module("myApp").directive('closeMenu', ['$document', function ($document) {
    return {
        restrict: 'E',
        require: '?ngModel',
        scope: {
            choices: '=',
            selected: '='
        },
        templateUrl: 'select.html',
        replace: true,
        link: function (scope, element, attr) {

            scope.isPopupVisible = false;

            scope.toggleSelect = function () {
                scope.isPopupVisible = !scope.isPopupVisible;
            }

            $document.bind('click', function (event) {
                var isClickedElementChildOfPopup = element
                        .find(event.target)
                        .length > 0;

                if (isClickedElementChildOfPopup)
                    return;

                scope.isPopupVisible = false;
                scope.$apply();
            });
        }
    };
}]);
