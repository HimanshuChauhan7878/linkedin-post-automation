📌 LinkedIn Post Automation – AI Agent (Ollama + Selenium)

This project is a fully functional AI Agent that autonomously generates, prepares, and posts LinkedIn content using a single user prompt.
It combines local LLM reasoning, browser automation, and agentic workflow execution.

With one command, the agent will:

1.Take your prompt
2.Generate a polished LinkedIn post using Ollama (Llama 3.1)
3.Ask for confirmation
4.Open Chrome with your existing logged-in LinkedIn profile
5.Navigate to LinkedIn
6.Click Start Post
7.Paste the generated content
8.You manually click the final Post (LinkedIn restriction)

This creates a seamless “AI posts for you” experience.

🚀 Features
🧠 AI Content Generation

1.Generates high-quality LinkedIn posts using Ollama (local LLM)
2.Works with any natural language prompt
3.Automatically structures the post in LinkedIn style
4.Supports tones & customization

🤖 Agentic Workflow

1.Multi-step reasoning + execution
2.Human-in-the-loop confirmation
3.Automatic Chrome launch in debugging mode
4.Automatic LinkedIn UI actions (popup closing, scrolling, Start Post click, text insertion)

🌐 Browser Automation
1.Uses Selenium + Chrome DevTools debugging
2.Runs with your real Chrome profile
3.Never requires logging in again
4.Safely bypasses LinkedIn bot posting restrictions (final click is manual)

🔧 Modular Code Structure

main.py → Agent Orchestrator
llm_agent.py → LLM logic
automation.py → Selenium automation
utils.py → Helper utilities

🛠️ Tech Stack
Component	Technology
AI Model	Ollama (Llama 3.1 or any compatible model)
Automation	Selenium WebDriver
Browser	Google Chrome (Debug Mode)
Language	Python 3.10+
Environment	Windows 10/11
Terminal	VS Code / PowerShell

📂 Project Workflow
Below is the complete workflow from user input to final LinkedIn post:

1️⃣ User Input
You run:
python main.py --cmd "Your prompt here"

2️⃣ AI Reasoning (LLM)
llm_agent.py:
Takes your prompt
Generates LinkedIn-ready content
Adds structure, brevity, hashtags, tone

3️⃣ Human Approval
You see a preview → Type "yes" to proceed

4️⃣ Browser Automation
automation.py:
Launches Chrome in debug mode
Loads Profile 2 (already logged in)
Opens LinkedIn feed
Scrolls container
Locates “Start a post” (even inside nested React layers)
Clicks Start Post
Finds text editor
Pastes AI-generated content

5️⃣ Manual Post
You click Post manually (LinkedIn policy)

6️⃣ Agent Shutdown

Selenium disconnects and Chrome stays open.
📦 Requirements
Python 3.10+
Google Chrome (version 140+ recommended)
VS Code / PowerShell
Git (optional)
Chrome Requirements
Chrome must have a persistent user profile
LinkedIn must already be logged in
No Chrome window should be open before running the agent
Python Packages

Create requirements.txt:
selenium
webdriver-manager
ollama
python-dotenv
Install packages:
pip install -r requirements.txt

⚙️ Installation
1. Clone the repository
git clone https://github.com/HimanshuChauhan7878/linkedin-post-automation.git
cd linkedin-post-automation

2. Create virtual environment
python -m venv venv

3. Activate venv
PowerShell:
.\venv\Scripts\Activate.ps1

4. Install dependencies
pip install -r requirements.txt

5. Ensure Ollama is running
Start Ollama server:
ollama serve

▶️ Usage
1. Run the agent with any prompt:
python main.py --cmd "Write a post about my new AI agent"

2. Preview appears
You type yes to proceed

3. Chrome opens
LinkedIn loads automatically

4. The AI agent:
Clicks "Start post"
Pastes content

5. You press the Post button manually
🐞 Troubleshooting
❌ Chrome opens but LinkedIn does not load
→ Ensure no Chrome window is already open
→ Project launches its own debug instance
❌ Start Post button not clicked
→ UI may be nested; ensure scroll section is visible
→ Agent includes fallback JS-clicks
❌ LLM not generating content
→ Check if Ollama is running
→ Try:
ollama pull llama3.1

🔮 Future Enhancements
Scheduled daily posting at 9 AM
Multi-platform support (Twitter/Threads)
Auto-comment or auto-engage agent
Content calendar integration
Voice command support
History of posted drafts
Multi-prompt draft choices