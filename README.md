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

docker build -t azur_github_action .
docker image ls
docker login
docker tag 5d10b12679a4 hareshkm999/azur_github_action:firsttry
docker run -p 80:80 azur_github_action:firsttry
docker push hareshkm999/azur_github_action:firsttry
```