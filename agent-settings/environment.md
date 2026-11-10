# Environment (all agents)

## One shared venv

All Python work in any stream runs through the single shared venv:

```
tools/venv/              (gitignored)
tools/requirements.txt   (tracked)
```

### Invoking it

- Windows: `tools\venv\Scripts\python.exe <script.py>`
- macOS/Linux: `tools/venv/bin/python <script.py>`

### Rules

1. Never create a per-stream `venv/` or `.venv/`. Use `tools/venv`.
2. If a script needs a package that is missing, `pip install` it into `tools/venv`, **then** add it (with a
   version floor) to `tools/requirements.txt` so the environment stays reproducible.
3. If `tools/venv` does not exist on this machine, recreate it:

   ```bash
   python -m venv tools/venv
   # Windows:
   tools/venv/Scripts/pip install -r tools/requirements.txt
   # macOS/Linux:
   tools/venv/bin/pip install -r tools/requirements.txt
   ```

4. Never commit `tools/venv` (it is gitignored). Only `tools/requirements.txt` travels with the repo.