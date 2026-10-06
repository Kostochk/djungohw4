from django.shortcuts import render
import datetime

def song_view(request, lang='en'):
    translations = {
        'en': {
            'text': "Rose-gold seat on a helicopter\nDouble C, no Chanel, 'cause she bad, bad, bad\nRidin' Kawasaki, and I could cop you a new 'Rari\nLet you ride it, know you're rare and you're bad, bad, bad",
            'title': 'English'
        },
        'fr': {
            'text': "Siège en or rose dans un hélicoptère\nDouble C, pas de Chanel, car elle est mauvaise, mauvaise, mauvaise\nEn Kawasaki, et je замовив тобі нову Феррарі\nLaisse-toi la conduire, je sais que tu es rare...",
            'title': 'Français'
        },
        'de': {
            'text': "Roségoldener Sitz in einem Hubschrauber\nDoppel-C, kein Chanel, weil sie böse, böse, böse ist\nKawasaki fahren, und ich könnte dir einen neuen Ferrari kaufen...",
            'title': 'Deutsch'
        },
        'es': {
            'text': "Asiento de oro rosa en un helicóptero\nDoble C, nada de Chanel, porque ella es mala, mala, mala\nMontando una Kawasaki, y podría comprarte un Ferrari nuevo...",
            'title': 'Español'
        }
    }
    data = translations.get(lang, translations['en'])
    return render(request, 'song.html', data)

def cars_view(request, brand='home'):
    brands = {
        'home': {'name': 'Головна', 'desc': 'Ласкаво просимо до нашого автосалону!'},
        'toyota': {'name': 'Тойота', 'desc': 'Toyota — лідер надійності та якості.'},
        'honda': {'name': 'Хонда', 'desc': 'Honda — потужність та технологічність.'},
        'renault': {'name': 'Рено', 'desc': 'Renault — європейський комфорт.'},
    }
    context = brands.get(brand, brands['home'])
    return render(request, 'cars.html', context)


def day_view(request):
    days = [
        {'name': 'Понеділок', 'color': '#f39c12'}, 
        {'name': 'Вівторок', 'color': '#e74c3c'},   
        {'name': 'Середа', 'color': '#9b59b6'},    
        {'name': 'Четвер', 'color': '#3498db'},    
        {'name': 'П’ятниця', 'color': '#2ecc71'},   
        {'name': 'Субота', 'color': '#1abc9c'},     
        {'name': 'Неділя', 'color': '#34495e'},     
    ]
    today_index = datetime.date.today().weekday()
    context = {'day': days[today_index]}
    return render(request, 'day.html', context)

def headphones_view(request):
    model_id = request.GET.get('model')
    catalog = {
        'budslive': {
            'full_name': 'Samsung Galaxy Buds Live',
            'specs': 'Активне шумозаглушення, форма "бобів", до 21 години роботи.'
        },
        'airpods': {
            'full_name': 'Apple AirPods',
            'specs': 'Процесор H1, швидке підключення, чистий звук.'
        }
    }
    info = catalog.get(model_id, {'full_name': 'Модель не знайдена', 'specs': 'Оберіть модель зі списку.'})
    return render(request, 'headphones.html', {'info': info})