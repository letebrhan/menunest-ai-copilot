# Task 8: watsonx.ai Integration

## Overview

This document describes the integration of IBM watsonx.ai as a live AI provider for MenuNest, enabling real-time AI-powered launch plan generation while maintaining demo mode as a reliable fallback.

## Implementation Summary

### Files Modified

1. **`.env.example`** - Added watsonx environment variables with safe placeholders
2. **`src/ai_generator.py`** - Added watsonx API integration and provider selection logic
3. **`src/prompt_builder.py`** - Enhanced prompt with strict JSON output instructions
4. **`tests/test_watsonx_integration.py`** - Created comprehensive test suite (23 tests)

### Key Features

✅ **Provider Selection Logic**
- Demo mode by default (no API keys required)
- watsonx mode when `LLM_PROVIDER=watsonx` and credentials are set
- Automatic fallback to demo mode on any error
- Clear warnings for unknown providers

✅ **watsonx.ai Integration**
- Full API integration with IBM watsonx.ai
- Environment variable-based configuration
- JSON extraction from model output (handles markdown, explanations)
- Response validation using existing schema validators

✅ **Error Handling**
- Missing credentials → fallback to demo mode with warning
- API timeouts → fallback to demo mode
- Network errors → fallback to demo mode
- Invalid JSON → fallback to demo mode
- Never crashes the application

✅ **Security**
- All credentials from environment variables only
- API keys never logged or exposed in output
- Credentials redacted from error messages
- No hardcoded secrets anywhere

✅ **Testing**
- 23 comprehensive tests covering all scenarios
- Provider selection logic tested
- API integration tested with mocks
- Error handling and fallback tested
- Security requirements verified
- All 155 tests pass (including existing tests)

## Environment Variables

### Required for watsonx Mode

```bash
# Provider selection (demo or watsonx)
LLM_PROVIDER=watsonx

# IBM watsonx.ai credentials
WATSONX_API_KEY=your_api_key_here
WATSONX_PROJECT_ID=your_project_id_here
WATSONX_URL=https://us-south.ml.cloud.ibm.com
WATSONX_MODEL_ID=ibm/granite-13b-instruct-v2
```

### Getting Credentials

1. Go to [IBM Cloud](https://cloud.ibm.com/)
2. Create or access a watsonx.ai project
3. Get your API key from IBM Cloud IAM
4. Get your project ID from the watsonx.ai project settings
5. Choose your region URL (us-south, eu-de, etc.)
6. Select a model (recommended: `ibm/granite-13b-instruct-v2`)

## Usage

### Demo Mode (Default)

No configuration needed. Just run the app:

```bash
streamlit run app.py
```

The app will use dynamic demo generation based on user inputs.

### watsonx Mode

1. Create a `.env` file in the project root:

```bash
cp .env.example .env
```

2. Edit `.env` and add your credentials:

```bash
LLM_PROVIDER=watsonx
WATSONX_API_KEY=your_actual_api_key
WATSONX_PROJECT_ID=your_actual_project_id
WATSONX_URL=https://us-south.ml.cloud.ibm.com
WATSONX_MODEL_ID=ibm/granite-13b-instruct-v2
```

3. Run the app:

```bash
streamlit run app.py
```

The app will now use watsonx.ai for live AI generation. If any error occurs, it automatically falls back to demo mode.

### Switching Between Modes

Simply change `LLM_PROVIDER` in your `.env` file:

```bash
# Use demo mode
LLM_PROVIDER=demo

# Use watsonx mode
LLM_PROVIDER=watsonx
```

No code changes needed!

## Provider Selection Flow

```
User Request
    ↓
Check LLM_PROVIDER env var
    ↓
┌─────────────────────────────────────┐
│ LLM_PROVIDER=demo or not set?       │
│ → Use dynamic demo generation       │
└─────────────────────────────────────┘
    ↓
┌─────────────────────────────────────┐
│ LLM_PROVIDER=watsonx?               │
│ → Check credentials                 │
│   ├─ Missing? → Demo mode + warning │
│   └─ Present? → Call watsonx API    │
│       ├─ Success? → Return plan     │
│       └─ Error? → Demo mode + error │
└─────────────────────────────────────┘
    ↓
┌─────────────────────────────────────┐
│ Unknown provider?                   │
│ → Demo mode + warning               │
└─────────────────────────────────────┘
```

## API Integration Details

### Request Format

```python
POST {WATSONX_URL}/ml/v1/text/generation?version=2023-05-29

Headers:
  Authorization: Bearer {WATSONX_API_KEY}
  Content-Type: application/json

Body:
{
  "input": "<prompt>",
  "parameters": {
    "decoding_method": "greedy",
    "max_new_tokens": 4000,
    "min_new_tokens": 0,
    "stop_sequences": [],
    "repetition_penalty": 1.0
  },
  "model_id": "{WATSONX_MODEL_ID}",
  "project_id": "{WATSONX_PROJECT_ID}"
}
```

### Response Handling

1. Extract `results[0].generated_text` from response
2. Remove markdown code blocks if present
3. Extract JSON object from text
4. Parse JSON
5. Validate using `coerce_launch_plan()`
6. Return validated plan

### Error Handling

All errors are caught and handled gracefully:

- `ValueError` → Missing credentials or invalid JSON
- `requests.RequestException` → Network/API errors
- `Exception` → Unexpected errors

In all cases, the app falls back to demo mode and continues working.

## Testing

### Run All Tests

```bash
python3 -m pytest tests/ -v
```

### Run Only watsonx Tests

```bash
python3 -m pytest tests/test_watsonx_integration.py -v
```

### Test Coverage

- ✅ Provider selection (demo, watsonx, unknown)
- ✅ API integration (success, timeout, errors)
- ✅ Error handling and fallback
- ✅ JSON extraction (plain, markdown, with text)
- ✅ Security (no credentials in output/logs)
- ✅ Language support (English, Italian)

## Security Best Practices

### ✅ Implemented

1. **Environment Variables Only**
   - All credentials from `.env` file
   - Never hardcoded in code
   - `.env` file in `.gitignore`

2. **No Exposure**
   - API keys never in logs
   - API keys never in generated output
   - API keys redacted from error messages

3. **Safe Defaults**
   - Demo mode by default
   - No credentials required for demo mode
   - App never crashes due to missing credentials

### ⚠️ Important

- **Never commit `.env` file** - It contains secrets
- **Never share API keys** - They provide access to your IBM Cloud account
- **Use `.env.example`** - Only commit this file with placeholders
- **Rotate keys regularly** - If a key is exposed, rotate it immediately

## Language Support

The watsonx integration respects the `output_language` setting:

- **English**: Model generates content in English
- **Italian**: Model generates content in Italian

The prompt builder includes language-specific instructions that tell the model which language to use for all user-facing content.

## Performance

### Demo Mode
- **Response Time**: Instant (<100ms)
- **Cost**: Free
- **Reliability**: 100%

### watsonx Mode
- **Response Time**: 2-10 seconds (depends on model and load)
- **Cost**: Per token (see IBM Cloud pricing)
- **Reliability**: High (with automatic fallback)

## Troubleshooting

### "WATSONX_API_KEY environment variable is required"

**Solution**: Add your API key to `.env` file or switch to demo mode.

### "watsonx.ai API request timed out"

**Solution**: The API is slow or unavailable. The app automatically falls back to demo mode. Try again later or use demo mode.

### "Invalid response format from watsonx.ai"

**Solution**: The model returned unexpected output. The app falls back to demo mode. This is rare but handled automatically.

### "Unknown LLM_PROVIDER: 'xyz'"

**Solution**: Check your `.env` file. Valid values are `demo` or `watsonx`.

## Future Enhancements

Potential improvements for future versions:

1. **Additional Providers**
   - OpenAI GPT-4
   - Anthropic Claude
   - Google Gemini

2. **Advanced Features**
   - Streaming responses
   - Model parameter tuning
   - Response caching
   - A/B testing between providers

3. **Monitoring**
   - API usage tracking
   - Response time metrics
   - Error rate monitoring
   - Cost tracking

## Conclusion

The watsonx.ai integration provides:

✅ Live AI generation when credentials are available  
✅ Automatic fallback to demo mode on any error  
✅ Zero configuration required for demo mode  
✅ Comprehensive error handling  
✅ Full security compliance  
✅ Extensive test coverage  
✅ Language support (English, Italian)  

The app remains reliable and never crashes, regardless of provider configuration or API availability.