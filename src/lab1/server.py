from flask import Flask, request
import os
import shutil

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, this is NIS7021 Lab1!\n"


def save_file(file, dirname, proj_dir, proj_files, source_filename):
    try:
        # create directory
        os.makedirs(dirname, exist_ok=True)
        for proj_file in proj_files:
            shutil.copy(f"{proj_dir}/{proj_file}", dirname + proj_file)
        # write bytes into file
        file.save(dirname + source_filename)
        return True
    except OSError as e:
        print(e)
        return False


def build_and_test(dirname, program, value):
    # build the code using pre-provided Makefile
    if not os.system("make -C " + dirname) == 0:
        return False
    # test the return value of command
    if not os.system("qemu-riscv64 " + dirname + program) == value:
        return False
    else:
        return True


@app.route("/upload/asm", methods=["POST"])
def get_asm_code():
    # using student id as directory name
    file = request.files.get("file")
    dirname = f"upload/asm/{os.path.splitext(file.filename)[0]}/"
    if not save_file(file, dirname, "inner_product", ["Makefile"], "inner_product.s"):
        shutil.rmtree(dirname)
        return "Failed to save your file\n"
    if not build_and_test(dirname, "inner_product", 47104):
        shutil.rmtree(dirname)
        return "Failed to pass test\n"
    return "Great! You've passed the test\n"


@app.route("/upload/crypto", methods=["POST"])
def get_source_code():
    # using student id as directory name
    file = request.files.get("file")
    dirname = f"upload/crypto/{os.path.splitext(file.filename)[0]}/"
    if not save_file(file, dirname, "crypto-algorithms", ["Makefile", "crypto_test.c", "crypto.h"], "crypto.c"):
        shutil.rmtree(dirname)
        return "Failed to save your file\n"
    if not build_and_test(dirname, "crypto_test", 0):
        shutil.rmtree(dirname)
        return "Failed to pass test\n"
    return "Great! You've passed the test\n"
