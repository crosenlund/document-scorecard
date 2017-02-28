var _ = require('lodash');

module.exports = FeedbackService;

/**
 *
 * @constructor
 */
function FeedbackService() {

    var _this = this;

    var _containers = {};

    /**
     * Store reference to a container.
     *
     * @param {string} id
     * @param {ng.element} $element
     */
    this.registerContainer = function (id, $element) {
        _containers[id] = $element;
    };

    /**
     * Return container element by id
     *
     * @param {string} id
     * @returns {ng.element}
     */
    this.getContainer = function (id) {
        return _containers[id];
    };

    /**
     * Append a message element to a specific container
     *
     * @param {ng.element} msg
     * @param {string} id
     */
    this.sendMsgToContainer = function(msg, id) {
        var container = _this.getContainer(id);
        if (container) {
            container.append(msg);
        }
    };

    /**
     * Clear messages from a single container
     *
     * @param {string} id
     */
    this.clearContainer = function(id) {
        var container = _this.getContainer(id);
        if (container) {
            container[0].api.closeAll();
        }
    };

    /**
     * Clear messages from all containers
     */
    this.clearAllContainers = function () {
        _.forEach(_containers, function (container) {
            container[0].api.closeAll();
        });
    };

}
