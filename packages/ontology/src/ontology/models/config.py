from pathlib import Path

from pydantic import FilePath
from pydantic_settings import BaseSettings, SettingsConfigDict

CONFIG_DIRECTORY_PATH = Path(__file__).parent.parent.parent.absolute()
DATA_DIRECTORY_PATH = Path(__file__).parent.parent.absolute() / "data"
INPUT_DATA_DIRECTORY_PATH = DATA_DIRECTORY_PATH / "input"


class Config(BaseSettings):
    """Pydantic BaseSettings to store config variables."""

    sovtech_jsonld_context: FilePath = INPUT_DATA_DIRECTORY_PATH / "context.json"

    model_config = SettingsConfigDict(
        env_file=(
            CONFIG_DIRECTORY_PATH / ".env.local",
            CONFIG_DIRECTORY_PATH / ".env.secret",
        ),
        extra="ignore",
        env_file_encoding="utf-8",
        validate_default=False,
    )
