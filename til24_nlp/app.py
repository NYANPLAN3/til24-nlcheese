"""Main app."""

from dotenv import load_dotenv

load_dotenv()

import logging

from fastapi import FastAPI, Request

from .NLPManager import NLPManager

__all__ = ["create_app"]

log = logging.getLogger(__name__)


def create_app():
    """App factory."""
    app = FastAPI()
    nlp = NLPManager()

    @app.get("/health")
    async def health():
        """Competition admin needs this."""
        return {"message": "health ok"}

    @app.post("/extract")
    async def extract(req: Request):
        """Performs QA extraction given a context string.

        returns a dictionary with fields:

        {
            "heading": str,
            "target": str,
            "tool": str,
        }
        """
        # NOTE: This is just in case the server is giving non-compliant requests for some reason.
        data = await req.json()

        preds = []
        for instance in data["instances"]:
            out_data = nlp.extract(instance["transcript"])
            preds.append(out_data)

        return {"predictions": preds}

    return app
