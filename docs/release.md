# Releases

`pyproject.toml` is the source of truth for the project version. The metadata workflow validates the software metadata.

| Policy | Value |
| --- | --- |
| Current version | `0.1.0` |
| Versioning scheme | SemVer |

## Release process

1. Update `project.version` in `pyproject.toml`.
2. Move completed entries from `Unreleased` in `CHANGELOG.md` into a section for the new version.
3. Run the metadata, test, documentation, and release checks configured for the project.
