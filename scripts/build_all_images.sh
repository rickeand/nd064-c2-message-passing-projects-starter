docker buildx build --platform linux/amd64,linux/arm64 ../modules/persons -f ../modules/persons/Dockerfile --tag rickeand/nd064-persons-api:latest
docker push rickeand/nd064-persons-api:latest

docker buildx build --platform linux/amd64,linux/arm64 ../modules/grpc -f ../modules/grpc/Dockerfile --tag rickeand/nd064-grpc:latest
docker push rickeand/nd064-grpc:latest

docker buildx build --platform linux/amd64,linux/arm64 ../modules/locations -f ../modules/locations/Dockerfile-api --tag rickeand/nd064-locations-api:latest
docker push rickeand/nd064-locations-api:latest

docker buildx build --platform linux/amd64,linux/arm64 ../modules/locations -f ../modules/locations/Dockerfile-kafka-consumer --tag rickeand/nd064-kafka-consumer:latest
docker push rickeand/nd064-kafka-consumer:latest

docker buildx build --platform linux/amd64,linux/arm64 ../modules/persons -f ../modules/persons/Dockerfile --tag rickeand/nd064-persons-api:latest
docker push rickeand/nd064-persons-api:latest

docker buildx build --platform linux/amd64,linux/arm64 ../modules/persons -f ../modules/persons/Dockerfile --tag rickeand/nd064-persons-api:latest
docker push rickeand/nd064-persons-api:latest

docker buildx build --platform linux/amd64,linux/arm64 ../docker-kafka -f ../docker-kafka/Dockerfile --tag rickeand/kafka:latest
docker push rickeand/kafka:latest

docker buildx build --platform linux/amd64,linux/arm64 ../docker-zookeeper -f ../docker-zookeeper/Dockerfile --tag rickeand/zookeeper:latest
docker push rickeand/zookeeper:latest
