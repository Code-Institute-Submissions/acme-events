/*
Employed within checkout.html and checkout procedures
*/

let stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1,);
let clientSecret = $('#id_client_secret').text().slice(1, -1);

let stripe = Stripe(stripePublicKey);
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