# port forwardを使ってserviceを8080 portにつないだ時

from kfmd import metadata, openapi_client
from kfmd.openapi_client import Configuration, ApiClient, MetadataServiceApi

config = Configuration()
config.host = "http://localhost:8080"
client = MetadataServiceApi(ApiClient(config))

print(client.list_artifact_types())
