# Notas de clase

## Links cursos
Platzi - Azure Devops
https://platzi.com/cursos/azure-devops/permisos-y-grupos-de-usuarios-en-azure-d/
Diplomado Javeriana
https://educacioncontinua.javerianacali.edu.co/d2l/le/enhancedSequenceViewer/401153?url=https%3A%2F%2F4d08695f-f803-489f-8d3e-2e68a7e386fc.sequences.api.brightspace.com%2F401153%2Factivity%2F3073364%3FfilterOnDatesAndDepth%3D1

## Clase 3/20.

Caracteristicas del DevOps:
* Concepto del 2009.
* Es un concepto de mejora continua que involucra cada uno de los aspectos de TI y procesos de desarrollo.
* Se enfoca en relacionar las personas, los procesos y las herramientas.

Entonces: A partir de una buena definición de proceso y un buen kit de herramientas se realicen soluciones optimas para la mejora de los procesos. 

Hay una relación directa del Agilismo con la cultura DevOps, pues este ultimo es un pilar fundamental para apalancar los despliegues continuos y rapidos.

DevOps no es: 
* Un puesto de trabajo.
* Una herrmaienta.
* Una metodología ágil.
* Una tecnología.
* Un rol.

DevOps es una cultura que converge entre las personas, las herramientas y los procesos.

Herramientas que utilizan esta cultura:
Azure
Jira
gitLab y GitHub (GitHub action)
Jenkins

Entonces DevOps va de la mano con:
* Agilismo.
* Automatización.
* Soporte de infraestructura.
* Integración continua y despliegue continuo.

Grafico resumen del objetivo de automatización del ciclo DevOps:
![alt text](image.png)

### Proceso DevOps - ciclo de vida (versión texto)

El diagrama es un símbolo de infinito dividido en dos mitades que representan un ciclo continuo sin fin:

- **Dev** (mitad izquierda, sentido antihorario): `Plan -> Code -> Build -> Test`
- **Release** (punto de cruce entre ambas mitades, pasa de Dev a Ops)
- **Ops** (mitad derecha, sentido horario): `Deploy -> Operate -> Monitor`, y vuelve a cerrar el ciclo hacia `Plan`

Secuencia completa del ciclo/bucle OODA:

```
Plan -> Code -> Build -> Test -> Release -> Deploy -> Operate -> Monitor -> (vuelve a Plan)
```

```mermaid
flowchart LR
    Plan --> Code --> Build --> Test --> Release --> Deploy --> Operate --> Monitor --> Plan
```

*Bucle OODA en la práctica:*
- Observe: Supervisión de métricas empresariales, tendencias de mercado, comportamiento del usuario y datos de telemetría.
- Oriente: Analiza opciones para lo que puedes ofrecer, posiblemente a través de experimentos.
- Decidir: determinar qué perseguir en función de los datos y las prioridades empresariales.
- Acto: Entrega de software de trabajo a usuarios reales y recopilación de comentarios.

*Ejercicio de cálculo del tiempo de ciclo:* Piense en el proceso de desarrollo actual. Cuánto tiempo tarda en ir de:
- ¿Confirmación de código → implementación de producción?
- ¿Solicitud de características → comentarios del cliente?
- Informe de errores → ¿Corregir en producción?

*Ejemplo:* Si tardamos 2 semanas en implementar un cambio de configuración de una sola linea. Entonces, el timepo de ciclo es de 2 semanas. Esto se convierte en una restricción de velocidad.

Frase interesante: *Sé informado por los datos, no completamente dirigido por datos.*

Informar para la toma de decisiones y no quedarse estancado en el análisis. Alguna implementaciones seran malas, otras buenas y otras no aportaran nada aparentemente medible. A lo que se refiere esto es que hay que dejarse de tanto pereque, interpretar y ejecutar otro ciclo guiado de: *Fallar rapido en las iniciativas que no avanzan en los objetivos empresariales y redoblar los esfuerzos en los resultados que apalancan los objetico

Link de mucho interés: https://learn.microsoft.com/es-es/azure/devops/get-started/?view=azure-devops

AZURE DevOps:
- Es la suite DevOps de Microsoft.
- Cabe resaltar que Microsoft en dueña de GitHub y son productos complementarios. SOn enfoques distintos.
- Antes Azure DevOps era Visual Studio Online. 
- Cubre todo el proceso de desarrollo.
- Se integra con multicloude (AWS, Azure, GCP).
- Versión: Azure DevOps Server - Esto permite instalar en la propia infraestructura de la empresa los servicios de A. DevOps. Tiene sus limitantes pero a veces esto le conviene a algunas compañias con politicas de seguridad estrictas.




Principales herramientas de Azure DevOps:

* Azure Boards

Herramientas de planeación ágiles

Mantenga un seguimiento del trabajo con paneles kanban, registros de trabajo pendiente interactivos y herramientas de planeamiento muy eficaces. Los informes y la rastreabilidad sin igual convierten a Boards en el lugar perfecto para todas sus ideas, grandes o pequeñas.

----------------------------------------------
* Azure Repos

Repositorios privados gratuitos ilimitados

Consiga un excelente hospedaje GIT, flexible y con revisiones de código muy eficaces, así como repositorios gratuitos ilimitados para todas sus ideas, desde un proyecto de una sola persona hasta el repositorio más grande del mundo.
----------------------------------------------

* Azure Pipelines

CI/CD para cualquier plataforma

Compile, pruebe e implemente soluciones con cualquier lenguaje, en cualquier nube o en el entorno local. Ejecute archivos en paralelo en Linux, macOS y Windows, e implemente contenedores en hosts individuales o en Kubernetes.
----------------------------------------------

* Azure Artifacts

Repositorio de paquetes universal

Comparta paquetes Maven, npm, NuGet y Python de orígenes públicos y privados con todo su equipo. Integre el uso compartido de paquetes en sus canalizaciones de CI/CD de una forma sencilla y escalable.
----------------------------------------------

* Azure Test Plans

Pruebas manuales y exploratorias

Realice pruebas periódicas y publique versiones con confianza. Mejore la calidad global del código con herramientas de pruebas manuales y exploratorias para sus aplicaciones.


#################################
# CONTROL DE VERSIONES
#################################

UTILIZAR HERRAMIENTAS DE OCNTROL DE VERSIONES EN EL DESARROLLO DE SOFTWARE BRINDA BENEFICIOS COMO UN HISTORIAL COMPLETO DE CAMBIOS, FACILIDAD DE COLABORACIÓN, GESTIÓN DE CONFLICTOS Y CAPACIDAD DE ROLLBACK. Por otro lado, no utilizar estas herramientas puede generar problemas como la perdida de cambios, dificultades en la colaboración, falta de seguimiento y trazabilidad, así como el riesgo de pérdida de código. Por lo tanto, es altamente recomendable utilizar herramientas de control de versiones para mejorar la eficiencia y la calidad del desarrollo de software.
Las principales herramientas son:
* GIT: COntrol de versiones distribuida (main+ramas+clones).
* SUBVERSION(SVN): Control de versiones centralizada(main).
* MERCURIAL: Control de versiones distribuida.

#################################
# AUTOMATIZACIÓN DE PRUEBAS Y DESPLIEGUE
#################################
Beneficios de la automatización de pruebas y despliegue de software:

* Eficiencia y ahorro de tiempo: La automatización de pruebas y despliegue de software permite ejecutar pruebas de manera rápida y repetible, lo que ahorra tiempo y recursos. Las pruebas automatizadas se pueden ejecutar automáticamente, lo que reduce la dependencia de las pruebas manuales y permite a los equipos de desarrollo liberar software de manera más rápida y frecuente. 
* Mayor cobertura de pruebas: La automatización de pruebas permite realizar pruebas exhaustivas en diferentes escenarios y configuraciones, lo que ayuda a garantizar una mayor cobertura de pruebas. Esto significa que se pueden identificar y solucionar problemas de manera más efectiva antes de que el software se despliegue en producción. 
* Detección temprana de errores: Al automatizar las pruebas, es posible detectar errores y problemas de manera temprana en el ciclo de desarrollo. Esto permite a los equipos abordar los problemas rápidamente y evitar la propagación de errores a lo largo del proceso de desarrollo, lo que ahorra tiempo y esfuerzo en la resolución de problemas más adelante. 
* Consistencia y confiabilidad: Las pruebas automatizadas aseguran que las pruebas se realicen de manera consistente y confiable. Elimina la posibilidad de errores humanos y garantiza que las pruebas se realicen siguiendo un proceso estandarizado, lo que mejora la calidad del software entregado.

1.2. Problemas asociados con la falta de automatización de pruebas y despliegue:

* Retrasos en el tiempo de entrega: Si las pruebas y el despliegue de software se realizan manualmente, puede llevar mucho tiempo completar estas tareas. Esto puede resultar en retrasos en la entrega del software y afectar la capacidad de respuesta del equipo de desarrollo.
* Errores humanos: Las pruebas manuales están sujetas a errores humanos, ya sea por omisión, falta de atención o inconsistencias en el proceso. Esto puede llevar a la introducción de errores en el software y afectar negativamente su calidad.  
* Falta de cobertura de pruebas adecuada: Las pruebas manuales tienden a ser limitadas en términos de cobertura y pueden pasar por alto ciertos escenarios y configuraciones críticas. Esto puede resultar en la falta de detección de errores importantes y afectar la estabilidad y confiabilidad del software.  
* Mayor costo y esfuerzo: Las pruebas manuales requieren más recursos humanos y tiempo, lo que puede aumentar los costos y la carga de trabajo. Además, la falta de automatización puede generar la necesidad de repetir pruebas en cada ciclo de desarrollo, lo que implica un mayor esfuerzo y consume recursos valiosos.  

En resumen, la automatización de pruebas y despliegue de software brinda beneficios como la eficiencia, el ahorro de tiempo, mayor cobertura de pruebas, detección temprana de errores, consistencia y confiabilidad. Por otro lado, la falta de automatización puede resultar en retrasos en el tiempo de entrega, errores humanos, falta de cobertura de pruebas adecuada y mayor costo y esfuerzo. Por lo tanto, es altamente recomendable automatizar estas tareas para mejorar la eficiencia, la calidad y la entrega de software.

#################################
# HERRAMIENTAS DE INTEGRACIÓN CONTINUA (CI - CONTINUOUS INTEGRATION) Y ENTREGA CONTINUA (CD - CONTINUOUS DELIVERY)
#################################
Las herramientas de integración continua (CI) y entrega continua (CD) ofrecen una serie de beneficios significativos en el desarrollo de software:  

1. Detección temprana de errores: La CI permite la integración automática y regular del código, lo que ayuda a identificar problemas rápidamente, antes de que se conviertan en problemas más grandes.  
2. Entrega más rápida: La automatización en la CD reduce el tiempo entre la escritura del código y su implementación, permitiendo actualizaciones más frecuentes y ágiles.  
3. Mejora en la calidad del software: La ejecución continua de pruebas asegura la calidad del código, lo que reduce la presencia de errores en el producto final.  
4. Facilita la colaboración: La CI fomenta un entorno en el que varios desarrolladores pueden trabajar en el mismo proyecto sin problemas, ya que sus cambios se integran automáticamente.  
5. Mayor eficiencia y productividad: Al automatizar tareas repetitivas como pruebas, compilación y despliegue, los equipos pueden centrarse en tareas más creativas y estratégicas.

Los inconvenientes de no utilizar estas herramientas pueden ser bastante significativos: 
1. Mayor propensión a errores: Sin CI/CD, los errores pueden pasar desapercibidos durante mucho tiempo, lo que resulta en costosos errores de último minuto o en problemas que solo se descubren en etapas avanzadas del desarrollo. 
2. Procesos manuales lentos: Sin automatización, las pruebas, compilaciones y despliegues requieren más tiempo y esfuerzo humano, lo que ralentiza el proceso de desarrollo. 
3. Menor flexibilidad y agilidad: La falta de CI/CD puede hacer que los equipos sean menos ágiles para adaptarse a cambios rápidos o implementar actualizaciones frecuentes, lo que afecta la competitividad y la capacidad de respuesta. 
4. Dificultades en la colaboración: La integración manual del código puede llevar a conflictos entre versiones, dificultando la colaboración entre desarrolladores y generando más trabajo para resolver discrepancias. 

En resumen, la implementación de herramientas de CI/CD ayuda a mejorar la calidad, la velocidad y la eficiencia del desarrollo de software, mientras que la falta de estas herramientas puede resultar en problemas que afectan directamente la calidad del producto final y la eficiencia del equipo de desarrollo.

**Herramientas de Integración Continua (CI):**
1. Jenkins: Es una de las herramientas CI más populares y de código abierto. Permite la integración continua de forma automatizada y es altamente personalizable mediante plugins.
2. Travis CI: Es una plataforma de CI en la nube que se integra fácilmente con repositorios de GitHub. Es conocida por su sencillez de uso y configuración.
3. CircleCI: Ofrece CI/CD en la nube, con soporte para una variedad de lenguajes y frameworks. Proporciona una configuración basada en archivos y una amplia gama de opciones de personalización.
4. GitLab CI/CD: Integrado directamente en GitLab, ofrece un flujo de trabajo de CI/CD que permite a los equipos construir, probar y desplegar proyectos de forma automática. 
5. TeamCity: Ofrece una solución CI potente y fácil de usar, con integración con múltiples herramientas y plataformas.

**Herramientas de Entrega Continua (CD):**
1. Ansible: Automatiza el aprovisionamiento, la configuración y el despliegue de aplicaciones. Se utiliza para orquestar y administrar infraestructuras. 
2. Docker: No es específicamente una herramienta de CD, pero es fundamental para la implementación continua. Proporciona contenedores que simplifican la implementación y portabilidad de aplicaciones.
3. Spinnaker: Diseñada originalmente por Netflix, es una plataforma de CD de código abierto que permite la implementación continua en múltiples nubes.
4. AWS CodePipeline: Es un servicio de AWS que permite orquestar y automatizar la entrega continua de manera sencilla dentro del ecosistema de Amazon Web Services.
5. Google Cloud Build: Herramienta de Google Cloud Platform que permite crear, probar y desplegar aplicaciones de forma automática en la nube.
6. Microsoft Azure Pipeline: es la solución de Microsoft integrada a su plataforma de gestión de equipos Azure, funciona de forma similar al pipeline de AWS. 

Estas herramientas son solo algunas de las disponibles, y su elección dependerá de las necesidades específicas del proyecto, la infraestructura utilizada y las preferencias del equipo de desarrollo.

#################################
# INFRAESTRUCTURA COMO CÓDIGO (IaC) Y HERRAMIENTAS
#################################
La infraestructura como código (IaC) es una metodología que consiste en manejar y gestionar la infraestructura de sistemas informáticos utilizando código, en lugar de configuraciones manuales o procesos interactivos. Básicamente, es aplicar los principios de desarrollo de software al manejo de la infraestructura.
En lugar de configurar servidores, redes o cualquier otro componente de la infraestructura de manera manual, se utiliza código para definir y automatizar estos recursos. Esto se logra mediante el uso de lenguajes de programación específicos o herramientas diseñadas para este propósito, como Terraform, AWS CloudFormation, Ansible o Chef, entre otros. 

**Aspectos relevantes.**

```mermaid
mindmap
	root((IaC))
		Abstraccion de la infraestructura
			Describe la infraestructura deseada usando codigo
			Facilita la creacion de entornos complejos con coherencia
		Automatizacion y consistencia
			Automatiza maquinas virtuales, redes y seguridad
			Reduce errores humanos y mantiene implementaciones consistentes
		Control de versiones y reproducibilidad
			Permite versionar los cambios
			Ayuda a reconstruir entornos exactamente como estaban
		Escalabilidad y flexibilidad
			Facilita crear y destruir entornos rapidamente
			Se adapta a desarrollo, pruebas y produccion
```
Resumen:
- **Abstraccion de la infraestructura:** permite describir la infraestructura deseada utilizando codigo.
- **Automatizacion y consistencia:** ayuda a automatizar tareas repetitivas y evita errores humanos.
- **Control de versiones y reproducibilidad:** permite rastrear cambios y reconstruir entornos con precision.
- **Escalabilidad y flexibilidad:** facilita ajustar la infraestructura segun las necesidades del proyecto.

La infraestructura como código es una práctica que utiliza código para definir, configurar y administrar la infraestructura de manera automatizada y escalable, mejorando la eficiencia, la consistencia y la agilidad en el despliegue y gestión de sistemas informáticos. 

**Cuando no se utiliza IaC, pueden surgir varios problemas:**
1. Inconsistencia: La infraestructura manual tiende a ser inconsistente, ya que las configuraciones pueden variar entre diferentes entornos (desarrollo, pruebas, producción). Esto puede provocar errores inesperados y dificultar la replicación de entornos. 
2. Dificultad en la gestión: Gestionar manualmente la infraestructura es más propenso a errores y más lento en términos de implementación y cambios. Esto puede causar problemas de tiempo de inactividad y retrasos en la entrega. 
3. Falta de trazabilidad y documentación: Sin IaC, es más difícil mantener un registro claro de los cambios en la infraestructura y entender cómo se configuró un entorno en particular. Esto puede complicar la resolución de problemas y la colaboración entre equipos. 
4. Mayor riesgo de errores humanos: La configuración manual aumenta la posibilidad de cometer errores durante la implementación o la actualización de la infraestructura, lo que puede tener repercusiones costosas en términos de tiempo y recursos.

En resumen, adoptar prácticas de infraestructura como código proporciona consistencia, agilidad y eficiencia en el desarrollo y gestión de la infraestructura, mientras que la falta de uso puede llevar a problemas de consistencia, errores humanos y dificultades en la gestión y mantenimiento.

Existen varias herramientas de infraestructura como código, cada una con sus fortalezas y casos de uso específicos. Aquí te presento algunas de las principales:
1. Terraform: Es una herramienta ampliamente utilizada y agnóstica de proveedor, lo que significa que puedes usarla para gestionar recursos en múltiples plataformas (AWS, Azure, Google Cloud, entre otros). Es ideal cuando se requiere trabajar con entornos heterogéneos o migrar entre proveedores en el futuro. Terraform utiliza archivos de configuración declarativos (llamados archivos HCL) para describir la infraestructura.
2. AWS CloudFormation: Es específica de Amazon Web Services (AWS) y se utiliza para definir y desplegar recursos en la nube de AWS. Si te enfocas exclusivamente en AWS, CloudFormation puede ser una elección sólida, ya que está integrada completamente en el ecosistema de AWS. 
3. Azure Resource Manager (ARM) Templates: Similar a CloudFormation pero para Microsoft Azure. Permite describir y desplegar recursos en Azure utilizando archivos de plantilla JSON. Si trabajas principalmente en Azure, esta puede ser la opción más natural.
4. Ansible: Aunque es conocida principalmente como una herramienta de automatización de configuración, Ansible también se puede utilizar para manejar la infraestructura como código. Es agente-less y utiliza YAML para describir configuraciones. Es particularmente útil para la configuración de software y el despliegue en múltiples nodos. 
5. Chef y Puppet: Estas herramientas se centran más en la configuración y gestión de la infraestructura en sistemas y servidores. Son excelentes para configuraciones complejas y gestionar el estado deseado de los sistemas a lo largo del tiempo.


**La elección de la herramienta depende de varios factores:**
*  Entorno de nube específico: Si estás comprometido con un proveedor de nube específico, como AWS o Azure, su herramienta nativa (CloudFormation o ARM) puede ser la mejor opción debido a su integración y compatibilidad. 
* Requerimientos de multi-cloud o portabilidad: Si necesitas trabajar en múltiples nubes o mantener la capacidad de cambiar fácilmente entre proveedores, Terraform puede ser más adecuada debido a su agnosticismo de proveedor.
* Habilidades y preferencias del equipo: La experiencia del equipo en una herramienta específica puede influir en la elección. Es posible que un equipo que ya esté familiarizado con Ansible, Chef o Puppet prefiera seguir utilizando esas herramientas.

En última instancia, la mejor herramienta depende de las necesidades específicas del proyecto, el entorno de implementación y las habilidades del equipo.

#################################
# VISUAL STREAM MAPPING
#################################
1. Gestión del flujo de valor en un entorno ágil
Muchas organizaciones enfrentan obstaculos para alacanzar los resultados prometidos por Agile, y un obstaculo común son los *silos organizativos*.

¿Qué es la gestión del flujo de valor?
Es una *solución sistemática* para comprender y mejorar el **flujo de valor empresarial**. Desde la solicitud del cliente hasta la entrega de valor. Este enfoque va más allá del compromiso tradicional y busca **impulsar la mejora continua y generar más valor para el cliente** (Jeff Rosenbaugh).

El flujo de valor es: La secuencia de pasos que agregan valor para el cliente.Enotnces, se trata de optimizar los desperdicios y optimizar el proceso basado en ese flujo. Desde una perspectiva ágil el flujo de valor permite:
* Priorizar resultados sobre la producción de funciones. Escencal para cerrar la brecha entre prácticas ágiles y la verdadera promesa de valor. 

En mis palabras. Uno puede ágilizar tambien tareas que no generan nada, tareas basura. Por tanto, entender el flujo de valor es crucial, para priorizar aquellas actividades que le dan valor al cliente y 
por tanto tienen un ROI (sea economico, temporal, de lobby) mucho más palpable que otras actividades.

2. Beneficios de la gestión del flujo de valor.
flowchart TD
    A["Aceleración del tiempo<br/>de obtención de valor"] --> B["Alineación de equipos<br/>multifuncionales"]
    B --> C["Medición clara del<br/>desempeño del sistema"]
    C --> D["Inversiones basadas<br/>en datos"]
    D --> E["Eliminación de desperdicios<br/>y mejora de la efectividad"]
    E --> A

* Aceleración del tiempo para obtener valor: Al enfocarse en el flujo completo, naturalmente se obtiene valor de forma más rapida.
* Alineación de equipos multifuncionales: Objetivos comunes, priorización de tareas criticas y eliminación de duplicidad.
* Medición clara del desempeño del sistema: Al medir proporciona una visual/comprensión transparente de los flujos de valor permitiendouna medición mas acertiva.
* Permite presupuestar los flujos completos y no segmentado por poryectos.
* Eliminación de desperdicios y mejora de la efectividad: Porque al levantar el flujo, se detecta y se eliminan desperdicios del ciclo, esto aumenta la eficiencia y reduce la sobrecarga de los equipos.

3. Errores comunes en la gestión del flujo de valor.
A pesar de sus beneficios, las organizaciones pueden resistirse a adoptar la gestión del flujo de valor debido a:
* *Alterar el Statu Quo:* El cambio puede revelar prioridades desalineadas e ineficiencias, lo que algunas organizaciones prefieren evitar.
* *Sesgo de sofisticación:* La percepción de que la gestión del flujo de valor es demasiado simple o que requiere inversiones costosas puede ser un obstáculo.
* *Entornos laborales cambiantes:* La transición a entornos de trabajo híbridos y remotos requiere adaptaciones en la forma en que se mapean y gestionan los flujos de valor.

4. ¿Qué medir en los flujos de valor?
* **Tasa de entrega de valor (Flow Velocity):** cantidad de elementos de flujo completados en un periodo determinado. Su objetivo es medir cuánto valor logra terminar el sistema en una ventana de tiempo dada.
* **Tiempo de flujo (Flow Time):** tiempo total que tarda un elemento de flujo desde que inicia el trabajo hasta que se completa, incluyendo tanto tiempo activo como tiempo de espera. Sirve para evaluar la velocidad real de entrega.
* **Carga de flujo (Flow Load):** número de elementos de flujo que se encuentran en progreso al mismo tiempo dentro del flujo de valor. Ayuda a detectar sobrecarga, exceso de trabajo en curso y cuellos de botella.
* **Distribución del flujo (Flow Distribution):** proporción de los distintos tipos de trabajo completados en un periodo, por ejemplo funcionalidades, defectos, deuda técnica o riesgos. Permite entender en qué se está consumiendo la capacidad del equipo.

Estas métricas se correlacionan con resultados comerciales deseados, conectando el trabajo con el impacto al cliente, el negocio y los ingresos.

5. KPIs adicionales útiles en este contexto.
* **Eficiencia de flujo (Flow Efficiency):** porcentaje del tiempo total en que un elemento realmente estuvo siendo trabajado frente al tiempo que permaneció esperando. Es útil para identificar desperdicio dentro del proceso.
* **Frecuencia de despliegue:** número de despliegues a producción realizados en un periodo determinado. Permite medir la capacidad del pipeline para entregar cambios de forma continua.
* **Tasa de fallos por cambio (Change Failure Rate):** porcentaje de despliegues o cambios que generan incidentes, rollback o degradación del servicio. Complementa la velocidad con una visión de estabilidad.
* **Tiempo medio de recuperación (MTTR):** tiempo promedio necesario para restaurar el servicio después de una falla en producción. Indica la resiliencia operativa del flujo.
* **Predictibilidad de entrega:** porcentaje de compromisos cumplidos frente a lo planificado para una iteración, sprint o periodo de entrega. Es clave para saber si el flujo produce resultados confiables para el negocio.

6. Herramientas para la gestión del flujo de valor.
* **Lucidchart:** herramienta de diagramación que interviene en la etapa de modelado del flujo. Sirve para mapear el flujo de valor, visualizar etapas, actores, dependencias, cuellos de botella y puntos de espera.
* **Miro:** pizarra colaborativa que interviene en la construcción colectiva del flujo. Ayuda a talleres de descubrimiento, identificación de desperdicios, priorización de mejoras y alineación entre negocio, desarrollo y operaciones.
* **Jira:** herramienta de gestión del trabajo que interviene en la ejecución y seguimiento del flujo. Permite visualizar backlog, trabajo en curso, estados, tiempos de ciclo y bloqueos sobre cada ítem de valor.
* **Azure DevOps:** plataforma que interviene en la trazabilidad del flujo desde la demanda hasta la entrega. Integra tableros, repositorios, pipelines y despliegues para seguir cómo una necesidad del cliente avanza hasta producción.
* **Planview Viz:** herramienta especializada en value stream management que interviene en la medición integral del flujo. Consolida datos de distintas herramientas para calcular métricas como Flow Velocity, Flow Time, Flow Load y Flow Distribution.

7. Consejos para la implementación.

La implementación de la gestión del flujo de valor no debería abordarse como una actividad aislada, sino como una práctica continua de observación, medición y mejora. Una forma útil de hacerlo es seguir estos pasos:

* **1. Comenzar de forma sencilla:** el primer esfuerzo debe centrarse en visualizar el flujo actual sin intentar optimizar todo al mismo tiempo. Lo recomendable es seleccionar un flujo concreto, por ejemplo desde que se solicita un cambio hasta que se despliega en producción, y mapear solo sus etapas principales. Aquí son útiles metodologías como **Lean**, porque ayudan a identificar desperdicio, y **Kanban**, porque permite visualizar el trabajo en curso y limitarlo. Un ejemplo sería iniciar con un tablero simple de cinco estados: solicitud, análisis, desarrollo, pruebas y despliegue. Esto da una primera fotografía real del sistema antes de introducir más detalle.

* **2. Aplicar mapeo inverso:** en lugar de comenzar describiendo tareas internas, conviene partir del resultado que espera el cliente o el negocio y retroceder hasta encontrar qué actividades permiten alcanzarlo. Esta lógica es propia del **Value Stream Mapping (VSM)** y también se alinea con enfoques de **product thinking**, donde primero se define el valor entregado. Por ejemplo, si la meta es reducir el tiempo para publicar una mejora crítica, se puede empezar desde la liberación en producción y retroceder hacia pruebas, desarrollo, análisis, aprobación y solicitud original. Esto ayuda a diferenciar pasos que agregan valor de pasos que solo agregan espera o burocracia.

* **3. Abrazar el aprendizaje continuo:** ningún flujo queda bien definido desde el primer intento. La organización necesita revisar datos, detectar patrones y ajustar tanto el proceso como los roles involucrados. Aquí encajan muy bien **Kaizen**, **retrospectivas ágiles** y el ciclo **PDCA (Plan-Do-Check-Act)**, porque convierten la mejora en una disciplina recurrente. Un ejemplo práctico sería revisar cada dos semanas el tiempo de flujo y la carga de flujo para detectar si las aprobaciones están retrasando la entrega. Si el cuello de botella aparece siempre en el mismo punto, el aprendizaje debe traducirse en un cambio concreto del proceso.

* **4. Mantener un documento vivo:** el mapa del flujo, sus políticas y sus métricas deben actualizarse conforme cambia la realidad operativa. No sirve documentar una vez y archivar, porque el flujo evoluciona con nuevas herramientas, nuevas dependencias y nuevas formas de trabajo. Este principio puede apoyarse en prácticas de **gestión del conocimiento**, **documentación continua** y **gobernanza ligera de procesos**. Un ejemplo sería mantener en Confluence, Notion o una wiki interna un mapa del flujo con responsables, criterios de entrada y salida por etapa, métricas observadas y mejoras pendientes. Así, el documento deja de ser descriptivo y se convierte en una herramienta de gestión.

* **5. Preguntar por qué de manera sistemática:** cuando aparece un retraso, retrabajo o falla, no conviene quedarse en la explicación superficial. La técnica de los **Cinco Porqués** permite profundizar hasta llegar a causas raíz, y puede complementarse con **Ishikawa** o análisis de causa raíz. Por ejemplo, si una entrega se retrasa, la primera respuesta puede ser "faltaron pruebas"; al seguir preguntando por qué, puede descubrirse que no había ambientes disponibles, que la automatización era insuficiente o que la definición de terminado era ambigua. La intervención correcta cambia por completo cuando se entiende la causa raíz real.

En conjunto, estos pasos permiten implementar la gestión del flujo de valor de manera progresiva y con foco en resultados. La clave no es mapear por mapear, sino usar el mapa, las métricas y el aprendizaje para tomar decisiones que reduzcan tiempos, eliminen desperdicios y aumenten la entrega de valor.

#################################
# SEGURIDAD EN DevOps
#################################
## 1. Automatización de pruebas de seguridad

### Concepto
La automatización de pruebas de seguridad busca incorporar controles de seguridad directamente en los pipelines CI/CD para detectar vulnerabilidades de forma temprana. OWASP destaca que DevSecOps incorpora actividades como SAST, DAST, IAST, análisis de dependencias (SCA) y escaneo de infraestructura dentro del ciclo de entrega continua. [Fuente: OWASP DevSecOps Guideline]

### Ejemplos concretos
- Ejecutar SonarQube o CodeQL en cada Pull Request.
- Escanear dependencias con Dependabot o Snyk.
- Ejecutar OWASP ZAP automáticamente antes de promover una versión a producción.
- Analizar imágenes Docker en busca de vulnerabilidades antes de publicarlas.

### Caso real
Log4Shell (2021) afectó millones de sistemas debido a una vulnerabilidad en Log4j. Las organizaciones con procesos automatizados de escaneo de dependencias pudieron identificar los sistemas afectados mucho más rápido.

### Lecturas recomendadas
- https://owasp.org/projects/devsecops-guideline
- https://devguide.owasp.org/en/09-operations/01-devsecops/
- https://learn.microsoft.com/es-es/training/modules/introduction-to-secure-devops/

### Cursos
- Microsoft Learn: Introducción a Secure DevOps
- Coursera: Introduction to DevSecOps

---

## 2. Gestión de configuración segura

### Concepto
Consiste en asegurar que servidores, aplicaciones, contenedores y servicios mantengan configuraciones seguras y consistentes.

### Ejemplos
- Deshabilitar servicios innecesarios.
- Utilizar Infrastructure as Code (Terraform, Bicep).
- Gestionar secretos mediante Azure Key Vault o Hashicorp Vault.
- Implementar políticas automáticas de configuración en Kubernetes.

### Caso real
Numerosas brechas en AWS han ocurrido debido a buckets S3 configurados erróneamente y expuestos públicamente.

### Lecturas
- OWASP DevSecOps Guideline
- Azure DevSecOps

---

## 3. Monitoreo y detección temprana

### Concepto
La seguridad no termina con el despliegue. Debe existir monitoreo continuo para detectar actividad sospechosa.

### Ejemplos
- Microsoft Sentinel para correlación de eventos.
- Detección de accesos anómalos.
- Alertas sobre escalamiento de privilegios.
- Detección de ejecución de código sospechoso.

### Caso real
El ataque a SolarWinds mostró la importancia de monitorear continuamente tanto el pipeline como los entornos productivos.

---

## 4. Segmentación y control de acceso

### Concepto
NIST define Zero Trust como un paradigma donde ningún usuario o dispositivo recibe confianza implícita solamente por su ubicación en la red.

### Ejemplos
- MFA obligatorio.
- Acceso Just-In-Time para administradores.
- Separación de ambientes Desarrollo, QA y Producción.
- Microsegmentación de redes.

### Caso de uso
Un desarrollador puede acceder al repositorio Git, pero no a la base de datos productiva.

### Lecturas
- NIST SP 800-207 Zero Trust Architecture.
- Microsoft Zero Trust.

---

## 5. Gestión de vulnerabilidades

### Concepto
Proceso continuo de identificación, clasificación, priorización y remediación de vulnerabilidades.

### Ejemplos
- Escaneo semanal con Nessus.
- Clasificación según CVSS.
- Parcheo automatizado de sistemas.

### Caso real
La vulnerabilidad Log4Shell mostró la necesidad de inventarios de software actualizados y escaneo permanente.

---

## 6. Educación y concienciación

### Concepto
La seguridad efectiva requiere una cultura organizacional en la que desarrolladores, operadores y responsables de negocio conozcan los riesgos de seguridad.

### Ejemplos
- Simulaciones de phishing.
- Laboratorios OWASP Juice Shop.
- Talleres de Secure Coding.

### Recurso recomendado
OWASP WebGoat y OWASP Juice Shop.

---

## 7. Principio de responsabilidad compartida

### Concepto
DevSecOps promueve que la seguridad sea responsabilidad de todos los equipos y no exclusivamente del área de seguridad.

Microsoft indica que DevSecOps convierte la seguridad en una responsabilidad compartida respaldada por automatización, validaciones continuas y políticas integradas al ciclo de desarrollo.

### Ejemplo
- Desarrollo corrige vulnerabilidades.
- Operaciones protege infraestructura.
- Seguridad define controles y monitorea riesgos.

---

## 8. Evaluación y mejora continua

### Concepto
OWASP SAMM proporciona un modelo de madurez para evaluar y mejorar continuamente la postura de seguridad del desarrollo de software.

### Ejemplos de métricas
- Tiempo promedio de remediación.
- Porcentaje de cobertura SAST.
- Vulnerabilidades críticas abiertas.
- Cobertura de MFA.

### Lecturas
- https://owasp.org/projects/samm
- https://owaspsamm.org/

# Integración de seguridad en pipelines CI/CD: aportes del video

El video aterriza los conceptos generales de DevSecOps a controles concretos que pueden incorporarse en un pipeline de Integración Continua y Despliegue Continuo (CI/CD). Mientras el material del módulo explica la importancia de la automatización de pruebas de seguridad y la gestión de identidades y accesos (IAM), el video detalla qué controles específicos deben automatizarse y en qué momento del pipeline aplicarlos.

1. Análisis Estático de Código (SAST)
¿Qué es?

El análisis estático de seguridad (Static Application Security Testing - SAST) consiste en revisar el código fuente sin necesidad de ejecutar la aplicación. El objetivo es detectar vulnerabilidades, errores de programación y malas prácticas antes de que el código sea integrado al repositorio principal.

Hallazgos típicos
Credenciales hardcodeadas.
Inyecciones SQL.
Validaciones insuficientes de entrada.
Uso inseguro de criptografía.
Exposición de información sensible.
Herramientas mencionadas en el video
SonarQube
ESLint
Checkmarx
Ejemplo práctico

Supongamos que un desarrollador introduce el siguiente código:

query = "SELECT * FROM usuarios WHERE id = " + user_input


Una herramienta SAST detectaría que el código es vulnerable a SQL Injection incluso antes de ejecutar la aplicación.

Caso real

La vulnerabilidad SQL Injection continúa formando parte de las categorías más frecuentes identificadas por OWASP en aplicaciones web empresariales.

Lecturas recomendadas
OWASP Code Review Guide
https://docs.sonarsource.com/

2. Escaneo de Dependencias (SCA)
¿Qué es?

El análisis de composición de software (Software Composition Analysis - SCA) busca identificar vulnerabilidades en bibliotecas de terceros utilizadas por la aplicación.

Actualmente la mayoría de los proyectos modernos contienen más código de terceros que código propio, lo que convierte esta práctica en una de las más importantes del pipeline.

Herramienta mencionada
OWASP Dependency Check
Ejemplo práctico

Si una aplicación utiliza:

log4j 2.14.1


un escaneo SCA identificaría la vulnerabilidad Log4Shell y bloquearía su despliegue hasta actualizarla.

Caso real

Log4Shell (CVE-2021-44228) afectó millones de sistemas en todo el mundo porque la librería vulnerable estaba presente en innumerables aplicaciones empresariales.

Recursos
OWASP Dependency Check
https://nvd.nist.gov/

3. Pruebas Automáticas de Seguridad
¿Qué son?

Son pruebas integradas al pipeline que validan automáticamente la aplicación y la infraestructura buscando vulnerabilidades conocidas.

Vulnerabilidades mencionadas en el video
SQL Injection
Cross-Site Scripting (XSS)
Configuraciones inseguras
Herramientas mencionadas
OWASP ZAP
Nessus
Ejemplo práctico

Después de desplegar una aplicación en un entorno temporal:

Build
 ↓
Deploy temporal
 ↓
OWASP ZAP Scan
 ↓
Promover a Producción


Si se detecta un formulario vulnerable a XSS, el pipeline falla automáticamente.

Beneficios
Retroalimentación inmediata para el desarrollador.
Menor costo de corrección.
Menos vulnerabilidades en producción.

4. Análisis Dinámico de Seguridad (DAST)
¿Qué es?

A diferencia del SAST, el análisis dinámico (Dynamic Application Security Testing - DAST) evalúa la aplicación mientras está ejecutándose.

Qué detecta
Errores de autenticación.
Configuraciones inseguras.
Exposición de APIs.
Fallos en sesiones.
Vulnerabilidades explotables en tiempo de ejecución.
Ejemplo práctico

Un escáner DAST revisa una aplicación desplegada e identifica que:

/api/clientes


permite acceder a información sin autenticación adecuada.

| Característica | SAST (Static Application Security Testing) | DAST (Dynamic Application Security Testing) |
|----------------|--------------------------------------------|---------------------------------------------|
| Momento de ejecución | Durante el desarrollo | Después del despliegue |
| Objeto analizado | Código fuente | Aplicación en ejecución |
| Requiere aplicación desplegada | No | Sí |
| Detecta | Errores de programación, malas prácticas y vulnerabilidades en el código | Fallos explotables en tiempo de ejecución y configuraciones inseguras |
| Velocidad | Generalmente más rápido | Generalmente más lento |
| Ventaja principal | Identifica problemas tempranamente | Simula escenarios más cercanos a un ataque real |
| Ejemplos de herramientas | SonarQube, Checkmarx, CodeQL | OWASP ZAP, Burp Suite, Nessus |

5. Verificación de Cumplimiento
¿Qué es?

El video enfatiza que los pipelines pueden validar automáticamente requisitos regulatorios y políticas internas.

Marcos normativos mencionados
PCI DSS
HIPAA
Ejemplos
PCI DSS

En sistemas que procesan tarjetas de crédito:

Cifrado obligatorio.
Registro de eventos.
Restricción de privilegios.
HIPAA

En sistemas de salud:

Protección de información médica.
Control de accesos.
Auditoría de actividades.
Beneficio

El cumplimiento deja de ser una auditoría puntual y pasa a evaluarse continuamente.

6. Automatización de Parches y Actualizaciones
¿Qué es?

El video destaca la importancia de automatizar la aplicación de parches de seguridad.

Ejemplo

Pipeline:

Nueva imagen Docker
    ↓
Escaneo de vulnerabilidades
    ↓
Actualización automática
    ↓
Pruebas
    ↓
Despliegue

Beneficios
Reduce ventanas de exposición.
Disminuye errores manuales.
Mejora tiempos de remediación.
Caso real

Muchas organizaciones afectadas por ransomware habían postergado actualizaciones críticas que ya contaban con parches disponibles.

7. Monitoreo Continuo
¿Qué es?

El video resalta que la seguridad debe extenderse a:

Desarrollo
Pruebas
Producción
Capacidades recomendadas
SIEM
Alertas automáticas
Detección de anomalías
Correlación de eventos
Herramientas recomendadas
Microsoft Sentinel
Splunk
Elastic Security
Caso de uso

Detectar:

Usuario de Desarrollo
↓
Acceso inusual a Producción
↓
Alerta automática
↓
Respuesta inmediata

Arquitectura DevSecOps sugerida

```mermaid
flowchart TD
    A[Repositorio Git] --> B[SAST<br/>SonarQube / Checkmarx]
    B --> C[SCA<br/>Dependency Check]
    C --> D[Build]
    D --> E[Pruebas de Seguridad<br/>OWASP ZAP / Nessus]
    E --> F[Despliegue Temporal]
    F --> G[DAST<br/>Pruebas en ejecución]
    G --> H[Compliance<br/>PCI DSS / HIPAA]
    H --> I[Producción]
    I --> J[Monitoreo Continuo<br/>Sentinel / Splunk]
```

Conclusiones clave del video

Los conceptos nuevos o ampliados respecto al material original son:

Diferenciación clara entre SAST y DAST.
Importancia específica del escaneo de dependencias (SCA).
Incorporación de validaciones de cumplimiento normativo dentro del pipeline.
Automatización de parches y actualizaciones de seguridad.
Seguridad entendida como una cadena continua desde el desarrollo hasta producción.
Herramientas concretas para implementar DevSecOps: SonarQube, ESLint, Checkmarx, OWASP Dependency Check, OWASP ZAP y Nessus.
Necesidad de automatizar al máximo los controles para detectar problemas tempranamente y reducir riesgos durante el despliegue.

Todo esto complementa directamente el contenido base del módulo sobre automatización de pruebas de seguridad, IAM e integración de la seguridad a lo largo del ciclo de vida del desarrollo descrito en ScreenshotsDeSeguridad.docx>.

# Fuentes

1. OWASP DevSecOps Guideline: https://owasp.org/projects/devsecops-guideline
2. OWASP Developer Guide - DevSecOps: https://devguide.owasp.org/en/09-operations/01-devsecops/
3. Microsoft Learn - Introducción a Secure DevOps: https://learn.microsoft.com/es-es/training/modules/introduction-to-secure-devops/
4. Microsoft Security - What is DevSecOps: https://www.microsoft.com/es-es/security/business/security-101/what-is-devsecops
5. NIST SP 800-207 Zero Trust Architecture: https://csrc.nist.gov/pubs/sp/800/207/final
6. OWASP SAMM: https://owasp.org/projects/samm
7. OWASP SAMM Model: https://owaspsamm.org/


#################################
# CULTURA Y COLABORACIÓN en DevOps
#################################

La cultura es uno de los pilares más importantes de DevOps. Más allá de las herramientas y la automatización, DevOps promueve que los equipos de desarrollo, operaciones, seguridad y negocio trabajen como una sola unidad con objetivos compartidos.

Una cultura colaborativa reduce los silos organizacionales, mejora la comunicación y permite identificar problemas más rápido. En DevSecOps, esta colaboración también incluye a los equipos de seguridad, integrando los controles de seguridad desde las primeras etapas del desarrollo.

La verdadera transformación DevOps ocurre cuando la organización pasa de una mentalidad de "áreas independientes" a una cultura de responsabilidad colectiva, comunicación abierta y mejora continua. Esto permite entregar software de manera más rápida, segura y alineada con las necesidades del negocio.

## Aspectos clave

### Alineación de objetivos

DevOps busca alinear los objetivos tecnológicos con los objetivos estratégicos del negocio. Todos los equipos trabajan hacia una misma meta: entregar valor al cliente de forma rápida, segura y confiable.

Esta alineación evita conflictos entre áreas, mejora la priorización de iniciativas y facilita la toma de decisiones basadas en el impacto para el negocio.

**Ejemplo práctico:** en lugar de medir únicamente la cantidad de funcionalidades desarrolladas, los equipos comparten métricas comunes como disponibilidad del servicio, satisfacción del cliente y tiempo de entrega de nuevas funcionalidades.

---

### Comunicación efectiva

La comunicación constante permite compartir información crítica, detectar riesgos tempranamente y responder más rápido ante incidentes o cambios en los requisitos.

Una cultura colaborativa fomenta la comunicación abierta entre desarrollo, operaciones, seguridad y negocio, reduciendo malentendidos y aumentando la transparencia durante todo el ciclo de vida del software.

**Ejemplo práctico:** cuando una vulnerabilidad es detectada durante una revisión de código, los equipos reciben la alerta de forma inmediata y coordinan rápidamente las acciones necesarias para su corrección.

---

### Flexibilidad y adaptabilidad

La colaboración entre equipos permite responder de forma más rápida a los cambios del negocio, nuevas necesidades de los usuarios o amenazas emergentes. Al compartir conocimiento y responsabilidades, los equipos pueden realizar ajustes y mejoras sin depender excesivamente de una única área.

En entornos ágiles y DevOps, esta capacidad de adaptación resulta fundamental para mantener ciclos de entrega rápidos sin comprometer la calidad ni la seguridad.

**Ejemplo práctico:** si se descubre una vulnerabilidad crítica en una dependencia de software, los equipos de desarrollo, operaciones y seguridad pueden coordinarse rápidamente para evaluar el impacto, actualizar la dependencia y desplegar la corrección en producción.

---

### Mejora continua

Una cultura colaborativa fomenta la retroalimentación constante entre los equipos. Los errores, incidentes y experiencias adquiridas durante el desarrollo se convierten en oportunidades para optimizar procesos y fortalecer las prácticas de trabajo.

La mejora continua es uno de los principios fundamentales de DevOps y busca que cada iteración aporte mayor calidad, eficiencia y seguridad que la anterior.

Las retrospectivas, los análisis de causa raíz y las métricas operativas permiten identificar oportunidades de optimización y aprender de los errores para evitar su repetición.

**Ejemplo práctico:** después de una falla en producción, el equipo realiza una retrospectiva para identificar causas raíz, documentar lecciones aprendidas y aplicar acciones preventivas en el pipeline de despliegue.

---

### Responsabilidad compartida

En DevOps, la responsabilidad sobre el software no termina cuando el código es entregado. Todos los equipos participan activamente en la calidad, disponibilidad, rendimiento y seguridad de la solución.

Este enfoque elimina los silos organizacionales tradicionales y genera un mayor sentido de pertenencia respecto a los resultados del producto. La colaboración entre áreas facilita una resolución más rápida de incidentes y una toma de decisiones más efectiva.

En DevSecOps, la seguridad también se convierte en una responsabilidad compartida, evitando que sea una actividad aislada ejecutada únicamente por un equipo especializado.

**Ejemplo práctico:** si ocurre una caída del servicio, desarrollo, operaciones y seguridad trabajan conjuntamente para restaurar la operación, identificar la causa del incidente y prevenir futuras ocurrencias.

---

### Innovación y creatividad

La colaboración entre equipos con diferentes conocimientos, experiencias y perspectivas impulsa la generación de ideas innovadoras. Cuando desarrolladores, operadores, especialistas de seguridad y áreas de negocio trabajan juntos, es más probable encontrar soluciones eficientes a problemas complejos.

DevOps fomenta la experimentación controlada, el aprendizaje continuo y la búsqueda constante de mejoras en procesos, herramientas y productos. Esta diversidad de enfoques no solo mejora la calidad del software, sino que también acelera la adopción de nuevas tecnologías y prácticas.

La integración de múltiples disciplinas favorece la creación de soluciones más robustas que consideran aspectos técnicos, operativos y de negocio desde una visión integral.

**Ejemplo práctico:** un equipo detecta que la validación manual de configuraciones consume varias horas por semana. Gracias a la colaboración entre desarrollo y operaciones, se implementa una validación automática dentro del pipeline CI/CD que reduce tiempos y errores humanos.

---

### Reducción de cuellos de botella

Uno de los principales objetivos de DevOps es eliminar las barreras que ralentizan la entrega de valor. La colaboración continua entre equipos permite identificar tempranamente procesos ineficientes, dependencias innecesarias o tareas manuales que retrasan el desarrollo y despliegue.

La automatización, la comunicación transparente y la responsabilidad compartida ayudan a optimizar los flujos de trabajo y a reducir los tiempos de espera entre etapas del ciclo de vida del software.

#### Beneficios principales

- Menores tiempos de entrega.
- Menos dependencias entre equipos.
- Resolución más rápida de problemas.
- Mayor estabilidad en los despliegues.
- Incremento de la productividad general.

**Ejemplo práctico:** si las aprobaciones manuales de despliegue generan retrasos recurrentes, el equipo puede implementar validaciones automáticas, pruebas de calidad y controles de seguridad en el pipeline CI/CD para agilizar la liberación de nuevas versiones sin comprometer la seguridad.

---

## Ejemplo integral de DevSecOps

En un modelo tradicional, el equipo de seguridad suele intervenir al final del proyecto, retrasando las entregas al encontrar vulnerabilidades cuando el desarrollo ya ha finalizado.

En DevSecOps, desarrollo, operaciones y seguridad participan desde el inicio. Las revisiones de código, pruebas automatizadas, escaneos de vulnerabilidades y controles de configuración se ejecutan automáticamente dentro del pipeline CI/CD. Esto permite detectar problemas tempranamente, reducir retrabajos y acelerar la entrega de software seguro.

---

## Idea clave para exponer

> La tecnología habilita DevOps, pero la cultura lo hace posible. Sin comunicación, colaboración y responsabilidad compartida, ninguna herramienta puede ofrecer todos los beneficios de DevOps. La cultura DevOps elimina los silos organizacionales y permite que los equipos trabajen como una sola unidad para entregar software de forma rápida, confiable y segura.

## Para profundizar

### Videos en español

- DevOps explicado desde cero:
  https://www.youtube.com/results?search_query=devops+desde+cero+espa%C3%B1ol

- Cultura DevOps y transformación organizacional:
  https://www.youtube.com/results?search_query=cultura+devops+espa%C3%B1ol

- Introducción a DevSecOps:
  https://www.youtube.com/results?search_query=devsecops+espa%C3%B1ol

### Lecturas recomendadas

- The DevOps Handbook:
  https://itrevolution.com/the-devops-handbook/

- Azure Well-Architected Framework:
  https://learn.microsoft.com/azure/well-architected/

- AWS - What is DevOps?:
  https://aws.amazon.com/devops/what-is-devops/

## Fuentes

- Microsoft Learn – DevOps Culture.
- AWS – What is DevOps?
- The DevOps Handbook (Gene Kim, Jez Humble, Patrick Debois y John Willis).
- Azure Well-Architected Framework.

#############

## Glosario

### DevOps
Conjunto de prácticas y principios culturales que integran desarrollo (Dev) y operaciones (Ops) para entregar software de forma más rápida, confiable y eficiente.

### DevSecOps
Extensión de DevOps que incorpora la seguridad como una responsabilidad compartida durante todo el ciclo de vida del software.

### Silos organizacionales
Situación en la que los equipos trabajan de manera aislada, con poca comunicación y objetivos independientes.

### Pipeline CI/CD
Proceso automatizado que permite compilar, probar y desplegar aplicaciones de forma continua.

### Retroalimentación (Feedback)
Información obtenida de usuarios, métricas o incidentes que permite mejorar productos y procesos.

### Cultura organizacional
Conjunto de valores, comportamientos, hábitos y formas de trabajo compartidos dentro de una organización.

### Cuello de botella
Actividad, proceso o recurso que limita la velocidad de entrega de valor.

### Responsabilidad compartida
Principio según el cual todos los participantes son responsables de la calidad, disponibilidad y seguridad de una solución.

### Mejora continua
Práctica de evaluar constantemente procesos, herramientas y resultados para identificar oportunidades de optimización.

---

# Contexto

La cultura y la colaboración son la base sobre la cual se construye DevOps. Aunque la automatización y las herramientas son importantes, el verdadero éxito de DevOps depende de la capacidad de las personas para trabajar de forma coordinada, compartir responsabilidades y mantener una comunicación efectiva.

DevOps busca eliminar los silos organizacionales tradicionales y fomentar la colaboración entre desarrollo, operaciones, seguridad y negocio. Esto permite acelerar la entrega de valor, mejorar la calidad del software y responder con mayor rapidez a los cambios del entorno.

Además, la adopción de DevOps requiere liderazgo, gestión del cambio y una cultura de aprendizaje continuo que permita a los equipos evolucionar constantemente, aprender de los errores y adaptarse a nuevas necesidades tecnológicas y de negocio.

---

# ¿Cómo identificar una buena cultura DevOps?

Una organización puede tener las mejores herramientas del mercado y aun así fracasar en su transformación si la cultura organizacional no acompaña esos cambios.

## Señales positivas

- Los equipos comparten objetivos comunes.
- Los errores se analizan para aprender, no para buscar culpables.
- Existe una comunicación abierta y transparente.
- El conocimiento está distribuido entre varias personas.
- Las mejoras pueden ser propuestas por cualquier miembro del equipo.
- Desarrollo, operaciones y seguridad trabajan de manera coordinada.

## Señales de alerta

- Equipos que se culpan mutuamente durante los incidentes.
- Dependencia excesiva de expertos únicos.
- Procesos manuales excesivos.
- Falta de documentación.
- Retrasos frecuentes por aprobaciones innecesarias.
- Resistencia constante a nuevas formas de trabajo.

---

# Preguntas para analizar la cultura de un equipo

Al observar una organización, intenta responder:

1. ¿Quién es responsable de los errores?
2. ¿Las áreas colaboran o trabajan separadas?
3. ¿Qué sucede cuando ocurre una falla?
4. ¿Existe aprendizaje después de los incidentes?
5. ¿Se comparten los conocimientos?
6. ¿Las decisiones son transparentes?
7. ¿Los procesos pueden mejorarse fácilmente?
8. ¿Las personas tienen libertad para proponer cambios?

Las respuestas suelen revelar más sobre la madurez DevOps de una organización que cualquier herramienta tecnológica.

---

# Aspectos clave

## Alineación de objetivos

DevOps busca alinear los objetivos tecnológicos con los objetivos estratégicos del negocio. Todos los equipos trabajan hacia una misma meta: entregar valor de forma rápida, segura y confiable.

Cuando los equipos entienden el impacto de su trabajo sobre el negocio, las decisiones técnicas se orientan a generar valor real para los usuarios.

### Ejemplo positivo

Una plataforma de comercio electrónico detecta que muchos usuarios abandonan sus compras por tiempos de carga elevados.

Desarrollo, operaciones y negocio establecen un objetivo común: reducir el tiempo de respuesta por debajo de dos segundos.

Todos los esfuerzos técnicos se alinean para alcanzar dicho resultado.

### Señal de alerta

Desarrollo mide únicamente funcionalidades entregadas mientras operaciones se enfoca únicamente en estabilidad. Ambas áreas terminan optimizando métricas distintas y entrando en conflicto.

---

## Comunicación efectiva

La comunicación efectiva implica compartir información de forma clara, oportuna y transparente entre todos los participantes del ciclo de vida del software.

Una buena comunicación reduce errores de interpretación, facilita la coordinación y acelera la resolución de incidentes.

### Ejemplo positivo

El equipo de seguridad detecta una dependencia vulnerable y comunica el hallazgo mediante un canal compartido.

Los desarrolladores corrigen el problema el mismo día evitando que llegue a producción.

### Ejemplo práctico cotidiano

Durante una reunión diaria, un desarrollador informa que necesita acceso a un entorno para continuar una tarea. Operaciones lo habilita en pocas horas y se evita un retraso de varios días.

### Señal de alerta

Los problemas se comunican únicamente por correo y nadie tiene claridad sobre el estado real de las incidencias críticas.

---

## Flexibilidad y adaptabilidad

La colaboración entre equipos permite responder rápidamente a cambios del negocio, nuevas necesidades de usuarios o amenazas emergentes.

Los equipos pueden realizar ajustes sin depender completamente de una sola persona o área.

### Ejemplo positivo

Una nueva regulación exige almacenar registros de auditoría durante cinco años.

Los equipos coordinan cambios en infraestructura, bases de datos y aplicaciones para implementar el requisito sin afectar la operación.

### Ejemplo práctico cotidiano

Se descubre una vulnerabilidad crítica en una librería utilizada por la aplicación. Gracias a los procesos automatizados y la colaboración entre áreas, el parche puede desplegarse el mismo día.

### Señal de alerta

Cada modificación requiere múltiples aprobaciones manuales y semanas de coordinación.

---

## Mejora continua

Cada despliegue, incidente o proyecto genera información valiosa que puede utilizarse para optimizar procesos y herramientas.

La mejora continua busca convertir los errores en oportunidades de aprendizaje.

### Ejemplo positivo

Después de una caída de servicio, el equipo identifica que la causa fue una configuración incorrecta.

En lugar de buscar culpables, crean validaciones automáticas para evitar que vuelva a ocurrir.

### Ejemplo práctico cotidiano

El equipo analiza métricas de pruebas y descubre que varias incidencias provienen de errores repetitivos. Como resultado, automatizan pruebas adicionales y reducen significativamente los defectos en producción.

### Señal de alerta

Los mismos incidentes ocurren una y otra vez porque nunca se investigan las causas raíz.

---

## Responsabilidad compartida

En DevOps, la calidad, disponibilidad y seguridad no pertenecen exclusivamente a un área específica.

Todos los participantes son responsables del éxito del producto.

### Ejemplo positivo

Una actualización genera errores en producción.

Desarrollo, operaciones y seguridad colaboran conjuntamente para identificar la causa, aplicar correcciones y prevenir futuras incidencias.

### Ejemplo práctico cotidiano

Si aumenta el consumo de recursos de una aplicación, no se espera a que operaciones "arregle el problema". El equipo completo analiza métricas, código y configuraciones para encontrar la solución.

### Señal de alerta

Las conversaciones suelen terminar con frases como:

- "Es un problema de infraestructura."
- "Es un problema de desarrollo."
- "Es un problema de seguridad."

---

## Innovación y creatividad

La colaboración entre diferentes disciplinas fomenta la innovación al combinar perspectivas técnicas, operativas y de negocio.

Las mejores soluciones suelen surgir cuando personas con conocimientos distintos trabajan juntas.

### Ejemplo positivo

Un desarrollador propone automatizar pruebas.

Operaciones sugiere integrarlas al pipeline.

Seguridad agrega análisis de vulnerabilidades.

El resultado es una solución más completa que la idea original.

### Ejemplo práctico cotidiano

Un equipo detecta que la creación de ambientes de prueba consume varias horas cada semana. Como resultado, implementan infraestructura como código y reducen ese proceso a pocos minutos.

### Señal de alerta

Las nuevas ideas suelen ser rechazadas con argumentos como:

> "Siempre lo hemos hecho así."

---

## Reducción de cuellos de botella

Todo proceso posee restricciones que limitan la velocidad de entrega.

La misión de DevOps es identificarlas y eliminarlas progresivamente.

### Beneficios

- Menor tiempo de entrega.
- Mayor productividad.
- Menos dependencias entre equipos.
- Mejor capacidad de respuesta ante incidentes.
- Mayor estabilidad operativa.

### Ejemplo positivo

Un despliegue requiere tres aprobaciones manuales.

El equipo implementa controles automáticos de calidad y seguridad dentro del pipeline CI/CD.

El tiempo de despliegue pasa de varios días a pocos minutos.

### Ejemplo práctico cotidiano

Una única persona aprueba todas las solicitudes de acceso a servidores. Durante vacaciones, múltiples proyectos quedan bloqueados. La organización implementa flujos automatizados y elimina la dependencia.

### Señal de alerta

Las tareas siempre terminan acumulándose en las mismas personas o equipos.

---

# Liderazgo y gestión del cambio

La transformación DevOps es principalmente un cambio cultural.

Los líderes deben:

- Comunicar claramente la visión.
- Promover la colaboración.
- Eliminar barreras organizacionales.
- Impulsar la experimentación.
- Fomentar el aprendizaje continuo.
- Reconocer los aprendizajes obtenidos de los errores.

## Ejemplo de resistencia al cambio

Un equipo acostumbrado a realizar despliegues manuales puede percibir la automatización como una amenaza.

Un buen líder explica los beneficios, ofrece capacitación y permite una adopción gradual en lugar de imponer cambios abruptos.

## ¿Cómo detectar liderazgo efectivo?

- Se escuchan propuestas del equipo.
- Los errores se transforman en aprendizaje.
- Las decisiones son transparentes.
- Existe apoyo para experimentar y mejorar.

---

# Cultura de aprendizaje continuo

En DevOps, el aprendizaje continuo es esencial para mantener la innovación y la capacidad de adaptación.

Los equipos deben disponer de espacios seguros para experimentar, compartir conocimientos y aprender tanto de los éxitos como de los errores.

## Prácticas recomendadas

- Capacitaciones frecuentes.
- Sesiones de intercambio de conocimiento.
- Retrospectivas.
- Documentación colaborativa.
- Laboratorios de experimentación.
- Comunidades técnicas internas.

## Ejemplo práctico

Después de implementar una nueva plataforma de contenedores, el equipo documenta los errores encontrados, organiza sesiones internas de capacitación y comparte las mejores prácticas con otras áreas.

De esta forma, el conocimiento deja de estar concentrado en unas pocas personas.

---

# Reflexión final

Cuando quieras evaluar la madurez DevOps de una organización, no empieces observando las herramientas.

Empieza observando a las personas:

- ¿Cómo se comunican?
- ¿Cómo reaccionan ante los errores?
- ¿Cómo toman decisiones?
- ¿Cómo comparten el conocimiento?
- ¿Cómo colaboran entre áreas?
- ¿Cómo enfrentan los cambios?

Las respuestas a estas preguntas suelen explicar el éxito o fracaso de una iniciativa DevOps mucho más que cualquier tecnología utilizada.

---

# Idea clave para exponer

> DevOps no es únicamente una metodología tecnológica. Es una transformación cultural basada en la colaboración, la comunicación, el liderazgo y el aprendizaje continuo. Cuando las personas comparten objetivos, conocimientos y responsabilidades, la organización puede entregar software de forma más rápida, segura y alineada con las necesidades del negocio.