# ValentineVerses

This repository contains the backend code for ValentineVerses - a Love Letter/Poem Generator application - built using FastAPI and integrated with the Groq AI service.

## Overview

The backend provides API endpoints for generating personalized love letters and poems using the Llama 3 model via Groq's API. It receives requests from the frontend, interacts with the AI model, and returns the generated text.

## Features

*   **API Endpoints:**  Provides endpoints for generating love letters and poems.
*   **Pydantic Models:** Uses Pydantic models for request validation and data serialization.
*   **CORS Support:** Configured with CORS to allow requests from the frontend.
*   **AI Integration:** Integrates with the Groq AI service to generate text.
*   **Environment Variable Configuration:**  Loads API keys and other configuration from environment variables.
*   **Error Handling:** Implements robust error handling to manage exceptions and provide informative error messages to the client.

## Technologies Used

*   **FastAPI:** A modern, high-performance web framework for building APIs with Python.
*   **Pydantic:** A data validation and settings management library using Python type annotations.
*   **Groq:** A service providing access to the Llama 3 model.
*   **Python:** The primary programming language.
*   **Uvicorn:** An ASGI server to run the FastAPI application.

## Setup Instructions

1.  **Clone the repository:**

    ```
    git clone https://github.com/ayomikun-ade/valentineverses.be.git
    cd valentineverses.be.
    ```

2.  **Create a virtual environment (recommended):**

    ```
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**

    ```
    pip install -r requirements.txt
    ```

4.  **Environment Variables:**

    *   Create a `.env` file in the root directory.
    *   Add your Groq API key.

    ```
    GROQ_API_KEY=YOUR_GROQ_API_KEY
    ```

5.  **Run the application:**

    ```
    uvicorn main:app --reload
    ```

    The application will be accessible at `http://localhost:8000` (or the port configured in your `uvicorn` command).

## Endpoints

*   **`POST /generate-love-letter`:** Generates a love letter based on the provided sender and receiver names, and additional information.  Accepts a JSON body with the following structure:

    ```
    {
      "sender_name": "John Doe",
      "receiver_name": "Jane Smith",
      "additional_info": "You mean the world to me!"
    }
    ```

    Returns a JSON response with the generated love letter:

    ```
    {
      "love_letter": ["Line 1 of the letter", "Line 2 of the letter", ...]
    }
    ```

*   **`POST /generate-poem`:** Generates a poem based on the provided requests. Accepts a JSON body with the following structure:

    ```
    {
      "requests": "Write about love and spring"
    }
    ```

    Returns a JSON response with the generated poem:

    ```
    {
      "poem": ["Line 1 of the poem", "Line 2 of the poem", ...]
    }
    ```

## Contributing

Contributions are welcome! Please fork the repository, create a new branch for your feature or bug fix, and submit a pull request.

**Ciao!**

