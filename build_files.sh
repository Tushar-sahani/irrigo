# build_files.sh
python -m pip install -r requirements.txt
python3.9 manage.py collectstatic 