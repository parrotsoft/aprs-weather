# aprs-weather

Script mínimo en Python que envía un paquete de posición (baliza meteorológica) a APRS-IS.

## Requisitos

- Python 3.12
- [uv](https://docs.astral.sh/uv/)

## Instalación

```bash
uv sync
```

## Configuración

Copia `.env.example` a `.env` y completa los valores:

| Variable      | Descripción                                  |
|---------------|----------------------------------------------|
| `CALLSIGN`    | Indicativo de estación                       |
| `PASSCODE`    | Código de acceso APRS-IS                     |
| `LATITUDE`    | Latitud en formato APRS (ej. `1035.27N`)     |
| `LONGITUDE`   | Longitud en formato APRS (ej. `07447.03W`)   |
| `CITY`        | Ciudad para consultar clima (ej. `Barranquilla`) |
| `COUNTRY`     | Código de país ISO 3166-1 alfa-2 (ej. `co`) |
| `OWM_API_KEY` | API key de OpenWeatherMap                    |

## Uso

```bash
uv run main.py
```

El script consulta la temperatura actual via OpenWeatherMap y envía un paquete APRS con el formato:

```
CALLSIGN>APRS:=LAT/LON>Ciudad 31°C
```

## Conexión

- **Servidor**: `rotate.aprs2.net:14580`
