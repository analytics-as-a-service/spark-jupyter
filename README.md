# spark-jupyter
Image source for singleuser image in `bitnami/spark` and `jupyterhub/jupyter` helm charts having spark and jupyter notebook configured to use spark for computation on jupyter notebook. This repository uses the image sources from [bitnami/spark](https://github.com/bitnami/containers/tree/main/bitnami/spark) and [bitnami/jupyter-base-notebook](https://github.com/bitnami/containers/tree/main/bitnami/jupyter-base-notebook)
- Image after build is made available [here](https://hub.docker.com/r/akhil15935/spark-jupyter)
- To build the image make all the script files as executables and then run the following command
```
docker build . -t <image-name>:<image-tag>
```mkdir /data-nn /data-dn
