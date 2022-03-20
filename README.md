```bash
conda create --prefix ./env python=3.7 -y
```

```bash
conda activate ./env
```
OR
```bash
source activate ./env
```
```


## docker commands

```

docker build -t circleci_haresh .
docker image ls
docker login
docker tag 0cdd7a19c265 hareshkm999/circleci_haresh:firsttry
docker run -p 80:80 circleci_haresh:firsttry
docker push hareshkm999/circleci_haresh:firsttry
```