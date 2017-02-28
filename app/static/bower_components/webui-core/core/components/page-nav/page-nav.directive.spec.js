/**
 * Created by aivakhnenko on 2/15/2016.
 */
(function () {
    'use strict';

    require('test/harness');
    require('./page-nav');

    var $ = require('jquery');

    describe('components/page-nav/page-nav.js', function () {

        var $rootScope, compile, element, pageNavService, $scope, items;

        beforeEach(angular.mock.module('spsui.pagenav'));

        beforeEach(inject(function(_$rootScope_, _$compile_, _pageNavService_) {
            compile = _$compile_;
            pageNavService = _pageNavService_;
            $rootScope = _$rootScope_;
            items = [
                { state: 'app.overview', name: 'Overview' },
                { state: 'app.transactions', name: 'Transactions' },
                { state: 'app.intelligence', name: 'Intelligence' },
                { url: 'http://www.google.com', name: 'Google' }]
        }));

        describe('directive tests', function () {

            beforeEach(function () {
                $scope = $rootScope.$new();
                $scope.itemsObject = items;

                var html = '<div><spsui-page-nav items="itemsObject" title="Sample Application" logo-image-url="application-logo.svg" title-state="dashboard"></spsui-page-nav></div>';
                element = compile(html)($scope).find('spsui-page-nav');
                $scope.$digest();
            });

            it('should populate nav items in controller collection', function () {
                expect(element.isolateScope().vm.items.length).toEqual(4);
                expect(element.isolateScope().vm.items).toEqual(items);
            });

            it('should generate navigation items for each item in object', function() {
                expect(element.find('ul.page-nav-items li').length).toBe(4);
            });

            it('should populate application title from attributes', function () {
                expect(element.isolateScope().vm.title).toEqual('Sample Application');
            });

            it('should populate application logo css from attributes', function () {
                expect(element.isolateScope().vm.logoImageUrl).toEqual('application-logo.svg');
                expect(element.find('h1 a').attr('style')).toMatch(/application-logo\.svg/);
            });

            it('should populate application-logo css class when logo-image-url attribute specified', function () {
                expect(element.find('h1 a').hasClass('application-logo')).toBeTruthy();
            });

            it('should populate default application state from attributes', function () {
                expect(element.isolateScope().vm.titleState).toEqual('dashboard');
                expect(element.find('h1 a').attr('ui-sref')).toBe('dashboard');
            });

            it('should populate default application state from first state if not specified in title-state attribute', function () {
                var html = '<div><spsui-page-nav items="itemsObject" title="Sample Application" logo-image-url="application-logo.svg"></spsui-page-nav></div>';
                element = compile(html)($scope).find('spsui-page-nav');
                $scope.$digest();

                expect(element.isolateScope().vm.titleState).toEqual('app.overview');
                expect(element.find('h1 a').attr('ui-sref')).toBe('app.overview');
            });

            it('should populate menu item with absolute url if specified', function () {
                expect(element.find('ul.page-nav-items li a').eq(3).attr('href')).toBe('http://www.google.com');
            });
        });
    });
})();
