var _ = require('lodash');
var moment = require('moment');
require('moment-timezone');

var filters = require('./datetime.filters');
var locales = require('./datetime.locales');

moment.locale('en', {
    longDateFormat : {
        LT: 'h:mm A',
        LTS: 'h:mm:ss A',
        L: 'MM/DD/YYYY',
        LL: 'MMMM D, YYYY',
        LLL: 'MMMM D, YYYY @ LT',
        LLLL: 'dddd MMMM D, YYYY @ LT'
    }
});

module.exports = DateTimeFilter;

DateTimeFilter.$inject = ['$log', 'currentUser'];

function DateTimeFilter($log, currentUser) {

    return function(input, filter, relative) {

        var mmnt;
        var format = filters[filter];
        var locale = _.get(currentUser, 'preferences.locale') || 'en';
        var timezone = _.get(currentUser, 'preferences.timezone') || moment.tz.guess();

        if (!format) {
            $log.warn('Unknown spsuiDate filter format:', format);
            return input;
        }

        if (!locales[locale]) {
            $log.warn('Unknown spsuiDate filter locale:', locale);
            return input;
        }

        if (input instanceof moment) {
            mmnt = input.tz(timezone);
        } else if (input instanceof Date) {
            mmnt = moment.tz(input, timezone);
        } else if (typeof input === 'string') {
            mmnt = moment.tz(new Date(input), timezone);
        }

        if (!mmnt || !mmnt.isValid()) {
            $log.warn('Date passed to spsuiDate filter is invalid:', input);
            return input;
        } else {
            mmnt.locale(locale);
            moment.locale(locale);
        }

        // According to the rules outlined by the design team,
        // relative dates should only be displayed if the date
        // is within ±7 days.  Otherwise render the fallback
        // date format.

        if (relative) {
            var diff = Math.abs(moment().diff(mmnt, 'd', true));
            if (diff <= 7) {
                return moment().to(mmnt);
            }
        }

        return mmnt.format(format);

    };
}
