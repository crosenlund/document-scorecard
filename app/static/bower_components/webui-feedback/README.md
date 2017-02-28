# webui-feedback

Angular component for SPS styled feedback alert messages.

Examples can be found on the [Demo Page](http://spscommerce.github.io/webui-feedback/)

### Dependencies

* angular v1.4
* [webui-core v2](https://github.com/SPSCommerce/webui-core)

### Installation

#### JSPM

```
jspm install webui-feedback=github:SPSCommerce/webui-feedback
```

app.js

```javascript
var angular = require('angular');
var webcore = require('webui-core');
var feedback = require('webui-feedback');
module.exports = angular.module('myApp', [webcore.name, feedback.name]);
```

index.html

```html
<head>
    <script src="jspm_packages/system.js"></script>
    <script src="config.js"></script>
    <script>
        System.import('./app').then(function(app){
            angular.bootstrap(document, [app.name]);
        });
    </script>
</head>
```


#### Bower

```
bower install git@github.com:SPSCommerce/webui-feedback.git
```

app.js

```javascript
angular.module('myApp', ['webui-core', 'webui-feedback']);
```

index.html

```html
<head>
    <!-- core dependencies -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/lodash.js/3.10.1/lodash.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/angular.js/1.4.8/angular.min.js"></script>

    <!-- webui-core -->
    <link href="/bower_components/webui-core/dist/webui-core.min.css" rel="stylesheet">
    <script src="/bower_components/webui-core/dist/webui-core.min.js"></script>

    <!-- webui-feedback -->
    <link href="/bower_components/webui-feedback/dist/bundle.min.css" rel="stylesheet">
    <script src="/bower_components/webui-feedback/dist/bundle.min.js"></script>

    <!-- your app -->
    <script src="app.js"></script>
</head>
```

---

### ```<spsui-feedback-msg>```

Stylized feedback message elements.

#### Options

##### type [optional]

Specify the style of message.

Default: info

Options:

* success
* warning
* error
* info
* tip

```html
<spsui-feedback-msg type="warning">
    This is a warning message
</spsui-feedback-msg>
```

---

##### label [optional]

Override the default message label.

Default: _differs between msg types_

```html
<spsui-feedback-msg type="success" label="Good Work!">
    Success message with custom label
</spsui-feedback-msg>
```

---

##### icon [optional]

Override the default message icon, use FontAwesome classes.

Default: _differs between msg types_

```html
<spsui-feedback-msg type="success" icon="fa-thumbs-o-up">
    Success message with custom icon
</spsui-feedback-msg>
```

---

##### noicon [optional]

Remove the icon from the message.

Default: false

```html
<spsui-feedback-msg type="success" noicon>
    Success message with no icon
</spsui-feedback-msg>
```

---

##### closeable [optional]

Set whether the message can be closed by the user.

Default: false

```html
<spsui-feedback-msg type="success" closeable>
    Closeable success message
</spsui-feedback-msg>
```

---

##### flash [optional]

Set the message to automatically close in a given duration (in ms).

Default: false

```html
<spsui-feedback-msg type="success" flash="10000">
    Message will close automatically in 10 seconds.
</spsui-feedback-msg>
```

If no value is passed, the default duration is used (5000ms).

```html
<spsui-feedback-msg type="success" flash>
    Message will close automatically in the default duration.
</spsui-feedback-msg>
```


---

### ```<spsui-feedback-container>```

Container element for sending feedback messages.

#### Options

##### feedback-id [required]

A string ID used for sending messages to the container.

```html
<spsui-feedback-container feedback-id="myMessages"></spsui-feedback-container>
```

---

### FeedbackFactory

Angular service for creating feedback messages programatically.

Works well with feedback containers.

```javascript

myController.$inject = ['FeedbackFactory'];

function myController(FeedbackFactory) {

    this.someMethod = function() {

        // create a success message element
        var msg = FeedbackFactory.success('Nicely done!');

        // append the message to a container
        msg.api.sendTo('myMessages');
    }
}

```

#### Methods

##### success({string} text, {object} opts) => returns HTMLElement

Generate a success message with the supplied text content and options.

```javascript
var msg = FeedbackFactory.success('Closeable Success Message', {closeable: true});
```

##### warning({string} text, {object} opts) => returns HTMLElement

Generate a warning message with the supplied text content and options.

```javascript
var msg = FeedbackFactory.warning('Warning Message');
```

##### error({string} text, {object} opts) => returns HTMLElement

Generate an error message with the supplied text content and options.

```javascript
var msg = FeedbackFactory.error('Error Message');
```

##### info({string} text, {object} opts) => returns HTMLElement

Generate an info message with the supplied text content and options.

```javascript
var msg = FeedbackFactory.info('Info Message');
```

##### tip({string} text, {object} opts) => returns HTMLElement

Generate a pro-tip message with the supplied text content and options.

```javascript
var msg = FeedbackFactory.tip('Pro-tip Message');
```

##### newMessage({string} text, {object} opts) => returns HTMLElement

Generate any type of message with the supplied text content and options.

```javascript
FeedbackFactory.newMessage('Success Message', {type: 'success'});
```

#### Options

```javascript
{
    type: '',
    icon: '',
    label: '',
    flash: false,
    noicon: false,
    closeable: false
}
```

---

### FeedbackService

Service for working with containers.

```javascript

myController.$inject = ['FeedbackService'];

function myController(FeedbackService) {

    this.clearMessages = function() {

        // clear messages from all containers
        FeedbackService.clearAllContainers();

        // clear messages from a single container
        FeedbackService.clearContainer('myMessages');
    }
}

```

#### Methods

##### registerContainer({string} id, {ng.element} $element)

Register a container element with the service.

All spsui-feedback-container elements are registered automatically.

Used by ```source/container/container.ctrl.js```

```javascript
FeedbackService.registerContainer('foo', myContainer);
```

##### getContainer({string} id) => returns $element

Get a container element by it's feedback id.

```javascript
var container = FeedbackService.getContainer('foo');
```

##### sendMsgToContainer({ng.element} msg, {string} id)

Append a message element to a container.

Used by ```source/container/message/message.ctrl.js```

```javascript
var msg = FeedbackFactory.success('Nicely Done!');
FeedbackService.sendMsgToContainer(msg, 'foo');
```

##### clearContainer({string} id)

Remove all messages in a given container.

```javascript
FeedbackService.clearContainer('foo');
```


##### clearAllContainers()

Remove all messages in all registered containers.

```javascript
FeedbackService.clearAllContainers();
```


