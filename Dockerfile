FROM gcr.io/grid-backend-266721/grid-images__gpu-cuda-pytorch:1.10-pl-1.5.9-metrics-0.7.0-20220128
WORKDIR '/gridai/project'
COPY . /gridai/project/
RUN apt-get update && \
    apt-get install ffmpeg libsm6 libxext6 -y && \
    pip install --no-cache -e . && \
    pip install -r requirements.txt
