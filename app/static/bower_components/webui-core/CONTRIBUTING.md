# Contributing

Anyone is welcome to help us build out features or squash bugs. We ask that you reach out to us before beginning any
significant development effort, as your ideas may already be in the works. Also, for maximum mergeability, please keep
Pull Requests small, concise, and well documented.

This is a quick rundown on how you can contribute features or bug fixes to WebUI-Core.

1. Create a fork of WebUI-Core.
1. Create a new branch.
1. Make your changes.
1. Write/update unit tests.
1. Shoot for high test-coverage.
1. JSHint should have no warnings.
1. Commit to your branch.
1. Push to your remote origin.
1. Pull Request against upstream.
1. Commerce Platform team will review.
1. Commerce Platform team will merge.

# Local Development of WebUI-Core

To develop locally, you need to [fork this repo](https://github.com/SPSCommerce/webui-core#fork-destination-box), clone it, and install the dev dependencies.

```
git clone git@github.com:YourGithubUser/webui-core.git
```

```
cd webui-core/
```

```
npm install
```

```
jspm install
```

If you have not used JSPM before, please [refer to these instructions](https://github.com/SPSCommerce/webui-example-app#install-jspm) on how to get started.

### Gulp Tasks

After your fork is cloned locally, run ```gulp``` to see a list of available Gulp tasks.

    Available tasks
        build                  Build core and documentation from source.
        clean                  Remove all static build files.
        dist                   Prepare core and modules for distribution.
        lint                   Perform static analysis on JS files.
        server                 Start simple server, reload source files on change.
        tdd                    Start TDD server, rebuild, test, lint source files on change.
        test                   Lint and unit test Core JS.


#### ```gulp build```

Builds all core files from source, copies markdown files into documentation folder.

#### ```gulp bundle```

Compiles the entire core into a self-executing bundle, for distribution via Bower.

### Testing

We use Karma + Jasmine to run unit tests on our Core components and services.

#### ```karma start```

Runs the test suite and generates code coverage reports in ```test/reports/coverage/```

#### ```gulp lint```

Runs all JS source files through JSHint static analysis, reports warnings and errors.

#### ```gulp test```

Runs all JS source files through JSHint static analysis, runs Karma test suite once and then exits.

#### ```gulp tdd```

Similar to ```gulp server``` but also runs Karma and a livereload server on the coverage reports.
Changes to any source files are automatically linted, tested, and the coverage reports updated and reloaded.

