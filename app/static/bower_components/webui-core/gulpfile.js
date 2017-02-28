// Use of Gulp Help requires passing Gulp to the
// gulp-help plugin.  This is also where we
// specify the global Gulp Help options.

var gulp = require('gulp-help')(require('gulp'), {
    hideEmpty: true,
    hideDepsMessage: true
});

var sequence = require('run-sequence');

/***********************
 * PATHS
 ***********************/

var root = __dirname + '/';
var core = root + 'core/';
var dist = root + 'dist/';
var docs = root + 'gh-pages/';

var paths = {

    config: {
        npm: root + 'package.json',
        jspm: root + 'jspm_packages/',
        karma: root + 'karma.conf.js',
        system: root + 'config.js',
        bundle: root + 'bundle.config.js'
    },

    core: {
        dist: dist,
        all: core + 'all.js',
        css: core + 'style/css/',
        sass: core + 'style/sass/',
        modules: core + 'modules/',
        components: core + 'components/'
    },

    docs: {
        source: docs + 'source/',
        sass: docs + 'style/sass/',
        css: docs + 'style/css/'
    }
};

/***********************
 * GLOBS
 ***********************/

var globs = {

    core: {
        js: [core + '**/!(*spec).js'],
        md: [
            root + 'ROADMAP.md',
            root + 'CHANGELOG.md',
            root + 'CONTRIBUTING.md',
            core + '**/*.md'],
        sass: {
            main: [

                // Files that are watched and then rebuilt into
                // core.min.css when they are modified.

                paths.core.sass + 'main.scss',
                paths.core.sass + '_settings.scss'
            ],
            comp: [

                // Files that are watched and then rebuilt into
                // their own respective folders when modified.

                paths.core.components + '**/*.scss',
                paths.core.modules + '**/*.scss',
                paths.core.sass + '_settings.scss'
            ],
            vendor: [

                // Files that are watched and then rebuilt into
                // vendor.min.css when they are modified.

                paths.core.sass + 'vendor.scss',
                paths.core.sass + '_settings.scss',
                paths.core.sass + 'vendor/**/*.scss'
            ]
        }
    },

    docs: {
        sass: [paths.docs.sass + '**/*.scss']
    }
};


/***********************
 * MAIN TASKS
 ***********************/

gulp.task('default', ['help']);

gulp.task('clean', 'Remove all static build files.', function (done) {
    sequence(
        'clean-core-dist',
        done
    );
});

gulp.task('build', 'Build Core and documentation from source', function (done) {
    sequence(
        'build-core',
        'build-docs',
        done
    );
});

gulp.task('build-core', function (done) {
    sequence(
        'build-core-main-css',
        'build-core-comp-css',
        'build-core-vendor-css',
        done
    );
});

gulp.task('build-docs', function (done) {
    sequence(
        'build-docs-pages',
        'build-docs-css',
        done
    );
});

gulp.task('dist', 'Prepare core for distribution', function(done) {
    sequence(
        'clean',
        'build-core',
        'bundle',
        done
    );
});

gulp.task('test', 'Lint and unit test Core JS.', function(done) {
    sequence(
        'lint',
        'unit-test',
        done
    );
});

gulp.task('tdd', 'Start TDD server, rebuild, test, lint source files on change.', function (done) {
    sequence(
        'build',
        'build:watch',
        'lint:watch',
        'unit-test:watch',
        'build:server',
        'coverage:server',
        'results:server',
        'tdd:server',
        done
    );
});

gulp.task('server', 'Start simple server, reload source files on change.', function (done) {
    sequence(
        'build',
        'build:watch',
        'build:server',
        done
    );
});


/***********************
 * CLEAN
 ***********************/

gulp.task('clean-core-dist', function () {
    var del = require('del');
    return del([
        paths.core.dist + '*.map',
        paths.core.dist + '*.css',
        paths.core.dist + '*.js',
    ]);
});


/***********************
 * BUILD CORE
 ***********************/

gulp.task('build-core-main-css', function () {

    var sass = require('gulp-sass');
    var rename = require('gulp-rename');
    var minifyCSS = require('gulp-minify-css');
    var sourcemaps = require('gulp-sourcemaps');
    var sassJspm = require('sass-jspm-importer');

    return gulp.src(paths.core.sass + 'main.scss')
        .pipe(sourcemaps.init())
        .pipe(sass({
            errLogToConsole: true,
            includePaths: [paths.core.sass],
            functions: sassJspm.resolve_function(paths.config.jspm),
            importer: sassJspm.importer
        }).on('error', sass.logError))
        .pipe(rename({suffix: '.min'}))
        .pipe(minifyCSS())
        .pipe(sourcemaps.write('./'))
        .pipe(gulp.dest(paths.core.css));
});

gulp.task('build-core-comp-css', function () {

    var sass = require('gulp-sass');
    var rename = require('gulp-rename');
    var minifyCSS = require('gulp-minify-css');
    var sourcemaps = require('gulp-sourcemaps');
    var sassJspm = require('sass-jspm-importer');

    return gulp.src(globs.core.sass.comp, {base: './'})
        .pipe(sourcemaps.init())
        .pipe(sass({
            errLogToConsole: true,
            includePaths: [paths.core.sass],
            functions: sassJspm.resolve_function(paths.config.jspm),
            importer: sassJspm.importer
        }).on('error', sass.logError))
        .pipe(minifyCSS())
        .pipe(rename({suffix: '.min'}))
        .pipe(sourcemaps.write('./'))
        .pipe(gulp.dest('./'));
});

gulp.task('build-core-vendor-css', function () {

    var sass = require('gulp-sass');
    var rename = require('gulp-rename');
    var minifyCSS = require('gulp-minify-css');
    var sourcemaps = require('gulp-sourcemaps');
    var sassJspm = require('sass-jspm-importer');

    return gulp.src(paths.core.sass + 'vendor.scss')
        .pipe(sourcemaps.init())
        .pipe(sass({
            errLogToConsole: true,
            includePaths: [paths.core.sass],
            functions: sassJspm.resolve_function(paths.config.jspm),
            importer: sassJspm.importer
        }).on('error', sass.logError))
        .pipe(rename({suffix: '.min'}))
        .pipe(minifyCSS())
        .pipe(sourcemaps.write('./'))
        .pipe(gulp.dest(paths.core.css));
});


/***********************
 * BUILD DOCS
 ***********************/

gulp.task('build-docs-pages', function() {
    return gulp.src(globs.core.md)
        .pipe(gulp.dest(paths.docs.source));
});

gulp.task('build-docs-css', function () {

    var sass = require('gulp-sass');
    var concat = require('gulp-concat');
    var minifyCSS = require('gulp-minify-css');
    var sourcemaps = require('gulp-sourcemaps');
    var sassJspm = require('sass-jspm-importer');

    return gulp.src(globs.docs.sass)
        .pipe(sourcemaps.init())
        .pipe(sass({
            errLogToConsole: true,
            includePaths: [paths.core.sass],
            functions: sassJspm.resolve_function(paths.config.jspm),
            importer: sassJspm.importer
        }).on('error', sass.logError))
        .pipe(concat('style.min.css'))
        .pipe(minifyCSS())
        .pipe(sourcemaps.write('./'))
        .pipe(gulp.dest(paths.docs.css));
});

/***********************
 * BUNDLE
 ***********************/

gulp.task('bundle', 'Compile static asset bundles, takes optional -g argument', function () {
    var minimist = require('minimist');
    var options = minimist(process.argv.slice(2));
    var config = require(paths.config.bundle);
    var Bundler = require('jspm-bundler');
    var bundler = new Bundler(config);
    return bundler.bundle(options.g).catch(function (e) {
        throw e;
    });
});

gulp.task('unbundle', 'Removes static asset bundles, takes optional -g argument', function () {
    var minimist = require('minimist');
    var options = minimist(process.argv.slice(2));
    var config = require(paths.config.bundle);
    var Bundler = require('jspm-bundler');
    var bundler = new Bundler(config);
    return bundler.unbundle(options.g).catch(function (e) {
        throw e;
    });
});

/***********************
 * LINT
 ***********************/

// Report lint errors, one time run
gulp.task('lint', 'Perform static analysis on JS files', function () {
    var print = require('gulp-print');
    var jshint = require('gulp-jshint');
    return gulp.src(globs.core.js)
        .pipe(jshint())
        .pipe(jshint.reporter('jshint-stylish'))
        .pipe(print(function (filepath) {
            return 'Linted: ' + filepath;
        }));
});

// Report lint errors for watch task
gulp.task('lint:changed', function () {
    var cache = require('gulp-cached');
    var print = require('gulp-print');
    var jshint = require('gulp-jshint');
    return gulp.src(globs.core.js)
        .pipe(cache('linting'))  // Only lint changed or uncached files
        .pipe(jshint())
        .pipe(jshint.reporter('jshint-stylish'))
        .pipe(print(function (filepath) {
            return 'Linted: ' + filepath;
        }));
});

// Continual lint watching using lint:changed
gulp.task('lint:watch', ['lint:changed'], function () {
    gulp.watch(globs.core.js, ['lint:changed']);
});



/***********************
 * UNIT TEST
 ***********************/

gulp.task('unit-test', function (done) {
    var Karma = require('karma');
    new Karma.Server({
        configFile: paths.config.karma,
        singleRun: true
    }, done).start();
});

gulp.task('unit-test:watch', [], function (done) {
    var Karma = require('karma');
    var isdone = false;
    var server = new Karma.Server({
        configFile: paths.config.karma,
        autoWatch: true,
        singleRun: false
    });
    server.on('run_complete', function() {
        // this ensures done() is called so that the run
        // sequence is maintained, but also ensures that
        // done() is only called once.
        if (!isdone) { done(); isdone = 1; }
    });
    server.start();
});


/***********************
 * BROWSER SYNC
 ***********************/

gulp.task('build:watch', function () {

    // Watch Core SASS files for changes, rebuild as needed

    gulp.watch(globs.core.sass.main, ['build-core-main-css']);
    gulp.watch(globs.core.sass.comp, ['build-core-comp-css']);
    gulp.watch(globs.core.sass.vendor, ['build-core-vendor-css']);

    gulp.watch(globs.core.md, ['build-docs-pages']);
    gulp.watch(globs.docs.sass, ['build-docs-css']);

});

gulp.task('build:server', function (done) {

    var opn = require('opn');

    // Starts a BrowserSync server that watches both
    // Core and Docs and reloads on changes.

    var browserSync = require('browser-sync');

    browserSync.create().init({
        port: 8100,
        open: false,
        ui: { port: 8101 },
        https: true,
        server: root,
        notify: false,
        logLevel: 'info',
        ghostMode: false,
        logFileChanges: false,
        timestamps: false,
        files: [
            core + '**/*.html',
            core + '**/*.css',
            core + '**/!(*spec).js',
            docs + '**/*.html'
        ]
    });

    opn('https://dev.commerce.spscommerce.com/localhost/');

    done();
});


gulp.task('coverage:server', function (done) {

    // Starts a BrowserSync server that watches and
    // reloads coverage reports on changes.

    var browserSync = require('browser-sync');

    browserSync.create().init({
        port: 9200,
        ui: { port: 9201 },
        open: false,
        notify: false,
        ghostMode: false,
        logLevel: 'silent',
        logFileChanges: false,
        files: ['test/reports/coverage/**/*.html'],
        server: {baseDir: 'test/reports/coverage/'}
    });
    done();
});

gulp.task('results:server', function (done) {

    // Starts a BrowserSync server that watches and
    // reloads the Karam unit-test results pages.

    var browserSync = require('browser-sync');

    browserSync.create().init({
        port: 9300,
        ui: { port: 9301 },
        open: false,
        notify: false,
        ghostMode: false,
        logLevel: 'silent',
        logFileChanges: false,
        files: ['test/reports/results/**/*.html'],
        server: {
            directory: true,
            baseDir: 'test/reports/results/'
        }
    });
    done();
});


gulp.task('tdd:server', function(done) {

    // Starts a BrowserSync server that doesn't watch
    // any files, just serves the test index page so
    // that the Code Coverage and Unit Test Results
    // can be served in the same browser window.

    var browserSync = require('browser-sync');

    browserSync.create().init({
        port: 9400,
        ui: { port: 9401 },
        server: 'test/',
        open: 'local',
        files: false,
        notify: false,
        ghostMode: false,
        logLevel: 'silent',
        timestamps: false,
        logFileChanges: false
    });
    done();

});
