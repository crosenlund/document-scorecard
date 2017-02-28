var _ = require('lodash');
var moment = require('moment');
require('moment-timezone');

window.sps = window.sps || {};

/**
 * DateTime Module provides a date formatting filter that enables
 * consistent, localized date strings based upon user's preferences.
 * This module uses MomentJS and MomentTimezone for date formatting.
 */
window.sps.datetimeModule = require('angular')
    .module('webui-datetime', [])
    .filter('spsuiDate', require('./datetime.filter'))
    .run(DateTimeSetup);

module.exports = window.sps.datetimeModule;

DateTimeSetup.$inject = ['currentUser'];

function DateTimeSetup(currentUser) {

    // @TODO remove this when real user preferences are supported

    _.set(currentUser, 'preferences.locale', 'en');
    _.set(currentUser, 'preferences.timezone', moment.tz.guess());

}
