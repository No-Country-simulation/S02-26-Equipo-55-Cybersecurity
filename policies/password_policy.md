# 🔐 Política de Contraseñas
**Super App Security Kit – v1.0**  
**Clasificación:** Uso Interno  

---

## 1. Objetivo

Establecer lineamientos mínimos para la creación, uso y gestión de contraseñas dentro de la organización.

---

## 2. Alcance

Aplica a:

- Empleados
- Administradores
- Proveedores con acceso a sistemas
- Cuentas de servicio

---

## 3. Requisitos de Contraseña

Las contraseñas deben:

- Tener mínimo 12 caracteres.
- Incluir letras mayúsculas y minúsculas.
- Incluir números.
- Incluir caracteres especiales.
- No contener información personal.
- No reutilizarse en los últimos 5 cambios.

---

## 4. Rotación

- Cuentas administrativas: cada 90 días.
- Cuentas estándar: cada 180 días.
- Cuentas comprometidas: cambio inmediato.

---

## 5. Almacenamiento

- Las contraseñas deben almacenarse utilizando hash seguro (bcrypt, Argon2 o PBKDF2).
- Está prohibido almacenar contraseñas en texto plano.
- Las credenciales no deben estar en código fuente.

---

## 6. Autenticación Multifactor

El MFA es obligatorio para:

- Accesos administrativos.
- Operaciones financieras.
- Accesos a producción.

---

## 7. Incumplimiento

El incumplimiento de esta política puede resultar en suspensión de acceso o medidas disciplinarias.
