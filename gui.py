import tkinter as tk
from tkinter import scrolledtext, messagebox
import requests
from bs4 import BeautifulSoup

from backend.embedding import vector_store
from backend.model_factory import get_generator
from backend.news_fetcher import fetch_latest_fragments


def fetch_article(url: str) -> str:
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, 'html.parser')
    paragraphs = [p.get_text() for p in soup.find_all('p')]
    return '\n'.join(paragraphs)


def analyze_text(text: str) -> str:
    context = '\n'.join(vector_store.search(text))
    news = fetch_latest_fragments(text[:100])
    prompt_parts = []
    if context:
        prompt_parts.append(context)
    if news:
        prompt_parts.append('Context from news:\n' + news)
    prompt_parts.append(text)
    prompt = '\n\n'.join(prompt_parts)

    generator = get_generator('gpt2')
    return generator(prompt, num_return_sequences=1)[0]['generated_text']


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('ScamScanner')
        self.geometry('700x500')

        tk.Label(self, text='Article URL:').pack(anchor='w')
        self.url_entry = tk.Entry(self, width=80)
        self.url_entry.pack(fill='x', padx=5, pady=5)

        tk.Button(self, text='Analyze', command=self.on_analyze).pack(pady=5)

        self.out_box = scrolledtext.ScrolledText(self, wrap='word')
        self.out_box.pack(expand=True, fill='both', padx=5, pady=5)

    def on_analyze(self) -> None:
        url = self.url_entry.get().strip()
        if not url:
            messagebox.showwarning('No URL', 'Please enter article URL.')
            return
        try:
            text = fetch_article(url)
            result = analyze_text(text)
            self.out_box.delete('1.0', tk.END)
            self.out_box.insert(tk.END, result)
        except Exception as e:
            messagebox.showerror('Error', str(e))


def main() -> None:
    App().mainloop()


if __name__ == '__main__':
    main()
