$(document).ready(function() {
    $('#readProfile').click(function () {
        let profile = localStorage.getItem('profile');
        alert(profile);
    });
});