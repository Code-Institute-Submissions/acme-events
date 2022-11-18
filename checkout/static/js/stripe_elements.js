/*
Employed within checkout.html and checkout procedures
*/

let stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1,);
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
    console.log('js stage one')
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
console.log('js: identified form')

form.addEventListener('submit', function(ev) {
    console.log('js: entered event listenter: submit')
    ev.preventDefault();
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);
    console.log('js: identified key elements')
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        console.log('js: into function result')
        if (result.error) {
            // In the event of an error:
            console.log('js: result: error')
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            // Display error message
            $('#payment-form').fadeToggle(100);
            $('#loading-overlay').fadeToggle(100);
            // Uncover payment form
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);
            // Re-eable card-details inputs and submit button
            console.log('js stage 11')
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                console.log('js: result:success')
                form.submit();
            }
        }
    });
});
