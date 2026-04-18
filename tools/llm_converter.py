import json
import urllib.request
import urllib.error
import re

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "codellama:latest"

def generate_playwright_code(selenium_code: str, target_lang: str) -> str:
    """
    Calls the local Ollama LLM to convert Selenium Java code to Playwright TS/JS.
    """
    system_prompt = (
        f"You are an expert SDET. Your single task is to convert the provided Selenium Java TestNG code "
        f"into perfect Playwright {target_lang} code.\n"
        f"Rules:\n"
        f"1. Implement a 1:1 mapping of logic.\n"
        f"2. Keep all original comments.\n"
        f"3. Return ONLY valid {target_lang} code without any markdown wrappers, no ```javascript or ```typescript blocks, "
        f"just the raw text code.\n"
        f"4. ONLY use modern Playwright Locator API (e.g., `page.locator('...').click()`, `page.locator('...').textContent()`). DO NOT use outdated ElementHandles like `page.$()` or `page.$$()`.\n"
        f"5. If a mapping is impossible, leave a comment: '// TODO: mapping requires manual intervention'."
    )
    
    payload = {
        "model": MODEL_NAME,
        "prompt": f"System: {system_prompt}\n\nUser Code:\n{selenium_code}",
        "stream": False,
        "options": {
            "temperature": 0.1
        }
    }
    
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(OLLAMA_URL, data=data, headers={'Content-Type': 'application/json'})
    
    try:
        with urllib.request.urlopen(req, timeout=120) as response:
            result = json.loads(response.read().decode('utf-8'))
            code_result = result.get("response", "").strip()
            
            # DeepSeek might still output <think> tags or markdown. Clean it up.
            if "</think>" in code_result:
                code_result = code_result.split("</think>")[-1].strip()
                
            # Use regex to extract from markdown blocks if available.
            match = re.search(r"```[a-zA-Z]*\n(.*?)\n```", code_result, re.DOTALL)
            if match:
                code_result = match.group(1).strip()
            # Fallback if no closing tick found but starts with tick
            elif code_result.startswith("```"):
                lines = code_result.split("\n")
                if len(lines) > 2:
                    code_result = "\n".join(lines[1:-1])
            return code_result
    except urllib.error.URLError as e:
        raise Exception(f"Failed to connect to Ollama. Ensure Ollama is running and has {MODEL_NAME}. Error: {str(e)}")
    except Exception as e:
        raise Exception(f"LLM Processing Error: {str(e)}")

# Minimal handshake test block
if __name__ == "__main__":
    test_code = "driver.get(\"https://google.com\");"
    print("Testing handshake with Ollama.")
    try:
        print(generate_playwright_code(test_code, "javascript"))
        print("Handshake successful!")
    except Exception as e:
        print("Handshake failed:", e)
