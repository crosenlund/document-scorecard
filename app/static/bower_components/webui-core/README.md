# webui-core

[![Build Status][build-img]][build-link]

WebUI-Core is a collection of core Angular components, services, and objects that are designed to ease the
development of SPS web applications.  WebUI-Core also contains Foundation CSS with SPS-specific style settings to
simplify the process of adopting the SPS look-and-feel.

If you are starting a new SPS web app from scratch, please see the [webui-example-app](https://github.com/SPSCommerce/webui-example-app).

WebUI-Core is maintained by the Commerce Platform team (kkorth, cmason).

## [View the complete WebUI-Core documentation](http://spscommerce.github.io/webui-core/)

Also see: [CONTRIBUTING](CONTRIBUTING.md), [CHANGELOG](CHANGELOG.md), and [ROADMAP](ROADMAP.md)

### What is Included

**Third-Party Libraries**

* angular 1.4.8 [\*](#bring-your-own-libraries)
* angular-cookie 4.0.x
* angular-foundation 0.6.x
* angular-sanitize 1.4.x
* angular-ui-router 0.2.15
* chosen 1.4.x †
* datetimepicker 2.4.x †
* font-awesome 4.5.x
* foundation 5.5.2
* jquery 2.1.4 [\*](#bring-your-own-libraries)
* lodash 3.10.1 [\*](#bring-your-own-libraries)
* modernizr 2.8.x
* normalize.css 3.0.3
* Platform Messages API
* Source Code Pro (Google Font)
* Source Sans Pro (Google Font)

**Angular Components**

* [spsui-application](./core/components/application/)
* [spsui-page-title](./core/components/pagetitle/)
* [spsui-viewport](./core/components/viewport/)
* [spsui-sidebar](./core/components/sidebar/)
* [spsui-footer](./core/components/footer/)

_\* Not included in Bower distribution_

_† Will be moved to an external module in a future release_

## Installation

WebUI-Core is a frontend dependency which can be installed via JSPM or Bower.

#### JSPM

```
jspm install webui-core=github:SPSCommerce/webui-core
```

_Note: You will need to setup a [Github Access Token for JSPM](https://github.com/SPSCommerce/webui-example-app#generate-a-github-access-token-for-jspm) to install from SPS repositories._

### Bower

```
bower install git@github.com:SPSCommerce/webui-core.git
```

_Note: Bower package does not include Angular, jQuery, or Lodash. You need to include them separately._

## Usage

To use the core components (sidebar, page title, etc), you need to bootstrap an Angular application
that requires the webui-core module as a dependency.  Your exact implementation will vary.

### JSPM + SystemJS

app.js

```javascript
require('webui-core');
module.exports = angular.module('myApp', ['webui-core']);
```

index.html

```html
<html>
<head>
    <script src="/jspm_packages/system.js"></script>
    <script src="/config.js"></script>
    <script>
        System.import('./app').then(function (module) {
            angular.bootstrap(document, [module.name]);
        });
    </script>
</head>
<body>
    <spsui-application>
        <spsui-sidebar config-obj="{}"></spsui-sidebar>
        <spsui-page-title page-title="'My Application'"></spsui-page-title>
        <spsui-viewport></spsui-viewport>
    </spsui-application>
</body>
</html>
```

### Bower

app.js

```javascript
angular.module('myApp', ['webui-core']);
```

index.html

```html
<html>
<head>
    <!-- webui-core stylesheet -->
    <link href="/bower_components/webui-core/dist/webui-core.min.css" rel="stylesheet">

    <!-- third party libraries -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/angular.js/1.4.8/angular.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/lodash.js/3.10.1/lodash.js"></script>

    <!-- webui-core and module scripts -->
    <script src="/bower_components/webui-core/dist/webui-core.min.js"></script>
    <script src="/bower_components/webui-core/dist/webui-datetime.min.js"></script>

    <!-- your application code -->
    <script src="app.js"></script>
</head>
<body ng-app="myApp">
    <spsui-application>
        <spsui-sidebar config-obj="{}"></spsui-sidebar>
        <spsui-page-title page-title="'My Application'"></spsui-page-title>
        <spsui-viewport></spsui-viewport>
    </spsui-application>
</body>
</html>
```

## Updating

Once installed, it should be easy to stay up to date with new versions of WebUI-Core

### JSPM

```
jspm update webui-core
```

### Bower

```
bower update webui-core
```

## Testing

When running Karma with the Bower version of webui-core, you may encounter the [following PhantomJS error](https://github.com/SPSCommerce/webui-core/issues/175):

```
SYNTAX_ERR: DOM Exception 12: An invalid or illegal string was specified.
at /bower_components/webui-core/dist/core/webui-core.min.js:4
```

The solution is to load the ```webui-core.min.css``` file in Karma files before the ```webui-core.min.js```.

```javascript
files: [
    '/bower_components/webui-core/dist/core/webui-core.min.css',
    '/bower_components/webui-core/dist/core/webui-core.min.js',
]
```

<!-- Badge images and Links -->

[build-link]: https://magnum.travis-ci.com/SPSCommerce/webui-core
[build-img]: https://magnum.travis-ci.com/SPSCommerce/webui-core.svg?token=dJTiJyPtAPx43Aa9by9E&branch=master
