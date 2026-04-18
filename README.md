# Selenium to Playwright TS/JS LLM Converter

A local, deterministic API and web interface for seamlessly migrating standard Selenium Java TestNG codebases to modern Playwright JavaScript/TypeScript setups. Built using the B.L.A.S.T Protocol's 3-Layer Architecture rules to guarantee maximum privacy and robust parsing, utilizing your offline hardware models via Ollama. 

## ⚡ Key Features

- **100% Offline via Local LLMs**: Zero external API dependencies. Translates code via your local `codellama:latest` daemon utilizing Ollama.
- **Glassmorphism Web UI**: A stunning, animated Vanilla HTML/CSS interface that handles code pasting, model loading feedback, and 1-click clipboard options.
- **Automated Directory Deliverables**: Rather than solely displaying in the interface, the back-end automatically stages and copies your finalized code into timestamped `.ts` or `.js` structures in an isolated `delivery/` directory to prevent data loss.
- **3-Layer Separation of Concerns**: Strict delineation between Architecture SOPs, Navigation Logic (Python Flask Server), and tools logic (`tools/llm_converter.py`). 

## 🚀 Getting Started

### Prerequisites
- [Python 3.9+](https://www.python.org/downloads/)
- [Ollama](https://ollama.com/) running securely on `localhost:11434`
- The `codellama:latest` standard model downloaded (`ollama run codellama`)

### Installation 

1. **Clone the repository**:
```bash
git clone https://github.com/sreenietltesting17-sys/Project2-Seleniumt2PlaywrightconverterLocalLLM.git
cd Project2-Seleniumt2PlaywrightconverterLocalLLM
```

2. **Install core environment dependencies**:
```bash
pip3 install flask requests
```

### Usage

1. **Launch the Flask Application Server:**
```bash
python3 navigation/app.py
```
*(The server binds cleanly to `http://localhost:3000`)*

2. **Open your browser** and visit `http://localhost:3000`.
3. Paste standard Selenium TestNG java strings (or the inner class methodologies) into the source window.
4. Select your target framework execution language (**JavaScript** or **TypeScript**).
5. Watch the `codeLlama` engine generate the Playwright code and safely save it into `delivery/`.

## 🏗️ Architecture Matrix
- `architecture/converter_sop.md`: Rules and constraints that lock in determinism.
- `navigation/app.py`: Acts as the router handling traffic and HTML rendering.
- `navigation/static/`: Vanilla UI logic (Glassmorphism design system).
- `tools/llm_converter.py`: Safe, isolated payload requests to the LLM.
- `tools/file_manager.py`: Controls strict disk creation routines inside `.tmp/` and `/delivery/`.
