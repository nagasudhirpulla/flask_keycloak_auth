from dataclasses import dataclass, field
import json


@dataclass
class AppConfig:
    oauthAppClientId: str = field(default="")
    oauthAppClientSecret: str = field(default="")
    oauthProviderDiscoveryUrl: str = field(default="")


def loadAppConfig(fName="config/config.json") -> AppConfig:
    global jsonConfig
    with open(fName) as f:
        data = json.load(f)
        jsonConfig = AppConfig(**data)
        return jsonConfig


def getAppConfig() -> AppConfig:
    global jsonConfig
    return jsonConfig
