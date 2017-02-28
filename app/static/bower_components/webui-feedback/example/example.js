var angular = require('angular');
var feedback = require('../source/index');

module.exports = angular
    .module('ExampleApp', [feedback.name])
    .controller('FactoryExample', FactoryExample);

FactoryExample.$inject = ['$element', 'FeedbackFactory', 'FeedbackService'];

function FactoryExample($element, FeedbackFactory, FeedbackService) {

    var _types = ['success', 'warning', 'error', 'info'];

    this.growl = false;

    this.selected = {
        label: '',
        text: 'This is an example message',
        type: 'random',
        icon: true,
        flash: false,
        closeable: true
    };

    /**
     * Using the settings chosen by the user in the form, create
     * a new message using the FeedbackFactory and append the
     * message element to our container.
     */
    this.addMessage = function() {

        var opts = angular.copy(this.selected);

        if (opts.type === 'random') {
            opts.type = _types[Math.floor(Math.random() * _types.length)];
        }

        if (!opts.icon) { opts.noicon = true; }
        delete opts.icon; // icon is only set to override defaults

        var container = (this.growl) ? 'myGrowler' : 'myMessages';

        FeedbackFactory.newMessage(opts.text, opts).api.sendTo(container);

    };

    /**
     * Just add a simple success message via the factory
     */
    this.addSuccess = function() {

        var msg = 'Congratulations, you generated a success message!';
        FeedbackFactory.success(msg).api.sendTo('myMessages');

    };

    /**
     * Clear all messages from all containers
     */
    this.clearMessages = function() {
        FeedbackService.clearAllContainers();
    }
}
