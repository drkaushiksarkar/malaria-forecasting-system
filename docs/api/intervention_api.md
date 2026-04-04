# Intervention API Reference

## Endpoints

### GET /api/v1/intervention

Returns all intervention records.

**Parameters:**
- `limit` (int): Max results (default: 100)
- `offset` (int): Pagination offset
- `filter` (string): Filter expression

### POST /api/v1/intervention

Create a new intervention record.

**Request Body:**
```json
{
  "name": "string",
  "type": "string",
  "metadata": {}
}
```

### GET /api/v1/intervention/{id}

Get intervention by ID.

### DELETE /api/v1/intervention/{id}

Delete intervention record.
