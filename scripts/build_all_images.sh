docker buildx build --platform linux/amd64,linux/arm64 ../modules/frontend -f ../modules/frontend/Dockerfile --tag rickeand/nd064-frontend:latest --push

docker buildx build --platform linux/amd64,linux/arm64 ../modules/persons -f ../modules/persons/Dockerfile --tag rickeand/nd064-persons-api:latest --push

docker buildx build --platform linux/amd64,linux/arm64 ../modules/connections -f ../modules/connections/Dockerfile --tag rickeand/nd064-connections-api:latest --push

docker buildx build --platform linux/amd64,linux/arm64 ../modules/grpc -f ../modules/grpc/Dockerfile --tag rickeand/nd064-grpc:latest --push

docker buildx build --platform linux/amd64,linux/arm64 ../modules/locations -f ../modules/locations/Dockerfile-api --tag rickeand/nd064-locations-api:latest --push

docker buildx build --platform linux/amd64,linux/arm64 ../modules/locations -f ../modules/locations/Dockerfile-kafka-consumer --tag rickeand/nd064-kafka-consumer:latest --push

docker buildx build --platform linux/amd64,linux/arm64 ../modules/persons -f ../modules/persons/Dockerfile --tag rickeand/nd064-persons-api:latest --push

docker buildx build --platform linux/amd64,linux/arm64 ../modules/persons -f ../modules/persons/Dockerfile --tag rickeand/nd064-persons-api:latest --push

docker buildx build --platform linux/amd64,linux/arm64 ../docker-kafka -f ../docker-kafka/Dockerfile --tag rickeand/kafka:latest --push

docker buildx build --platform linux/amd64,linux/arm64 ../docker-zookeeper -f ../docker-zookeeper/Dockerfile --tag rickeand/zookeeper:latest --push
