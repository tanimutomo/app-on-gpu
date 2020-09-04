# app-on-gpu
app-on-gpu enables you to create a new CUDA-based web application running on your GPU server easily.

This repo is sample application predicting imagenet class which uses 
- pytorch + flask (nvidia docker)
- nginx (docker)
- https-portal (docker) <- supports https

You can use other deep learning library than pytorch such as tensorflow, keras.


## Start sample webapp

### Setup
```
$ copy .env.default .env

# set variables in .env

$ docker network create app-on-gpu
```

### Start service (stg)
```
$ bash ./scripts/run.sh
```

### Start service (prod)

Create ssl with Let's Encrypt.

```
$ bash ./scripts/run.sh prod
```

### Predict

Predict imagenet class for posted image.

`POST /image`

Request

- Authorization
  - Basic Auth

- Headers
  - Content-Type: application/json

- Body (json)
```
{
  "image": "${base64_encoded_image}"
}
```

Response (json)
```
{
  "id": ${class_id},
  "name": "${class_name}",
}
```


## Customize application

You can use your flask application by replacing `app/api/` to it.

You don't have to customize other directories.
You can use same settings as this repo.
