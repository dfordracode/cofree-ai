"""Materials Project API client abstractions."""


class MaterialsProjectClient:
    """Simple client stub for interacting with the Materials Project API."""

    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_material(self, material_id: str):
        """Retrieve material details by ID."""
        raise NotImplementedError()
