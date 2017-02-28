var WebFont = require('webfont');

WebFont.load({
    google: {
        families: [
            'Source Code Pro:400,600,700',
            'Source Sans Pro:300,400,600,700,300italic,400italic,600italic,700italic'
        ]
    }
});

require('./css/vendor.min.css!');
require('./css/main.min.css!');
