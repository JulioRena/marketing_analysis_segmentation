@echo off

:: Rodar FastAPI
start cmd /k "uvicorn api.app:app --reload"

:: Aguardar 5 segundos para garantir que o FastAPI esteja em execução
timeout /t 5

:: Rodar Streamlit
start cmd /k "streamlit run ./api/interface.py"