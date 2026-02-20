# Dashboard Portfolio with AI Chatbot

A modern, dashboard-style portfolio website built with Flask, HTML, CSS, and JavaScript. It features a glassmorphic design, responsive layout, and an integrated AI chatbot powered by Groq to answer questions about the portfolio owner.

## Features

-   **Dashboard UI:** Sidebar navigation, widget-based content (Profile, Skills, Projects, Experience).
-   **Glassmorphism:** Premium aesthetic with semi-transparent, blurred elements.
-   **AI Chatbot:** Uses Groq API (Llama 3.3) to answer questions based on the resume.
-   **Responsive:** optimized for desktop and mobile devices.
-   **Dynamic Content:** Populated from `G ROSHNI PROFFESIONAL RESUME.pdf`.

## Project Structure

-   `app.py`: Main Flask application.
-   `templates/`: HTML templates (`layout.html`, `dashboard.html`).
-   `static/`: CSS styles and JavaScript files.
-   `requirements.txt`: Python dependencies.
-   `Procfile`: Deployment configuration for Render.

## Setup & Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd PORTFOLIO2
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the application:**
    ```bash
    python app.py
    ```

4.  **Visit:** `http://127.0.0.1:5000`

## Deployment on Render

1.  Push this repository to GitHub.
2.  Log in to [Render](https://render.com/).
3.  Click **New +** -> **Web Service**.
4.  Connect your GitHub repository.
5.  Render will automatically detect the `requirements.txt` and `Procfile`.
6.  **Add Environment Variable:**
    -   Key: `GROQ_API_KEY`
    -   Value: `your_api_key_here`
7.  Click **Create Web Service**.

## Credits

-   **Developer:** G Roshni / Aspiring Web Developer
-   **Tech Stack:** Flask, HTML5, CSS3, Groq API
