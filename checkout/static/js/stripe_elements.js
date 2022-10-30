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

