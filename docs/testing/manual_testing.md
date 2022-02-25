# Testing Functionality, Usability and Responsiveness

Functionality, Usability and Responsiveness of the key website elements were tested manually following the plan:

**Navigation:**

- The navbar automatically collapses at the lg (large) breakpoint (992px).

    <img src="images/manual_testing/navbar_collaps.jpg" alt="The navbar automatically collapses at the lg (large) breakpoint (992px)." width="500px" height="auto">

- The *My Account*,  *All Products*, *Face*, *Eyes*, *Lips* and *Nails* buttons have a dropdown menu which is toggled by clicking.

    <img src="images/manual_testing/dropdown_menu.jpg" alt="Dropdown menu." width="500px" height="auto">

- For not logged in users, *My Account* menu displays links only to 2 pages: *Register* and *Login*.
    
    <img src="images/manual_testing/links_for_not_logged_in_users.jpg" alt="Links for not logged in users." width="200px" height="auto">

- A logged in user can view the following links: *Product Management*, *My Profile* and *Logout*.
    Buttons *Log In* and *Register* disappear. 

    <img src="images/manual_testing/links_for_logged_in_users.jpg" alt="Links for logged in users." width="200px" height="auto">

- For small devices, the products menu is displayed as a dropdown menu.

    <img src="images/manual_testing/navbar_mobile_devices.jpg" alt="Products dropdown menu." width="200px" height="auto">

- All buttons of the navbar are clickable and open correct pages.

---

**Pages layout:**

- *Home* page rearranges correctly at certain breakpoints.

    <img src="images/manual_testing/home_page_layout.jpg" alt="Home page layout." width="600px" height="auto">

- *Products* page rearranges correctly at certain breakpoints.

    <img src="images/manual_testing/products_page_layout.jpg" alt="Products page layout." width="600px" height="auto">

- *Add a product* and *Edit a Product* pages rearrange correctly at certain breakpoints.

    <img src="images/manual_testing/add_product_page_layout.jpg" alt="Add a product layout." width="600px" height="auto">

- *Sign Up* and *Sign In* pages rearrange correctly at certain breakpoints.

    <img src="images/manual_testing/signup_page_layout.jpg" alt="Sign Up page layout." width="600px" height="auto">

- *Product Details* page rearranges correctly at certain breakpoints.

    <img src="images/manual_testing/product_details_page_layout.jpg" alt="Product Details page layout." width="600px" height="auto">

- *Shopping Bag* and *Wishlist* pages rearrange correctly at certain breakpoints.

    <img src="images/manual_testing/shopping_bag_page_layout.jpg" alt="Shopping Bag page layout." width="600px" height="auto">

- *My Profile* page rearranges correctly at certain breakpoints.

    <img src="images/manual_testing/my_profile_page_layout.jpg" alt="My Profile page layout." width="600px" height="auto">

- *Checkout* page rearranges correctly at certain breakpoints.

    <img src="images/manual_testing/checkout_page_layout.jpg" alt="Checkout page layout." width="600px" height="auto">

- *Checkout Success* page rearranges correctly at certain breakpoints.

    <img src="images/manual_testing/checkout_success_page_layout.jpg" alt="Checkout Success page layout." width="600px" height="auto">

---

***Register*, *Log In* and *Log Out* functionality**

A big part of *Register*, *Log In* and *Log Out* functionality testing is described in the *As a site user* section of [user stories testing](testing_user_stories.md).

Additional testing:

- The password should match a specific pattern. If the input does not match a pattern, a message appears to help users.

    <img src="images/manual_testing/password_requirements.jpg" alt="The password should match a specific pattern." width="300px" height="auto">

- If the user tries to register an account with the email that was already registered, the warning message appears.

    <img src="images/manual_testing/user_already registered.jpg" alt="Message that email already exists." width="300px" height="auto">

- If the user tries to register an account with the username that was already registered, the warning message appears.

    <img src="images/manual_testing/username_already registered.jpg" alt="Message that username already exists." width="300px" height="auto">

- If the user, trying to log in, enters an incorrect username or/and password, the warning message appears.

    <img src="images/manual_testing/incorrect_username_or_password.jpg" alt="Message that username or/and password are incorrect." width="300px" height="auto">
