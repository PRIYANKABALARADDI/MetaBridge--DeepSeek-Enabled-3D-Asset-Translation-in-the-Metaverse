# MetaBridge API Reference  

## Overview  
MetaBridge provides APIs for uploading, analyzing, and converting 3D assets.

## Endpoints  

### `POST /upload`
- **Description**: Upload a 3D asset.
- **Request Format**: Multipart form data with file upload.
- **Response**:  
```json
{
  "status": "success",
  "message": "File uploaded successfully",
  "asset_id": "123456"
}
