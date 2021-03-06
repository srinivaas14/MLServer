from fastapi.responses import Response

from ..types import (
    MetadataModelResponse,
    MetadataServerResponse,
    InferenceRequest,
    InferenceResponse,
)
from ..handlers import DataPlane

from .utils import to_status_code


class Endpoints:
    """
    Implementation of REST endpoints.
    These take care of the REST/HTTP-specific things and then delegate the
    business logic to the internal handlers.
    """

    def __init__(self, data_plane: DataPlane):
        self._data_plane = data_plane

    def live(self) -> Response:
        is_live = self._data_plane.live()
        return Response(status_code=to_status_code(is_live))

    def ready(self) -> Response:
        is_ready = self._data_plane.ready()
        return Response(status_code=to_status_code(is_ready))

    def model_ready(self, model_name: str, model_version: str = None) -> Response:
        is_ready = self._data_plane.model_ready(model_name, model_version)
        return Response(status_code=to_status_code(is_ready))

    def metadata(self) -> MetadataServerResponse:
        return self._data_plane.metadata()

    def model_metadata(
        self, model_name: str, model_version: str = None
    ) -> MetadataModelResponse:
        return self._data_plane.model_metadata(model_name, model_version)

    def infer(
        self, payload: InferenceRequest, model_name: str, model_version: str = None,
    ) -> InferenceResponse:
        return self._data_plane.infer(payload, model_name, model_version)
