import os
import sys
from flask import Flask, request, jsonify

# Ensure we can import from tools folder
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from tools.llm_converter import generate_playwright_code
from tools.file_manager import save_converted_file

app = Flask(__name__, static_folder="static", static_url_path="")

@app.route("/")
def index():
    return app.send_static_file("index.html")

@app.route("/api/convert", methods=["POST"])
def convert():
    try:
        data = request.json
        source_code = data.get("sourceCode")
        target_lang = data.get("targetLanguage", "javascript")
        
        if not source_code:
            return jsonify({"status": "error", "errorDetails": "No source code provided"}), 400
            
        print(f"Starting conversion to {target_lang}...")
        playwright_code = generate_playwright_code(source_code, target_lang)
        
        print("Saving file...")
        output_path = save_converted_file(playwright_code, target_lang)
        
        return jsonify({
            "status": "success",
            "convertedCode": playwright_code,
            "outputDirectoryPath": output_path
        })
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({
            "status": "error",
            "errorDetails": str(e)
        }), 500

if __name__ == "__main__":
    app.run(debug=True, port=3000)
