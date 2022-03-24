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

docker build -t azur_github_action555:firsttry .
docker image ls
docker login
docker tag 356feacc6bbf hareshkm999/azur_github_action555:firsttry
docker run -p 5000:5000 azur_github_action555:firsttry
docker push hareshkm999/azur_github_action555:firsttry
```