#!/command/with-contenv sh

cd /app
python -m {{ cookiecutter.project_name }} setup
