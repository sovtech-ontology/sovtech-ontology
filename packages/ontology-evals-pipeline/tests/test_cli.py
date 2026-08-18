from typer.testing import CliRunner

from ontology_evals_pipeline.cli import app

runner = CliRunner()


def test_help_lists_all_stages() -> None:
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    for command in ("extract", "evaluate", "store", "run"):
        assert command in result.output
