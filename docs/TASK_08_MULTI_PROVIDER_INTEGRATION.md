# Task 8: Multi-Provider AI Integration

## Overview

MenuNest now supports four AI provider modes, allowing users to choose between demo mode (no API keys required) and three live AI providers (IBM watsonx.ai, OpenAI, Anthropic Claude). All providers include automatic fallback to demo mode on any error, ensuring the app never crashes.

## Supported Providers

### 1. Demo Mode (Default)
- **Cost:** Free
- **Speed:** Instant (<100ms)
- **Reliability:** 100%
- **Use Case:** Testing, presentations, judging, development
- **Configuration:** `LLM_PROVIDER=demo` (or not set)

### 2. IBM watsonx.ai
- **Models:** Granite, Llama, and other IBM/open-source models
- **Use Case:** Enterprise deployments, IBM Cloud users
- **Configuration:** Requires `WATSONX_API_KEY`, `WATSONX_PROJECT_ID`, `WATSONX_URL`, `WATSONX_MODEL_ID`

### 3. OpenAI
- **Models:** GPT-4, GPT-3.5
- **Use Case:** High-quality generation, wide model selection
- **Configuration:** Requires `OPENAI_API_KEY`, `OPENAI_MODEL`

### 4. Anthropic Claude
- **Models:** Claude 3 Opus, Sonnet
- **Use Case:** Advanced reasoning, long context
- **Configuration:** Requires `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`

## Implementation Summary

### Files Modified

1. **`.env.example`** - Added environment variables for all four providers
2. **`requirements.txt`** - Added `openai` and `anthropic` packages
3. **`src/ai_generator.py`** - Added provider integration functions and selection logic
4. **`tests/test_watsonx_integration.py`** - Extended tests to cover all providers (now 31 tests)
5. **`README.md`** - Added comprehensive provider setup instructions
6. **`docs/TASK_08_MULTI_PROVIDER_INTEGRATION.md`** - This documentation

### New Functions in ai_generator.py

1. **`call_watsonx_api(prompt: str) -> dict`**
   - Integrates with IBM watsonx.ai
   - Validates environment variables
   - Handles API authentication and requests
   - Extracts and validates JSON from response

2. **`call_openai_api(prompt: str) -> dict`**
   - Integrates with OpenAI API
   - Uses OpenAI SDK
   - Supports GPT-4 and GPT-3.5 models
   - Extracts and validates JSON from response

3. **`call_anthropic_api(prompt: str) -> dict`**
   - Integrates with Anthropic API
   - Uses Anthropic SDK
   - Supports Claude 3 models
   - Extracts and validates JSON from response

4. **`extract_json_from_text(text: str) -> str`**
   - Extracts JSON from model output
   - Handles markdown code blocks
   - Handles explanatory text before/after JSON
   - Validates extracted JSON

### Provider Selection Flow

```
User Request
    ↓
Check LLM_PROVIDER environment variable
    ↓
┌─────────────────────────────────────────┐
│ LLM_PROVIDER=demo or not set?           │
│ → Use dynamic demo generation           │
└─────────────────────────────────────────┘
    ↓
┌─────────────────────────────────────────┐
│ LLM_PROVIDER=watsonx?                   │
│ → Check credentials                     │
│   ├─ Missing? → Demo mode + warning     │
│   └─ Present? → Call watsonx API        │
│       ├─ Success? → Return plan         │
│       └─ Error? → Demo mode + error     │
└─────────────────────────────────────────┘
    ↓
┌─────────────────────────────────────────┐
│ LLM_PROVIDER=openai?                    │
│ → Check credentials                     │
│   ├─ Missing? → Demo mode + warning     │
│   └─ Present? → Call OpenAI API         │
│       ├─ Success? → Return plan         │
│       └─ Error? → Demo mode + error     │
└─────────────────────────────────────────┘
    ↓
┌─────────────────────────────────────────┐
│ LLM_PROVIDER=anthropic?                 │
│ → Check credentials                     │
│   ├─ Missing? → Demo mode + warning     │
│   └─ Present? → Call Anthropic API      │
│       ├─ Success? → Return plan         │
│       └─ Error? → Demo mode + error     │
└─────────────────────────────────────────┘
    ↓
┌─────────────────────────────────────────┐
│ Unknown provider?                       │
│ → Demo mode + warning                   │
└─────────────────────────────────────────┘
```

## Environment Variables

### Demo Mode (No Configuration Needed)

```bash
LLM_PROVIDER=demo
```

### IBM watsonx.ai

```bash
LLM_PROVIDER=watsonx
WATSONX_API_KEY=your_api_key_here
WATSONX_PROJECT_ID=your_project_id_here
WATSONX_URL=https://us-south.ml.cloud.ibm.com
WATSONX_MODEL_ID=ibm/granite-13b-instruct-v2
```

### OpenAI

```bash
LLM_PROVIDER=openai
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-4-turbo-preview
```

### Anthropic

```bash
LLM_PROVIDER=anthropic
ANTHROPIC_API_KEY=your_api_key_here
ANTHROPIC_MODEL=claude-3-opus-20240229
```

## Usage Examples

### Using Demo Mode

```bash
# No configuration needed
streamlit run app.py
```

### Using watsonx.ai

```bash
# 1. Create .env file
cp .env.example .env

# 2. Edit .env and add your watsonx credentials
# LLM_PROVIDER=watsonx
# WATSONX_API_KEY=your_actual_key
# WATSONX_PROJECT_ID=your_actual_project_id
# ...

# 3. Run the app
streamlit run app.py
```

### Using OpenAI

```bash
# 1. Create .env file
cp .env.example .env

# 2. Edit .env and add your OpenAI credentials
# LLM_PROVIDER=openai
# OPENAI_API_KEY=your_actual_key
# OPENAI_MODEL=gpt-4-turbo-preview

# 3. Run the app
streamlit run app.py
```

### Using Anthropic

```bash
# 1. Create .env file
cp .env.example .env

# 2. Edit .env and add your Anthropic credentials
# LLM_PROVIDER=anthropic
# ANTHROPIC_API_KEY=your_actual_key
# ANTHROPIC_MODEL=claude-3-opus-20240229

# 3. Run the app
streamlit run app.py
```

## Error Handling

All providers implement comprehensive error handling:

### Missing Credentials
```
⚠️  OPENAI_API_KEY environment variable is required for openai provider.
ℹ️  Falling back to demo mode for reliability.
```

### API Failures
```
⚠️  OpenAI API call failed: Connection timeout
ℹ️  Falling back to demo mode for reliability.
```

### Invalid Responses
```
⚠️  OpenAI returned invalid JSON. The model output could not be parsed.
ℹ️  Falling back to demo mode for reliability.
```

### Unknown Provider
```
⚠️  Unknown LLM_PROVIDER: 'xyz'
ℹ️  Supported providers: 'demo', 'watsonx', 'openai', 'anthropic'
ℹ️  Falling back to demo mode.
```

## Security Features

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

4. **Import Safety**
   - Provider SDKs imported only when needed
   - Graceful handling of missing packages
   - Clear error messages for missing dependencies

### ⚠️ Important Security Notes

- **Never commit `.env` file** - It contains secrets
- **Never share API keys** - They provide access to your accounts
- **Use `.env.example`** - Only commit this file with placeholders
- **Rotate keys regularly** - If a key is exposed, rotate it immediately
- **Use environment-specific keys** - Different keys for dev/staging/prod

## Testing

### Run All Tests

```bash
python3 -m pytest tests/ -v
```

### Run Only Provider Tests

```bash
python3 -m pytest tests/test_watsonx_integration.py -v
```

### Test Coverage

The test suite includes 31 tests covering:

- ✅ Provider selection (demo, watsonx, openai, anthropic, unknown)
- ✅ API integration for all providers
- ✅ Missing credentials handling
- ✅ API failures and timeouts
- ✅ Invalid response handling
- ✅ JSON extraction (plain, markdown, with text)
- ✅ Security (no credentials in output/logs)
- ✅ Language support (English, Italian)
- ✅ Fallback behavior
- ✅ Multi-provider selection logic

### Test Results

```
============================= 31 passed ==============================
```

All tests pass, including:
- 23 original watsonx tests
- 3 OpenAI integration tests
- 3 Anthropic integration tests
- 2 multi-provider selection tests

## Language Support

All AI providers respect the `output_language` setting:

- **English**: Model generates content in English
- **Italian**: Model generates content in Italian

The prompt builder includes language-specific instructions that tell the model which language to use for all user-facing content.

**Important:** Internal JSON keys remain in English for validation. Only user-facing text values are localized.

## Performance Comparison

| Provider | Response Time | Cost | Reliability | Quality |
|----------|--------------|------|-------------|---------|
| Demo | <100ms | Free | 100% | Good |
| watsonx.ai | 2-10s | Per token | High* | Very Good |
| OpenAI | 2-8s | Per token | High* | Excellent |
| Anthropic | 2-10s | Per token | High* | Excellent |

*With automatic fallback to demo mode

## Recommended Models

### IBM watsonx.ai
- **Best Quality:** `meta-llama/llama-3-70b-instruct`
- **Balanced:** `ibm/granite-13b-instruct-v2`
- **Fast:** `ibm/granite-8b-instruct`

### OpenAI
- **Best Quality:** `gpt-4-turbo-preview`
- **Balanced:** `gpt-4`
- **Fast/Cheap:** `gpt-3.5-turbo`

### Anthropic
- **Best Quality:** `claude-3-opus-20240229`
- **Balanced:** `claude-3-sonnet-20240229`
- **Fast:** `claude-3-haiku-20240307`

## Troubleshooting

### "Import 'openai' could not be resolved"

**Solution:** Install the package:
```bash
pip install openai
```

### "Import 'anthropic' could not be resolved"

**Solution:** Install the package:
```bash
pip install anthropic
```

### "API key not found"

**Solution:** Check your `.env` file:
1. Ensure `.env` exists in project root
2. Verify the API key variable name matches the provider
3. Ensure no extra spaces or quotes around the key
4. Restart the app after changing `.env`

### "API call failed"

**Solution:** The app automatically falls back to demo mode. Check:
1. Internet connection
2. API key validity
3. Account credits/quota
4. API service status

## Future Enhancements

Potential improvements for future versions:

1. **Additional Providers**
   - Google Gemini
   - Cohere
   - Hugging Face Inference API
   - Azure OpenAI

2. **Advanced Features**
   - Streaming responses
   - Model parameter tuning (temperature, top_p, etc.)
   - Response caching
   - A/B testing between providers
   - Cost tracking per provider

3. **Monitoring**
   - API usage tracking
   - Response time metrics
   - Error rate monitoring
   - Cost analytics dashboard

4. **Provider Selection UI**
   - In-app provider selection
   - Model selection dropdown
   - Real-time provider status
   - Cost estimates

## Conclusion

MenuNest now supports four AI provider modes:

✅ **Demo mode** - Free, instant, 100% reliable (default)  
✅ **IBM watsonx.ai** - Enterprise-grade AI with IBM models  
✅ **OpenAI** - Industry-leading GPT models  
✅ **Anthropic Claude** - Advanced reasoning and long context  

All providers include:
- Automatic fallback to demo mode
- Comprehensive error handling
- Security best practices
- Language support (English, Italian)
- Full test coverage

The app remains reliable and never crashes, regardless of provider configuration or API availability.