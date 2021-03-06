from typing import List, Optional
from pydantic import BaseSettings

from .version import __version__
from .types import MetadataTensor


class Settings(BaseSettings):
    debug: bool = True

    # Server metadata
    server_name: str = "mlserver"
    server_version: str = __version__
    extensions: List[str] = []

    # Server settings
    http_port: int = 8080
    grpc_port: int = 8081
    grpc_workers: int = 10


class ModelParameters(BaseSettings):
    """
    Parameters that apply only to a particular instance of a model.
    This can include things like model weights.
    The main difference with respect to ModelSettings is that parameters can
    change on each instance (e.g. each version) of the model.
    """

    uri: Optional[str] = None


class ModelSettings(BaseSettings):
    name: str
    version: str

    # Model metadata
    platform: str = ""
    versions: Optional[List[str]] = []
    inputs: Optional[List[MetadataTensor]] = []
    outputs: Optional[List[MetadataTensor]] = []

    # Custom model class implementation
    implementation: str = "mlserver.model.MLModel"

    # Model parameters are meant to be set directly by the MLServer runtime.
    # However, it's also possible to override them manually.
    parameters: Optional[ModelParameters] = None
