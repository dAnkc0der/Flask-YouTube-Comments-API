# Submission-ylytic

This repository contains a Flask API that provides a search interface for fetching comments from a YouTube video using the Ylytic API. The API supports various search parameters such as author name, date range, like and reply count range, and search text.

## Getting Started

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/submission-ylytic.git
   cd submission-ylytic

2. Install the required dependencies using pip:

    ``` pip install flask ```.

3. Run the Flask app:- The API will be accessible at http://127.0.0.1:5000.

    ```python app.py```.

4. Query Parameters
   
    search_author: Search comments by author name.

    at_from and at_to: Search comments within a date range.

    like_from and like_to: Search comments with a like count range.

    reply_from and reply_to: Search comments with a reply count range.

    search_text: Search comments containing specific text.

# Examples

1. Search by author: 

    ```http://127.0.0.1:5000/search?search_author=Fredrick```

2. Combined search:

    ```http://127.0.0.1:5000/search?search_author=Fredrick&at_from=2023-01-01&at_to=2023-02-01&like_from=0&like_to=5&reply_from=0&reply_to=5&search_text=economic```
