require('test/harness');
require('./identity.module');
var Provider = require('./identity.service.provider');

describe('modules/identity/identity.service', function () {

    var $http;
    var $injector;
    var $httpBackend;

    var service;
    var provider;

    var envs = {
        dev: 'https://dev.id.spsc.io/identity/',
        test: 'https://test.id.spsc.io/identity/',
        stage: 'https://stage.id.spsc.io/identity/',
        prod: 'https://id.spsc.io/identity/',
    };

    afterEach(function () {
        service = null;
        provider = null;
    });

    beforeEach(function(){

        angular.mock.module(function ($provide) {
            $provide.value('commercePlatform', require('webui-core/services/commercePlatform/commercePlatform.mock'));
        });

        angular.mock.module('spsui.identity', function(identityServiceProvider){
            provider = identityServiceProvider;
        });

        inject(function (_$http_, _$httpBackend_, _$injector_) {
            $http = _$http_;
            $injector = _$injector_;
            $httpBackend = _$httpBackend_;
        });
    });


    function getService() {
        service = $injector.get('identityService');
        return service;
    }

    describe('provider', function () {

        it('should have getEnv()', function () {
            expect(provider).toHaveMethod('getEnv');
        });

        it('should have setEnv()', function () {
            expect(provider).toHaveMethod('setEnv');
        });

        it('should have getUrl()', function () {
            expect(provider).toHaveMethod('getUrl');
        });

        it('should have setUrl()', function () {
            expect(provider).toHaveMethod('setUrl');
        });

        it('should default to prod', function () {
            var result = provider.getEnv();
            expect(result).toBe('prod');
        });

        it('should setEnv to dev', function(){
            var result = provider.setEnv('dev');
            expect(provider.getEnv()).toBe('dev');
            expect(provider.getUrl()).toBe(envs.dev);
            expect(result).toBe(envs.dev);
        });

        it('should setEnv to test', function(){
            var result = provider.setEnv('test');
            expect(provider.getEnv()).toBe('test');
            expect(provider.getUrl()).toBe(envs.test);
            expect(result).toBe(envs.test);
        });

        it('should setEnv to stage', function(){
            var result = provider.setEnv('stage');
            expect(provider.getEnv()).toBe('stage');
            expect(provider.getUrl()).toBe(envs.stage);
            expect(result).toBe(envs.stage);
        });

        it('should setEnv to prod', function(){
            var result = provider.setEnv('prod');
            expect(provider.getEnv()).toBe('prod');
            expect(provider.getUrl()).toBe(envs.prod);
            expect(result).toBe(envs.prod);
        });

        it('should not change env if invalid', function(){
            var result = provider.setEnv('foo');
            expect(provider.getEnv()).toBe('prod');
            expect(provider.getUrl()).toBe(envs.prod);
            expect(result).toBeFalse();
        });

        it('should setUrl correctly', function(){
            var url = 'http://foo.com/bar';
            var result = provider.setUrl(url);
            expect(provider.getEnv()).toBe('');
            expect(provider.getUrl()).toBe(url);
            expect(result).toBe(url);
        });

    });

    describe('identityService', function () {

        beforeEach(function(){
            service = $injector.get('identityService');
        })

        it('should have getEnv()', function () {
            expect(service).toHaveMethod('getEnv');
        });

        it('should have setEnv()', function () {
            expect(service).toHaveMethod('setEnv');
        });

        it('should have getUrl()', function () {
            expect(service).toHaveMethod('getUrl');
        });

        it('should have setUrl()', function () {
            expect(service).toHaveMethod('setUrl');
        });

        it('should have get()', function () {
            expect(service).toHaveMethod('get');
        });

        it('should have delete()', function () {
            expect(service).toHaveMethod('delete');
        });

        it('should have head()', function () {
            expect(service).toHaveMethod('head');
        });

        it('should have post()', function () {
            expect(service).toHaveMethod('post');
        });

        it('should have put()', function () {
            expect(service).toHaveMethod('put');
        });

        it('should have patch()', function () {
            expect(service).toHaveMethod('patch');
        });

        it('should have whoami()', function () {
            expect(service).toHaveMethod('whoami');
        });

        it('should useToken with $http.get()', function(done){
            service.setEnv('dev');
            var url = envs.dev + 'foobar';
            $httpBackend.expect('GET', url).respond(200, {});
            service.get('foobar').then(function(response){
                expect(response.config).toHaveTrue('useToken');
                done();
            });
            $httpBackend.flush();
        });

        it('should useToken with $http.delete()', function(done){
            service.setEnv('dev');
            var url = envs.dev + 'foobar';
            $httpBackend.expect('DELETE', url).respond(200, {});
            service.delete('foobar').then(function(response){
                expect(response.config).toHaveTrue('useToken');
                done();
            });
            $httpBackend.flush();
        });

        it('should useToken with $http.head()', function(done){
            service.setEnv('dev');
            var url = envs.dev + 'foobar';
            $httpBackend.expect('HEAD', url).respond(200, {});
            service.head('foobar').then(function(response){
                expect(response.config).toHaveTrue('useToken');
                done();
            });
            $httpBackend.flush();
        });

        it('should useToken with $http.post()', function(done){
            service.setEnv('dev');
            var url = envs.dev + 'foobar';
            $httpBackend.expect('POST', url).respond(200, {});
            service.post('foobar').then(function(response){
                expect(response.config).toHaveTrue('useToken');
                done();
            });
            $httpBackend.flush();
        });

        it('should useToken with $http.put()', function(done){
            service.setEnv('dev');
            var url = envs.dev + 'foobar';
            $httpBackend.expect('PUT', url).respond(200, {});
            service.put('foobar').then(function(response){
                expect(response.config).toHaveTrue('useToken');
                done();
            });
            $httpBackend.flush();
        });

        it('should useToken with $http.patch()', function(done){
            service.setEnv('dev');
            var url = envs.dev + 'foobar';
            $httpBackend.expect('PATCH', url).respond(200, {});
            service.patch('foobar').then(function(response){
                expect(response.config).toHaveTrue('useToken');
                done();
            });
            $httpBackend.flush();
        });

        it('should return response.data from whoami()', function(done){
            service.setEnv('dev');
            var url = envs.dev + 'users/me/';
            $httpBackend.expect('GET', url).respond(200, {foo: 1});
            service.whoami().then(function(response){
                expect(response).toHaveMember('foo');
                done();
            });
            $httpBackend.flush();
        });

    });

});
