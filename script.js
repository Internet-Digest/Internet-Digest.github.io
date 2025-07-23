document.addEventListener('DOMContentLoaded', function() {
    const pageUrl = window.location.href;
    const siteTitle = "Internet Digest";

    // Кнопки "Поделиться" в Telegram
    const shareTgButtons = document.querySelectorAll('.share-tg');
    shareTgButtons.forEach(button => {
        const newsTitle = button.closest('.digest-item').querySelector('h2').textContent;
        const text = `🔥 ${newsTitle} — в новом выпуске ${siteTitle}!`;
        const telegramUrl = `https://t.me/share/url?url=${encodeURIComponent(pageUrl)}&text=${encodeURIComponent(text)}`;
        button.href = telegramUrl;
        button.target = '_blank';
    });

    // Кнопки "Поделиться" в Twitter
    const shareTwButtons = document.querySelectorAll('.share-tw');
    shareTwButtons.forEach(button => {
        const newsTitle = button.closest('.digest-item').querySelector('h2').textContent;
        const text = `🔥 ${newsTitle} — в новом выпуске Internet Digest!`;
        const twitterUrl = `https://twitter.com/intent/tweet?url=${encodeURIComponent(pageUrl)}&text=${encodeURIComponent(text)}`;
        button.href = twitterUrl;
        button.target = '_blank';
    });
});
