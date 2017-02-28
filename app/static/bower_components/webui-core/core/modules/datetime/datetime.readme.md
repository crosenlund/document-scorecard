## DateTime Module

| First Available 	| Lifecycle     | Files |
|-----------------	|----------     |------ |
| v2.3.0 	        | New        | [modules/datetime][datetimeModule] 	|

*Notice: This is a new feature. You are encouraged to use it and [report any issues you may find][issues].*

The DateTime Module provides tools for formatting dates and times in a manner that is consistent
with the product design guidelines. The DateTime module uses MomentJS under the hood for powerful,
localized date formatting.

#### How To Import

This module is not imported automatically into your app with WebUI-Core.  If you choose to use it,
you need to set the DateTime Module as a dependency in your application.

**JSPM + SystemJS**

```javascript
require('webui-core');
require('webui-core/modules/datetime');

module.exports = angular.module('myApp', ['webui-core', 'webui-datetime']);
```

**Bower**

DateTime Module requires ```Moment v2.11.2``` and ```Moment-Timezone v0.5.0```.

You can install them with Bower into your project **OR** load them from CDN at runtime.

```bash
$> bower install moment#2.11.2 moment-timezone#0.5.0
```

index.html

```html
<head>
    <!-- Load Moment and Moment-Timzone from CDN -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.11.2/moment.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/moment-timezone/0.5.0/moment-timezone.min.js"></script>

    <!-- webui-core and module scripts -->
    <script src="/bower_components/webui-core/dist/webui-core.min.js"></script>
    <script src="/bower_components/webui-core/dist/webui-datetime.min.js"></script>
</head>
```

app.js

```javascript
angular.module('myApp', ['webui-core', 'webui-datetime']);
```

#### Date Formatting Filter

Provided in the DateTime Module is a date formatting filter that supports localized date strings
and relative dates.  The filter uses the current user's preferences for locale and timezone to
make sure the dates and times are formatted to their liking.

* If the user has not set a locale preference, ```English (US)``` is used.
* If the user has not set a timezone preference, their local timezone is guessed.

##### Usage

In a view
```html
<!-- Formatted Date -->
<p>{{ctrl.date | spsuiDate : 'FORMAT_STRING'}}</p>

<!-- Relative Date -->
<p>{{ctrl.date | spsuiDate : 'FORMAT_STRING' : 'RELATIVE'}}</p>
```

In a controller
```javascript
MyController.$inject = ['spsuiDateFilter'];

function MyController(spsuiDateFilter) {

    var date = new Date();
    var formattedDate = spsuiDateFilter(date, 'FORMAT_STRING');
    var relativeDate = spsuiDateFilter(date, 'FORMAT_STRING', 'RELATIVE');
}
```

##### Supported Object Types

The date filter supports JS date objects, Moment objects, and date strings. If the date filter cannot
parse a date it will log a warning in the console and return the original input value.

```javascript
function MyController() {

    // Date filter supports the following date types:

    this.date = moment();
    this.date = new Date();
    this.date = '02/29/2016 3:03:50 PM CST';
}
```

##### Available Formats

Dates and times will be formatted according to the user's preferred locale and timezone settings.

```html
<p>{{ctrl.date | spsuiDate : 'SHORT_TIME_ZONE'}}</p> <!-- 3:03 PM CST -->
<p>{{ctrl.date | spsuiDate : 'LONG_DATE'}}</p> <!-- February 29, 2016 -->
```

Below is a list of the available formats with example localized outputs.

| Format String | English (US) Output | Ukrainian Output |
|-------------- |-------------------- |----------------- |
| SHORT_TIME | 3:03 PM | 15:03 |
| SHORT_TIME_ZONE | 3:03 PM CST | 15:03 CST |
| LONG_TIME | 3:03:50 PM | 15:03:50 |
| LONG_TIME_ZONE | 3:03:50 PM CST | 15:03:50 CST |
| NUM_DATE | 02/29/2016 | 29.02.2016 |
| SHORT_DATE | Feb 29, 2016 | 29 лют 2016 р. |
| LONG_DATE | February 29, 2016 | 29 лютого 2016 р. |
| SHORT_DATETIME | Feb 29, 2016 @ 3:03 PM | 29 лют 2016 р., 15:03 |
| SHORT_DATETIME_ZONE | Feb 29, 2016 @ 3:03 PM CST | 29 лют 2016 р., 15:03 CST |
| LONG_DATETIME | February 29, 2016 @ 3:03 PM | 29 лютого 2016 р., 15:03 |
| LONG_DATETIME_ZONE | February 29, 2016 @ 3:03 PM CST | 29 лютого 2016 р., 15:03 CST |
| SHORT_FULLDATETIME | Mon Feb 29, 2016 @ 3:03 PM | пн, 29 лют 2016 р., 15:03 |
| SHORT_FULLDATETIME_ZONE | Mon Feb 29, 2016 @ 3:03 PM CST | пн, 29 лют 2016 р., 15:03 CST |
| LONG_FULLDATETIME | Monday February 29, 2016 @ 3:03 PM | понеділок, 29 лютого 2016 р., 15:03 |
| LONG_FULLDATETIME_ZONE | Monday February 29, 2016 @ 3:03 PM CST | понеділок, 29 лютого 2016 р., 15:03 CST |

##### Relative Dates and Times

Occasionally a product design may indicate that the date will be displayed in a relative manner.
Design guidelines dictate that relative dates should not be used if the date is greater than 7 days.
The date filter takes care of this automatically and resorts to the specified format if the date is
too far away.

```javascript
ctrl.date1 = moment().subtract(3, 'days');
ctrl.date2 = moment().subtract(2, 'weeks');
```

```html
<!-- "3 days ago" -->
<p>{{ctrl.date1 | spsuiDate : 'LONG_DATE' : 'RELATIVE'}}</p>

<!-- "February 15, 2016" -->
<p>{{ctrl.date2 | spsuiDate : 'LONG_DATE' : 'RELATIVE'}}</p>
```

---

[datetimeModule]: https://github.com/SPSCommerce/webui-core/blob/master/core/modules/datetime
