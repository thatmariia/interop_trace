# Developer guide

## Architecture

The project metadata describes its public functions, interfaces, quality tools,
and collaboration policy. Keep implementation code and tests in clearly owned
locations, and keep generated public files synchronized with that metadata.

## Development setup

```bash
poetry install --all-extras
```

## Local checks

| Check | Command |
| --- | --- |
| Format | `poetry run ruff format --check .` |
| Lint | `poetry run ruff check .` |
| Type check | `poetry run mypy src` |
| Tests | `poetry run python -m pytest` |

See `CONTRIBUTING.md` in the repository root for the complete contribution policy.

## Interface contracts

Keep public interface descriptions aligned with implementation files, documentation, and stability status.

- Command-line tool (Stable)
- Library (Stable)

## Project architecture

The generated Python package uses a `src` layout.
Runtime dependencies point inward: public entry points delegate reusable
behavior to the service layer.

```text
public entry points
    -> adapters/
    -> services/
```

Services must not import interface adapters.

Generated component paths:
- `src/interop_trace/services/`
- `src/interop_trace/adapters/`
- `tests/`

### Command-line tool

See the generated component paths above.

## Generated automation

- `docs.yml`
- `metadata.yml`
- `quality.yml`
- `tests.yml`
