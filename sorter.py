import os
import shutil

import llm_clients
import processor
import router


def sort(source, target, config, llm):
    if llm == 0:
        local_sort(source, target, config)
    else:
        llm_sort(source, target, config, llm)


def local_sort(source, target, config):

    rules = router.load_config(config)

    for file in os.listdir(source):
        filename = os.fsdecode(file)
        folder = router.regex_categorise(filename, rules)

        # regex on filename first
        if folder != "":
            file_path = os.path.join(source, filename)
            target_path = os.path.join(target, folder)
            shutil.move(file_path, target_path)
        else:
            # if that doesn't work, extract text and regex on that
            file_path = os.path.join(source, filename)
            if filename.lower().endswith((".pdf", ".docx", ".txt")):
                extracted_text = processor.doc_extract(file_path)
            elif filename.lower().endswith((".jpg", ".jpeg", ".png")):
                extracted_text = processor.tesseract_img_extract(file_path)
            else:
                continue

            folder = router.regex_categorise(extracted_text, rules)

            if folder not in (
                "-1",
                "-2",
                "-3",
            ):  # on sucessfull text extraction, move file to appropriate directory
                target_path = os.path.join(target, folder)
                shutil.move(file_path, target_path)


def llm_sort(source, target, config, llm):

    rules = config

    for file in os.listdir(source):
        filename = os.fsdecode(file)
        file_path = os.path.join(source, filename)
        file_path = os.path.join(source, filename)
        if filename.lower().endswith((".pdf", ".docx", ".txt")):
            extracted_text = processor.doc_extract(file_path)
        elif filename.lower().endswith((".jpg", ".jpeg", ".png")):
            extracted_text = processor.tesseract_img_extract(file_path)
        else:
            continue

        if llm == "gemini":
            folder = llm_clients.call_gemini(extracted_text)
        elif llm == "ollama":
            # Assuming you define a model name
            folder = llm_clients.call_ollama(extracted_text, "llama3")

        if folder:
            target_path = os.path.join(target, folder)
            shutil.move(file_path, target_path)
