from typing import NamedTuple


class MongoConfig(NamedTuple):
    host: str
    port: str
    
    def get_uri(self) -> str:
        return "mongodb://%(host)s:%(port)s" % {
            "host": self.host,
            "port": self.port
        }
