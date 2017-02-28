module.exports = DeepLinking;

DeepLinking.$inject = [
    '$rootScope',
    '$location',
    'postMessage'
];

function DeepLinking($rootScope, $location, postMessage) {

    // This sends every application state change to the Commerce Platform
    // via PostMessage.  Platform then appends this location to it's own
    // URL to form a nice human readable deeplink.

    $rootScope.$on('$stateChangeSuccess', function () {
        postMessage.sendToPlatform({
            type:'appStateChange',
            params: {
                path: $location.path(),
                search: $location.search()
            }
        });
    });

}
