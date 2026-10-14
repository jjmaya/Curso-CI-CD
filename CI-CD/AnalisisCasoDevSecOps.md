# Analisis Caso DevSecOps

## Contexto general

Una plataforma de comercio electronico no solo debe funcionar bien, tambien debe estar pensada para resistir ataques comunes desde el diseño. Si la empresa desarrolla una app para crear cuentas, buscar y comprar productos, gestionar pedidos y hacer pagos en linea, entonces la seguridad tiene que entrar desde el inicio del ciclo de vida, no al final como un parche.

Desde lo visto en clase, esto encaja muy bien con la idea de DevOps, CI/CD, automatizacion, trazabilidad y control de cambios. En otras palabras: si el desarrollo se mueve rapido, la seguridad tambien tiene que moverse rapido, pero sin improvisar.

---

## 1. Creacion de cuentas

### Problemas de seguridad posibles

- **Registro de usuarios con datos falsos o automatizados:** un atacante puede crear muchas cuentas para fraude, spam o abuso de promociones.
- **Contraseñas debiles:** si el sistema no exige buenas politicas, los usuarios terminan usando claves faciles de adivinar.
- **Exposicion de datos personales:** nombre, correo, telefono o documentos pueden filtrarse si hay malas validaciones o consultas inseguras.
- **Ataques de fuerza bruta o credential stuffing:** si el login no tiene protecciones, un atacante puede probar credenciales robadas masivamente.
- **Secuestro de cuenta:** si el flujo de recuperacion de contrasena es debil, alguien puede tomar control de la cuenta.

### Estrategias de mitigacion

- **Validacion fuerte de entrada y salida:** validar correo, telefono, contrasena y cualquier dato sensible desde backend, no solo desde el frontend.
- **Politicas de contrasena robustas:** exigir longitud minima, complejidad razonable y bloqueo de contrasenas comunes.
- **Hash seguro de contrasenas:** almacenar claves con algoritmos resistentes como bcrypt, scrypt o Argon2, nunca texto plano.
- **MFA o autenticacion de doble factor:** agregar una capa extra reduce mucho el impacto de robo de credenciales.
- **Rate limiting y CAPTCHA:** frena automatizacion y ataques masivos de registro o login.
- **Verificacion de correo o telefono:** ayuda a confirmar que la cuenta corresponde a un usuario real.
- **Recuperacion de cuenta segura:** enlaces temporales, tokens de un solo uso y expiracion corta.

### Ventajas

Estas practicas reducen la superficie de ataque desde el arranque. Si las contrasenas se guardan bien, aunque haya una fuga no se expone todo tan facil. Si se limita el numero de intentos y se valida el origen de la cuenta, se le complica mucho la vida al atacante. En seguridad, hacer mas dificil el abuso ya es una gran victoria.

---

## 2. Busqueda y compra de productos

### Problemas de seguridad posibles

- **Inyeccion SQL o consultas mal construidas:** si la busqueda no esta bien parametrizada, pueden acceder o alterar informacion de la base de datos.
- **Manipulacion de precios o carrito:** un usuario malicioso puede cambiar valores desde el navegador y pagar menos de lo debido.
- **Cross-Site Scripting (XSS):** un atacante puede insertar scripts en campos de busqueda, comentarios o filtros.
- **Acceso no autorizado a productos o datos internos:** catalogos, descuentos o reglas internas pueden quedar expuestos.
- **Fraude en la compra:** uso de tarjetas robadas, bots comprando rapido o abuso de cupones.

### Estrategias de mitigacion

- **Consultas parametrizadas y ORM seguro:** evitar concatenar strings en SQL.
- **Validacion en servidor de precios y totales:** nunca confiar en valores enviados por el cliente para calcular el cobro final.
- **Sanitizacion y codificacion de salida:** neutralizar contenido que pueda ejecutarse como script en el navegador.
- **Control de acceso por roles y permisos:** separar lo que ve un cliente normal de lo que ve un administrador o operador.
- **Firmar o recalcular el carrito en backend:** asi se evita que el usuario altere el monto final.
- **Monitoreo antifraude:** detectar patrones raros como muchas compras en poco tiempo o comportamientos automatizados.
- **Revisiones de codigo y pruebas automatizadas de seguridad:** incluir pruebas contra inyeccion, XSS y validaciones de negocio.

### Ventajas

La idea aqui es no confiar en lo que venga del navegador. El cliente puede mentir, tocar campos y alterar trafico; el backend es el que debe mandar. Si el precio real se calcula del lado del servidor y el codigo usa consultas seguras, se evita una buena parte del fraude y de la manipulacion del sistema.

---

## 3. Gestion de pedidos

### Problemas de seguridad posibles

- **IDOR o acceso indebido a pedidos ajenos:** si alguien cambia un identificador de pedido, podria ver informacion de otro cliente.
- **Alteracion del estado del pedido:** un atacante podria intentar marcar un pedido como pagado, enviado o entregado sin autorizacion.
- **Filtrado de informacion sensible:** direccion, telefono, historial de compras o detalles logisticos pueden quedar expuestos.
- **Problemas de trazabilidad:** si no hay logs claros, es dificil saber quien cambio un pedido y cuando.
- **Manipulacion de devoluciones o cancelaciones:** procesos mal protegidos pueden ser usados para fraude.

### Estrategias de mitigacion

- **Autorizacion por objeto y por rol:** verificar que el usuario tenga permiso para ver o modificar ese pedido en especifico.
- **Uso de identificadores opacos o no secuenciales:** disminuye la posibilidad de adivinar pedidos ajenos.
- **Registro de auditoria:** guardar quien hizo el cambio, desde donde y en que momento.
- **Estados de pedido controlados por reglas de negocio:** solo permitir transiciones validas, por ejemplo, no pasar de creado a entregado de forma directa.
- **Separacion de responsabilidades:** el cliente no debe poder forzar estados internos; el backend debe decidir los cambios.
- **Pruebas automatizadas sobre reglas de negocio:** validar que un pedido no pueda ser alterado fuera del flujo esperado.

### Ventajas

La gestion de pedidos no solo es un tema funcional, tambien es de confianza. Si un usuario puede tocar pedidos ajenos o saltarse estados, el sistema pierde integridad. Con autorizacion bien aplicada, reglas claras y auditoria, el proceso queda mas controlado y mucho mas facil de investigar si algo sale mal.

---

## 4. Pagos en linea

### Problemas de seguridad posibles

- **Exposicion de datos financieros:** tarjetas, tokens o referencias de pago pueden quedar visibles si la integracion esta mal hecha.
- **Intercepcion de transacciones:** sin proteccion adecuada, un atacante puede intentar interceptar o manipular la comunicacion.
- **Reutilizacion de tokens o sesiones:** si los tokens viven demasiado o no estan bien acotados, se pueden reutilizar.
- **Fraude de pago:** compras con tarjetas robadas o intentos de repetir cobros.
- **Errores de integracion con pasarelas:** una mala configuracion puede duplicar cargos o confirmar pagos incompletos.

### Estrategias de mitigacion

- **Uso de pasarelas certificadas:** reducir la cantidad de datos sensibles que toca directamente la aplicacion.
- **HTTPS obligatorio y configuracion segura de TLS:** proteger la informacion en transito.
- **Tokenizacion de datos de pago:** evitar almacenar informacion completa de tarjetas.
- **Cumplimiento de buenas practicas tipo PCI DSS:** aunque no se haga toda la certificacion completa, si conviene seguir sus principios basicos.
- **Validacion de callbacks y webhooks:** confirmar que la respuesta realmente venga del proveedor de pagos.
- **Idempotencia en cobros:** evitar cobros duplicados si la peticion se repite.
- **Monitoreo de transacciones sospechosas:** detectar montos raros, reintentos excesivos o patrones automatizados.

### Ventajas

En pagos, el objetivo no es solo que funcione, sino que sea confiable. HTTPS, tokenizacion y validacion de callbacks ayudan a reducir el riesgo de fuga o manipulación. Y la idempotencia es clave porque en sistemas reales las peticiones pueden repetirse; si no se controla eso, aparecen cobros dobles y caos operativo.

---

## 5. Estrategias transversales de desarrollo seguro

Ademas de lo especifico por funcion, la plataforma necesita practicas de base que sostengan toda la seguridad:

- **CI/CD con pruebas de seguridad automatizadas:** integrar pruebas unitarias, de integracion y de seguridad en el pipeline.
- **Analisis estatico de codigo:** detectar vulnerabilidades antes de llegar a produccion.
- **Control de versiones y revisiones de codigo:** evita cambios invisibles y mejora la trazabilidad.
- **IaC para infraestructura repetible:** servidores, redes y configuraciones deben definirse como codigo para reducir errores humanos.
- **Principio de minimo privilegio:** cada servicio y usuario solo debe tener lo estrictamente necesario.
- **Monitoreo y alertas:** detectar comportamientos anormales a tiempo.
- **Gestion de secretos:** no guardar llaves, tokens ni credenciales en el codigo fuente.
- **Backups y plan de recuperacion:** si algo falla, el sistema debe poder volver rapido.

### Ventajas

Esto conecta directamente con lo visto en clase: automatizacion, trazabilidad, control de cambios y mejora continua. Cuando la seguridad entra al pipeline, el equipo detecta fallos mas temprano y a menor costo. Es mucho mejor romper algo en pruebas que descubrirlo despues en produccion.

---

## 6. Conclusión

Una plataforma de comercio electronico necesita seguridad en cada punto donde el usuario interactua con el sistema. En cuentas, compras, pedidos y pagos, el riesgo siempre cambia, pero la logica es la misma: validar, controlar accesos, registrar eventos, automatizar pruebas y no confiar en el cliente.

La idea practica es sencilla: si el desarrollo ya usa cultura DevOps y CI/CD, entonces la seguridad no debe ser un agregado final. Debe ir dentro del proceso. Asi la plataforma gana en confianza, integridad y capacidad de respuesta frente a errores o ataques.
