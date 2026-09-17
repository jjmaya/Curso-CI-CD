# Notas de clase

Link curso:
https://platzi.com/cursos/pruebas-software/

Ensayo en Postman destok - conexión api Claude
https://api.anthropic.com/v1/messages
Headers
x-api-key: API-KEY
content-type: application/json
anthropic-version: 2023-06-01

Body - POST:
{
    "model": "claude-sonnet-4-6",
    "max_tokens": 1000,
    "messages": [
        {
            "role": "user", 
            "content": "¿Qué es IA?"
        }
    ],
    "temperature": 0.8
    "n": 1,
    "stream": false,
    "thinking": {
            "type": "adaptive"
          },
}

response
{
    "model": "claude-sonnet-4-6",
    "id": "msg_011CeuvRh1jrYPBCsih9LRLY",
    "type": "message",
    "role": "assistant",
    "content": [
        {
            "type": "text",
            "text": "# ¿Qué es la Inteligencia Artificial (IA)?\n\nLa **Inteligencia Artificial** es una rama de la informática que busca crear sistemas capaces de realizar tareas que normalmente requieren **inteligencia humana**.\n\n## Capacidades principales\n\n- 🧠 **Aprender** de datos y experiencias\n- 💬 **Comprender** lenguaje natural\n- 👁️ **Reconocer** imágenes y patrones\n- 🔍 **Resolver** problemas complejos\n- 🤖 **Tomar decisiones** de forma autónoma\n\n## Tipos principales\n\n| Tipo | Descripción |\n|------|-------------|\n| **IA Estrecha** | Especializada en una tarea específica (ej. reconocimiento facial) |\n| **IA General** | Capaz de realizar cualquier tarea intelectual humana (aún en desarrollo) |\n| **IA Superinteligente** | Superaría la inteligencia humana (teórica) |\n\n## Ejemplos cotidianos\n\n- Asistentes virtuales (Siri, Alexa)\n- Recomendaciones de Netflix o Spotify\n- Filtros de spam en el correo\n- Autos autónomos\n- Chatbots como **yo** 😊\n\n## En resumen\n\n> La IA permite que las máquinas **imiten procesos cognitivos humanos** para resolver problemas de manera eficiente.\n\n¿Te gustaría profundizar en algún aspecto específico? 🤔"
        }
    ],
    "container": null,
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
        "input_tokens": 17,
        "cache_creation_input_tokens": 0,
        "cache_read_input_tokens": 0,
        "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 0
        },
        "output_tokens": 388,
        "service_tier": "standard",
        "inference_geo": "global"
    }
}