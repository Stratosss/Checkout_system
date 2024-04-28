#  Checkout system
## Overview
This project concerns a shopping checkout system application. The concept is that there are four products available, each with a price per unit. Some products have a special price when bought in certain quantities (e.g. 3 of product A costs 140, not 150).
The checkout system consumes a data source (e.g. JSON file) and returns the sub total when queried.
There are two functions in this application which are analysed below.
The application opens the JSON file and initially converts it into a list of dictionaries.
- The first function taps into each list item and then creates a dictionary with product labels as keys, and values for their respective quantities.
Then, it validates if the input data are correct before proceeding with calculations, otherwise it terminates the application in a controlled fashion.
The application will terminate and throw an error message if:
  - Wrong item code is given.
  - Quantity value is either string or decimal.
  - Quantity value is a negative number.
- The second function dynamically performs the calculations for the total.
The function considers the discounts and applies them to every other number of items bought. For example, product A costs £50 / unit, and one can buy 3 units for £140, if someone buys 6 units, they pay twice the discount price: 140+140= £280.
Finally, the function returns the total for printing out.

The application comes with a separate testing file, that performs eleven individual tests that check for all the above, to ensure that the application functions as it should. The testing file utilises the unit test framework library of Python.
