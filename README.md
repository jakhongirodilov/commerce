# E-commerce

This project is an online auction website that allows users to browse different categories, view listings, place bids, create their own listings, and manage their watchlist.

## Functionality

- **Categories**: The website supports the categorization of listings. Users can view different categories and browse listings within each category.

- **View Listings**: Users can view individual listings, including their title, description, image, current price, and bidding history.

- **Place Bids**: Users can place bids on active listings. If the placed bid is higher than the current highest bid, it will be saved, and the listing's price will be updated.

- **Create Listings**: Authenticated users can create their own listings by providing the title, description, image URL, price, and selecting a category.

- **Watchlist**: Users can add listings to their watchlist to keep track of interesting items. They can view their watchlist and easily remove items from it.

- **Commenting**: Authenticated users can leave comments on individual listings.

- **Closing Auctions**: The owner of a listing can close the auction, marking it as inactive and displaying a notification on the listing page.

- **User Authentication**: Users can register, log in, and log out of their accounts. Authentication is required for certain actions such as creating listings, placing bids, and leaving comments.

## Installation

To run the project locally, follow these steps:

1. Clone the repository:

```
git clone https://github.com/your-username/online-auction.git
```

2. Navigate to the project directory:

```
cd online-auction
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Apply database migrations:

```
python manage.py migrate
```

5. Start the development server:

```
python manage.py runserver
```

6. Access the website at `http://localhost:8000` in your web browser.

Note: Make sure you have Python and Django installed on your system.

## Contributing

If you'd like to contribute to this project, follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch with a descriptive name.
3. Make your changes and additions.
4. Commit and push your changes to your forked repository.
5. Submit a pull request detailing your changes and the problem or feature they address.

Please ensure that your contributions align with the project's coding style and guidelines.


## Contact

For any questions or inquiries, please contact odilovjakhongir@gmail.com, www.linkedin.com/in/jakhongirodilov.

---

Feel free to customize the README file based on your project's specific requirements, additional features, or any other relevant information you'd like to include.
