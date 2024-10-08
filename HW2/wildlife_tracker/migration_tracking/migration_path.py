from typing import Optional
from wildlife_tracker.habitat_management.habitat import Habitat

class MigrationPath:
    def __init__(self, path_id: int, start_location: Habitat, destination: Habitat, species: str, duration: Optional[int] = None) -> None:
        self.path_id: int = path_id
        self.start_location: Habitat = start_location
        self.destination: Habitat = destination
        self.species: str = species
        self.duration: Optional[int] = duration

    def get_migration_path_details(path_id) -> dict:
        pass

    def update_migration_path_details(path_id: int, **kwargs) -> None:
        pass