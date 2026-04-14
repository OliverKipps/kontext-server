import json
import os
from pathlib import Path
from typing import Optional

DATA_DIR = Path(__file__).parent.parent / "data" / "contexts"


def _ensure_data_dir() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)


def _get_context_path(user_id: str) -> Path:
    safe_user_id = user_id.replace("/", "_").replace("\\", "_")
    return DATA_DIR / f"{safe_user_id}.json"


def load_context(user_id: str) -> dict:
    _ensure_data_dir()
    path = _get_context_path(user_id)
    if not path.exists():
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}


def save_context(user_id: str, context: dict) -> bool:
    _ensure_data_dir()
    path = _get_context_path(user_id)
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(context, f, indent=2, ensure_ascii=False)
        return True
    except IOError:
        return False


def list_contexts() -> list[str]:
    _ensure_data_dir()
    contexts = []
    for path in DATA_DIR.glob("*.json"):
        contexts.append(path.stem)
    return sorted(contexts)


def delete_context(user_id: str) -> bool:
    _ensure_data_dir()
    path = _get_context_path(user_id)
    if path.exists():
        path.unlink()
        return True
    return False
