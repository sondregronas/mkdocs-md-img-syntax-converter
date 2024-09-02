# md-img-syntax-converter

A super simple markdown image syntax converter.

> Note: This plugin converts EVERYTHING inside the markdown, including inside of codefences.

## Example conversions

`![Alt Text|64](img.png)` -> `![Alt Text](img.png){width="64"}`

`![Alt Text|64x128](img.png)` -> `![Alt Text](img.png){width="64"; height="128"}`

> Note: mkdocs aspect-ratio CSS properties will override the height by default.

## Install

Add to mkdocs.yml:

```yaml
markdown_extensions:
  - attr_list

plugins:
    - search
    - md-img-syntax-converter
```