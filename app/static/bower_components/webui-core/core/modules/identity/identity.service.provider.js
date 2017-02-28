var _ = require('lodash');

module.exports = IdentityServiceProvider;

function IdentityServiceProvider() {

    var _prot = 'https://';
    var _base = 'id.spsc.io/identity/';

    var _envs = {
        dev: _prot + 'dev.' + _base,
        test: _prot + 'test.' + _base,
        stage: _prot + 'stage.' + _base,
        prod: _prot + _base
    };

    var _env = _envs.prod;

    /**
     * Publicize _getEnv().
     * @type {_getEnv}
     */
    this.getEnv = _getEnv;

    /**
     * Publicize _setEnv().
     * @type {_setEnv}
     */
    this.setEnv = _setEnv;

    /**
     * Publicize _getUrl().
     * @type {_getUrl}
     */
    this.getUrl = _getUrl;

    /**
     * Publicize _setUrl().
     * @type {_setUrl}
     */
    this.setUrl = _setUrl;

    /**
     * Fetch the current environment name.
     *
     * @returns {String|False}
     * @private
     */
    function _getEnv() {
        return _.invert(_envs)[_env] || '';
    }

    /**
     * During the config phase the user can select which Identity
     * environment they want to use for this session. Returns the
     * resulting server address if the value was valid, or false
     * if option is not valid.
     *
     * Options: dev | test | stage | prod
     * Returns: https://dev.id.spsc.io/identity/
     *          https://test.id.spsc.io/identity/
     *          https://stage.id.spsc.io/identity/
     *          https://id.spsc.io/identity/
     *
     * @param {String} env
     * @returns {String|Boolean}
     */
    function _setEnv(env) {
        if (_envs[env]) {
            _env = String(_envs[env]);
            return _env;
        }
        return false;
    }

    /**
     * Fetch the current environment url.
     *
     * @returns {String}
     * @private
     */
    function _getUrl() {
        return _env;
    }

    /**
     * During the config phase, the user can set which Identity server
     * they want to use by passing in the entire URL. No validation is
     * done on the URL, assume that the user knows what they are doing.
     * Returns the value that was passed in.
     *
     * @param {String} url
     * @returns {String}
     */
    function _setUrl(url) {
        _env = String(url);
        return _env;
    }

    /**
     * Factory for the service provider.
     */
    this.$get = ['$q', '$http', function ($q, $http) {

        /**
         * IdentityService
         *
         * @constructor
         */
        function IdentityService() {

            var _this = this;

            var _ready = $q.defer();

            /**
             * Returns promise that is resolved when the Identity
             * environment is set and the API is ready to use.
             * 
             * @returns Promise - resolved when env is set
             */
            this.whenReady = function () {
                return _ready.promise;
            };

            /**
             * Externally resolve the ready promise. This is used
             * when the Identity env is set from auto-detection of
             * the Commerce Platform environment.
             */
            this.ready = function() {
                _ready.resolve();
            };

            /**
             * Allow user to get env during run phase.
             * @type {_getEnv}
             */
            _this.getEnv = _getEnv;

            /**
             * Allow user to set env during run phase.
             * @type {_setEnv}
             */
            _this.setEnv = _setEnv;

            /**
             * Allow user to get url during run phase.
             * @type {_getUrl}
             */
            _this.getUrl = _getUrl;

            /**
             * Allow user to set url during run phase.
             * @type {_setUrl}
             */
            _this.setUrl = _setUrl;

            /**
             * HTTP GET request to Identity.
             *
             * @param {String} path
             * @param {Object} [config]
             * @returns {Promise}
             */
            _this.get = function (path, config) {
                return $http.get(_url(path), _config(config));
            };

            /**
             * HTTP DELETE request to Identity.
             *
             * @param {String} path
             * @param {Object} [config]
             * @returns {Promise}
             */
            _this.delete = function (path, config) {
                return $http.delete(_url(path), _config(config));
            };

            /**
             * HTTP HEAD request to Identity.
             *
             * @param {String} path
             * @param {Object} [config]
             * @returns {Promise}
             */
            _this.head = function (path, config) {
                return $http.head(_url(path), _config(config));
            };

            /**
             * HTTP POST request to Identity.
             *
             * @param {String} path
             * @param {Object} [data]
             * @param {Object} [config]
             * @returns {Promise}
             */
            _this.post = function (path, data, config) {
                return $http.post(_url(path), data, _config(config));
            };

            /**
             * HTTP PUT request to Identity.
             *
             * @param {String} path
             * @param {Object} [data]
             * @param {Object} [config]
             * @returns {Promise}
             */
            _this.put = function (path, data, config) {
                return $http.put(_url(path), data, _config(config));
            };

            /**
             * HTTP PATCH request to Identity.
             *
             * @param {String} path
             * @param {Object} [data]
             * @param {Object} [config]
             * @returns {Promise}
             */
            _this.patch = function (path, data, config) {
                return $http.patch(_url(path), data, _config(config));
            };

            /**
             * GET request for fetching the user details of a given token.
             *
             * @emits spsui.identity.whoami
             * @param {String} token
             * @returns {Promise}
             */
            _this.whoami = function (token) {
                return _this.get('users/me/', {
                    params: {access_token: token}
                }).then(function (response) {
                    return response.data;
                });
            };

            /**
             * Generate the Identity URL based upon the current environment
             * selection and any path variable passed in.
             *
             * @param {String} path
             * @returns {String}
             * @private
             */
            function _url(path) {
                return String(_env) + String(path);
            }

            /**
             * Extend the user's config to make sure that they are always
             * sending Identity their token in the Authorization header.
             *
             * @param config
             * @returns {Object}
             * @private
             */
            function _config(config) {
                config = config || {};
                config.useToken = true;
                return config;
            }

        }

        return new IdentityService();
    }];
}



