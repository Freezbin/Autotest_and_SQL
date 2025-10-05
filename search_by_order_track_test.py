import sender_stand_request as sender
import data

def get_new_order():
    res = sender.post_new_order(data.orders_body)
    json_data = res.json()
    return json_data['track']

def test_order_creation_and_retrieval():
    # Создаем заказ
    response = sender.post_new_order(data.orders_body)
    
    # Извлекаем трек-номер из ответа
    track_number = response.json()['track']
    
    # Получаем заказ по трек-номеру
    order_response = sender.get_order_by_track(track_number)
    
    # Проверяем статус-код ответа
    assert order_response.status_code == 200, "Ошибка получения заказа"

# Запуск теста
if __name__ == '__main__':
    test_order_creation_and_retrieval()
