## postMessage

| First Available 	| Lifecycle     | Files |
|-----------------	|----------     |------ |
| v2.1.0 	        | Stable        | [services/postMessage][postMessage] 	|

This service is meant to simplify the postMessage communication from application iframe to parent
Commerce Platform. This will eventually replace the wickedly old Rubicon messaging API.

#### Usage

```javascript
MyController.$inject = ['postMessage'];

function MyController(postMessage) {

    // Send a postMessage to Commerce Platform

    postMessage.sendToPlatform({
        type: 'messageType',
        params: {
            foo: 1,
            bar: 2,
            baz: 3
        }
    });

}
```

---

[postMessage]: https://github.com/SPSCommerce/webui-core/tree/master/core/services/postMessage/postMessage.js
