module.exports = {

    baseURL: '.',
    dest: 'dist',

    builder: {
        sfx: true,
        minify: true,
        mangle: true,
        sourceMaps: true,
        separateCSS: true,
        lowResSourceMaps: false,

        globalDeps: {
            'lodash': 'window._',
            'jquery': 'window.jQuery',
            'angular': 'window.angular',
            'moment': 'window.moment',
            'moment-timezone': 'window.moment.tz'
        },

        config: {
            meta: {
                angular: {
                    exports: 'window.angular',
                    format: 'global',
                    build: false
                },
                jquery: {
                    exports: 'window.jQuery',
                    format: 'global',
                    build: false
                },
                lodash: {
                    exports: 'window._',
                    format: 'global',
                    build: false
                },
                moment: {
                    exports: 'window.moment',
                    format: 'global',
                    build: false
                },
                'moment-timezone': {
                    exports: 'window.moment.tz',
                    format: 'global',
                    build: false
                }
            }
        }
    },

    bundles: {
        libs: {
            bundle: false,
            items: [
                'angular',
                'jquery',
                'lodash',
                'moment',
                'moment-timezone'
            ]
        },
        core: {
            exclude: ['libs'],
            items: {
                'core/all': 'webui-core'
            }
        },
        modules: {
            exclude: ['libs', 'core'],
            items: {
                'core/modules/datetime': 'webui-datetime',
                'core/modules/intercom': 'webui-intercom'
            },
            builder: {
                separateCSS: false
            }
        }
    }
};
