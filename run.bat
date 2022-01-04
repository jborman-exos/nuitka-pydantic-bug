REM python3.9 -m venv .venv
CALL .venv\Scripts\activate && \
    pip install -r requirements.txt && \
    python -m test_my_module && \
    python -m nuitka --module my_module --include-package my_module && \
    rename my_module _my_module && \
    python -m test_my_module && \
    rename _my_module my_module
