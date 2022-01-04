# python3.9 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m test_my_module
python -m nuitka --module my_module --include-package my_module
mv my_module _my_module
python -m test_my_module
mv _my_module my_module