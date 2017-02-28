module.exports = {

    remove: {
        duration: 300
    },

    flash: {
        duration: 5000
    },

    default: 'info', // which type to use if none is specified

    types: {

        info: {
            label: 'FYI:',
            icon: 'fa-info-circle'
        },
        warning: {
            label: 'Warning:',
            icon: 'fa-exclamation-triangle'
        },
        success: {
            label: 'Success:',
            icon: 'fa-check'
        },
        error: {
            label: 'Error:',
            icon: 'fa-exclamation-circle'
        },
        tip: {
            label: 'Pro Tip:',
            icon: 'fa-lightbulb-o'
        }
    }
};
