export FLASK_APP=app
export FLASK_ENV=development
export FLASK_DEBUG=True
flask run


flask db init
flask db migrate
flask db upgrade

# flask run -h 0.0.0.0 -p 8000

# gera o report e roda os testes
coverage run --source=app -m unittest discover -s tests/ -v
# mostra um resumo da cobertura em shell
coverage report
# gera o path '/htmlcov' com htmls estáticos da cobertura
coverage html

behave tests/behavior_tests/features/
