# Outbreak API Reference

## Endpoints

### GET /api/v1/outbreak

Returns all outbreak records.

**Parameters:**
- `limit` (int): Max results (default: 100)
- `offset` (int): Pagination offset
- `filter` (string): Filter expression

### POST /api/v1/outbreak

Create a new outbreak record.

**Request Body:**
```json
{
  "name": "string",
  "type": "string",
  "metadata": {}
}
```

### GET /api/v1/outbreak/{id}

Get outbreak by ID.

### DELETE /api/v1/outbreak/{id}

Delete outbreak record.
