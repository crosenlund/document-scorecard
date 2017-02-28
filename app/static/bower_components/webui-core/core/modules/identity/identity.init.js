
module.exports = IdentityInit;

IdentityInit.$inject = [
    'commercePlatform',
    'identityService'
];

/**
 * Setup Identity service to use the same environment as the current
 * version of Commerce Platform. User access tokens only work in the
 * environment that they were issued. We can safely assume that if the
 * application is being run from dev.commerce.spscommerce.com that the
 * Identity environment that issued the token is dev.
 *
 * Fun fact, if the application is not running in Commerce Platform,
 * the promise won't ever resolve and the Identity environment won't
 * be set. This allows local devs to set which env of identity to use.
 *
 * @param commercePlatform
 * @param identityService
 * @constructor
 */
function IdentityInit(commercePlatform, identityService) {

    commercePlatform.getEnvironment().then(function(env) {
        identityService.setEnv(env);
        identityService.ready();
    });

}
