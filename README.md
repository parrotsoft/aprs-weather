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

El script consulta el clima via OpenWeatherMap y envía:

1. **Paquete de posición** con datos meteorológicos en formato APRS estándar:

```
CALLSIGN>APRS:=LAT/LON_DDD/SSSgTTTtTTTrRRRpPPPhDDBDDDDDComentario
```

| Código  | Significado                       | Ejemplo                  |
|---------|-----------------------------------|--------------------------|
| `DDD/`  | Dirección del viento              | `052/` → 52°             |
| `SSS`   | Velocidad del viento (nudos)      | `011` → 11 nudos         |
| `gTTT`  | Ráfagas (nudos)                   | `g019` → 19 nudos        |
| `tTTT`  | Temperatura (°F)                   | `t081` → 27°C (81°F)     |
| `rRRR`  | Lluvia última hora (centésimas in) | `r000` → 0.00 in         |
| `pPPP`  | Lluvia desde media noche (cent. in) | `p000` → 0.00 in        |
| `hDD`   | Humedad (%)                        | `h79` → 79%              |
| `bDDDDD`| Presión (décimas de hPa)           | `b10060` → 1006.0 hPa    |

2. **Paquete de estado** con texto descriptivo (aparece en "Ultimo estado" en aprs.fi):

```
CALLSIGN>APRS:>Estacion meteorologica APRS - Ciudad
```
