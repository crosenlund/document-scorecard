## currentUser

| First Available 	| Lifecycle     | Files |
|-----------------	|----------     |------ |
| v2.1.0 	        | Stable        | [services/currentUser][currentUser] 	|

This service provides details about the current logged in user.

#### Usage

```javascript
MyController.$inject = ['currentUser'];

function MyController(currentUser) {

    // The user access token
    console.log(currentUser.token);

    // Details about the user
    console.log(currentUser.details);

    // The user preferences (values will be blank)
    console.log(currentUser.preferences);

    // Fetch the current user details from Identity.
    // This step is run automatically on bootstrap
    // to populate the currentUser.details object.

    currentUser.whoami().then(function(userDetails){
        console.log(userDetails);
    });
}
```

#### User Details Object

```json
{
  "first_name": "Foo",
  "last_name": "Bar",
  "roles": [
    "comp:dev",
    "comp:user"
  ],
  "user_type": "Company Employee",
  "email": "fbar@company.com",
  "user_search": "fbar@company.com Foo Bar",
  "meta": {
    "owner": "aaa:org:use1-00000000-0000-0000-0000-000000000000",
    "created_by": "aaa:user:use1-00000000-0000-0000-0000-000000000000",
    "created": "2016-02-29T15:03:03.030303Z"
  },
  "identity_id": "12345678901234567890123456789012345678",
  "organization": {
    "organization_name": "Company",
    "organization_site": "www.company.com",
    "namespace": "comp",
    "id": "use1-00000000-0000-0000-0000-000000000000",
    "identity_id": "987654321098765432109876543210987654321"
  },
  "id": "use1-abcd1234-abc1-1234-a123-123abcde4567",
  "types": [
    "comp:obj",
    "comp:user"
  ],
  "job_title": "Foo Bar"
}
```

---

[currentUser]: https://github.com/SPSCommerce/webui-core/tree/master/core/modules/currentUser/currentUser.service.js
