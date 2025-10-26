# Using Marp VS Code extension

This short README explains how to use, key commands and ways to export slides using the Marp extension for Visual Studio Code.

## Helpful links

* [marpit.marp.app](https://marpit.marp.app/) 

## Directives

[**Directives**](https://marpit.marp.app/directives) allow you to format your slides in an array of ways.  The below list are a few directives and options to use

### theme

```markdown
theme: default 
theme: gaia
theme: uncover
```

### style
A directive that allows you to embed CSS directly within the marp file
```markdown
        ---
        theme: base-theme
        style: |
          section {
            background-color: #ccc;
          }
        ---
```

### Local Directives

```markdown
<!-- backgroundColor: aqua -->
```

## Marp Configuration

### Emojis

Out of the box, MARP supports Emoji shortcuts.  For example
* 😰 :cold_sweat: 
* 🚀 :rocket:

An expansive list can be found [here](https://gist.github.com/rxaviers/7360908) 

### Comments

To add comments to slides add the below line at the top of your file 

```javascript 
const { comments } = marpit.render(`
)
```
>The trailing **)** Should be placed at the end of the file, or the last slide where you have comments

## Preview in VS Code

>**Markdown Preview Enhanced** plugin does not work to view marp formatting, this will need disabled or when previewing select default viewer

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

