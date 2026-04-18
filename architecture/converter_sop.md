# Converter Standard Operating Procedure (SOP)

## Purpose
This SOP governs the logic for converting standard Selenium Java/TestNG scripts into Playwright JavaScript/TypeScript scripts utilizing an LLM backend (Ollama).

## Input Constraints
1. **Source Code**: Raw string containing Selenium Java imports, annotations (e.g. `@Test`), and class/method logic.
2. **Target Language**: `javascript` or `typescript`.
3. **Model**: The standard model utilized for this operation is `codellama:latest`.

## Execution Mechanics
1. **Tool Invocation**: `navigation/app.py` delegates execution to `tools/llm_converter.py` by providing the source code and target language.
2. **System Prompt**:
   - MUST instruct the LLM to provide a 1:1 conversion.
   - MUST dictate outputting ONLY raw code, with no markdown code blocks (or explicitly stripping them in post-processing).
   - Preserves comments.
3. **Response Handling**:
   - Extract code.
   - Route to `tools/file_manager.py` to save temporarily in `.tmp/` and finalizing into `delivery/` folder.
   - Return absolute paths and status to UI.

## Golden Rules
- DO NOT hallucinate business logic.
- If a Selenium API doesn't have a direct equivalent (e.g., highly specialized WebDriver options), the local LLM must insert a placeholder comment `// TODO: Manual intervention needed for ...`.
- Tools MUST remain deterministic. The API call is the only probabilistic element, and its output is strictly shaped by prompt engineering.
