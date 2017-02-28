require('test/harness');

var _ = require('lodash');
var Service = require('./postMessage');

describe('services/postMessage.service', function () {

    var service;
    var $window;
    var $timeout;
    var $rootScope;
    var unwatch;

    var mock = {
        target: {
            postMessage: function(){}
        },
        callback: function(){}
    };

    beforeEach(function () {

        inject(function (_$window_, _$timeout_, _$rootScope_) {
            $window = _$window_;
            $timeout = _$timeout_;
            $rootScope = _$rootScope_;
            service = new Service($window, $rootScope);
        });
    });

    afterEach(function() {
        if (typeof unwatch === 'function') {
            unwatch();
        }
    });

    describe('sendMessage', function () {

        it('should ensure that postMessage is a function', function(){
            var result = service.sendMessage({}, {});
            expect(result).toBeFalse();
        });

        it('should JSON.stringify the message data', function(){
            var spy = spyOn(mock.target, 'postMessage').and.callThrough();
            service.sendMessage(mock.target, {type: 'bar'});
            expect(spy).toHaveBeenCalledWith('RUBICON_{"type":"bar"}', '*');
        });
    });

    describe('sendToPlatform', function(){
        it('should sendMessage to parent', function(){
            var msg = {foo: 'bar'};
            var spy = spyOn(service, 'sendMessage');
            service.sendToPlatform(msg);
            expect(spy).toHaveBeenCalledWith(parent, msg);
        });
    });

    describe('sendToIframe', function(){
        it('should sendMessage to iframe', function(){
            var msg = {foo: 'bar'};
            var spy = spyOn(service, 'sendMessage');
            service.sendToIframe(msg);
            expect(spy).toHaveBeenCalledWith($window.frames[0], msg);
        });
    });

    describe('receiveMessage', function(){

        it('should ignore messages not for RUBICON', function(done) {
            var spy = spyOn(mock, 'callback');
            unwatch = $rootScope.$on('bar', spy);
            window.postMessage('FOOBAR_{"type":"bar"}', '*');
            setTimeout(function(){
                expect(spy).not.toHaveBeenCalled();
                done();
            }, 100);
        });

        it('should broadcast rootScope event', function(done){
            var spy = spyOn(mock, 'callback');
            unwatch = $rootScope.$on('bar', spy);
            service.sendMessage(window, {type: 'bar'});
            $rootScope.$digest();
            setTimeout(function(){
                expect(spy).toHaveBeenCalled();
                done();
            }, 100);
        });

        it('should check for message type', function(done){
            var spy = spyOn(mock, 'callback');
            unwatch = $rootScope.$on('bar', spy);
            service.sendMessage(window, {foo: 'bar'});
            $rootScope.$digest();
            setTimeout(function(){
                expect(spy).not.toHaveBeenCalled();
                done();
            }, 100);
        });

        it('should check for message params', function(done){
            var params = {foo: 'bar', baz: 'qux'};
            unwatch = $rootScope.$on('bar', function(event, data){
                expect(data).toEqual(params);
                done();
            });
            service.sendMessage(window, {type: 'bar', params: params});
            $rootScope.$digest();
        });


    });


});
