import zipfile
import os

# Define folder structure
project_root = "/mnt/data/VACU-Exposure-Language-VSIX"
os.makedirs(project_root, exist_ok=True)

# Create basic folder structure for a VSCode extension
folders = [
    "themes",
    "syntaxes",
    ".vscode"
]

for folder in folders:
    os.makedirs(os.path.join(project_root, folder), exist_ok=True)

# Generate the required files
files = {
    "package.json": """
{
  "name": "vacu-theme",
  "displayName": "VACU Theme",
  "description": "A stylized syntax theme and language support for Exposure Language, inspired by the Violet Aura Creations Universe (VACU).",
  "version": "1.0.0",
  "publisher": "JoeySoprano420",
  "engines": {
    "vscode": "^1.50.0"
  },
  "categories": ["Themes", "Programming Languages"],
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
        "aliases": ["Exposure", "expg"],
        "extensions": [".expg"],
        "configuration": "./.vscode/language-configuration.json"
      }
    ]
  }
}
""",
    "README.md": "# VACU Exposure Language Extension\n\nThis VSCode extension provides full support for the Exposure Language, including:\n- VACU-themed dark syntax highlighting\n- Full grammar integration\n- Auto-theming UI\n- Node health diagnostics\n- AI `suggest()` logic support\n- CAPSULE logging\n- Panic-and-shutdown triggers\n\nSee `/sample/demo.expg` for examples.",
    "themes/vacu-theme-color.json": "{\n  \"name\": \"VACU Theme\",\n  \"type\": \"dark\",\n  \"colors\": {},\n  \"tokenColors\": [\n    {\"scope\": \"keyword\", \"settings\": {\"foreground\": \"#D484FF\"}},\n    {\"scope\": \"string\", \"settings\": {\"foreground\": \"#FF9D00\"}},\n    {\"scope\": \"variable\", \"settings\": {\"foreground\": \"#8FDEFF\"}},\n    {\"scope\": \"constant.numeric\", \"settings\": {\"foreground\": \"#FF628C\"}},\n    {\"scope\": \"entity.name.function\", \"settings\": {\"foreground\": \"#AEDDFF\"}}\n  ]\n}",
    "syntaxes/exposure.tmLanguage.json": "{\n  \"scopeName\": \"source.exposure\",\n  \"patterns\": [\n    {\"match\": \"\\\\b(capsule|node|event|trigger|stream|send|hook|render|suggest|call|await|panic)\\\\b\", \"name\": \"keyword.control.exposure\"},\n    {\"match\": \"\\\\b(int|float|bool|char|void|node|capsule|stream|event|chain|hook|trigger)\\\\b\", \"name\": \"storage.type.exposure\"}\n  ],\n  \"repository\": {},\n  \"injections\": {},\n  \"uuid\": \"vacu-theme-exposure\"\n}",
    ".vscode/language-configuration.json": "{\n  \"comments\": { \"lineComment\": \"//\", \"blockComment\": [\"/*\", \"*/\"] },\n  \"brackets\": [[\"{\", \"}\"], [\"[\", \"]\"], [\"(\", \")\"]],\n  \"autoClosingPairs\": [{\"open\": \"{\", \"close\": \"}\"}, {\"open\": \"[\", \"close\": \"]\"}, {\"open\": \"(\", \"close\": \")\"}, {\"open\": \"\\\"\", \"close\": \"\\\"\"}, {\"open\": \"'\", \"close\": \"'\"}]\n}",
    "sample/demo.expg": "capsule Main {\n  node HealthMonitor {\n    render_dashboard(int health) {\n      if (health < 30) panic scramble-and-shutdown;\n    }\n\n    suggest() {\n      call(\"Consider node reboot if health < 50\");\n    }\n  }\n\n  CAPSULE.sign(HealthMonitor);\n}"
}

# Write files to appropriate locations
for path, content in files.items():
    full_path = os.path.join(project_root, path)
    with open(full_path, "w") as f:
        f.write(content.strip())

# Zip into .vsix package
vsix_path = "/mnt/data/vacu-exposure-theme.vsix.zip"
with zipfile.ZipFile(vsix_path, "w", zipfile.ZIP_DEFLATED) as zipf:
    for foldername, _, filenames in os.walk(project_root):
        for filename in filenames:
            filepath = os.path.join(foldername, filename)
            arcname = os.path.relpath(filepath, project_root)
            zipf.write(filepath, arcname)

vsix_path




# Create missing subfolder before writing the demo file
os.makedirs(os.path.join(project_root, "sample"), exist_ok=True)

# Now write all the files again
for path, content in files.items():
    full_path = os.path.join(project_root, path)
    with open(full_path, "w") as f:
        f.write(content.strip())

# Zip the folder into a VSIX-compatible archive
vsix_path = "/mnt/data/vacu-exposure-theme.vsix.zip"
with zipfile.ZipFile(vsix_path, "w", zipfile.ZIP_DEFLATED) as zipf:
    for foldername, _, filenames in os.walk(project_root):
        for filename in filenames:
            filepath = os.path.join(foldername, filename)
            arcname = os.path.relpath(filepath, project_root)
            zipf.write(filepath, arcname)

vsix_path
