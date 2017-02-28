var urlUtils = require('webui-core/utils/url');
var injector = require('./token.injector');

module.exports = TokenServiceProvider;

TokenServiceProvider.$inject = ['$httpProvider'];

function TokenServiceProvider($httpProvider) {

    var _injectAuthHeader = false;

    // Attach the HTTP Header Token Injector onto the $httpProvider.
    // Whether or not the header is actually attached to the request
    // is determined at the time of the request.

    $httpProvider.interceptors.push(injector);

    /**
     * Configuration option for the TokenService.
     *
     * If true, it sets the header AUTHORIZATION: 'Bearer {token}' on
     * every $http request.  This can be useful if the user is making
     * many calls to SPS APIs that require the user token.
     *
     * If false, it does not set the header by default.
     *
     * Defaults to false.
     *
     * @param {Boolean} val
     */
    this.injectAuthHeader = function(val) {
        _injectAuthHeader = Boolean(val);
    };

    this.$get = ['$window', function ($window) {

        /**
         * TokenService provides a way for users to gain access to the
         * user access token as passed from Commerce Platform. It tries
         * to capture the token immediately on module bootstrap, but
         * provides a public capture() method in case the token does
         * come later.
         *
         * @constructor
         */
        function TokenService() {

            var _this = this;

            this.token = '';

            Object.defineProperties(this, {
                injectAuthHeader: {
                    get: function(){
                        return _injectAuthHeader;
                    }
                }
            });

            /**
             * Capture the User Access Token out of a url. If no URL is
             * specified, then use the $window.location.href.
             *
             * @param {String} [url]
             * @returns {String}
             */
            this.capture = function(url) {
                var tokenKey = 'access_token';
                url = url || $window.location.href;
                _this.token = urlUtils.getParams(url)[tokenKey] || '';
                return _this.token;
            };

            this.capture();

        }

        return new TokenService();
    }];
}



