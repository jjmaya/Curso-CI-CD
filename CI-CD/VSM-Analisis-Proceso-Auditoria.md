# 📊 ANÁLISIS VSM - PROCESO DE AUDITORÍA CONTINUA
## Empresa: Grupo XXX
## Período de análisis: 20/09/2026
## Responsable del documento: Juan José Maya Salcedo

---

## 📋 CONTEXTO DEL ENTREGABLE

### Nombre del proceso auditado: Reporteria via Correo de Monitoreo Continuo
________________

### Descripción breve (2-3 líneas):
**En pro de ser un apoyo para las diferentes areas de la empresa, Auditoria Interna despliega Monitoreos Continuos a la información que respalda los principales puntos. Para ello, una vez se tienen unos tableros de control de los procesos en cuestión, se despliegan informes mensuales (diarios, semanales u otros) para alertar a los interesados de los focos que podrían generar problemas.**
________________

### Valor esperado para el negocio:
**Disminuir los tiempos de cambio por la falta de modularización de la estrutura base (el software base) para realizar los correos de reporteria.**
________________

### Stakeholders principales:
- Lider de Auditoria Análitica.
- Equipo de Desarrollo.
- Director de Auditoria.
- Accionista Principal.

---

## 🚀 FASE 1: PREPARACIÓN ✅ (Completado)

### Equipo multifuncional asignado:

| Rol/Área | Persona | Responsabilidad |
|----------|---------|-----------------|
| Auditoría Interna | Cordinadores de auditoria | Definir focos de auditoría |
| Ingeniería de Datos | Cualquiera de los 3 Dev | Extraer y procesar datos |
| Análisis | Coordinador y Dev | Analizar hallazgos |
| Comunicación | Dev | Reportar a Diligent/PowerBI |
| Desarrollo | Dev | Crear informes y dashboards |
| Operaciones | Dev | Despliegue en producción |

### Herramientas disponibles:

| Herramienta | Uso | Responsable |
|-------------|-----|-------------|
| Excel, Claud | Definición de pruebas | Coordinador de auditoria |
| ACL, AWS-EC2 y Python | Ingeniería de datos | Dev |
| Python y Claude-API | Análisis | Dev |
| Power BI | Dashboards/PowerBI | Dev |
| Python, Claude-API, Outlook | Desarrollo de informes | Dev |
| Outlook | Monitoreo continuo | Dev |

---

## 🎯 FASE 2: VISUALIZACIÓN INICIAL

### 2.1 FLUJO ACTUAL - DIAGRAMA DE ESTADOS

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    PROCESO DE AUDITORÍA CONTINUA                        │
└─────────────────────────────────────────────────────────────────────────┘

  1️⃣ NECESIDAD              2️⃣ DEFINICIÓN           3️⃣ INGENIERÍA
  DE AUDITAR                DE PRUEBAS              DE DATOS               ___
       │                         │                       │                    |
       ├─────────────────────────┤                       │                    |
       │ Proceso particular      │ Focos a auditar       │                    |
       │ identificado            │ Ejemplo: "Motos       │ Extracción         |
       │                         │ en planta como CBU    │ y procesamiento    |
       │                         │ sin OrdProd"          │ de datos           |
       │                         │                       │                    |
       └─────────────────────────────────────────────────┘                    |
                                │                                             | Auditoria continua (AC)
                                ▼                                             |    Se repite cada x numero
  4️⃣ ANÁLISIS                5️⃣ COMUNICACIÓN         6️⃣ DESARROLLO           |     de meses
       │                     DE RESULTADOS            DE INFORME              |
       │ Revisión de         │                        │                       |
       │ hallazgos           ├─→ Diligent             │ Informe               |
       │                     │                        │ + Dashboard           |
       │                     └─→ PowerBI              │ de monitoreo          |
       │                                              │                       |
       └──────────────────────────────────────────────┘                    ___|
                              │
                              ▼
      7️⃣ MONITOREO CONTINUO   __________________________
       │                                                |
       ├─ Seguimiento constante de procesos             |
       ├─ Detección temprana de desviaciones            |
       ├─ Aliado del negocio (no policía)               |
       └─ Levanta la mano antes de errores graves       |
                              │                         |   MONITOREO CONTINUO (MC)
                              ▼                         |   Son informes de frecuencia mayor
      8️⃣ DESPLIEGUE                                    |       que AC. 
       │                                                |
       └─ Puesta en producción del sistema              |
          de monitoreo continuo                     ____| 
```

---

### 2.2 DESCRIPCIÓN DETALLADA POR ESTADO

#### **ESTADO 1: NECESIDAD DE AUDITAR**

**Descripción:**  
Se identifica un proceso particular de la empresa que requiere auditoría o seguimiento.

**Responsable:**  
Coordinadores de Auditoria + Líder Auditoria Analítica

**Duración promedio:**  
- Identificación de necesidad: 5 días
- Aprobación/Priorización: 1 día
- **Total en este estado: 6 días**

**Tareas/Actividades:**
- Reunión inicial con el usuario(s) del proceso. Formalidad de apertura y correo.
- Ideas preliminares de pruebas a realizar y conversación con el usuario para entender de donde sale la data. Se asigna a cada prueba un usuario responsable del negocio. 
- Creación de la AC en Diligent ONE para la implementación del AC - en este se suben las pruebas ya definidas.

**Herramientas utilizadas:**
- Micrsoft Teams.
- Excel.
- Diligent ONE.

**Documentación de entrada/salida:**
- Entra: Preguntas de la alta genrencia sobre el proceso y desde la dirección de Auditoria.
- Sale: Documento de definición de la AC (Necesidad documentada y aprobada)

**Cuellos de botella identificados:**
- Disponibilidad de stakeholders (usuarios del proceso): Agenda congestionada, requiere coordinación entre departamentos.
- Claridad de comunicación: Conceptos del negocio no siempre traducibles a criterios técnicos sin iteraciones.

**Observaciones:**
La ambigüedad introducida en esta fase se amplifica exponencialmente en Estado 3. Por ejemplo, si no se aclara bien "Motos en planta como CBU sin OrdProd", el Dev pasará días haciendo queries que no cumplen con lo esperado. Es común que el Coordinador deba seguir en contacto durante el Estado 3 para validar datos intermedios.

---

#### **ESTADO 2: DEFINICIÓN DE PRUEBAS**

**Descripción:**  
Se definen los focos específicos a auditar. Ejemplo: "Número de motos en planta como CBU sin órdenes de producción".

**Responsable:**  
Coordinador(a) de Auditoria.

**Duración promedio:**  
- Diseño de pruebas: 5 días
- Validación con stakeholders: 3 días
- **Total en este estado: 8 días**

**Tareas/Actividades:**
- Definir criterios de auditoría con ejemplos concretos
- Identificar datos necesarios y sus fuentes SAP (Hanna, módulo específico)
- Documentar reglas de validación y excepciones
- Crear mockups o ejemplos de resultado esperado
- Validar con stakeholder y obtener firma de aprobación

**Herramientas utilizadas:**
- Microsoft Teams
- Excel
- Claude code
- SAP ERP

**Documentación de entrada/salida:**
- Entra: Necesidad documentada
- Sale: Preguntas definidas, Fuentes de data definidas, KPIs definidos (Especificación de pruebas)

**Cuellos de botella identificados:**
- Definiciones ambigüas que generan iteraciones (Ej: "Revisar motos" es vago. "Revisar motos con status=CBU Y sin OrdProd asociada en tabla AUFK" es claro).
- Disponibilidad de expertos de negocio para validar: Solo 1-2 personas conocen ciertos procesos. Si están en reuniones, el Dev espera 2-3 días.
- Falta de documentación: No existe catálogo de campos/tablas SAP disponibles. El Dev debe preguntar o investigar.

**Observaciones:**
Esta fase es corta (8 días) pero crítica. La calidad de definición aquí determina si Estado 3 toma 10 o 15 días. Problema recurrente: Una vez que el Dev está en Estado 3, se descubre que faltan datos o no están donde se pensaba, causando retrabajos. Recomendación: Añadir un "Design Review" con el Dev de 2 horas al final de Estado 2 para validar viabilidad técnica antes de pasar a ingeniería.

---

#### **ESTADO 3: INGENIERÍA DE DATOS**

**Descripción:**  
Extracción, transformación y procesamiento de datos desde fuentes de la empresa.

**Responsable:**  
Desarrolldor(a)

**Duración promedio:**  
- Diseño de queries: Entre 8 y 10 días
- Extracción: 0.5 días
- Validación de datos: Entre 2 y 4 días
- **Total en este estado: Entre 10.5 y 14.5 días**

**Tareas/Actividades:**
- Identificar tablas en SAP Hanna (AUFK, RESB, MARC, etc.) donde residen los datos
- Mapear relaciones entre tablas (claves foráneas, FK)
- Diseñar queries SQL complejos (JOINs múltiples, subconsultas)
- Extraer datos en bruto vía ACL (herramienta de auditoría) o Python
- Validar completitud (¿obtuvimos todos los datos?) y precisión (¿los datos son correctos?)
- Iterar cuando las definiciones del Estado 2 no coinciden con la realidad de datos

**Herramientas utilizadas:**
- Conectores a las tablas ODC de SAP Hanna via ACL 
- Python

**Documentación de entrada/salida:**
- Entra: Especificación de pruebas
- Sale: Dataset procesados + KPis

**Cuellos de botella identificados (🔴 CRÍTICO):**
- **Documentación incompleta de SAP Hanna:** No existe catálogo actualizado de tablas, campos y relaciones. El Dev debe explorar manualmente. Tiempo perdido: 2-4 días por AC.
- **Complejidad de JOIN entre tablas:** Algunos datos requieren cruzar 5-7 tablas (AUFK → RESB → MARC → MARA → etc.). Sin documentación, requiere trial-and-error.
- **Datos históricos dispersos:** Auditoría necesita datos de 6-24 meses. Están en tablas separadas (activa vs. archivo). Requiere queries adicionales.
- **Permisos de acceso:** El Dev no siempre tiene acceso a todas las tablas requeridas. Requiere tickets a TI, espera 1-2 días.
- **Validación posterior incompleta:** Una vez extraído, se descubre que faltan excepciones (Ej: "Hay motos CBU que SÍ tienen OrdProd pero en estado cancelado - ¿eso cuenta?"). Requiere volver al Estado 2 → Estado 3 nuevamente.

**Observaciones:**
**Este es el mayor cuello de botella (29.8% del tiempo total).** El problema raíz no es la habilidad del Dev, sino la falta de documentación. Solución viable:
- Crear wiki/Confluence con mapa de relaciones SAP Hanna (quién → con quién → cómo).
- Documentar los 20 queries más comunes para auditoría (Ej: "Órdenes sin material", "Recepción sin OC").
- Asignar 4-5 días la primera vez para crear templates. La segunda vez será 1-2 días.

**Impacto de mejora:** Si se reduce de 12.5 a 8 días, el ciclo completo baja de 42.2 a ~37.7 días (-11%).

---

#### **ESTADO 4: ANÁLISIS**

**Descripción:**  
Revisión profunda de datos para identificar hallazgos, patrones y desviaciones.

**Responsable:**  
Auditor y apoya Dev

**Duración promedio:**  
- Análisis exploratorio: 2 días
- Identificación de hallazgos: 2 días
- Documentación: 4 días
- **Total en este estado: 6 días**

**Tareas/Actividades:**
- Revisar dataset con lupa de auditor (¿qué saltó a la vista?)
- Identificar anomalías/excepciones que violen criterios
- Cuantificar: ¿Cuántas motos? ¿Qué % del total? ¿Desde cuándo existe el problema?
- Determinar causa raíz (si es visible en datos)
- Redactar hallazgos en lenguaje ejecutivo (no técnico)
- Documentar en template estándar con evidencia (ejemplos específicos de registros)

**Herramientas utilizadas:**
- Diligent One (in-line) -> visual solo para Auditor

**Documentación de entrada/salida:**
- Entra: Dataset procesado
- Sale: Reporte de hallazgos

**Cuellos de botella identificados:**
- Disponibilidad del Auditor: Solo hay 1-2 auditores para revisar múltiples auditorías en paralelo. Si hay 3-4 AC en Estado 4 simultáneamente, se forma cola.
- Complejidad de hallazgos: Algunos requieren investigación adicional (¿por qué existen estas motos sin OrdProd? ¿Es un fallo de control o una excepción válida?). Requiere seguimiento con el negocio.
- Validación de contexto: El hallazgo puede parecer crítico en datos pero ser irrelevante en realidad. Requiere validación con stakeholder (2-3 días de espera).

**Observaciones:**
Esta fase es rápida (6 días) pero vulnerable a interrupciones. El Auditor que está revisando puede ser sacado de contexto por urgencias, alargando el tiempo. El hallazgo redactado debe ser claro y sin ambigüedades para que PowerBI y Diligent puedan procesarlo sin retrabajos en Estado 5.

---

#### **ESTADO 5: COMUNICACIÓN DE RESULTADOS**

**Descripción:**  
Reportar hallazgos a Diligent (sistema de control) y PowerBI (visualización).

**Responsable:**  
Dev

**Duración promedio:**  
- Preparación de reportes: 5 días
- Carga en Diligent: 0.1 días
- Creación de visuales PowerBI: 3 días
- **Total en este estado: 8.1 días**

**Tareas/Actividades:**
- Formatear hallazgos según schema de Diligent ONE (campos requeridos, valores válidos, clasificaciones)
- Convertir datos de formato Word/PDF a CSV/Excel para carga
- Cargar datos en Diligent ONE con validación de integridad
- Crear visuales en PowerBI (gráficos, tablas, filtros)
- Testing en ambiente de staging (¿se ve bien? ¿son correctos los datos?)
- Validar con Auditor antes de publicar

**Herramientas utilizadas:**
- Diligent ONE
- PowerBI
- Python + Claude API

**Documentación de entrada/salida:**
- Entra: Reporte de hallazgos
- Sale: Hallazgos cargados en Diligent ONE + Dashboard PowerBI con visuales interactivas

**Cuellos de botella identificados (🟡 RIESGO MEDIO):**
- **Formato inconsistente entre Diligent y PowerBI:** Los campos en Diligent tienen estructura fija (Hallazgo ID, Descripción, Severidad, Estado). PowerBI necesita otros campos para visualización (fecha detección, propietario, tendencia). Requiere transformación manual (Python). Tiempo: 1-2 días.
- **Validación de datos compleja:** Un campo erróneo carga en Diligent pero rompe el dashboard. Requiere revisión manual antes de publicar. Si hay errores, hay que volver a formatear y recargar (½ día perdido).
- **Permisos en Diligent:** Algunos auditores tienen permisos de lectura, otros de edición. Requiere validar antes de cargar.
- **Cambios de última hora:** El Auditor revisa el dashboard y pide cambios en visualización ("Ponme la columna X en lugar de Y"). Requiere rehacerlo en PowerBI (1 día).

**Observaciones:**
Esta fase parece corta (8.1 días) pero puede alargarse mucho si hay validaciones fallidas. La mejor práctica es automatizar la transformación Diligent-PowerBI (crear script Python reutilizable) para que cualquier Dev pueda cargar datos en 1-2 horas sin errores. Actualmente, cada AC requiere trabajo manual.

---

#### **ESTADO 6: DESARROLLO DE INFORME Y MONITOREO CONTINUO**

**Descripción:**  
Creación de un informe ejecutivo y montaje de un sistema de monitoreo continuo que funcione como aliado del proceso, levantando la mano antes de que sucedan errores graves.

**Responsable:**  
Dev

**Duración promedio:**  
- Diseño del informe: 0.3 días
- Configuración de monitoreo: 0.2 días
- Testing: 0.1 días
- **Total en este estado: 0.6 días**

**Tareas/Actividades:**
- Crear informe ejecutivo
- Definir métricas de monitoreo
- Configurar alertas automáticas
- Establecer frecuencia de revisión
- Generar template de correo automático

**Herramientas utilizadas:**
- Python
- Anthropic API

**Documentación de entrada/salida:**
- Entra: Datos formato plano y/o Screenshot PowerBI
- Sale: Informe + Sistema de monitoreo listo (correo)

**Características del "Monitoreo Continuo":**
- ¿Qué se monitorea? Los tableros de control KPIs y hallazgos
- ¿Con qué frecuencia? Diaria/Semanal/Mensual (según AC)
- ¿Quién recibe alertas? Usuario responsable del negocio
- ¿Qué acción se toma? El usuario revisa el correo. Auditoría levanta la mano tempranamente.

**Cuellos de botella identificados:**
- Automatización incompleta del proceso: Requiere intervención manual en cada iteración para generar template de correo.

**Observaciones:**
Este es el estado más eficiente (0.6 días, 1.4% del tiempo). El monitoreo continuo es **el valor real del proceso**. Una vez cargados datos en Diligent y PowerBI, el script de Python genera correos automáticos (diarios, semanales, mensuales según configuración) y los envía a los usuarios responsables vía Outlook. El modelo es escalable: agregar una nueva AC no suma tiempo, solo costo de infraestructura (servidor).

**Mejora potencial:** Si se crea una librería estándar de templates de correos (que hoy son customizados por AC), se podría bajar a 0.2 días.

---

#### **ESTADO 7: DESPLIEGUE**

**Descripción:**  
Puesta en producción del sistema de auditoría continua.

**Responsable:**  
Dev + Líder de Auditoria Analítica

**Duración promedio:**  
- Preparación/testing final: 0.5 días
- Despliegue en producción: 2 horas
- Validación post-despliegue: 0.5 días
- **Total en este estado: 1 día**

**Tareas/Actividades:**
- Testing en ambiente de staging
- Comunicar a usuarios finales vía correo
- Despliegue de correo automático en producción
- Monitoreo de entrega en primeros ciclos

**Herramientas utilizadas:**
- Outlook (envío de correos automáticos)
- AWS-EC2 (servidor de ejecución de scripts Python)
- Scheduler (cron jobs para ejecutar monitoreo según frecuencia)

**Documentación de entrada/salida:**
- Entra: Informe ejecutivo + Script Python de monitoreo configurado
- Sale: Sistema de Monitoreo Continuo en vivo (correos automáticos desplegados)

**Cuellos de botella identificados:**
- **Testing en ambiente de staging:** Requiere validar que los correos se envíen correctamente, que contengan los datos correctos y que lleguen a los buzones adecuados. Si hay error, requiere debugging (½ día).
- **Validación de listas de distribución:** A veces los usuarios finales cambian de correo o departamento. Requiere actualizar listas antes de desplegar (control manual, propenso a errores).
- **Comunicación con usuarios:** El Dev debe notificar a los usuarios que recibirán correos de monitoreo. Requiere documentación clara (qué esperar, cómo actuar, a quién reportar si algo falla).

**Observaciones:**
Esta es la puerta de entrada al Monitoreo Continuo. Una vez desplegado, el sistema entra en modo automático. Los usuarios recibirán reportes con la frecuencia acordada (Ej: correos diarios cada mañana a las 8 AM con un resumen de hallazgos del día anterior).

**Modelo de valor:** A partir de aquí, cada vez que se ejecute el monitoreo, se genera valor sin intervención manual. Si el Estado 3 encontró 5 motos sin OrdProd, el usuario lo sabrá en 24 horas sin que Auditoría tenga que hacer nada más. Eso es diferente del modelo antiguo donde Auditoría entrega un reporte cada trimestre.

---

### 2.3 RESUMEN DE TIEMPOS POR ESTADO

| Estado | Responsable | Duración promedio | % del tiempo total | Notas |
|--------|-------------|-------------------|-------------------|-------|
| 1. Necesidad de auditar | Coordinador Aud. | 6 días | 14.3% | Incluye aprobación |
| 2. Definición de pruebas | Coordinador Aud. | 8 días | 19.0% | Requiere validaciones |
| 3. Ingeniería de datos | Dev | 12.5 días | 29.8% | 🔴 CUELLO BOTELLA |
| 4. Análisis | Auditor + Dev | 6 días | 14.3% | Revisión profunda |
| 5. Comunicación resultados | Dev | 8.1 días | 19.3% | PowerBI + Diligent |
| 6. Desarrollo + Monitoreo | Dev | 0.6 días | 1.4% | Automatizado |
| 7. Despliegue | Dev + Líder | 1 día | 2.4% | Correos en vivo |
| **TOTAL** | | **42.2 días** | **100%** | ~6 semanas |

---

### 2.4 DEPENDENCIAS Y BLOQUEOS

**Dependencias externas (qué bloquea este flujo):**

| Dependencia | Estado afectado | Duración de espera | Frecuencia | Impacto |
|-------------|-----------------|-------------------|-----------|---------|
| Disponibilidad de Coordinador Aud. | Estado 1-2 | 1-3 días | 50% de proyectos | Alto |
| Disponibilidad de Dev | Estado 3-7 | 2-4 días | 70% de proyectos | Alto |
| Documentación de SAP Hanna | Estado 3 | 2-5 días | 30% de proyectos | Alto |
| Validación de stakeholders | Estado 2 | 1-2 días | 40% de proyectos | Medio |

**Puntos de espera o cuellos de botella más críticos:**
- 🔴 **ESTADO 3 (Ingeniería de Datos):** 12.5 días (29.8% del tiempo total). Requiere queries complejas y documentación de tablas.
- 🟡 **ESTADO 2 (Definición de Pruebas):** 8 días. Ambigüedades aquí generan retrabajos en Estado 3.
- 🟡 **ESTADO 5 (Comunicación):** 8.1 días. Formato inconsistente entre herramientas.
- 🟢 **Oportunidad:** El Estado 6 (Desarrollo) solo toma 0.6 días. Si se automatizara más, podría bajar a 0.2 días.