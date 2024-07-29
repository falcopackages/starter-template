#!/command/with-contenv sh

cd /app
python {{ cookiecutter.project_name }}/__main__.py setup