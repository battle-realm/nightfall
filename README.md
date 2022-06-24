# nightfall
Service bypass Cloudflare. Sử dụng cloudscraper từ pypi.

Chạy mặc định ở port 5000:
`docker-compose up`

Paths:
```javascript
"/": HTTP POST
Request example:
    body:
        "[
            {
                "id": "11",
                "method":"GET",
                "url":"http://google.com"
            },
            {
                "id": "12",
                "method": "POST",
                "url": "https://google.com",
                "post_data" : "zz"
            }
         ]"

Response example:
    body:
       "[
          {
            "id": "10",
            "status_code": 200,
            "response": "<!DOCTYPE html>..."
          },
          {
            "id": "11",
            "status_code": 405,
            "respones": "405 (Method Not Allowed)"
          }
        ]
       " 
```