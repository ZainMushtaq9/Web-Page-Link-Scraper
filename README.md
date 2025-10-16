# 🔗 Web Link Scraper

A simple yet powerful web scraper application built with Python, Streamlit, and BeautifulSoup. This tool provides an interactive UI to enter any website URL and a specific keyword, then extracts all hyperlinks from the page that contain that keyword.

The results are displayed cleanly in the app, making it a handy tool for quick data extraction and link analysis.

---

## ✨ Features

- **Interactive Web UI**: Clean and simple interface built entirely in Python with Streamlit.
- **Dynamic Scraping**: Allows users to input any target URL and a custom keyword to filter links.
- **Robust Link Handling**: Correctly constructs full, absolute URLs from relative paths (e.g., from `/page` to `https://example.com/page`).
- **Error Handling**: Gracefully handles invalid URLs and common network errors during the scraping process.
- **Realistic Requests**: Mimics a real browser by sending a `User-Agent` header, increasing the chance of a successful scrape.

---

## 🛠️ Technologies Used

- **Python 3**
- **Streamlit**: For building the interactive web application.
- **BeautifulSoup4**: For parsing HTML and extracting data.
- **Requests**: For making robust HTTP requests.

---

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

You need to have Python 3.7+ installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
    cd your-repository-name
    ```

2.  **Create and activate a virtual environment (recommended):**
    -   **On macOS/Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    -   **On Windows:**
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

3.  **Install the required dependencies:**
    Create a `requirements.txt` file with the following content:
    ```
    streamlit
    beautifulsoup4
    requests
    ```
    Then, run the following command to install them:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```
    Your web browser will automatically open with the running application.

---

## Usage

1.  Once the app is running, enter the full URL of the website you want to scrape (e.g., `https://news.google.com/`).
2.  Enter a keyword that should be present in the links you want to find (e.g., `articles`).
3.  Click the **"Scrape for Links"** button.
4.  The app will display the total number of links found and list them below.

---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.
