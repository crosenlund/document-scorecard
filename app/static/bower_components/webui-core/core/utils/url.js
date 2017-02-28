var _ = require('lodash');

module.exports = {

    /**
     * Simple function for getting query string parameters from javascript.
     * Optionally provide a url to search (defaults to current url)
     *
     * @param name
     * @param url
     * @returns {String}
     */
    getParameterByName: function getParameterByName(name, url) {

        if (url === null) {
            url = window.location.search;
        }

        name = name.replace(/[\[]/, '\\\[').replace(/[\]]/, '\\\]');
        var regexS = '[\\?&]' + name + '=([^&#]*)';
        var regex = new RegExp(regexS);
        var results = regex.exec(url);
        if (results === null) {
            return '';
        }
        return decodeURIComponent(results[1].replace(/\+/g, ' '));
    },

    /**
     * Return object of all the URL search query params. No regex, compact.
     *
     * Solution taken from:
     * http://www.timetler.com/2013/11/14/location-search-split-one-liner/
     *
     * @returns {Object}
     */
    getParams: function getParams(url) {
        url = url || window.location.href;
        var parts = this.parseUrl(url).search.slice(1).split('&');
        var map = _.map(parts, function (item) { if (item) { return item.split('='); } });
        return _.object(_.compact(map));
    },

    /**
     * Given two urls, returns true if they have the same host and protocol
     *
     * @param url1
     * @param url2
     * @returns {boolean}
     */
    hostAndProtocolMatch: function hostAndProtocolMatch(url1, url2) {
        var a = this.parseUrl(url1);
        var b = this.parseUrl(url2);
        return (a.host === b.host && a.protocol === b.protocol);
    },

    /**
     * Parse a url so that its components can be accessed individually
     * from http://stackoverflow.com/questions/6644654/
     *
     * @param url
     * @returns {Element}
     */
    parseUrl: function parseUrl(url) {
        var a = document.createElement('a');
        a.href = url;
        return a;
    },

    /**
     * Add a query parameter to a url, or change it if it already exists
     * from http://stackoverflow.com/questions/5999118/
     *
     * @param url
     * @param key
     * @param val
     * @returns {string}
     */
    updateQueryString: function updateQueryString(url, key, val) {

        url = url || window.location.href;

        var query = [];
        var parts = this.parseUrl(url);
        var params = this.getParams(url);

        var host = parts.origin;
        var path = parts.pathname;
        var hash = parts.hash;

        _.set(params, key, val);
        if (val === null) { delete params[key]; }

        _.each(params, function(key, val) {
            query.push(key + '=' + val);
        });

        query = query.join('&');

        return host + path + ((query) ? '?' + query : '') + hash;
    }
};







