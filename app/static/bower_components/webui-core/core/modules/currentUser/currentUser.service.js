
module.exports = CurrentUser;

CurrentUser.$inject = ['$q', 'tokenService', 'identityService'];

function CurrentUser($q, tokenService, identityService) {

    var _this = this;

    var _ready = $q.defer();

    /**
     * Returns promise that is resolved when the current user
     * details have been loaded and the object is ready for use.
     *
     * @returns Promise - resolved when env is set
     */
    this.whenReady = function() {
        return _ready.promise;
    };

    /**
     * Resolve the ready promise, used internally when whoami()
     * completes. Can also be resolved externally if needed.
     */
    this.ready = function () {
        _ready.resolve();
    };

    /**
     * User details as retrieved from Identity. This is populated during
     * the currentUser.whoami() method call.
     *
     * @type {Object}
     */
    this.details = {};

    /**
     * User access token, populated when WebUI-Core is bootstrapped
     * and an access token is provided from Commerce Platform.
     *
     * @type {String}
     */
    this.token = tokenService.token;

    /**
     * User preferences, not automatically populated from anything,
     * instead just placeholders for future settings.
     *
     * @type {Object}
     */
    this.preferences = {
        locale: '',
        timezone: ''
    };

    /**
     * Convenience method for making an Identity call to check the current user's
     * token. The results of the whoami call are then used to populate the current
     * user's details.
     *
     * @returns {Promise}
     */
    this.whoami = function () {
        return identityService.whoami(_this.token).then(function (userDetails) {
            _this.details = userDetails;
            _this.ready();
            return userDetails;
        });
    };

}
