# Project Constitution

## Data Schemas

### Input Schema (Raw Input)
```json
{
  "sourceCode": "string (Selenium Java TestNG Code)",
  "targetLanguage": "string (javascript | typescript)",
  "options": {
    "preserveComments": "boolean (default: true)",
    "priority": "readability"
  }
}
```

### Output Schema (Delivery Payload)
```json
{
  "status": "success | error",
  "convertedCode": "string (Playwright JS/TS Code)",
  "outputDirectoryPath": "string (Path to saved files)",
  "errorDetails": "string (if applicable)"
}
```

## Behavioral Rules
- Convert everything given in the input without omitting logic.
- Prioritize readability with 1:1 mapping from Selenium/TestNG concepts to Playwright equivalents.
- Use Local LLM for the core conversion logic.
- Do not guess business logic; leave placeholders as comments if a direct 1:1 mapping requires manual intervention.

## Architectural Invariants
- 3-layer architecture (Architecture, Navigation, Tools)
- Tools must be deterministic scripts in `tools/`
- Intermediate files in `.tmp/`
- User Interface will capture the input and display the converted output, while saving to a local directory.
