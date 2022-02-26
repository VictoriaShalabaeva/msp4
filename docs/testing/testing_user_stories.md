# Testing User Stories

### **As a shopper**:

 **I want to view a list of products and select some to purchase.**
  
  - A shopper can click the links in the navigation bar or on the button *Shop Now* and be redirected to the corresponding products page. 

    <img src="images/user_stories/all_products.jpg" alt="All products." width="500px" height="auto">
  
  - The *All Products* page display all products available in the webshop. 

    <img src="images/user_stories/list_of_products.jpg" alt="All products." width="500px" height="auto">


**I want to view individual products details and identify the price, description, product rating, product image and available colors.** 

  - A shopper can click the product of interest and be redirected to a *Product Details* page. Here he will find more detailed information on a specific product.

    <img src="images/user_stories/product_details.jpg" alt="Product details page." width="500px" height="auto">

**I want to easily select the color and quantity of a product when purchasing it.**

  - In the *Product Details* page, a shopper can select a color and quantity of each product.

    <img src="images/user_stories/color_and_quantity.jpg" alt="Product color and quantity." width="500px" height="auto">

  - The quantity of the product can be further adjusted on the *Shopping Bag* page.

    <img src="images/user_stories/product_quantity_in_shopping_bag.jpg" alt="Product quantity on the shopping bag page." width="500px" height="auto">

**I want to view reviews left by other customers for products (to understand whether the product is worth purchasing).**

  - Before taking a decision on purchasing any product, a shopper can read reviews on a specific product left by other users."

    <img src="images/user_stories/reviews.jpg" alt="Product reviews." width="500px" height="auto">

**I want to leave a review on a product, so that other users may be able to benefit from my opinion on a specific product.**

  - On the *Product details* page, a shopper can click the *Add a Review* button to write a review (see an image with an *Add a Review* button above). When clicking the button, a shopper can write a review by filling in a form.

    <img src="images/user_stories/add_review.jpg" alt="Add Review page." width="200px" height="auto">

**I want to be able to edit or delete my reviews (in case I change my opinion).**

  - After a review submission, a shopper can edit (or delete) his reviews by clicking *Edit* (or *Delete*) buttons available at the bottom of each review. Upon clicking the *Edit* button, a shopper is redirected to an *Edit Review* page to resubmit a form. If the *Delete* button is clicked, the review is deleted and an info message is shown.

    <img src="images/user_stories/edit_review.jpg" alt="Edit Review page." width="500px" height="auto">

**I want to sort the list of available products and easily identify the best rated, best priced, categorically and brand sorted products.**

  - Products can be sorted from the dropdown menu in the navigation bar.

    <img src="images/user_stories/products_sorting.jpg" alt="Product sorting from dropdown menu." width="500px" height="auto">

**I want to sort a specific category of products (to find the best priced or best rated products in a specific category, or sort the products in that category by name or brand).**

  - A specific category of products can be chosen from the navigation bar and then be further sorted from the filter box.

    <img src="images/user_stories/products_sorting_filter_box.jpg" alt="Product sorting from filter box." width="500px" height="auto">

**I want to search by name, brand or description to find a specific product I would like to purchase.**

  - A shopper can search by name, brand or description to find a specific product using a search box on the top of each page.

    <img src="images/user_stories/search_bar.jpg" alt="Search bar." width="500px" height="auto">

**I want to easily see what I have searched for and the number of results.**

  - A shopper can easily view a number of search results.

    <img src="images/user_stories/search_result.jpg" alt="Search results." width="500px" height="auto">

**I want to view items in my bag to be purchased.**

  - The items to be purchased can be viewed on the *Shopping Bag* page. 

    <img src="images/user_stories/items_in_shopping_bag.jpg" alt="Items in the shopping bag." width="500px" height="auto">
    
  - When a new item is added to a shopping bag, the summary of items can be seen in the info box that appears in the top right corner.

    <img src="images/user_stories/info_box.jpg" alt="Info box." width="200px" height="auto">

**I want to adjust the quantity of individual items in my bag.**

  - The product quantity can be adjusted on the *Shopping Bag* page (please see image above).

**I want to easily view the total of my purchases at any time to avoid spending too much.**

  - A shopper can view the total of his purchases at the top right corner of each page. 

    <img src="images/user_stories/bag_total.jpg" alt="Bag purchases total." width="500px" height="auto">

**I want to easily enter my payment information and check out quickly without hassles**

  - A shopper can click the "Secure Checkout" button either from a *Shopping bag* page or from an info window with a shopping bag summary.

    <img src="images/user_stories/secure_checkout.jpg" alt="Secure checkout buttons." width="500px" height="auto">

  - On the *Checkout* page a shopper will find a form to fill in a delivery information (if a shopper is logged in, the delivery information will be pre-populated). If the user is not logged in, the order will be processed for an anonymous user. 
  
  - A shopper can view a summery of his order. 

    <img src="images/user_stories/checkout_page.jpg" alt="Checkout page." width="500px" height="auto">
  
  - The payment information is on the bottom of the page, the validation is done via Stripe. Clicking the *Complete Order* button will display an overlay with a spinning icon while the payment is processed. 

    <img src="images/user_stories/overlay.jpg" alt="Overlay with a spinning icon while the payment is processed." width="500px" height="auto">

**I want to view an order confirmation after checkout.**

- A user can view the *Checkout Success* page with a success info message on the top right corner of the page, summary of his order and delivery information. A user also receives a confirmation email on his order.

    <img src="images/user_stories/complete_order.jpg" alt="Checkout Success page." width="500px" height="auto">

**I want to create my wishlist (to add and remove products).**

- On the *Product Details* page, a logged in user can view a button *Add to Wishlist* (not logged in users can't view this button). When clicking this button, products are added to the user's wishlist. 

  <img src="images/user_stories/add_to_wishlist_btn_2.jpg" alt="Add to Wishlist button on Product Details page." width="500px" height="auto">

- It is possible to add several colors of the same product to a wishlist.  

    <img src="images/user_stories/different_colors_in_wishlist.jpg" alt="Different colors of the same product in Wishlist." width="500px" height="auto">

- If an user tries to add the same item to a wishlist (the same product with the same color), he will see a warning message that the product is already in his wishlist.

  <img src="images/user_stories/add_to_wishlist_btn_and_warning_message.jpg" alt="Warning message that product is already in Wishlist." width="500px" height="auto">

- In order to access a wishlist, a user can click the *heart* icon on the navigation bar. The page with a wishlist will list all added products. Products can be removed from wishlist by clicking the *Remove* button.

    <img src="images/user_stories/wishlist_page.jpg" alt="Wishlist page." width="500px" height="auto">

- If a not logged in user clicks the heart icon on the navigation bar, he will be redirected to *Sign In* page.

**I want to add items to the shopping bag directly from my wishlist.**

- A user can add items to a shopping bag directly from the *Wishlist* page (see image above).

---

### **As a site user:**

**I want to easily register for an account and receive an email confirmation.**

- A user can click the *Register* on *My Account* tab on the navigation bar.

    <img src="images/user_stories/register_btn.jpg" alt="Register tab." width="200px" height="auto">

- A user can view *Sign Up* page and fill in a form.

    <img src="images/user_stories/signup.jpg" alt="Sign Up page." width="400px" height="auto">

- After form submission, a user will receive a confirmation email.

  <img src="images/user_stories/confirmation_email.jpg" alt="Confirmation email." width="500px" height="auto">

- A user should check his email and open the link to view a *Confirm Email Address* page.

    <img src="images/user_stories/confirm_email_address.jpg" alt="Confirm email address page." width="500px" height="auto">

- After a user clicks the *Confirm* button, he will be redirected to *Sign In* page and view the success info message.

    <img src="images/user_stories/success_confirmation.jpg" alt="Successful email confirmation." width="500px" height="auto">

**I want to easily login/logout and to view my profile.**

- A user can click the *Login* on *My Account* tab on the navigation bar.

    <img src="images/user_stories/login_btn.jpg" alt="Login tab." width="200px" height="auto">

- A user can view *Sign In* page and fill a form with his email address and password.

    <img src="images/user_stories/signin.jpg" alt="Sign Ip page." width="300px" height="auto">

- After signing in, a user is redirected to *My Profile* page.

    <img src="images/user_stories/my_account_page.jpg" alt="My Profile page." width="400px" height="auto">

- A user can logout by clicking the *Logout* button on *My Account* tab on the navigation bar.

    <img src="images/user_stories/logout_btn.jpg" alt="Logout tab." width="200px" height="auto">

- A user can view the *Sign Out* page and click *Sign Out*.

    <img src="images/user_stories/signout.jpg" alt="Sign Out page." width="200px" height="auto">  

**I want to easily recover my password in case I forget it.**

- On the *Sign In* page, a user can click *Forgot password* in case he forgot it. 

    <img src="images/user_stories/reset_password_page.jpg" alt="Reset password page." width="200px" height="auto"> 

- After filling in an email address, an email with a link to reset password will be sent.

    <img src="images/user_stories/reset_password_email.jpg" alt="Reset password email." width="200px" height="auto"> 

- After clicking a link received by email, a user is redirected to *Change Password* page.

    <img src="images/user_stories/change_password.jpg" alt="Change Password page." width="200px" height="auto"> 

- After a user has submitted a new password for his account, he will view a successful info message. by clicking *Set Password*, he will be redirected to *Sign In* page.

    <img src="images/user_stories/password_change_successful.jpg" alt="Password changed successfully." width="500px" height="auto"> 

**I want to view my personal order history and save my delivery information.** 

- On *My Profile* page, a user can view his order history and update his delivery information.

    <img src="images/user_stories/delivery_info_and_order_history.jpg" alt="Delivery information and order history on My Profile page." width="500px" height="auto">

---

### **As a store owner:**

**I want to add new items to my store.**

- When logged in as an admin, a user can view an additional link to a *Product Management* page (equivalent to *Add a Product* page) on the *My Account* tab.

    <img src="images/user_stories/product_management_btn.jpg" alt="Product Management button." width="200px" height="auto">

- A store owner can add a new product by filling in a form.

    <img src="images/user_stories/add_product_page.jpg" alt="Product Management page." width="300px" height="auto">

**I want to edit/update products details.**

- A store owner can edit product details by clicking the *Edit* button either from *Products* page or from individual *Product Details* page.

    <img src="images/user_stories/edit_btn.jpg" alt="Edit product button." width="500px" height="auto">

- On the *Edit a Product* page, a store owner will see a prefilled form. He can make changes to the fields and save them.

    <img src="images/user_stories/edit_product_page.jpg" alt="Edit product page." width="300px" height="auto">

**I want to delete items that are no longer for sale.**

- A store owner can delete products by clicking the *Delete* button either from the *Products* page or from individual *Product Details* page. Please see image related to *Edit* button (above).

- When *Delete* button is pressed, a message will appear informing that the product was deleted. It would be useful to implement a popup window with a question whether a store owner is sure to delete a product. This is left as a future feature to apply.

    <img src="images/user_stories/product_deleted_message.jpg" alt="Product deleted message." width="200px" height="auto">

**I want to provide users with updates to any action.**

- Whatever action is performed by any user (whether it is a customer or a store owner), the user is always notified with info messages appearing on the right top of the page. The examples of such messages can be seen above in several images throughout the present document.