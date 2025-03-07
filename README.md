# 🎥 Cerebrone Video Content Generator Agent

🚀 **Cerebrone Video Content Generator Agent** is a powerful, AI-driven video generation application that leverages **LangChain, GPT-4, and Fal AI** to produce fully-automated, high-quality videos with professional voiceovers.

## ✨ Features

- **AI-Powered Video Production**
  - Deep-researched, AI-generated video scripts
  - Storyboard breakdowns with scene-by-scene details
  - Shot-by-shot planning with AI-generated prompts & voiceovers

- **Advanced Video & Voiceover Generation**
  - Asynchronous video & voiceover rendering using **Fal AI**
  - Structured and validated outputs using **Pydantic models**

- **Flexible & Configurable**
  - Customize video parameters (duration, target audience, style, etc.)
  - Robust error handling and logging for smooth execution

- **Modern API & UI**
  - **Flask** backend for scalable API handling
  - **Next.js** frontend for an intuitive user experience
  - CORS support for cross-origin accessibility
  - Health check endpoint for monitoring

## 📌 Prerequisites

Before getting started, ensure you have the following installed:

- **Python 3.11+**
- **Node.js 18+** (for the frontend)
- **Fal AI Account**
- **OpenAI API Key**
- **Serper Dev Key**
- **Docker (Optional, for containerized deployment)**

## 🔧 Installation

### 1️⃣ Clone the Repository
```sh
$ git clone https://github.com/cerebrone-ai/video-content-creation-agent.git
$ cd video-content-creation-agent
```

### 2️⃣ Backend Setup

1. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```
3. Configure environment variables:
    - Create a `.env` file inside the `backend/` directory:
    ```sh
    OPENAI_API_KEY=<your_openai_api_key>
    FAL_KEY=<your_fal_ai_key>
    SERPER_API_KEY=<Serper Key>
    ```
4. Start the backend server:
    ```sh
    cd backend
    python main.py
    ```

### 3️⃣ Frontend Setup

1. Navigate to the `frontend/` folder:
    ```sh
    cd frontend
    ```
2. Install dependencies:
    ```sh
    npm install -f
    ```
3. Configure environment variables:
    - Create a `.env.local` file inside `frontend/`:
    ```sh
    NEXT_PUBLIC_VIDEO_API_URL=http://localhost:5002/
    ```
4. Build and start the frontend application:
    ```sh
    npm run build
    npm start
    ```

## 🐳 Docker Deployment

For containerized deployment, follow these steps:

1. Copy environment variables into the project root directory:
    ```sh
    cp $PWD/backend/env.example $PWD/backend/.env.backend
    cp $PWD/frontend/env.example $PWD/frontend/.env.frontend
    ```

2. Run Docker Compose:
    ```sh
    docker-compose up --build
    ```

## 🎯 Contributing

We welcome contributions from the community! 🚀 If you'd like to contribute:

1. **Fork** the repository.
2. **Create a new branch** for your feature/fix.
3. **Commit your changes** with clear descriptions.
4. **Submit a pull request** for review.

## 📜 License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for more details.

## ⭐ Acknowledgements

- **OpenAI** for GPT-4
- **LangChain** for AI-driven workflow execution
- **Fal AI** for seamless video & voiceover generation

💡 If you find this project useful, consider giving it a **star ⭐ on GitHub**!

---
