# CommentAI

CommentAI is a completely free, automated AI agent that safely engages with posts on **Instagram** and **LinkedIn**. It runs entirely on your local machine using an open-source Llama 3 model (via Ollama), meaning **zero API costs**.

It also features a beautiful, local FastAPI + React web dashboard to monitor the agent's live activity!

## Core Features
- 🧠 **Local LLM Engine**: Uses `llama3:8b` running on your local machine for high-quality, free generation.
- 🛡️ **Advanced Anti-Spam Guardrails**: 
   - Never comments on the same post twice.
   - Enforces a 3-day cooldown per creator/author.
   - Prevents semantic repetition (won't generate the same comment 5 times in a row).
   - Simulates realistic human delays between engagements.
- 📊 **Real-time Web Dashboard**: Monitor total engagement, daily limits, and a live activity log.

---

## 🚀 Setup Instructions (For Friends & Collaborators)

If you are just cloning this repository, follow these steps to get your local AI agent running.

### 1. Prerequisites
You must have the following installed on your machine:
* **Python 3.10+**
* **Node.js 18+** (for the dashboard)
* **[Ollama](https://ollama.com/)** (to run the AI models locally)

Once Ollama is installed, open your terminal and pull the Llama 3 model:
```bash
ollama pull llama3:8b
```

### 2. Install Dependencies
Clone the repository and install the backend and frontend requirements:

```bash
# Install Python dependencies
pip install -r requirements.txt

# Install Dashboard dependencies
cd "Frontend"
npm install
npm run build
cd ..
```

### 3. Configure Your Credentials
1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```
2. Open `.env` and fill in your Instagram/LinkedIn credentials.
3. Configure your safe daily limits (Recommended: 15-20 max per day, with 300 to 1800 second delays).

### 4. Run the Agent & Dashboard
The easiest way to run the application is using `pm2` to keep the agent and dashboard alive in the background:

```bash
# Install pm2 globally
npm install -g pm2

# Start the agent and the dashboard securely in the background
npx pm2 start ecosystem.config.js
```

You can now view the live CommentAI dashboard by opening your browser to: **http://localhost:8000** 🟢
