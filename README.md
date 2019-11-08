# Debezium KSQL Demo


```shell
# Start the Kafka, Kafka Connect, KSQL server and CLI etc.
export DEBEZIUM_VERSION=0.8
docker-compose up

# Start Debezium Postgresql connector
curl -i -X POST -H "Accept:application/json" -H  "Content-Type:application/json" http://localhost:8083/connectors/ -d @register-postgres.json

# Launch KSQL CLI
docker-compose exec ksql-cli ksql http://ksql-server:8088

# Run KSQL commands

# Shut down the cluster
docker-compose down
```
