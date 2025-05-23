# import subprocess
# import os
# import time
# from datetime import datetime
# from app.pipeline.extract import extract_from_excel
# from app.pipeline.transform import transform_data, convert_df_to_parquet
# from app.pipeline.load import load_parquets, save_to_excel

# # Criar diretório de logs (docs/logs) se não existir
# os.makedirs('docs/logs', exist_ok=True)

# # Nome do arquivo de log com data e hora
# log_filename = f"docs/logs/log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

# def log_and_print(message: str):
#     """
#     Imprime e grava a mensagem no log.
#     """
#     print(message)
#     with open(log_filename, "a", encoding="utf-8") as log_file:
#         log_file.write(message + "\n")

# def log_event(stage: str, status: str, elapsed_time: float, message: str = ""):
#     """
#     Registra um evento no log com tempo de execução e status.
#     """
#     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     log_line = f"[{timestamp}] - {stage} - {status} - Tempo: {elapsed_time:.2f}s - {message}"
#     log_and_print(log_line)

# def run_tests(test_file: str, emoji: str) -> bool:
#     """
#     Executa testes unitários com pytest e registra no log.
#     """
#     start = time.perf_counter()
#     log_and_print(f"\n{emoji} Rodando testes: {test_file}")
#     result = subprocess.run(['pytest', test_file], capture_output=True, text=True)
#     elapsed = time.perf_counter() - start
#     log_and_print(result.stdout)
    
#     status = "SUCESSO" if result.returncode == 0 else "ERRO"
#     log_event(f"Test {os.path.basename(test_file)} {emoji}", status, elapsed)
    
#     return result.returncode == 0

# if __name__ == "__main__":
#     log_and_print("🚀 Iniciando pipeline ETL modular com validação intermediária e logging...\n")
#     log_event("Pipeline 🚀", "INÍCIO", 0.0, "Pipeline iniciado.")

#     # 🔹 Etapa Extract
#     start = time.perf_counter()
#     log_and_print("📥 Executando Extract...")
#     try:
#         df_extracted = extract_from_excel('data/input')
#         elapsed = time.perf_counter() - start
#         log_event("Extract 📥", "SUCESSO", elapsed)
#     except Exception as e:
#         elapsed = time.perf_counter() - start
#         log_event("Extract 📥", "ERRO", elapsed, str(e))
#         exit(1)

#     if not run_tests('tests/test_extract.py', '🧪'):
#         exit(1)

#     # 🔹 Etapa Transform
#     start = time.perf_counter()
#     log_and_print("🔧 Executando Transform...")
#     try:
#         df_transformed = transform_data(df_extracted)
#         convert_df_to_parquet(df_transformed, 'data/output/concatenated_data.parquet')
#         elapsed = time.perf_counter() - start
#         log_event("Transform 🔧", "SUCESSO", elapsed)
#     except Exception as e:
#         elapsed = time.perf_counter() - start
#         log_event("Transform 🔧", "ERRO", elapsed, str(e))
#         exit(1)

#     if not run_tests('tests/test_transform.py', '🧪'):
#         exit(1)

#     # 🔹 Etapa Load
#     start = time.perf_counter()
#     log_and_print("📤 Executando Load...")
#     try:
#         df_loaded = load_parquets('data/output')
#         save_to_excel(df_loaded, 'data/output/files_loaded.xlsx')
#         elapsed = time.perf_counter() - start
#         log_event("Load 📤", "SUCESSO", elapsed)
#     except Exception as e:
#         elapsed = time.perf_counter() - start
#         log_event("Load 📤", "ERRO", elapsed, str(e))
#         exit(1)

#     if not run_tests('tests/test_load.py', '🧪'):
#         exit(1)

#     # 🔹 Etapa Teste Final: Pipeline
#     if not run_tests('tests/test_pipeline.py', '✅'):
#         exit(1)

#     log_event("Pipeline 🎯", "FIM", 0.0, "Pipeline finalizado com sucesso.")
#     log_and_print("\n🎯 Pipeline completo e validado com sucesso!")

import subprocess
import os
import time
from datetime import datetime
from app.pipeline.extract import extract_from_excel
from app.pipeline.transform import transform_data, convert_df_to_parquet
from app.pipeline.load import load_parquets, save_to_excel

# Criar diretório de logs (docs/logs) com caminho absoluto
log_dir = os.path.abspath('docs/logs')

try:
    os.makedirs(log_dir, exist_ok=True)
except Exception as e:
    print(f"❌ Erro ao criar diretório de log: {e}")
    exit(1)

# Nome do arquivo de log com data e hora
log_filename = os.path.join(log_dir, f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")

def log_and_print(message: str):
    """
    Imprime e grava a mensagem no log.
    """
    print(message)
    try:
        with open(log_filename, "a", encoding="utf-8") as log_file:
            log_file.write(message + "\n")
    except Exception as e:
        print(f"❌ Erro ao escrever no log: {e}")

def log_event(stage: str, status: str, elapsed_time: float, message: str = ""):
    """
    Registra um evento no log com tempo de execução e status.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] - {stage} - {status} - Tempo: {elapsed_time:.2f}s - {message}"
    log_and_print(log_line)

def run_tests(test_file: str, emoji: str) -> bool:
    """
    Executa testes unitários com pytest e registra no log.
    """
    start = time.perf_counter()
    log_and_print(f"\n{emoji} Rodando testes: {test_file}")
    result = subprocess.run(['pytest', test_file], capture_output=True, text=True)
    elapsed = time.perf_counter() - start
    log_and_print(result.stdout)
    
    status = "SUCESSO" if result.returncode == 0 else "ERRO"
    log_event(f"Test {os.path.basename(test_file)} {emoji}", status, elapsed)
    
    return result.returncode == 0

if __name__ == "__main__":
    log_and_print("🚀 Iniciando pipeline ETL modular com validação intermediária e logging...\n")
    log_event("Pipeline 🚀", "INÍCIO", 0.0, "Pipeline iniciado.")
    log_and_print(f"📝 Log será salvo em: {log_filename}\n")

    # 🔹 Etapa Extract
    start = time.perf_counter()
    log_and_print("📥 Executando Extract...")
    try:
        df_extracted = extract_from_excel('data/input')
        elapsed = time.perf_counter() - start
        log_event("Extract 📥", "SUCESSO", elapsed)
    except Exception as e:
        elapsed = time.perf_counter() - start
        log_event("Extract 📥", "ERRO", elapsed, str(e))
        exit(1)

    if not run_tests('tests/test_extract.py', '🧪'):
        exit(1)

    # 🔹 Etapa Transform
    start = time.perf_counter()
    log_and_print("🔧 Executando Transform...")
    try:
        df_transformed = transform_data(df_extracted)
        convert_df_to_parquet(df_transformed, 'data/output/concatenated_data.parquet')
        elapsed = time.perf_counter() - start
        log_event("Transform 🔧", "SUCESSO", elapsed)
    except Exception as e:
        elapsed = time.perf_counter() - start
        log_event("Transform 🔧", "ERRO", elapsed, str(e))
        exit(1)

    if not run_tests('tests/test_transform.py', '🧪'):
        exit(1)

    # 🔹 Etapa Load
    start = time.perf_counter()
    log_and_print("📤 Executando Load...")
    try:
        df_loaded = load_parquets('data/output')
        save_to_excel(df_loaded, 'data/output/files_loaded.xlsx')
        elapsed = time.perf_counter() - start
        log_event("Load 📤", "SUCESSO", elapsed)
    except Exception as e:
        elapsed = time.perf_counter() - start
        log_event("Load 📤", "ERRO", elapsed, str(e))
        exit(1)

    if not run_tests('tests/test_load.py', '🧪'):
        exit(1)

    # 🔹 Etapa Teste Final: Pipeline
    if not run_tests('tests/test_pipeline.py', '✅'):
        exit(1)

    log_event("Pipeline 🎯", "FIM", 0.0, "Pipeline finalizado com sucesso.")
    log_and_print("\n🎯 Pipeline completo e validado com sucesso!")
