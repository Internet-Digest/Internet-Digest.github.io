import feedparser
import re
from datetime import datetime

# URL RSS-ленты Reddit Popular
RSS_URL = "https://www.reddit.com/r/popular/.rss"

def fetch_news():
    """Забирает 5 свежих новостей из RSS."""
    feed = feedparser.parse(RSS_URL)
    news_items = []
    for entry in feed.entries[:5]:
        # Убираем мусор из заголовка
        title = entry.title.replace('[link]', '').replace('[comments]', '').strip()
        link = entry.link
        news_items.append({'title': title, 'link': link})
    return news_items

def build_html(items):
    """Собирает HTML-блок из новостей."""
    html = '<!-- START_DIGEST -->\n'
    for item in items:
        html += '<article class="digest-item">\n'
        # Простая заглушка для картинки, т.к. RSS не всегда их отдает
        html += f'    <img src="https://placehold.co/800x400/1e1e1e/ffffff?text=🔥" alt="{item["title"]}" class="news-image">\n'
        html += '    <div class="news-content">\n'
        html += f'        <h2>{item["title"]}</h2>\n'
        html += '        <div class="news-footer">\n'
        html += f'            <a href="{item["link"]}" target="_blank" class="source-link">Источник (Reddit) &rarr;</a>\n'
        html += '            <div class="share-buttons">\n'
        html += '                <a class="share-tg" title="Поделиться в Telegram">Telegram</a>\n'
        html += '                <a class="share-tw" title="Поделиться в Twitter (X)">Twitter</a>\n'
        html += '            </div>\n'
        html += '        </div>\n'
        html += '    </div>\n'
        html += '</article>\n'
    
    # Добавляем метку времени
    now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')
    html += f'<!-- Last updated: {now} -->\n'
    html += '<!-- END_DIGEST -->'
    return html

def update_index_file(html_content):
    """Обновляет index.html, заменяя блок между метками."""
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Используем регулярное выражение для замены контента между метками
    new_content = re.sub(
        r'<!-- START_DIGEST -->(.|\n)*?<!-- END_DIGEST -->',
        html_content,
        content,
        flags=re.DOTALL
    )

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == "__main__":
    news = fetch_news()
    html = build_html(news)
    update_index_file(html)
    print("index.html has been updated successfully.")