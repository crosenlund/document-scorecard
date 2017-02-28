# Changelog

## v2.3.1 (2016-03-31)

#### Overview

Fixed broken internal imports in v2.3.0.

No breaking changes to the core.

## v2.3.0 (2016-03-30)

#### Overview

New Angular modules!

Deprecating ```<spsui-sidebar>``` and ```<spsui-page-title>``` components.

No breaking changes to the core.

#### New Default Modules

Added CurrentUser Module ```spsui.currentUser```

* Moved ```currentUser``` service to it's own module
* Does not change how it is consumed by the end user
* Added ```currentUser.whoami()``` method
* Added ```currentUser.details``` object
* Enabled by default when including WebUI-Core
* See [README](https://github.com/SPSCommerce/webui-core/blob/master/core/modules/currentUser/currentUser.readme.md)

Added Token Module ```spsui.token```

* Captures user access token from the URL
* Attaches the Authorization header to HTTP requests
* Enabled by default when including WebUI-Core
* See [README](https://github.com/SPSCommerce/webui-core/blob/master/core/modules/token/token.readme.md)

Added Identity Module ```spsui.identity```

* Provides ```identityService``` for communicating with Identity API
* Environment auto-detection and configuration when app is run from Commerce Platform
* Enabled by default when including WebUI-Core
* See [README](https://github.com/SPSCommerce/webui-core/blob/master/core/modules/identity/identity.readme.md)

#### New Optional Modules

Added DateTime Module ```webui-datetime```

* Provides ```spsuiDate``` filter
* Timezone support, guesses user's local timezone
* Will use ```currentUser.preferences``` once implemented
* Optional module, need to import as needed
* See [README](https://github.com/SPSCommerce/webui-core/blob/master/core/modules/datetime/datetime.readme.md)

Added Intercom Module ```webui-intercom```

* Enables the [Intercom Messenger](https://www.intercom.io/messenger)
* Configurable via ```intercomServiceProvider```
* Public API available via ```intercomService.api()```
* Optional module, need to import as needed
* See [README](https://github.com/SPSCommerce/webui-core/blob/master/core/modules/intercom/intercom.readme.md)

#### Components

Noted deprecation of ```<spsui-sidebar>``` and ```<spsui-page-title>``` in documentation

* Does not log a warning yet, will begin logging warnings starting v2.4.0
* Both components will be removed in v3.0.0

#### Local Development

```gulp server``` now runs in ```https```

* When first run you will need to approve the browser exception for the self-signed cert.
* Opens ```https://dev.commerce.spscommerce.com/localhost/``` instead of ```https://localhost:8100```

#### Misc

* Changed all npm devDependencies to regular dependencies
* Added ```npm-shrinkwrap.json``` to pin all dependency versions

----

## v2.2.3 (2016-03-22)

#### Overview

Style bug fixes.

No breaking changes to the core.

#### Bugs

* Fix dual scrollbar problem in Windows browsers
* Correctly push the footer to the bottom of the viewport
* Center the footer contents

----

## v2.2.2 (2016-02-29)

#### Overview

Bug fix.

No breaking changes to the core.

#### Documentation

* Fixed page-nav example not loading webui-core correctly.

----

## v2.2.1 (2016-02-24)

#### Overview

Bug fix.

No breaking changes to the core.

#### Bugs

* Add compiled page-nav .min.css and .min.css.map files. [#212](https://github.com/SPSCommerce/webui-core/issues/212)

----

## v2.2.0 (2016-02-22)

#### Overview

New component.

No breaking changes to the core.

#### Components

* Added ```<spsui-page-nav>``` component. Authored by @alexander-ivakhnenko

----

## v2.1.2 (2016-02-15)

#### Overview

Bug fix.

No breaking changes to the core.

#### Bugs

* Pinned datetimepicker dependency at v2.4.5 (due to v2.4.6 being broken)

----

## v2.1.1 (2016-02-04)

#### Overview

Removing the Pattern Library completely from WebUI-Core, plus bug fixes.

No breaking changes to the core.

#### Docs

* Completely removed the pattern library, [now in it's own repo](https://github.com/SPSCommerce/webui-pattern-library)
* Created a gh-pages branch for webui-core documentation

#### Structure

* ```dist/core/webui-core*``` moved back to ```dist/webui-core*```

#### Bugs

* Changed link to SPS logo in footer to load from https. [#197](https://github.com/SPSCommerce/webui-core/issues/197)
* Init Foundation plugins on ui-router state changes. [#198](https://github.com/SPSCommerce/webui-core/issues/198)
* Bower.json manifest declares jQuery, Lodash, and Angular dependencies. [#199](https://github.com/SPSCommerce/webui-core/issues/199)
* Fixed issue with FontAwesome icons not loading from CDN. [#206](https://github.com/SPSCommerce/webui-core/issues/206)

---

## v2.1.0 (2015-12-22)

#### Overview

Deeplinking support with a few new services.

Some breaking changes.

#### New

* Services:
    * currentUser service (stores user access token).
    * postMessage service (for working with postMessages).
    * commercePlatform service (for working with platform frame).

* Components:
    * ui-sref decorator to allow deeplinks to be opened in new tabs.

* During Setup:
    * a URL rule is set to capture the user access token.
    * a URL rule is set to auto-enforce slashes on URLs.
    * A state redirectTo property added for cleaner state redirects.
    * Register ui-router state changes with Platform deeplinking.

#### Breaking
* All ui-router states need their URLs to be defined with ending slashes.
* Removed spsui-feedback component from the core, [now external component](https://github.com/SPSCommerce/webui-feedback).

#### Misc
* Quit being clever and set the JSPM folder, config file back to default settings.
* Loosended up dependency versions, in attempt to create less forks when consumed.
* Removed unused JSPM loader.js (was used when initially setting up v2).
* Core components correctly export their angular modules.
* Use sass-jspm-importer during build for Sass importing.
* Updated Font-Awesome from v4.3 to v4.5 ([~100 more icons!](http://fontawesome.io/cheatsheet/))

---

## v2.0.4 (2015-11-24)

#### Overview

Cleanup and bug fixes.

No breaking changes to the core.

#### Bugs

* Set the messageApi onto the global window.sps.messageApi object.
* Attempting to fix jQuery load issue with xdan/datetimepicker [#178](https://github.com/SPSCommerce/webui-core/issues/178)
* Fix bower.json version mismatch [#182](https://github.com/SPSCommerce/webui-core/issues/182)

**Note: This was supposed to be v2.0.3 but got messed up, so v2.0.4 was born**

---

## v2.0.2 (2015-11-03)

#### Overview

Cleanup and bug fixes.

No breaking changes to the core.

#### Bugs

* Messages API - Check that event.data.match is a function before calling it. [Commit](https://github.com/SPSCommerce/webui-core/commit/24e2d044029ca892c751d48f23ed9501ceb21bae)
* Export a global to ```window.sps.webuiCore```. [#169](https://github.com/SPSCommerce/webui-core/issues/169)
* Remove explicit ```.js``` from Feedback component imports. [#168](https://github.com/SPSCommerce/webui-core/issues/168)
* Sidebar added support for reloadState option. [Commit](https://github.com/SPSCommerce/webui-core/commit/0acb617298e0430abf0e9a22b40057dad2f1954b)
* Bumped jQuery to v2.1.4 [#179](https://github.com/SPSCommerce/webui-core/issues/179)

---

## v2.0.1 (2015-10-15)

#### Overview

Cleanup and bug fixes.

No breaking changes to the core.

#### Structure

Moved Pattern Library dist files so they are deployed to the CDN ([WFW-354](https://spscommerce.atlassian.net/browse/WFW-354))

* ```dist/webui-core*``` moved to ```dist/core/webui-core*```

* ```docs/dist/``` moved to ```dist/docs/```

#### Core

* ```core/all.js``` imports Chosen, Datepicker, and Feedback components (accidentally left out of v2.0.0)
* Removed Handsontable as a dependency

#### Docs

* Broken sub-pages removed ([WFW-161](https://spscommerce.atlassian.net/browse/WFW-161))
* Old sidebar icons replaced with nearest Font-Awesome equivalents
* Removed **Editable Tables** section because it requires a not-yet-published component

#### Gulp

* ```gulp clean``` wipes out all dist and build files
* ```gulp build``` creates dist versions of core & docs

---

## v2.0.0 (2015-10-8)

#### Overview

This is a major reorganization, repackaging effort from the 1.x branch.

Core is now configured to use SystemJS.

#### New

Structure

* webui-core files moved to ```core/```
* pattern library files moved to ```docs/```

Angular Components

* spsui-application
* spsui-page-title
* spsui-sidebar
* spsui-viewport
* spsui-footer

Distribution files

* dist/webui-core.min.css
* dist/webui-core.min.js

Gulp

* ```gulp build-core```
* ```gulp build-docs```
* ```gulp server```
* ```gulp test```
* ```gulp tdd```
* ```gulp release```

#### Breaking

* Component ```spscp-sidebar``` changed to ```spsui-sidebar```
* Component ```spscp-page-title``` changed to ```spsui-page-title```

---
