// We're using Jasmine-matchers to expand our set of expect() methods.
// See: https://github.com/JamieMason/Jasmine-Matchers#available-matchers

module.exports = function (config) {
    config.set({

        port: 9876,

        basePath: './',

        colors: true,

        autoWatch: true,

        singleRun: false,

        browsers: ['PhantomJS'],

        frameworks: ['jspm', 'jasmine'],

        reporters: ['spec', 'html', 'coverage'],

        // possible values:
        // config.LOG_DISABLE ||
        // config.LOG_ERROR ||
        // config.LOG_WARN ||
        // config.LOG_INFO ||
        // config.LOG_DEBUG
        logLevel: config.LOG_DISABLE,

        plugins: [
            'karma-jspm',
            'karma-jasmine',
            'karma-coverage',
            'karma-chrome-launcher',
            'karma-phantomjs-launcher',
            'karma-jasmine-matchers',
            'karma-html-reporter',
            'karma-mocha-reporter',
            'karma-spec-reporter'
        ],

        files: [

            // These files are included before SystemJS loader is available,
            // so don't expect anything in here to be able to use require().

        ],

        exclude: [
            'docs/**/*',
            'test/reports/*'
        ],

        preprocessors: {
            'core/**/!(*spec|*mock).js': 'coverage'
        },

        specReporter: {
            maxLogLines: 1,
            suppressSkipped: true
        },

        mochaReporter: {
            ignoreSkipped: true
        },

        htmlReporter: {
            outputDir: 'test/reports/results',
            foldAll: true,
            namedFiles: true,
            urlFriendlyName: true,
            focusOnFailures: true,
            preserveDescribeNesting: false
        },

        coverageReporter: {
            dir: 'test/reports/',
            reporters: [
                {type: 'html', subdir: 'coverage'}, // Human readable
                {type: 'cobertura', subdir: '.', file: 'cobertura.xml'} // Jenkins
            ]
        },

        jspm: {
            useBundles: false,
            loadFiles: [
                'core/**/*.spec.js'
            ],
            serveFiles: [
                'jspm_packages/**/*',
                'config.js',
                'test/*.js',
                'core/**/*'
            ]
        },

        proxies: {
            '/jspm_packages/': '/base/jspm_packages/',
            '/config.js': '/base/config.js',
            '/test/': '/base/test/',
            '/core/': '/base/core/'
        }

    });
};
