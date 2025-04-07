from typing import Dict, List, TypedDict


report_analysis_schema = {
    "type": "object",
    "properties": {
        "tags": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
    },
    "required": [
        "tags",
    ]
}
class ReportAnalysis(TypedDict):
    tags: List[str]