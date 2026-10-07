# ============================================================
# Крок 3. Зробіть аналіз
# ============================================================
# Потрібно порахувати:
#   - середній бал по класу з кожного предмета (math, python, english);
#   - ім'я студента з найвищим середнім балом (по трьох предметах).
INPUT_FILE = "students.csv"
OUTPUT_FILE = "result.txt"

# TODO 1: відкрийте INPUT_FILE через with open(...) as f:
#   і пропустіть рядок заголовка (next(f))

subject_points = {"math": 0, "python": 0, "english": 0}
student_count = 0
best_student = None
best_average = 0

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    next(f)

    # TODO 2: пройдіться по рядках файлу (for line in f:), для кожного рядка:
    #   - приберіть символ переносу рядка (line.strip())
    #   - розбийте рядок по комі (line.split(","))
    #   - перетворіть оцінки на числа (int або float)
    for line in f:
        line = line.strip()
        name, math, python, english = line.split(",")
        math = float(math)
        python = float(python)
        english = float(english)

        # TODO 3: по ходу циклу накопичуйте:
        #   - суми оцінок з кожного предмета та кількість студентів
        #   - найкращого студента (ім'я та його середній бал) — порівнюйте
        #     середній бал поточного студента з найкращим на цей момент

        subject_points["math"] += math
        subject_points["python"] += python
        subject_points["english"] += english
        student_count += 1

        average = (math + python + english) / 3
        if average > best_average:
            best_average = average
            best_student = name

# TODO 4: після циклу порахуйте середній бал по класу з кожного предмета
#   (сума / кількість студентів)

math_average = subject_points["math"] / student_count
python_average = subject_points["python"] / student_count
english_average = subject_points["english"] / student_count

# ============================================================
# Крок 4. Збережіть результат у .txt файл
# ============================================================
# TODO 5: відкрийте OUTPUT_FILE в режимі 'w' і запишіть туди результат
#   у такому вигляді (числа округліть до одного знака після коми):
#
#   Середній бал по класу:
#   math: 67.8
#   python: 67.9
#   english: 67.9
#
#   Найкращий студент: Ім'я Прізвище (97.0)
#
# Також виведіть цей самий текст на екран через print().
#
# Запустіть скрипт (python analyze.py) і перевірте, що в папці
# з'явився файл result.txt.

with open(OUTPUT_FILE, "w") as f:
    f.write(f"Середній бал по класу:\n")
    f.write(f"math: {math_average:.1f}\n")
    f.write(f"python: {python_average:.1f}\n")
    f.write(f"english: {english_average:.1f}\n")
    f.write(f"\n")
    f.write(f"Найкращий студент: {best_student} ({best_average:.1f})\n")

    print(f"Середній бал по класу:")
    print(f"math: {math_average:.1f}")
    print(f"python: {python_average:.1f}")
    print(f"english: {english_average:.1f}")
    print(f"")
    print(f"Найкращий студент: {best_student} ({best_average:.1f})")