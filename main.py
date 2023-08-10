import os
import shutil
from googletrans import Translator
from googletrans.constants import LANGUAGES


def translate_text(text, target_language):
    return Translator().translate(text, dest=target_language).text


def translate_file(input_path, output_path, target_language):
    translated = 0
    with open(input_path, 'r', encoding='utf-8') as infile:
        with open(output_path, 'w', encoding='utf-8') as outfile:
            for line in infile:
                if not line.strip():
                    outfile.write("\n")
                else:
                    translated_line = translate_text(line, target_language)
                    # print(translated_line)
                    outfile.write(translated_line)
                    translated += 1


def main(input_directory, backup_directory, target_language):
    if not os.path.exists(backup_directory):
        os.makedirs(backup_directory)

    for root, dirs, files in os.walk(input_directory):
        for filename in files:
            if ((filename.endswith('.md')
                    and not os.path.exists(os.path.join(root, f"{filename}")))
                    and not filename.startswith("translated_")):
                print("Translating the file {}".format(filename))
                input_path = os.path.join(root, filename)
                output_path = os.path.join(backup_directory, filename)
                translated_output_path = os.path.join(root, f"translated_{filename}")

                shutil.copy2(input_path, output_path)
                translate_file(input_path, translated_output_path, target_language)
                os.remove(input_path)
                os.rename(translated_output_path, input_path)


if __name__ == "__main__":
    input_directory = "C:\\KPLR\\Aout-2023\\k8s-workshops\\solutions"
    backup_directory = "C:\\KPLR\\Aout-2023\\k8s-workshops-en"
    target_language = 'fr'  # Change this to your desired target language code

    main(input_directory, backup_directory, target_language)
