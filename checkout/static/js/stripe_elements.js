/*
Employed within checkout.html and checkout procedures
*/

let stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
let clientSecret = $('#id_client_secret').text().slice(1, -1);
let stripe = Stripe(stripePublicKey);

// Add Stripe Card Field to Checkout Form
let elements = stripe.elements();

let style = {
    base: {
        color: '#000000',
        fontFamily: 'Montserrat, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '14px',
        '::placeholder': {
            color: '#a7a9aa'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

let card = elements.create('card', {style: style});
card.mount('#card-element');

// Handle card validation errors:
card.addEventListener('change', function (event) {
    let errorDiv = document.getElementById('card-errors');
    if (event.error) {
        let html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = "";
    }
});

// Handle form submit (from Stripe Docs with modifications from Boutique Ado finished code via Code Institute):
let form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);
    let saveInfo = Boolean($('#id-save-info').attr('checked'));
    // Get value of checkbox by looking at its checked attr
    let csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    // From using {% csrf_token %} in the form
    let postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    let url = '/checkout/cache_checkout_data/';
    let first_name = $.trim(form.first_name.value);
    let last_name = $.trim(form.last_name.value);
    let full_name = first_name.concat(" ", last_name);
    $.post(url, postData).done(function () {
    // jQuery: send 'postData' to url and only when 'done'
    // proceed to the following (a callback function), but bear in
    // mind that this callback function only runs if you receive a
    // 200 OK response (see cache_checkout_data view):
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        billing_details: {
            name: full_name,
            phone: $.trim(form.telephone.value),
            email: $.trim(form.email.value),
            address:{
                line1: $.trim(form.street_address1.value),
                line2: $.trim(form.street_address2.value),
                city: $.trim(form.city_or_town.value),
                country: $.trim(form.country.value),
                state: $.trim(form.county.value),
            }
        }
    },
    }).then(function(result) {
        if (result.error) {
            // In the event of an error:
            $('#payment-form').fadeToggle(100);
            $('#loading-overlay').fadeToggle(100);
            // Uncover payment form
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);
            // Re-eable card-details inputs and submit button
            let errorDiv = document.getElementById('card-errors');
            let html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            // Display error message
            console.log(result.error.message)
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
}).fail(function () {
    // If view sends back a 400 Bad Request response instead,
    // just reload the page, the error will be in django messages
    console.log('triggered: fail function in stripe_elements.js')
    location.reload();
})
});
