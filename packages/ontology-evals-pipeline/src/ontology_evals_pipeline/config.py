from pathlib import Path

from pydantic import DirectoryPath, FilePath
from pydantic_settings import BaseSettings, SettingsConfigDict

PACKAGE_DIRECTORY_PATH = Path(__file__).parent.absolute()
CONFIG_DIRECTORY_PATH = PACKAGE_DIRECTORY_PATH.parent.parent.absolute()
DATA_DIRECTORY_PATH = PACKAGE_DIRECTORY_PATH / "data"
INPUT_DATA_DIRECTORY_PATH = DATA_DIRECTORY_PATH / "input"
OUTPUT_DATA_DIRECTORY_PATH = DATA_DIRECTORY_PATH / "output"


class Config(BaseSettings):
    """Pydantic BaseSettings to store config variables. Read once at the CLI
    boundary; no other module interacts with it."""

    prospectuses_dir: DirectoryPath = INPUT_DATA_DIRECTORY_PATH / "prospectuses"
    ground_truth_dir: Path = INPUT_DATA_DIRECTORY_PATH / "ground_truth"
    jsonld_context: FilePath = DATA_DIRECTORY_PATH / "context.json"
    output_dir: Path = OUTPUT_DATA_DIRECTORY_PATH
    llm_model: str = "anthropic:claude-sonnet-4-5"
    max_prospectus_chars: int = 150_000
    use_marker: bool = False
    lsh_threshold: float = 0.8
    lsh_num_perm: int = 128
    rdf_format: str = "turtle"

    model_config = SettingsConfigDict(
        env_file=(
            CONFIG_DIRECTORY_PATH / ".env.local",
            CONFIG_DIRECTORY_PATH / ".env.secret",
        ),
        extra="ignore",
        env_file_encoding="utf-8",
        validate_default=False,
    )
