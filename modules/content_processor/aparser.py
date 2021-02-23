from gensim.summarization import keywords
from gensim.summarization import summarize
from newspaper import Article, Config as NewspaperConfig


def make_html_bold(s: str) -> str:
    return f'<b>{s}</b>'


def parse_url(url, max_summary_sentences=4, max_summary_words=100, lang='en') -> str:
    text = ''

    conf = NewspaperConfig()
    conf.set_language(lang)
    conf.MAX_SUMMARY_SENT = max_summary_sentences
    article = Article(url, config=conf)

    article.download()
    article.parse()

    text += make_html_bold('AUTHORS:') + ' ' + ', '.join(article.authors) + '\n'
    text += make_html_bold('IMAGE:') + ' ' + str(article.top_image) + '\n'

    article.nlp()

    keywords_count = 12

    try:
        kw = keywords(article.text, words=keywords_count, split=True, lemmatize=True)  # article.keywords
    except IndexError:
        kw = []

    hashtags = [f'#{keyword}'.replace(' ', '_') for keyword in kw]

    summary = summarize(article.text, word_count=max_summary_words)  # article.summary

    # print(kw)
    text += make_html_bold('KEYWORDS:') + ' ' + ', '.join(hashtags) + '\n'

    text += make_html_bold('SUMMARY ({} sentences):\n'.format(max_summary_sentences)) + summary

    return text
