# Using the Marp for VS Code extension

This short README explains how to preview and export the `slides.md` deck in this repository using the Marp extension for Visual Studio Code.

## Preview in VS Code

1. Install the "Marp for VS Code" extension (search Extensions marketplace in VS Code).
2. Open this repository in VS Code and open `slides.md`.
3. Toggle the Marp preview by clicking the "Open Preview" button in the editor or using the command palette ("View: Open Preview to the Side").
4. Use the preview toolbar to change themes or presenter options.

## Exporting slides

Option A — From VS Code (recommended for quick exports):
- Use the command palette (Ctrl+Shift+P) -> type `Marp: Export` -> select desired format (HTML, PDF, PPTX).

Option B — Using Marp CLI (for automation):
1. Install Node.js (if not installed).
2. Install Marp CLI globally or in the project:

```powershell
npm install -g @marp-team/marp-cli
```

3. Export to HTML:

```powershell
marp "slides.md" -o "slides.html"
```

4. Export to PDF:

```powershell
marp "slides.md" -o "slides.pdf"
```

Notes:
- When using Marp CLI on Windows PowerShell, quoted paths are recommended.
- The Marp extension in VS Code provides a visual workflow and is usually sufficient for one-off exports.

## Troubleshooting

- If slides don't render, ensure front-matter contains `marp: true`.
- If images or assets are missing, use relative paths from the `slides.md` location.

## Next steps
- If you want, I can:
  - Generate a PDF export now.
  - Expand the deck with one slide per file in `Knowledge/`.
  - Add speaker notes extracted from the `.md` files.

