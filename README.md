# aprs-weather

Script mínimo en Python que envía un paquete de posición (baliza meteorológica) a APRS-IS y termina.

## Requisitos

- Python 3.12
- [uv](https://docs.astral.sh/uv/)

## Instalación

```bash
uv sync
```

## Configuración

Copia `.env.example` a `.env` y completa los valores:

| Variable    | Descripción                          |
|-------------|--------------------------------------|
| `CALLSIGN`  | Indicativo de estación               |
| `PASSCODE`  | Código de acceso APRS-IS             |
| `LATITUDE`  | Latitud en formato APRS (ej. `1035.27N`) |
| `LONGITUDE` | Longitud en formato APRS (ej. `07447.03W`) |

## Uso

```bash
uv run main.py
```

Envía un paquete con el formato:

```
CALLSIGN>APRS:=LAT/LON>Barranquilla 31°C
```

## Conexión

- **Servidor**: `rotate.aprs2.net:14580`
- **Comentario**: hardcodeado (`Barranquilla 31°C`)
