var urlUtils = require('../../utils/url');

module.exports = PlatformService;

PlatformService.$inject = ['$q', '$rootScope', 'postMessage'];

function PlatformService($q, $rootScope, postMessage) {

    var _this = this;

    var _cache = {};

    /**
     * Get the current application URL from Commerce Platform.
     *
     * The first time this is called, the resulting Promise is
     * cached locally. All subsequent calls get the cached Promise
     * unless the refresh param is set to true.
     *
     * Used by ui-sref component.
     *
     * Example:
     *
     * platformService.getAppURL().then(function (url) {
     *      // result something like:
     *      // https://commerce.spscommerce.com/fulfillment
     * });
     *
     * @param {Boolean} refresh
     * @returns {Promise} resolved with URL string
     */
    this.getAppURL = function (refresh) {

        if (_cache.appUrl && !refresh) {
            return _cache.appUrl;
        }

        postMessage.sendToPlatform({type: 'requestCurrentURL'});

        _cache.appUrl = $q(function (resolve, reject) {

            $rootScope.$on('currentURL', function (event, data) {

                if (!data || !data.url) {
                    reject('data.url not specified');
                    return false;
                }

                var url = urlUtils.parseUrl(data.url);
                var host = url.protocol + '//' + url.host;
                var app = url.pathname.split('/')[1];
                var full = host + ((app) ? '/' + app : '');

                resolve(full);
                return true;
            });
        });

        return _cache.appUrl;
    };

    /**
     * Determine which Commerce Platform environment we're currently
     * running in. This parses the current Commerce Platform URL and
     * resolves with a string indicating the current environment.
     *
     * This is used by the Identity Module to determine which env to
     * use when requesting user details via whoami().
     *
     * Possible envs: dev | test | stage | prod | none
     *
     * @returns {Promise} resolved with env string
     */
    this.getEnvironment = function () {

        return _this.getAppURL().then(function(url){

            var host = urlUtils.parseUrl(url).host;
            var env = host.split('.')[0];
            env = (env === 'commerce') ? 'prod' : env;
            return env || 'none';

        });
    };
}
