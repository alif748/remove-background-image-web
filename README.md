# Remove Background Image Web

Model from [MODNet](https://github.com/ZHKKKe/MODNet) with framework [FastAPI](https://fastapi.tiangolo.com/)

## Development
```
python -m uvicorn app.main:app --reload --port=5009
```

## Docker
Make sure you have docker desktop installed. Then
```
docker build -t user/myimage .
```

Or you can pull the image
```
docker pull alif748/rmbg
```
Run docker image with port number `5009`.

## Usage
Method `GET`
```
http://localhost:5009/rmbg
```
#### Request Query
| Key | Required | Description |
| :-: | :-: | :-: |
| url | Required | direct image link |

#### Example
```
http://localhost:5009/rmbg?url=https://pbs.twimg.com/media/FlY6-RkaUAAhVK3.jpg
```


## Support me on
[Buy Me a Coffee](https://buymeacoffee.com/alifm)

[Ko-fi](https://ko-fi.com/alifm)

[saweria.co](https://saweria.co/alifm)

[Trakteer](https://trakteer.id/alifm/tip)