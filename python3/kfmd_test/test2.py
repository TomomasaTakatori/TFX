from kfmd import metadata, openapi_client
from kfmd.openapi_client import Configuration, ApiClient, MetadataServiceApi

config = Configuration()
config.host = "http://130.211.212.251:30081"
client = MetadataServiceApi(ApiClient(config))

print(client.list_artifact_types())
