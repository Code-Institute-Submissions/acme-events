# Acme Events 
*Acme Events* is a portfolio site with a sense of humour. Ostensibly, the company organises and sells tickets to events at which would-be consumers can view the latest and greatest in the way of anvils.

An anvil is a blacksmithing tool more familiar to many as the heavy object often dropped on cartoon characters and made famous in this regard by Warner Brothers' Looney Tunes animations. Like almost all products within these Warner Bros. productions, anvils often bore a manufacturer's mark crediting them to ["Acme Corp."](https://en.wikipedia.org/wiki/Acme_Corporation). The ficticious corporation has since become a standin or placeholder wherever a fake company is needed and is even used in some jurisdictions Law Schools Admissions Tests as the plaintiff or defendent in example cases.

For the purely fictional business represented by this portfolio project, therefore, the company in question is "Acme Events". As the products showcased at the events do not matter and the purpose of the site is to demonstrate an online booking system for an events company, anvils were chosen as a humorous stand-in.  
  
<img src="https://acme-events.s3.eu-west-1.amazonaws.com/media/readme/screencapture-acme-events-landing.png" alt="Acme Events Home or Landing page" width="75%" height="auto">
  
## Contents
1. [Problem Statement](#problem-statement)  
2. [User Stories](#user-stories)
3. [Tech Stack](#tech-stack)  
4. [Design Statement](#design-statement)
5. [Features](#features)
    + [Future Features](#future-features)
6. [Testing](#testing)
7. [Deployment](#deployment)  
8. [Known Bugs](#known-bugs)
9. [Credits](#credits)  
  
## Problem Statement  
Events companies advertising online face a unique version of a common problem; they wish to capture the consumer's full attention at the point of peak interest and prompt the user to take action, however, the event itself may be at a distant point in the future. The ability to sell tickets or take bookings in advance therefore represents a tremendous advantage to their business.

Third-party platforms to meet this need are in no shortage; however, a percentage of ticket sales is usually lost to platform fees, and the business loses control over how their material is represented when it's rendered on another site. In addition, consumer interest may be lost as the customer clicks through to the platform and is often taken away from the event company's own website. In addition, such platforms depend on their revenue from maximising tickets sales across all events, and may therefore advertise related and even competing events to the customer. In short, the interests of the company and the platform are not entirely aligned.

Ideally therefore, an event company would have its own native booking system with integrated payment through a secure, reputable payment processing service. Such a system would not take the consumer-user away from the site and would allow them to make multiple bookings, even across multiple events, without leaving the site.

While many future features may yet be implemented, Acme Events demonstrates this solution in practice.  
  
For an events company, localised reach and customer retention are both vital and often in competition if not well managed. This is a function of staging events in multiple locations within a broader geographical region; in short, a customer may be interested only in events which take place locally to them and these may occur only sporadically.

Digital marketing tools can accomodate this, however, if mismanaged, these same tools can quickly become redundant. Mailchimp provides audience "Groups" which can be used to divide audiences by self-selected criteria, such as interests or geographical region. This allows the site owner to target specific subsections of their subscriber base ("segments" of their Mailchimp "audience") when issuing a newsletter, ensuring each newsletter is best suited to reach its target audience.
  
As a result, newsletters receive greater engagement and higher open and click-through rates, resulting in greater customer retention. Additionally, as well-targetted emails are less likely to be misreported as spam, the sender benefits from higher send-success rates, equally resulting in greater engagement. Although "Acme Events" is not operational in any region, the mechanics for this strategy are in place within the newsletter subscribe form in the site's footer. Here, subscribers can self-sort according to their interest in "Region 1", "Region 2" or "All Regions".
  
Social media's advance audience targetting can also be of benefit, allowing an events company to maintain a global presence on the internet and yet appeal to local audiences when advertising. Facebook Adverts, for instance, allows the advertiser to define a geographical region for users to which a particular advert should be shown. Combined with other factors, this increases the likelihood of engagement and interaction, as well as social sharing, while ensuring maximum cost-effectiveness. The other factors that might be used in social media advertisement include demographic and interest-based information, allowing the company to target users belonging to demographics considered more affluent or in possession of greater disposable income, for instance, as well as targetting specific interests and even professions. Given the variation in how this user information is often expressed, keywords used in social media marketting may show significant overlap, for example, "blacksmith", "blacksmithing", "metal work" "metalworking", "metalwork" and so on.  
  
<img src="https://acme-events.s3.eu-west-1.amazonaws.com/media/readme/acme-events-facebook-example.png" alt="Example mock-up of Facebook page" width="75%" height="auto">
  
For many platforms, a sense of engagement is also required in addition to paid advertising and can generate greater interest and enthusiasm. This involves creating original content likely to be of interest to the target audience. In our example case, that might range from blacksmithing tips and demonstrations to quickly-consumed and highly shareable humorous GIFs, videos and/or memes of Warner Bros. content featuring anvils. Although this does not come with a direct financial cost, a significant investment of time is required this should be borne in mind as a form of cost. Therefore, attempting to leverage social media purely as "free" advertising may be a false economy for many businesses. For Acme Events, some degree of paid advertising would be used in conjuction with content creation.  
  
As a small business, Google Ads is not considered the first priority for Acme Events but this will be revised as the business grows.  
  
## User Stories  
  **Types of User** 
  + Site Owner/Admin
  + Consumer-user
  + Browsing-user
   
  **As a site owner/admin, I can...** 
  + Advertise upcoming events with all relevant details concerning time, date, location and description.  
  + Link to this event-specific information from my social media (e.g. Facebook Event pages etc.)
  + Edit event details where necessary.  
  + Delete events if cancelled before their start date.  
  + Rely on automated processes within the site to display only those events that have not already passed (ie. expired events will not be presented to the public).  
  + Take bookings (sell tickets) online with ease and minimum investment of time.  
  + Link to and promote venues hosting these events to promote good relations between organiser and venue.  
  + Provide contact information for venues to reduce queries from users that would be more appropriately directed to the venue than the event organiser.  
  + Build a client contact database directly from my website using the integrated newsletter sign-up form.  
  + Access a receipt for each customer transaction through the Stripe dashboard.  
  + Benefit from validation methods around user account creation and newsletter sign-ups to reduce bot signups.  
  + Leverage newsletter signups with self-selecting "Groups" for maximum audience retention.  
  
**As a browsing-user, I can...** 
  + View key information concerning upcoming events at a glance (e.g. location, time, date, etc.) 
  + Easily browse this list of events in chronological order, without the confusion or distraction that might be caused by also seeing expired events.  
  + View more detailed information about a specific event that interests me.  
  + Share a specific event on social media or elsewhere with its dedicated link, for example, if I wish to invite a friend (event-detail view).  
  + Sign up to a newsletter if I wish to remain informed about upcoming events in a given region or all regions, as well as general announcments and other information.  
  + Create an account to save time at checkout if ever I become a consumer-user.  
  + View the website's privacy policy in a new tab.  
  + Access information about event venues, such as contact details and address.  
  + Access a venue's website or its location within an online map service with a single click. 
  
**As a consumer-user, I can...** 
  + Make one or more bookings for one or more events I may wish to attend.
  + Pay online through a secure, reputable payment processing service integrated directly into the event website.
  + Receive feedback from the site assuring me that a given event booking has been created in my "cart".  
  + Update my cart by increasing or decreasing the quantity of tickets I wish to book for any given event.  
  + Update my cart by deleting an event booking entirely. 
  + Receive realtime feedback from the site when I update my cart.   
  + Save time at checkout by reusing default information saved to my account.  
  + View my past purchases in a dedicated "My Bookings" profile section.  
  + Update my default information at checkout or within the "My Bookings" profile section of the site.  
  + Receive realtime feedback about any errors in my input, such as form errors or erroneous card details.  

These functions should also be available to users employing a screen reader. See [Accessibility Testing](#accessibility-testing).  
  
## Tech Stack  
1. Languages
  + HTML
  + CSS
  + Javascript
  + Python (current runtime: 3.8.15)
  + Django's Template Language

2. Libraries & Frameworks
  + Django 3.2
  + Bootstrap 4
  + jQuery
  + Popper JS
  + FontAwesome Icons
 
3. Additional Tools/Stacks
  + Balsamiq
  + Google Fonts
  + Heroku 20

 4. Dependencies
  + asgiref==3.5.2
  + backports.zoneinfo==0.2.1
  + boto3==1.26.15
  + botocore==1.29.15
  + dj-database-url==1.0.0
  + Django==4.1.2
  + django-allauth==0.51.0
  + django-countries==7.2.1
  + django-crispy-forms==1.14.0
  + django-storages==1.13.1
  + gunicorn==20.1.0
  + jmespath==1.0.1
  + oauthlib==3.2.1
  + Pillow==9.2.0
  + psycopg2==2.9.5
  + PyJWT==2.5.0
  + python3-openid==3.2.0
  + requests-oauthlib==1.3.1
  + s3transfer==0.6.0
  + sqlparse==0.4.3
  + stripe==4.2.0
  + types-cryptography==3.3.23
  
## Design Statement     - INCOMPLETE
The site relies on strong contrast between its dark and light components for visual impact. Many standard UI components will already be familiar to the majority of user's and there is minimal learning curve for the browsing- or consumer- users.  

Bootstrap 4 was chosen, over Bootstrap 5, for use with jQuery and support IE 10 and 11.
  
Wireframe sketches were drawn up in Balsamiq. These reflect basic layout considerations rather than aesthetics.

### Database Structure   - INCOMPLETE
The diagram below demonstrates the relationships between the project's models (database tables).  
  
## Features  
  
### Responsive Design

Acme Events is fully responsive and can be enjoyed on a wide range of devices. The site and its content will adapt to create the best user experience.  
  
<img src="https://acme-events.s3.eu-west-1.amazonaws.com/media/readme/screencapture-acme-events-events-list-mobile.png" alt="Event list as rendered on a small mobile screen of 320px width" width="50%" height="auto">
  
### Accounts  
  
Users can create an account to store default checkout information as well as a history of their bookings. This latter point is useful both in terms of record-keeping and as a convenient means to access one's booking information upon arrival at an event. Default information can be saved at the time of checkout and this can then be overwritten during subsequent checkouts should the information need to be updated. Equally, the information can be updated from the "My Bookings" section without needing to checkout.  
  
<img src="https://acme-events.s3.eu-west-1.amazonaws.com/media/readme/screencapture-acme-events-herokuapp-profile.png" alt="The profile section of the site visible to a logged-in user" width="75%" height="auto">
  
Login is required in order to view the "My Bookings" section as each iteration of this page is specific to one account. Similarly, user authentication ensures that only appropriate pages and options are shown to users according to their logged-in status and role.  
  
<img src="https://acme-events.s3.eu-west-1.amazonaws.com/media/readme/acme-events-sign-in.png" alt="Sign in page" width="75%" height="auto">
  
At the time of account creation, email verification is required, thereby reducing malicious behaviours such as bot sign-ups which would otherwise unecessarily increase the burden on the site and its storage costs.  
  
### Events  
One of the site's primary functions is simply to display event information. It does this in two ways, firstly with a chronological overview of events and secondly with a more detailed event-specific page for each event the site-owner has marked "published" and which is not yet expired.  
  
<img src="https://acme-events.s3.eu-west-1.amazonaws.com/media/readme/screencapture-acme-events-detail-mobile.png" alt="Event detail view as rendered on a small mobile screen of a desktop" width="50%" height="auto">
  
Events that have expired (ie. are now in the past) are not rendered but remain in the database for the admin's records. Events that are not marked "published" by the admin exist in the database but are not rendered for the user to see and this allows the admin to draft events wihout making them public, easing their workload.  
  
<img src="https://acme-events.s3.eu-west-1.amazonaws.com/media/readme/screencapture-acme-events-events-list.png" alt="The website's events list showing two events, one with an automatically-added placeholder image and one with an admin-selected image" width="75%" height="auto">
  
Events are linked to Locations (ie. venues), so that a company that hosts events in many of the same venues repeatedly does not have to re-enter location or venue information each time but can simply select the Location to use from the existing records. New Locations can also be added, as well being updated or deleted entirely as needed.  
  
In addition to location information, event data can include time and date information, short and long descriptions, ticket prices, and images. If an event lacks a featured image for any reason, a placeholder image will automatically be rendered instead. This is also true for the featured image associated with a Location.  
  
Events also feature a capacity variable, although this is not currently in use within the site but could be readily developed as a future feature. Likewise, an end_date variable exists which would be integrated into the site's logic to accomodate multi-day events, however, this would also be a future feature and is not currently in use within the site.  
    
### Online Transactions  
The other core component of the site is its ability to act as an e-commerce platform, allowing users to make the leap from browsing to purchasing with relative ease and at the moment of peak interest in the event(s) in question.

Bookings can be make for one or more events, and customers can book for one or more persons (ie. multiple tickets). Payments are processed by Stripe through the integrated payment form. This naturally requires the site owner to have a Stripe account, and naturally, a small percentage of the transaction will be paid over to Stripe in the form of fees. This is all handled automatically and Stripe issues invoices and suitable tax documents for business owners at regular intervals, making the administration burden of e-commerce in this form reasonably low and the costs always significanly lower than the revenue gained.  
  
<img src="https://acme-events.s3.eu-west-1.amazonaws.com/media/readme/acme-events-cart-page.png" alt="Screenshot shows the cart page options as shown on desktop, along with the cart icon in the navbar which indicates the number of tickets in the cart" width="70%" height="auto">
  
From the customer's perspective, this is a simple and convenient process with a quick checkout and the security and reassurance of using a known and reputable payment processor. The online shopping experience is straightforward and includes the option to modify would-be purchases before payment by updating cart contents or removing an item entirely as needed.  

### Error Handling and Feedback  
The site includes error handling that aids the user rather than causing alarm or frustration. This includes card errors, form validation, custom error 404 and 500 pages and concenient feedback in small, self-dismissing notifications.  
  
<img src="https://acme-events.s3.eu-west-1.amazonaws.com/media/readme/acme-events-500.png" alt="Custom Error 500 page" width="75%" height="auto">
  
Feedback also extends to a small icon in the shopping card icon visible on larger screens, presenting the number of items, if any, in the user's cart.  
  
To aid the user in navigating the site, the checkout page is not accessible when the user's cart is empty and instead, the user is redirected to the Events page with a notification informing them that their cart is currently empty. The checkout-succeess page is only assessible with suitable parameters and visiting the url `/checkout-success` with no additional parameters results in a 404 page with a prompt to return home.  
  
<img src="https://acme-events.s3.eu-west-1.amazonaws.com/media/readme/acme-events-no-items-in-cart.png" alt="Feeback informing user there are not items in their cart" width="25%" height="auto">
  
To prevent accidentaly sign out, confirmation is required before signing out.  
  
<img src="https://acme-events.s3.eu-west-1.amazonaws.com/media/readme/acme-events-sign-out.png" alt="Sign out confirmation page" width="75%" height="auto">
  
### Newsletter Sign Up  
The site features a newsletter sign up form embedded into the footer of all pages. This form is quick and easy to complete and integrated with MailChimp for maxmimum convenience to the site owner or marketing team. Users can self-select a "group" according to their interests, allowing them to receive less frequent and more targetted emails of genuine interest and relevance to them.  

<img src="https://acme-events.s3.eu-west-1.amazonaws.com/media/readme/acme-events-footer.png" alt="Newsletter sign-up form as presented in the site footer" width="75%" height="auto">
  
### Additional Features
In addition, the site uses custom 404 and 500 handlers to present the user with a UI in keeping with the rest of the site (avoiding causing undue alarm or disorientation) and a link to return 'Home', ie. the site's landing page.  
  
To reduce resource-wasting and potentially harmful bot traffic, the site's admin url has been customised. Within the admin panel, some basic listing and sorting functionality has been enabled, allowing the admin to identify bookings and other data with greater convenience.
  
### Future Features  
In addition to the features mentioned above (capacity handling and multi-day events), the site could make use of a package such as [qrcode](https://pypi.org/project/qrcode/) to turn booking IDs into QR Codes. These could be incorporated into post-sales emails as well as being displayed on the post-purchase checkout-success page and the My Bookings history section.  
  
Some aspects of the UI could be expanded to provide a more polished UX, notably the post-purchase checkout-success page which could include a detailed purchase summary.
  
## Testing  - INCOMPLETE  

<img src="https://acme-events.s3.eu-west-1.amazonaws.com/media/readme/html-validator-homepage.png" alt="HTML validator for the site's homepage showing 3 warnings not requiring alteration" width="75%" height="auto">
## Deployment  
<details><summary>
Click to Expand: Deployment Procedure
</summary></br>  
  
### Heroku  
The site was deployed to Heroku using the following procedure. Before beginning, ensure that requirements.txt is up to date. Similarly, ensure that ``DEBUG = False` in settings.py or that `DEBUG` is appropriately handled with a control flow that ensures it is only `True` in the local development environment.
  
1. An account was created on [Heroku.com](https://www.heroku.com/)  
2. Once logged in, select "Create new app".  
3. The app must then be given a unique name and the developer's region must be selected from a list of options.  
4. From the Settings tab of the next screen, select "Reveal config vars".  
5. A database url, port and secret key are required config vars which can be added in the Heroku project settings.  
6. An AWS access key and secret key (django) are also required to use the site in its current configuration, while a `USE_AWS` key can be set to `True` for the deployed version of the site.  
7. In addition, you may wish to make use of the email settings which require DEFAULT_FROM_EMAIL, EMAIL_HOST_PASS and EMAIL_HOST_USER keys to be set.  
8. You will need a `STRIPE_PUBLIC_KEY`, `STRIPE_SECRET_KEY` and `STRIPE_WH_SECRET` key.
9. Within the deploy section, select GitHub as the deployment method and authorise.
10. Input the name of the GitHub repository and click "Search", followed by "Connect".  
11. Choose either "Automatic deploys" or "Manual deploy". In this case, the developer opted for manual deploy for the initial deployment and, having verified that deployment was successful, enabled automatic deploys thereafter.  
12. Select the appropriate branch from which to deploy (in this case, the project had only the Main branch at the time of deployment).  
13. As a portfolio project, this application exists on Heroku's newly founded Eco Dynos and uses [ElephantSQL](https://elephantsql.com/) for its database.

  
### Forking & Cloning Repositories  
Forking a repository allows one to make a copy with which to experiment without affecting or jeopardising the original. This does not require any special permissions from or direct contact with the original developer provided the repository in question is public rather than private. You may wish to do this either to experiment with and learn from another party's code or aid in improving an open-source project by offering changes (note that forking is distinct from [branching](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches)). To do this, one must have a GitHub account and be logged in. Then, simply visit the main page of the repository in question, and select the "Fork" option located in the upper-right corner (desktop) as shown in the image below. [Learn more about forks from GitHub Docs](https://docs.github.com/en/get-started/quickstart/fork-a-repo#forking-a-repository).  

Forking a repository does not create locally-stored copies of its files on your computer. To achieve this, you will also need to Clone the repository. For example, you may wish to do this if you wish to have a functioning copy of another party's code in under to compile and execute it locally. Cloning options are found under the "Code" drop-down button of a repository's main page, as shown in the image below. [Learn more about cloning from GitHub Docs](https://docs.github.com/en/get-started/quickstart/fork-a-repo#cloning-your-forked-repository).  
</details>  
  
## Known Bugs  
At the time of writing, the site's webhook's feature is not fully operation. Once operational, this feature will allow bookings to be reconsituted from the data sent to Stripe when processing the payment, should the checkout form itself fail to submit to the site for any reason (for example, premature broswer closure resulting a charge being processed but no booking being created within the site's database). As a failsafe measure ensuring quality customer experience, the site should not ideally be deployed without resolving this issue, at least in the opinion of the developer.  
  
In addition, the implementation of webhooks within the site contains within it a mechanism to send post-purchase confirmation emails. At present, this feature is not operational as it is affected by the webhooks bug.  
  
# Credits:
- Hero Image (anvil) <a href="https://www.freepik.com/free-photo/close-up-photo-shoot-hammer-anvil-dark-smith-workshop_24917063.htm#query=anvil&position=1&from_view=search&track=sph">by fxquadro on Freepik</a>.  
- Event photo by igovar igovar [via Pexels](https://www.pexels.com/photo/)crop-man-forging-metal-in-smithy-4575137/
- Helpful article on Django slugs <a href="https://learndjango.com/tutorials/django-slug-tutorial">from Learn Django</a>.  

<!-- - <a target="_blank" href="https://icons8.com/icon/77797/metal">Site Favicon: "Metal"</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a> -->