
var angular = require('angular');

require('angular-ui-router');
require('./decorators/ui-sref/ui-sref');

var compApplication = require('./components/application/application');
var compPageTitle = require('./components/pagetitle/pagetitle');
var compPageNav = require('./components/page-nav/page-nav');
var compViewPort = require('./components/viewport/viewport');
var compSidebar = require('./components/sidebar/sidebar');
var compFooter = require('./components/footer/footer');

var setupFoundation = require('./setup/foundation');
var setupRedirectTo = require('./setup/redirectTo');
var setupDeepLinking = require('./setup/deepLinking');
var setupOptionalSlash = require('./setup/optionalSlash');

var utilsForm = require('./utils/form');

var postMessage = require('./services/postMessage/postMessage');
var commercePlatform = require('./services/commercePlatform/commercePlatform');

module.exports = angular.module('webui-core', [
    require('./modules/token'),
    require('./modules/identity'),
    require('./modules/currentUser'),
    compApplication.name,
    compPageTitle.name,
    compPageNav.name,
    compViewPort.name,
    compSidebar.name,
    compFooter.name,
    utilsForm.name,
    'ui.router'
]).service('postMessage', postMessage)
  .service('commercePlatform', commercePlatform)
  .config(setupOptionalSlash)
  .run(setupDeepLinking)
  .run(setupFoundation)
  .run(setupRedirectTo);


