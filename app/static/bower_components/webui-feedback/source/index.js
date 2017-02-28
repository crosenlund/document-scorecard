
require('webui-core');
require('./style/style.min.css!');

var angular = require('angular');
var factory = require('./factory');
var service = require('./service');
var message = require('./message/message');
var container = require('./container/container');

var webuiFeedback = angular
    .module('webui-feedback', ['webui-core'])
    .service('FeedbackFactory', factory)
    .service('FeedbackService', service)
    .directive('spsuiFeedbackMsg', message)
    .directive('spsuiFeedbackContainer', container);

window.sps = window.sps || {};
window.sps.webuiFeedback = webuiFeedback;

module.exports = webuiFeedback;
