# MenuNest Architecture

```text
User
 |
 v
Streamlit UI
 |
 v
Prompt Builder
 |
 v
AI Generator
 |
 v
JSON Validator
 |
 v
Report Renderer
 |
 v
Markdown / JSON Export
```

## Components

- `app.py`: Main Streamlit interface.
- `src/config.py`: Fixed UI options and default demo input.
- `src/prompt_builder.py`: Converts user inputs into an LLM-ready prompt.
- `src/ai_generator.py`: Returns demo data now and can later call a real LLM provider.
- `src/validators.py`: Validates generated JSON with Pydantic.
- `src/report_renderer.py`: Displays the launch plan in Streamlit.
- `src/export_utils.py`: Exports Markdown and JSON.
- `src/sample_data.py`: Stable fallback launch plan for demos.
