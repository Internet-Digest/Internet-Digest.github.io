import feedparser
import re
from datetime import datetime

# URL of the Reddit Popular RSS feed
RSS_URL = "https://www.reddit.com/r/popular/.rss"

def fetch_news():
    """Fetches the top 5 news items from the RSS feed."""
    feed = feedparser.parse(RSS_URL)
    news_items = []
    for entry in feed.entries[:5]:
        # Clean up the title
        title = entry.title.replace('[link]', '').replace('[comments]', '').strip()
        link = entry.link
        news_items.append({'title': title, 'link': link})
    return news_items

def build_html(items):
    """Builds the HTML block from the news items."""
    html = '<!-- START_DIGEST -->\n'
    for item in items:
        html += '<article class="digest-item">\n'
        # Simple placeholder for the image, as RSS doesn't always provide one
        html += f'    <img src="https://placehold.co/800x400/1e1e1e/ffffff?text=🔥" alt="{item["title"]}" class="news-image">\n'
        html += '    <div class="news-content">\n'
        html += f'        <h2>{item["title"]}</h2>\n'
        html += '        <div class="news-footer">\n'
        html += f'            <a href="{item["link"]}" target="_blank" class="source-link">Source (Reddit) &rarr;</a>\n'
        html += '            <div class="share-buttons">\n'
        html += '                <a class="share-tg" title="Share on Telegram">Telegram</a>\n'
        html += '                <a class="share-tw" title="Share on Twitter (X)">Twitter</a>\n'
        html += '            </div>\n'
        html += '        </div>\n'
        html += '    </div>\n'
        html += '</article>\n'
    
    # Add a timestamp
    now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')
    html += f'<!-- Last updated: {now} -->\n'
    html += '<!-- END_DIGEST -->'
    return html

def update_index_file(html_content):
    """Updates index.html by replacing the content between the markers."""
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Use a regular expression to replace the content between the markers
    new_content = re.sub(
        r'<!-- START_DIGEST -->(.|
)*?<!-- END_DIGEST -->',
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