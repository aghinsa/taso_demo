## TASO
* [Repo](https://github.com/jiazhihao/TASO)
* [Paper](https://dl.acm.org/doi/10.1145/3341301.3359630)

## Building and running container
``` console
 cd docker
 git clone --recursive https://github.com/jiazhihao/TASO.git
 docker build -t taso .
 ./run_docker.sh taso
```

## Viewing graph
* use [netron](https://github.com/lutzroeder/netron)
```console
pip install netron
python 0/visualize_onnx model.onnx
```