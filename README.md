# AI-coding-agent

A small command-line interface (CLI) coding assistant built on the Google Gemini API that can help you generate, modify or inspect code with minimal effort.

---

## 🚀 Features

- Interact via CLI to ask for code snippets, refactoring, or help with programming tasks.  
- Works by calling the Google Gemini API for natural-language to code generation.  
- Supports loading custom “functions” (in `functions/`) so you can extend or automate tasks.  
- Lightweight and simple — minimal dependencies, easy to set up.

## 🧭 Getting Started

### Prerequisites  
- Python 3.10+  
- Access to Google Gemini API (you’ll need API credentials/authorization)  
- (Optional) Virtual environment to isolate dependencies

### Installation  
 Clone this repository  
```bash
git clone https://github.com/varrahan/AI-coding-agent.git
cd AI-coding-agent
```
Create and activate a virtual environment (recommended)

```bash
python3 -m venv venv
source venv/bin/activate   # Linux/macOS  
venv\Scripts\activate      # Windows
```
Install dependencies

```bash
pip install -r requirements.txt
```

### Configuration
Add your Google Gemini API credentials/key (environment variable, config file, etc).

Optionally adjust settings inside pyproject.toml or config section in main.py.

Place or implement custom “functions” in the functions/ folder as needed.

### Usage
```bash
python main.py
```
You’ll be presented with a prompt where you can type e.g.

“Generate a Python function to parse JSON and save to CSV.”

“Refactor this code snippet to use async/await.”

The agent will call the API and return the generated code or response.

## 📂 Project Structure
```
├── functions/            # Custom function definitions or API wrappers
├── call_functions.py     # Helper to load and call functions
├── main.py               # Entry point of the agent CLI
├── pyproject.toml        # Project metadata and dependencies
├── .python-version       # Python version used (for pyenv or similar)
├── .gitignore            # Git ignore rules
└── README.md             # Project documentation
```
## 💡 Extending & Customizing
Add new “functions” in the functions/ folder (e.g., templates, code tasks, or tools) and register them so the agent can call them.

Modify the prompt templates inside main.py to change how you interact with the agent.

Integrate with other APIs or services (e.g., GitHub, CI/CD, local tools) by extending call_functions.py.

Use this as a base framework for building more advanced coding assistants (e.g., GUI, web interface, multiple languages).

## 🧰 Use Cases
Quickly prototype code snippets or functions in various languages.

Automate repetitive coding tasks (e.g., boilerplate generation).

Learn or explore how an AI coding assistant might help in your workflow.

Integrate into scripts or tools where you need dynamic code generation or transformation.

## ⚠️ Limitations & Warnings
As with any AI-generated code: please review and test thoroughly before using it in production.

The underlying model may produce incorrect, inefficient or insecure code — use judgment and apply best practices.

This is a lightweight proof-of-concept rather than a full-featured IDE plugin or service.

Usage of the Google Gemini API may incur costs, usage limitations, or privacy concerns — ensure you comply with the terms of service.

