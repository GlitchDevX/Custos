report_analysis_schema = {
    "type": "object",
    "properties": {
        "tags": {
        "type": "array",
        "items": {
            "type": "string"
        }
        },
        "falseReport": {
        "type": "boolean"
        }
    },
    "required": [
        "tags",
        "falseReport"
    ]
}