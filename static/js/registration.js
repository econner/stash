var T = {};

T.RegistrationForm = Backbone.View.extend({

    initialize: function(options) {
        this.registration_form = $(options.registration_form);
        this.fields = {};
        this.bind_validators();
        this.bind_submit();
    },

    bind_validators: function() {
        var self = this;

        $('input[id^="register"]', this.registration_form).each(function(idx, elem) {
            var timer;
            var done_typing_timeout = 200;

            $(elem).keyup(function() {
                timer = setTimeout(function() { self.validate_field(elem); },
                                   done_typing_timeout);
            });

            $(elem).keydown(function() {
                clearTimeout(timer);
            });
            // mark field invalid so it must validate
            self.mark_validity(elem, false);
        });
    },

    bind_submit: function() {
        var self = this;
        this.registration_form.bind("submit", function(ev) {
            var should_submit_form = true;
            $.each(self.fields, function(key, value) {
                if(!value) {
                    should_submit_form = false;
                }
            });

            // if(!should_submit_form) {
            //     ev.preventDefault();
            //     return false;
            // }
        });
    },

    validate_field: function(elem) {
        var field_name = $(elem).attr('data-validation-name');
        var field_value = $(elem).val();

        // validate password
        if(field_name == 'password') {
            if(field_value.length < 6) {
                this.mark_validity(elem, false, 'Too short.');
            } else {
                this.mark_validity(elem, true);
            }
        } else {
            // validate email or username
            this.validate_username_or_email(elem);
        }
    },

    validate_username_or_email: function(elem, status_elem) {
        var self = this;

        var field_name = $(elem).attr('data-validation-name');
        var field_value = $(elem).val();

        if(field_value.length <= 3) {
            self.mark_validity(elem, false, 'Too short.');
            return;
        }

        // ensure name has not been registered
        attrs = {};
        attrs[field_name] = field_value;
        $.ajax({
            type: 'GET',
            url: '/user/validate',
            data: attrs,
            success: function(response) {
                if(response['status'] !== 'success') {
                    alert("ERROR: " + response['message']);
                    return;
                }
                self.mark_validity(elem, response['valid'], response['message']);
            }
        });
    },

    mark_validity: function(field, is_valid, message) {
        // ensure we have a message to display
        if(typeof(message) === "undefined" || !message) {
            if(is_valid) {
                message = "OK.";
            } else {
                message = "";
            }
        }

        var status_elem = $(field).next();
        var field_name = $(field).attr('data-validation-name');
        this.fields[field_name] = is_valid;
        if(is_valid) {
            status_elem.addClass('valid');
        } else {
            status_elem.addClass('invalid');
        }
        status_elem.html(message);
    }
});