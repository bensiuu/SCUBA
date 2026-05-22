# Installation

Clone repository:

```bash
git clone https://github.com/bensiuu/SCUBA.git
cd SCUBA
```

Create virtual env:

```bash
python -m venv .venv
```

Activate venv:

Windows:

```bash
.venv\Scripts\activate
```

Linux:

```bash
source .venv/bin/activate
```

Install packages:

```bash
pip install -r requirements.txt
```

Download required MediaPipe model:

```text
hand_landmarker.task
```

Place:
- `hand_landmarker.task`
- `scubacat.mp4`

inside the project folder.

Run project:

```bash
python main.py
```
