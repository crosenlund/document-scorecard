
var _ = require('lodash');

module.exports = IntercomInit;

IntercomInit.$inject = ['currentUser', 'intercomService'];

function IntercomInit(currentUser, intercomService) {

    // This is what automatically configures the Intercom Messenger
    // with the current user's name, email, and organization data.
    // Using the currentUser.whenReady() promise ensures we do not
    // launch the Messenger until we have all of the user's details.

    currentUser.whenReady().then(function() {

        var u = currentUser.details;

        // If the currentUser details contain the user creation
        // date, then let's convert that into a Unix timestamp
        // and pass it into the Intercom Messenger.

        var createdVal = _.get(u, 'meta.created') || '';
        var createdDate = Math.floor(new Date(createdVal) / 1000);

        intercomService.config({
            user_id: u.id,
            email: u.email,
            created_at: createdDate,
            name: [u.first_name, u.last_name].join(' '),
            company: {
                id: u.organization.id,
                name: u.organization.organization_name,
            }
        });

        intercomService.launch();
    });
}
