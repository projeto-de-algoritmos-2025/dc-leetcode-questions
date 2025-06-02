# Smart API Compressor

O **Algoritmo de Huffman** é uma técnica de compressão que analisa a **frequência de caracteres** em um texto e cria códigos binários mais curtos para os caracteres que aparecem com mais frequência. Quando aplicado a respostas JSON de APIs, ele identifica padrões repetitivos e os substitui por representações mais compactas.

## Processo de Funcionamento

### **1. Interceptação da Resposta**

Quando uma API Django retorna uma resposta JSON, nosso middleware intercepta essa resposta antes dela ser enviada ao cliente.

### **2. Análise de Frequência**

O sistema analisa todo o conteúdo JSON e conta:

- **Caracteres individuais**: `{`, `}`, `"`, `:`, `,`, letras, números
- **Palavras comuns**: nomes de campos como `"id"`, `"name"`, `"email"`
- **Padrões repetitivos**: estruturas que se repetem no JSON

### **3. Construção da Árvore Huffman**

Com base nas frequências encontradas, constrói uma árvore binária onde:

- Caracteres mais frequentes ficam mais próximos da raiz (códigos curtos)
- Caracteres menos frequentes ficam nas folhas (códigos longos)

### **4. Codificação**

Substitui cada caractere por seu código binário correspondente na árvore.

### **5. Transmissão**

Envia o resultado comprimido junto com a árvore de decodificação para o cliente.

## Exemplo JSON Original de uma API

Sistema de Monitoramento IoT Industrial:

```json
{
  "timestamp": "2024-06-01T15:30:00.000Z",
  "factory_id": "FACTORY_SAO_PAULO_001",
  "status": "success",
  "data": {
    "sensors": [
      {
        "sensor_id": "TEMP_SECTOR_A_001",
        "type": "temperature",
        "status": "online",
        "location": "SECTOR_A_FLOOR_01",
        "value": 23.5,
        "unit": "celsius",
        "last_update": "2024-06-01T15:30:00.000Z",
        "battery_level": 85,
        "signal_strength": "strong",
        "maintenance_status": "ok"
      },
      {
        "sensor_id": "TEMP_SECTOR_A_002",
        "type": "temperature",
        "status": "online",
        "location": "SECTOR_A_FLOOR_01",
        "value": 24.1,
        "unit": "celsius",
        "last_update": "2024-06-01T15:30:00.000Z",
        "battery_level": 92,
        "signal_strength": "strong",
        "maintenance_status": "ok"
      },
      {
        "sensor_id": "TEMP_SECTOR_A_003",
        "type": "temperature",
        "status": "online",
        "location": "SECTOR_A_FLOOR_01",
        "value": 23.8,
        "unit": "celsius",
        "last_update": "2024-06-01T15:30:00.000Z",
        "battery_level": 78,
        "signal_strength": "strong",
        "maintenance_status": "ok"
      },
      {
        "sensor_id": "HUMID_SECTOR_A_001",
        "type": "humidity",
        "status": "online",
        "location": "SECTOR_A_FLOOR_01",
        "value": 65.2,
        "unit": "percentage",
        "last_update": "2024-06-01T15:30:00.000Z",
        "battery_level": 89,
        "signal_strength": "strong",
        "maintenance_status": "ok"
      },
      {
        "sensor_id": "HUMID_SECTOR_A_002",
        "type": "humidity",
        "status": "online",
        "location": "SECTOR_A_FLOOR_01",
        "value": 64.8,
        "unit": "percentage",
        "last_update": "2024-06-01T15:30:00.000Z",
        "battery_level": 91,
        "signal_strength": "strong",
        "maintenance_status": "ok"
      },
      {
        "sensor_id": "PRESS_SECTOR_A_001",
        "type": "pressure",
        "status": "online",
        "location": "SECTOR_A_FLOOR_01",
        "value": 1013.2,
        "unit": "hPa",
        "last_update": "2024-06-01T15:30:00.000Z",
        "battery_level": 84,
        "signal_strength": "strong",
        "maintenance_status": "ok"
      },
      {
        "sensor_id": "TEMP_SECTOR_B_001",
        "type": "temperature",
        "status": "online",
        "location": "SECTOR_B_FLOOR_01",
        "value": 22.9,
        "unit": "celsius",
        "last_update": "2024-06-01T15:30:00.000Z",
        "battery_level": 77,
        "signal_strength": "strong",
        "maintenance_status": "ok"
      },
      {
        "sensor_id": "TEMP_SECTOR_B_002",
        "type": "temperature",
        "status": "online",
        "location": "SECTOR_B_FLOOR_01",
        "value": 23.4,
        "unit": "celsius",
        "last_update": "2024-06-01T15:30:00.000Z",
        "battery_level": 88,
        "signal_strength": "strong",
        "maintenance_status": "ok"
      },
      {
        "sensor_id": "HUMID_SECTOR_B_001",
        "type": "humidity",
        "status": "online",
        "location": "SECTOR_B_FLOOR_01",
        "value": 63.7,
        "unit": "percentage",
        "last_update": "2024-06-01T15:30:00.000Z",
        "battery_level": 90,
        "signal_strength": "strong",
        "maintenance_status": "ok"
      },
      {
        "sensor_id": "PRESS_SECTOR_B_001",
        "type": "pressure",
        "status": "online",
        "location": "SECTOR_B_FLOOR_01",
        "value": 1012.8,
        "unit": "hPa",
        "last_update": "2024-06-01T15:30:00.000Z",
        "battery_level": 82,
        "signal_strength": "strong",
        "maintenance_status": "ok"
      }
    ],
    "summary": {
      "total_sensors": 10,
      "online_sensors": 10,
      "offline_sensors": 0,
      "warning_sensors": 0,
      "last_sync": "2024-06-01T15:30:00.000Z",
      "factory_status": "operational",
      "maintenance_required": "none"
    }
  }
}
```

**Tamanho original**: 3.247 caracteres

## Análise de repetição

### **Padrões ALTAMENTE Repetitivos Identificados:**

| Padrão/Campo                                | Repetições | Caracteres por Repetição | Total de Caracteres |
| ------------------------------------------- | ---------- | ------------------------ | ------------------- |
| `"status": "online"`                        | 10 vezes   | 17 chars                 | 170 chars           |
| `"signal_strength": "strong"`               | 10 vezes   | 28 chars                 | 280 chars           |
| `"maintenance_status": "ok"`                | 10 vezes   | 25 chars                 | 250 chars           |
| `"last_update": "2024-06-01T15:30:00.000Z"` | 11 vezes   | 45 chars                 | 495 chars           |
| `"SECTOR_A_FLOOR_01"`                       | 6 vezes    | 18 chars                 | 108 chars           |
| `"SECTOR_B_FLOOR_01"`                       | 4 vezes    | 18 chars                 | 72 chars            |
| `"type": "temperature"`                     | 5 vezes    | 21 chars                 | 105 chars           |
| `"type": "humidity"`                        | 3 vezes    | 18 chars                 | 54 chars            |
| `"type": "pressure"`                        | 2 vezes    | 18 chars                 | 36 chars            |
| `"unit": "celsius"`                         | 5 vezes    | 16 chars                 | 80 chars            |
| `"unit": "percentage"`                      | 3 vezes    | 19 chars                 | 57 chars            |
| `"unit": "hPa"`                             | 2 vezes    | 12 chars                 | 24 chars            |

**Total de caracteres repetitivos**: 1.731 caracteres (**53% do JSON total!**)
