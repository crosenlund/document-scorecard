var buildtools = require('webui-buildtools');

var paths = buildtools.defaults.paths;

var gulp = buildtools.gulp(require('gulp'), {
    // Custom Gulp config can go here

    bundler: {
        builder: {
            globalDeps: {
                'github:SPSCommerce/webui-core@2.2.2.js': 'window.sps.webuiCore'
            }
        }
    }

});
