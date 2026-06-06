Vapi Function Tool Definitions

This project integrates with Vapi by accepting a centralized tool-calls webhook at /vapi/tool-calls.

Server URL

All three Function Tools in Vapi should use the same Server URL (replace YOUR-NGROK-URL with your ngrok subdomain):

```
https://YOUR-NGROK-URL.ngrok-free.dev/vapi/tool-calls
```

Tool names (keep these exact):

- search_municipal_services
- create_appointment
- check_appointment

Vapi webhook payload

Vapi will POST a tool-calls payload to the server URL above. The backend receives the payload and internally dispatches it to the appropriate service handler (search, create, check).

Parameter definitions

search_municipal_services:
- query, string, required

create_appointment:
- full_name, string, required
- service_name, string, required
- preferred_date, string, required, format YYYY-MM-DD
- preferred_time, string, required, format HH:MM
- contact, string, required

check_appointment:
- appointment_id, string, optional
- contact, string, optional

Direct (manual/Swagger) endpoints

Manual or Swagger-based testing may use the direct backend endpoints which remain available:

- POST /tools/search-municipal-services
- POST /tools/create-appointment
- POST /tools/check-appointment

These endpoints accept the same parameters as the Vapi tool payloads and are useful for curl/Swagger testing.
