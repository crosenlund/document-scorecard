require('test/harness');
var Service = require('./currentUser.service');

describe('modules/currentUser/currentUser.service', function () {

    var $q;
    var service;
    var $rootScope;
    var $httpBackend;
    var tokenService;
    var identityService;

    afterEach(function () {
        service = null;
    });

    beforeEach(function(){

        angular.mock.module(function ($provide) {
            $provide.value('tokenService', require('webui-core/modules/token/token.service.mock'));
            $provide.value('identityService', require('webui-core/modules/identity/identity.service.mock'));
        });

        inject(function (_$q_, _$rootScope_, _$httpBackend_, _tokenService_, _identityService_) {
            $q = _$q_;
            $rootScope = _$rootScope_;
            $httpBackend = _$httpBackend_;
            tokenService = _tokenService_;
            identityService = _identityService_;
            service = new Service($q, tokenService, identityService);
        });
    });


    it('should have details property', function(){
        expect(service).toHaveObject('details');
    });

    it('should have token property', function(){
        expect(service).toHaveString('token');
    });

    it('should have preferences property', function(){
        expect(service).toHaveObject('preferences');
    });

    it('should have whoami method', function(){
        expect(service).toHaveMethod('whoami');
    });

    it('should pass user token to identityService.whoami()', function() {
        service.token = 'ABC123';
        var spy = spyOn(identityService, 'whoami').and.callThrough();
        service.whoami();
        expect(spy).toHaveBeenCalledWith('ABC123');
    });

    it('should populate details with whoami() results', function(done) {
        var data = {foo: 1, bar: 2};
        service.token = 'ABC123';
        spyOn(identityService, 'whoami').and.returnValue(Promise.resolve(data));
        service.whoami().then(function(details){
            expect(details).toBe(data);
            expect(service.details).toBe(details);
            done();
        });
        $rootScope.$digest();
    });

});
