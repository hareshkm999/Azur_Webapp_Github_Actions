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

docker build -t azur_github_action999:firsttry .
docker image ls
docker login
docker tag 0a6d5d64d86f hareshkm999/azur_github_action999:firsttry
docker run -p 5200:5200 azur_github_action999:firsttry
docker push hareshkm999/azur_github_action999:firsttry
```