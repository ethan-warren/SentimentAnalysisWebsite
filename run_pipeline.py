#Note: THE MAJORITY OF THIS FILE IS A TEMPLATE PROVIDED BY DOCUMENTATION FOR THE PYTHON LIBRARY SPACY

import os
from pathlib import Path
from typing import Optional

import typer
from wasabi import msg

from spacy_llm.util import assemble
import spacy_llm
import logging

spacy_llm.logger.addHandler(logging.StreamHandler())
spacy_llm.logger.setLevel(logging.NOTSET)

Arg = typer.Argument
Opt = typer.Option

def run_pipeline(
    # fmt: off
    text: str = Arg("", help="Text to perform text categorization on."),
    config_path: Path = Arg(..., help="Path to the configuration file to use."),
    examples_path: Optional[Path] = Arg(None, help="Path to the examples file to use (few-shot only)."),
    verbose: bool = Opt(False, "--verbose", "-v", help="Show extra information."),
    # fmt: on
):
    if not os.environ.get("OPENAI_API_KEY", None):
        msg.fail(
            "OPENAI_API_KEY env variable was not found. "
            "Set it by running 'export OPENAI_API_KEY=...' and try again.",
            exits=1,
        )

    msg.text(f"Loading config from {config_path}", show=verbose)
    nlp = assemble(
        config_path,
        overrides={}
        if examples_path is None
        else {"paths.examples": str(examples_path)},
    )
    doc = nlp(text)

    msg.text(f"Text: {doc.text}")
    msg.text(f"Categories: {doc.cats}")


if __name__ == "__main__":
    typer.run(run_pipeline)