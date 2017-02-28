require('test/harness');

var _ = require('lodash');
var Service = require('./commercePlatform');

describe('services/commercePlatform.service', function () {

    var $q;
    var service;
    var $rootScope;
    var postMessage;

    beforeEach(function () {

        angular.mock.module(function ($provide) {
            $provide.value('postMessage', require('../postMessage/postMessage.mock'));
        });

        inject(function (_$q_, _$rootScope_, _postMessage_) {
            $q = _$q_;
            $rootScope = _$rootScope_;
            postMessage = _postMessage_;
            service = new Service($q, $rootScope, postMessage);
        });
    });


    describe('getAppURL', function () {

        it('should return a promise', function () {
            var result = service.getAppURL();
            expect(result).toHaveMethod('then');
        });

        it('should immediately cache the promise', function () {
            var result1 = service.getAppURL();
            result1.uid = _.uniqueId();
            var result2 = service.getAppURL();
            expect(result1).toEqual(result2);
        });

        it('should return new promise when refreshed', function () {
            var result1 = service.getAppURL();
            result1.uid = _.uniqueId();
            var result2 = service.getAppURL(true);
            expect(result1).not.toEqual(result2);
        });

        it('should resolve promise on emit currentURL', function (done) {
            service.getAppURL().then(function (appURL) {
                expect(appURL).toBeString();
                done();
            });
            $rootScope.$emit('currentURL', {url: 'https://foo.com/bar/123/?a=b&c=d#qaz'});
            $rootScope.$digest();
        });

        it('should parse the URL correctly (1)', function (done) {
            service.getAppURL().then(function (appURL) {
                expect(appURL).toBe('http://foo.com');
                done();
            });
            $rootScope.$emit('currentURL', {url: 'http://foo.com/'});
            $rootScope.$digest();
        });

        it('should parse the URL correctly (2)', function (done) {
            service.getAppURL().then(function (appURL) {
                expect(appURL).toBe('https://foo.com/bar');
                done();
            });
            $rootScope.$emit('currentURL', {url: 'https://foo.com/bar'});
            $rootScope.$digest();
        });

        it('should parse the URL correctly (3)', function (done) {
            service.getAppURL().then(function (appURL) {
                expect(appURL).toBe('https://foo.com/bar');
                done();
            });
            $rootScope.$emit('currentURL', {url: 'https://foo.com/bar/123/?a=b&c=d#qaz'});
            $rootScope.$digest();
        });

        it('should reject promise if URL is not provided', function (done) {
            service.getAppURL().catch(function (err) {
                expect(err).toBeString();
                done();
            });
            $rootScope.$emit('currentURL', false);
            $rootScope.$digest();
        });


    });


});
