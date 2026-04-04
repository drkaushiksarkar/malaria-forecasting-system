# Vector API Reference

## Endpoints

### GET /api/v1/vector

Returns all vector records.

**Parameters:**
- `limit` (int): Max results (default: 100)
- `offset` (int): Pagination offset
- `filter` (string): Filter expression

### POST /api/v1/vector

Create a new vector record.

**Request Body:**
```json
{
  "name": "string",
  "type": "string",
  "metadata": {}
}
```

### GET /api/v1/vector/{id}

Get vector by ID.

### DELETE /api/v1/vector/{id}

Delete vector record.
