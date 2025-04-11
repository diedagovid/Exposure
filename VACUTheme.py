# Define a VACU-style Visual Studio Code theme (dark, immersive, high-contrast with signature VACU tones)
vacu_theme = {
    "name": "VACU Theme",
    "type": "dark",
    "colors": {
        "editor.background": "#0e0e15",
        "editor.foreground": "#f8f8f2",
        "editorCursor.foreground": "#ffb86c",
        "editor.lineHighlightBackground": "#1a1a2e",
        "editorLineNumber.foreground": "#6272a4",
        "editor.selectionBackground": "#44475a",
        "editor.inactiveSelectionBackground": "#282a36",
        "editorIndentGuide.background": "#3b3a50",
        "editorIndentGuide.activeBackground": "#9a86fd",
    },
    "tokenColors": [
        {
            "scope": ["keyword", "storage.type"],
            "settings": {"foreground": "#ff79c6", "fontStyle": "bold"}
        },
        {
            "scope": ["entity.name.function", "support.function"],
            "settings": {"foreground": "#50fa7b"}
        },
        {
            "scope": ["variable", "identifier"],
            "settings": {"foreground": "#f1fa8c"}
        },
        {
            "scope": ["string", "constant.character"],
            "settings": {"foreground": "#f0a7b3"}
        },
        {
            "scope": ["constant.numeric"],
            "settings": {"foreground": "#bd93f9"}
        },
        {
            "scope": ["comment", "punctuation.definition.comment"],
            "settings": {"foreground": "#6272a4", "fontStyle": "italic"}
        },
        {
            "scope": ["entity.name.type", "support.type"],
            "settings": {"foreground": "#8be9fd", "fontStyle": "bold"}
        },
        {
            "scope": ["keyword.control", "keyword.operator"],
            "settings": {"foreground": "#ff5555"}
        },
        {
            "scope": ["support.class", "entity.other.inherited-class"],
            "settings": {"foreground": "#ffb86c"}
        },
        {
            "scope": ["meta.annotation", "variable.annotation"],
            "settings": {"foreground": "#ffb86c", "fontStyle": "italic"}
        }
    ]
}

# Save the theme as a .json file
from pathlib import Path
theme_path = Path("/mnt/data/vacu-theme-color.json")
theme_path.write_text(json.dumps(vacu_theme, indent=2))

theme_path.name
