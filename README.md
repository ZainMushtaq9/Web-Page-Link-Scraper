
````markdown
# 🌐 Web Page Link Scraper

A powerful **Streamlit web application** that extracts all **URLs, internal/external links, and media links** from any public web page instantly.  
This tool is built with **Python**, **BeautifulSoup**, and **Streamlit**, providing a clean interface for link analysis, SEO research, and content audits.

---

## 🖼️ Screenshots

### 🔹 Home Interface
![Screenshot 1](1%20web.jpg)

### 🔹 Extraction Results
![Screenshot 2](2%20web.jpg)

### 🔹 Export Options
![Screenshot 3](3%20web.jpg)

> 📸 All screenshots (`1 web.jpg`, `2 web.jpg`, `3 web.jpg`) are stored in the same folder as this README file.

---

## 🚀 Live Demo

Try it now on Streamlit Cloud:  
👉 **[Open Live Demo — Web Page Link Scraper](https://web-page-link-scraper.streamlit.app/)**

---

## 🧩 Features

✅ Extracts **all hyperlinks** (internal & external)  
✅ Finds **media URLs** (images, videos, audios)  
✅ Exports results to **CSV / Excel**  
✅ Displays link statistics & domain insights  
✅ Clean, simple Streamlit interface  
✅ 100% browser-based — no installation required for users  

---

## 🧠 Tech Stack

- **Python 3.10+**
- **Streamlit** — web UI framework  
- **BeautifulSoup4** — HTML parsing  
- **Requests** — fetching web pages  
- **Pandas** — data manipulation and export  

---

## ⚙️ Run Locally

Follow these steps to run the scraper on your computer 👇

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/ZainMushtaq9/Web-Page-Link-Scraper.git
cd Web-Page-Link-Scraper
````

### 2️⃣ Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
# On macOS/Linux
source venv/bin/activate
# On Windows
venv\Scripts\activate
```

### 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the App

```bash
streamlit run app.py
```

Once the server starts, open your browser and go to:

```
http://localhost:8501
```

---

## 📦 Example requirements.txt

```
streamlit>=1.20.0
beautifulsoup4
requests
pandas
```

---

## 🧰 Usage

1. Enter any **website URL** (e.g., `https://example.com`).
2. Click **Scrape Links**.
3. View categorized results:

   * Internal links
   * External links
   * Media links (images, videos)
4. Export results as **CSV** or **Excel** for reporting.

---

## 📡 Deployment (Streamlit Cloud)

This app is already live at:
👉 **[https://web-page-link-scraper.streamlit.app/](https://web-page-link-scraper.streamlit.app/)**

To deploy your own version:

1. Fork or push the repo to your GitHub.
2. Go to [Streamlit Cloud](https://share.streamlit.io).
3. Click **New App** → Select your repo.
4. Choose branch and set file path to `app.py`.
5. Click **Deploy** — your app will go live automatically.

Your deployed app will look like:

```
https://web-page-link-scraper.streamlit.app/
```

---

## 🪪 License

This project is licensed under the **MIT License** — you’re free to use, modify, and distribute it.

---

## 👨‍💻 Author

**Zain Mushtaq**
🔗 [GitHub Profile](https://github.com/ZainMushtaq9)
🚀 [Live App](https://web-page-link-scraper.streamlit.app/)

---

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://web-page-link-scraper.streamlit.app/)

```
```
