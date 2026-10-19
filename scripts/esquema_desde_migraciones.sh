#!/usr/bin/env bash
# Levanta un PostgreSQL 16 con pgvector en Docker, aplica en orden de versión las
# migraciones Flyway del sistema (V*.sql) y deja la base lista para que
# scripts/diccionario_datos.py la introspeccione.
#
# Uso: scripts/esquema_desde_migraciones.sh /ruta/a/usal-tinku
# Variables opcionales: PUERTO (55432), CONTENEDOR (tinku-der).
set -euo pipefail
REPO="${1:?indicar la ruta del repositorio del sistema (usal-tinku)}"
MIG="$REPO/backend/src/main/resources/db/migration"
PUERTO="${PUERTO:-55432}"
CONTENEDOR="${CONTENEDOR:-tinku-der}"
export PGPASSWORD=pg

docker rm -f "$CONTENEDOR" >/dev/null 2>&1 || true
docker run -d --name "$CONTENEDOR" -e POSTGRES_PASSWORD=pg -e POSTGRES_DB=tinku \
    -p "$PUERTO:5432" pgvector/pgvector:pg16 >/dev/null
until pg_isready -h localhost -p "$PUERTO" -U postgres >/dev/null 2>&1; do sleep 1; done
sleep 2

# Orden numérico de versión (V1, V2, ..., V10), como lo aplica Flyway.
for f in $(ls "$MIG"/V*.sql | xargs -n1 basename | sort -t_ -k1.2 -n); do
    psql -h localhost -p "$PUERTO" -U postgres -d tinku -v ON_ERROR_STOP=1 -q -1 \
        -f "$MIG/$f" >/dev/null
    echo "aplicada $f"
done
echo "Esquema listo: PGHOST=localhost PGPORT=$PUERTO PGUSER=postgres PGPASSWORD=pg PGDATABASE=tinku"
