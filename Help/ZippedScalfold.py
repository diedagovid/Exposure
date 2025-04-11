import shutil

# Create a zip file for the VACU Theme scaffold including demo .expg file
project_folder = '/mnt/data/vacu-theme-scaffold'
output_zip = '/mnt/data/vacu-theme-scaffold.zip'

# Prepare project structure in the desired folder
project_structure = {
    "vacu-theme-scaffold/themes": {
        "vacu-theme-color.json": '''
{
  "type": "theme",
  "colors": {
    "editor.background": "#1e1e1e",
    "editor.foreground": "#d4d4d4",
    "editorCursor.foreground": "#d4d4d4",
    "editor.lineHighlightBackground": "#2a2d2e",
    "editor.selectionBackground": "#264f78",
    "editor.selectionHighlightBackground": "#a8c6f2",
    "editorIndentGuide.background": "#3b3b3b",
    "editorWhitespace.foreground": "#cccccc"
  },
  "tokenColors": [
    {
      "scope": ["keyword", "keyword.control"],
      "settings": {
        "foreground": "#d79eeb"
      }
    },
    {
      "scope": "variable",
      "settings": {
        "foreground": "#ffb2a7"
      }
    }
  ]
}
        '''
    },
    "vacu-theme-scaffold/syntaxes": {
        "exposure.tmLanguage.json": '''
{
  "fileTypes": ["expg"],
  "name": "Exposure Language",
  "patterns": [
    {
      "match": "\\b(capsule|node|stream|function|return|if|else|loop|call|await|panic)\\b",
      "name": "keyword.control.exposure"
    },
    {
      "match": "\\b(int|float|bool|char|string|node|capsule|stream|event)\\b",
      "name": "storage.type.exposure"
    }
  ],
  "scopeName": "source.exposure"
}
        '''
    },
    "vacu-theme-scaffold/language-configuration.json": '''
{
  "comments": {
    "lineComment": "//",
    "blockComment": ["/*", "*/"]
  },
  "brackets": [
    ["{", "}"],
    ["[", "]"],
    ["(", ")"]
  ],
  "autoClosingPairs": [
    {"open": "{", "close": "}"},
    {"open": "[", "close": "]"},
    {"open": "(", "close": ")"}
  ],
  "surroundingPairs": [
    {"open": "{", "close": "}"},
    {"open": "[", "close": "]"},
    {"open": "(", "close": ")"}
  ]
}
    ''',
    "vacu-theme-scaffold/extension": {
        "exposure.expg": '''
capsule SystemDiagnostics {
  node Monitor {
    int temperature = 70;

    suggest() {
      if (temperature > 85) {
        call("Activate coolant system");
      }
    }

    render_status() {
      GUI.monitor("System Status") -> call("Health check: OK");
    }
  }

  stream Telemetry(int id) {
    call("Transmitting telemetry...");
  }

  CAPSULE.sign(Monitor, immutable=true)
}
        '''
    },
    "vacu-theme-scaffold/package.json": '''
{
  "name": "vacu-theme-exposure",
  "displayName": "VACU Theme & Exposure Language",
  "description": "A Visual Studio Code extension for the VACU theme and Exposure language syntax.",
  "version": "1.0.0",
  "publisher": "JoeySoprano420",
  "engines": {
    "vscode": "^1.50.0"
  },
  "contributes": {
    "themes": [
      {
        "label": "VACU Theme",
        "uiTheme": "vs-dark",
        "path": "./themes/vacu-theme-color.json"
      }
    ],
    "grammars": [
      {
        "language": "exposure",
        "scopeName": "source.exposure",
        "path": "./syntaxes/exposure.tmLanguage.json"
      }
    ],
    "languages": [
      {
        "id": "exposure",
        "aliases": ["Exposure"],
        "extensions": [".expg"],
        "configuration": "./language-configuration.json"
      }
    ]
  }
}
        '''
    },
    "vacu-theme-scaffold/README.md": '''
# VACU Theme & Exposure Language

This extension provides a custom **VACU Theme** and syntax highlighting for the **Exposure Language** in Visual Studio Code.

## Features

- **VACU Theme**: A dark theme designed for code readability and style.
- **Exposure Language**: Syntax highlighting for the Exposure language, used for high-level scripting and diagnostics.

## Installation

1. Install the [VACU Theme & Exposure Language](https://marketplace.visualstudio.com/items?itemName=JoeySoprano420.vacu-theme-exposure) from the Visual Studio Marketplace.
2. Open any `.expg` file and experience the syntax highlighting and theme.

## License

MIT License
    '''
    },
    "vacu-theme-scaffold/.vscodeignore": '''
**/*.md
**/*.gitignore
.vscode
    '''
}

# Create the folder structure and files
for folder, files in project_structure.items():
    folder_path = f'{project_folder}/{folder}'
    shutil.os.makedirs(folder_path, exist_ok=True)
    for file_name, content in files.items():
        with open(f'{folder_path}/{file_name}', 'w') as file:
            file.write(content)

# Zip the folder
shutil.make_archive(output_zip.replace('.zip', ''), 'zip', project_folder)

output_zip  # Return the zip file path
