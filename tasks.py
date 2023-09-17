from invoke import task
from pathlib import Path
import os

PROJECT_ROOT = Path(os.environ["RINHA_ROOT"])
BUILD_DIR = Path(os.environ["RINHA_BUILD_DIR"])
TEST_DIR = Path(os.environ["RINHA_TEST_DIR"])
LLVM_CMAKE_DIR = Path(os.environ["LLVM_CMAKE"])
MLIR_CMAKE_DIR = Path(os.environ["MLIR_CMAKE"])


@task
def clean(c):
    with c.cd(PROJECT_ROOT):
        c.run("rm -rf build/")


@task
def build(c, nproc=1):
    BUILD_DIR.mkdir(exist_ok=True)
    with c.cd(BUILD_DIR):
        c.run(
            f"cmake .. -DLLVM_DIR={LLVM_CMAKE_DIR} -DMLIR_DIR={MLIR_CMAKE_DIR} -DCMAKE_EXPORT_COMPILE_COMMANDS=ON"
        )
        c.run(f"cmake --build . -j{nproc}")
