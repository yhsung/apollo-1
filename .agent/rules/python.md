# Python Environment

Always use the virtual environment at `./venv` for all Python operations:

- **Create venv**: `python -m venv ./venv`
- **Activate**: `source ./venv/bin/activate`
- **Install package**: `pip install -e .`
- **Run commands**: Always prefix with `source ./venv/bin/activate &&`

Never use system Python or create venvs in other locations.
