# Testing

## Manual Testing

Here are a list of manual tests carried out to ensure that the Taskosaurus backend API works correctly at time of deployment. These tests are designed to test each created view for functionality. I will not be testing authorisation routes for the Django Rest Framework as those can be assumed to work correctly.

## Root Route View

* The Root Route exists purely to demonstrate that the API is working as intended.

    * Test: A non-logged in user should see the message: "Welcome to Taskosaurus API!".
    * Result: A non-logged in user does see the message: "Welcome to Taskosaurus API!".
    * Test: A logged in user should see the message: "Welcome to Taskosaurus API!".
    * Result: A logged in user does see the message: "Welcome to Taskosaurus API!".