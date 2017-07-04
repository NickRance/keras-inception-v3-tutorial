#!/usr/bin/env bash

PRIJECT_NAME = messing-around-1473104491351

docker build -t predict-service .
docker tag predict-service gcr.io/$PROJECT_NAME/predict-service
gcloud docker -- push gcr.io/$PROJECT_NAME/predict-service

#sudo gcloud docker -- pull gcr.io/messing-around-1473104491351/predict_service:latest
#sudo docker run -td -p 80:80 gcr.io/messing-around-1473104491351/predict-service
# gsutil mb gs://nicktestsphotos

#make some notes for the tutorial gcloud docker -- pull instead of just pull
#test_cat.jpg instead of cat.jpg

