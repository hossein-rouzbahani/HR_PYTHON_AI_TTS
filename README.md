# Learning TTS (Text to Speech) - EDGE

- https://pypi.org/project/edge-tts
    - https://github.com/rany2/edge-tts

- https://pypi.org/project/rich
    - https://github.com/Textualize/rich
    - https://rich.readthedocs.io/en/latest

---

### References

- https://github.com/rany2/edge-tts/tree/master/examples
- https://huggingface.co/spaces/innoai/Edge-TTS-Text-to-Speech
- https://huggingface.co/spaces/innoai/Edge-TTS-Text-to-Speech/blob/main/app.py

---

### Setup Environment

##### In Windows PowerShell:

```shell
python -m pip install -U pip
```

```shell
pip install -U uv
```

```shell
uv --version
```

```shell
python --version
```

```shell
uv python install 3.9 3.10 3.11 3.12 3.13
```

```shell
uv python upgrade 3.9 3.10 3.11 3.12 3.13
```

```shell
uv python list
```

```shell
uv python list --only-installed
```

##### In VSCode Terminal:

```shell
uv init
```

- Added Folder:
    - .git
- Added Files:
    - uv.lock
    - README.md
    - .gitignore
    - pyproject.toml
    - .python-version

```shell
uv init --python 3.12
```

- Update files content and change the python version to 3.12
    - .python-version
        - 3.12
    - pyproject.toml
        - requires-python = ">=3.12"

```shell
uv venv
```

```shell
.\.venv\Scripts\activate
```

```shell
uv add rich
```

```shell
uv sync --upgrade-package rich
```

```shell
uv add gradio
```

```shell
uv sync --upgrade-package gradio
```

```shell
uv add edge-tts
```

```shell
uv sync --upgrade-package edge-tts
```

```shell
uv add python-dotenv
```

```shell
uv sync --upgrade-package python-dotenv
```

```shell
uv pip list
```

- Edge TTS CLI (Command Line Interface): Display All Voices:

```shell
edge-tts --list-voices
```

```shell
edge-tts --list-voices > voices_list.txt
```

Now! We Write / Modify / Delete / Run the Source Codes...

```shell
deactivate
```

---

### Run

```shell
uv run .\app_01.py
```

```shell
uv run .\app_02.py
```

```shell
uv run .\app_03.py
```

---
