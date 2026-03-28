import llm_clients
import processor
import router
import os
import shutil


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
        if(folder != ""):
            shutil.move(filename, folder)
        else
            # if that doesn't work, extract text and regex on that
            file_path = os.path.join(source, filename)
            if filename.lower().endswith((".pdf", ".docx", ".txt")):
                extracted_text = processor.doc_extract(file_path)
            elif filename.lower().endswith((".jpg", ".jpeg", ".png")):
                extracted_text = processor.tesseract_img_extract(file_path)
            else:
                continue

            folder = router.regex_categorise(extracted_text, rules)

            if(folder != "-1" || "-2" || "-3"): # on sucessfull text extraction, move file to appropriate directory
                shutil.move(filename, folder)



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

        folder = llm_clients()
