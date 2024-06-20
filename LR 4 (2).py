import hashlib
def verify_file_hash(file_path):
    with open(file_path, 'rb') as f:
        lines = f.readlines()
    # Вводим переменную, которая содержит контрольную хэш-сумму, взятую из файла
    original_hash = lines[-1].strip().decode()
    # Считываем файл без последней строки и вычисляем его хэш-сумму
    file_data_without_hash = b''.join(lines[:-1]).rstrip(b'\n')
    calculated_hash = hashlib.sha256(file_data_without_hash).hexdigest()
    print(calculated_hash)
    print(original_hash)
    # Сравниваем вычисленную хэш-сумму с контрольной
    if calculated_hash == original_hash:
        print('true')
    else:
        print('false')
verify_file_hash('test.txt')