# List all available commands
_default:
    @just --list

@install:
    uv sync

@clean:
    rm -rf .venv

# Run all formatters
@fmt:
    just --fmt --unstable
    uvx pyproject-fmt pyproject.toml

# Run sphinx autobuild
@docs-serve:
    uv run sphinx-autobuild docs docs/_build/html --port 8002

# Generate changelog
logchanges *ARGS:
    uvx git-cliff --output CHANGELOG.md {{ ARGS }} a2a1..HEAD

# Bump project version and update changelog
bumpver VERSION:
    #!/usr/bin/env bash
    set -euo pipefail
    uvx bump-my-version bump {{ VERSION }}
    just logchanges
    [ -z "$(git status --porcelain)" ] && { echo "No changes to commit."; git push && git push --tags; exit 0; }
    version="$(uv run bump-my-version show current_version)"
    git add -A
    git commit -m "Generate changelog for version ${version}"
    git tag -f "v${version}"
    git push && git push --tags

# Generate project tree files
tree:
    #!/usr/bin/env bash
    set -euo pipefail
    levels=(1 2 3)
    SED_CMD=$( [[ "$OSTYPE" == "darwin"* ]] && echo "sed -i ''" || echo "sed -i" )
    for level in "${levels[@]}"; do
      tree "{{{{ cookiecutter.project_name }}" -L $level --dirsfirst -o tree.txt --noreport -a -n -v -I '.env|requirements*|__pycache__|entries'
      $SED_CMD 's|{{{{ cookiecutter.project_name }}|demo|g' tree.txt
      $SED_CMD 's|demo/myjourney|myjourney|g' tree.txt
      mv tree.txt docs/_static/snippets/tree-$level.txt
    done
    rm -f tree.txt\'\'