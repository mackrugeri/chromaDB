from pathlib import Path
from common import fresh_collection
import json

_, source = fresh_collection()
_, destination = fresh_collection(seed=False)

export_path = Path("exports") / "records.json"
export_path.parent.mkdir(exist_ok=True)


