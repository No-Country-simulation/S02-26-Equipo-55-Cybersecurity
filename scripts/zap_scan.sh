#!/bin/bash

# ==========================================
# Super App Security Kit
# Script de Escaneo Básico con OWASP ZAP
# ==========================================

TARGET=$1

if [ -z "$TARGET" ]; then
  echo "Uso: ./zap_scan.sh https://example.com"
  exit 1
fi

echo "Iniciando escaneo contra $TARGET..."

zap-baseline.py -t $TARGET -r zap_report.html

echo "Escaneo finalizado."
echo "Reporte generado: zap_report.html"
