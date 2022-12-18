import model
from datetime import datetime

if __name__ == '__main__':
    # Данный код демонстрирует процесс создания экземпляра модели и
    # заполнения его данными, а также преобразование в json.
    # Будет полезен при разработке собственной модели ответа.
    response = model.Create(
        id=1
    )
    print(response.json())
