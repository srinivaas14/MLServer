from .types import InferenceRequest, InferenceResponse, MetadataModelResponse
from .settings import ModelSettings


class MLModel:
    """
    Abstract class which serves as the main interface to interact with ML
    models.
    """

    def __init__(self, settings: ModelSettings):
        self._settings = settings
        self.ready = False

    @property
    def name(self) -> str:
        return self._settings.name

    @property
    def version(self) -> str:
        return self._settings.version

    def metadata(self) -> MetadataModelResponse:
        return MetadataModelResponse(
            name=self.name,
            platform=self._settings.platform,
            versions=self._settings.versions,
            inputs=self._settings.inputs,
            outputs=self._settings.outputs,
        )

    def load(self) -> bool:
        self.ready = True
        return self.ready

    def predict(self, payload: InferenceRequest) -> InferenceResponse:
        raise NotImplementedError("predict() method not implemented")
