# 🔍 Ejemplo de Integración SAST
**Super App Security Kit – v1.0**

---

# 1. ¿Qué es SAST?

Static Application Security Testing (SAST) permite analizar el código fuente antes de desplegar la aplicación, identificando vulnerabilidades tempranas en el ciclo de desarrollo.

Su implementación reduce costos de remediación y mejora la seguridad desde etapas tempranas (Shift-Left Security).

---

# 2. Herramienta Recomendada

## SonarQube

SonarQube permite:

- Análisis estático automatizado.
- Detección de vulnerabilidades comunes (SQL Injection, XSS).
- Identificación de code smells y deuda técnica.
- Integración con pipelines CI/CD.

---

# 3. Ejecución Básica Local

Instalar sonar-scanner y ejecutar:

```bash
sonar-scanner \
  -Dsonar.projectKey=superapp \
  -Dsonar.sources=. \
  -Dsonar.host.url=http://localhost:9000 \
  -Dsonar.login=TOKEN
