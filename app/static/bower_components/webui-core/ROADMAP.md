# Roadmap

This roadmap is a place for us to publicly document our intentions for future releases.

Nothing here is set in stone and is subject to inevitable change.

## v2.3.1 (tbd ~April 2016)

#### Service Updates

* Move ```commercePlatform``` service to it's own module
    * Add ```commercePlatform.setTitle(str)```
    * Allow apps to update the Commerce Platform page title
    * Create documentation for ```commercePlatform``` service

#### Bug Fixes

* Fonts hosted by our own static-assets CDN [#200](https://github.com/SPSCommerce/webui-core/issues/200)
   * No longer load them from Google servers
   * Should reduce the number of HTTP requests on app load

----

## v2.4.0 (tbd ~May 2016)

#### New Optional Modules

* Permission Module ```webui-permission```
    * Definition for declaring role/permission relationships
    * Mechanism for requiring permissions to access states
    * Directive for requiring permissions to access features
    * Default 403 Forbidden view

* Modal Module ```webui-modal```
    * SPS Foundation modals in Angular
    * Base modal object class can be extended
    * Comes with ErrorModal and ConfirmModal dialogs

* Analytics Module ```webui-analytics```
    * Provide analyticsService for sending tracking events in a consistent way
    * Default tracking events are hooked into ui-router state changes
    * Components can take advantage of analyticsService

----

## v3.0.0 (tbd ~July 2016)

This version will be a major breaking version.

We intend to prune WebUI-Core down to the most useful pieces, removing a lot of cruft
left over from the Pattern Library transition. This will allow us to focus on what is really
core and identify what is extraneous.

The following libraries/plugins will be moved/removed in effort to reduce file size and
dependency bloat.

* jQuery
* Chosen
* Modernizr
* Datetimepicker
* Angular Cookie
* Angular Sanitize
* Angular Foundation

We would like to update to the latest 4.x version of Lodash and take advantage of the modular
system they have in place, allowing us to import just the specific functions needed instead
of the entire library. This should also help reduce the overall filesize of the core.

We may also decide to split the style portion of webui-core from the Angular portion. This
would allow developers to just import the look and feel without the extra javascript. And
vice-versa, a developer could import just the Angular modules/components without the CSS.

----
