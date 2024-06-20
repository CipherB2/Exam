import hashlib
def add_hash_to_file(file_path):
    with open(file_path, 'rb') as f:
        file_data = f.read()
    # Вычисляем SHA-256 хэш-сумму
    hash_sum = hashlib.sha256(file_data).hexdigest()
    with open(file_path, 'ab') as f:
        # Добавляем хэш-сумму как последнюю строку
        f.write(b'\n' + hash_sum.encode())
    print(f'Хэш-сумма {hash_sum} добавлена в файл.')
add_hash_to_file('test.txt')