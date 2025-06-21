import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
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


def analyze_text(text: str, model: str, fact_check: bool) -> str:
    context = '\n'.join(vector_store.search(text))
    news = fetch_latest_fragments(text[:100])
    prompt_parts = []
    if context:
        prompt_parts.append(context)
    if news:
        prompt_parts.append('Context from news:\n' + news)
    prompt_parts.append(text)
    prompt = '\n\n'.join(prompt_parts)

    generator = get_generator(model)
    out = generator(prompt, num_return_sequences=1)[0]['generated_text']
    if fact_check and 'uncertain' in out.lower():
        out += '\n\n[Fact check may be required]'
    return out


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('ScamScanner')
        self.geometry('800x600')

        container = ttk.Frame(self, padding=10)
        container.pack(expand=True, fill='both')

        url_row = ttk.Frame(container)
        url_row.pack(fill='x')
        ttk.Label(url_row, text='Article URL:').pack(side='left')
        self.url_entry = ttk.Entry(url_row)
        self.url_entry.pack(side='left', fill='x', expand=True, padx=5)

        opts = ttk.Frame(container)
        opts.pack(fill='x', pady=5)
        ttk.Label(opts, text='Model:').pack(side='left')
        self.model_var = tk.StringVar(value='gpt2')
        ttk.Combobox(opts, textvariable=self.model_var, values=['gpt2', 'distilgpt2'], width=15).pack(side='left', padx=5)
        self.fact_var = tk.BooleanVar()
        ttk.Checkbutton(opts, text='Fact-check', variable=self.fact_var).pack(side='left', padx=5)

        ttk.Button(container, text='Analyze', command=self.on_analyze).pack(pady=5)

        self.out_box = scrolledtext.ScrolledText(container, wrap='word', font=('Arial', 11))
        self.out_box.pack(expand=True, fill='both')

        self.status = ttk.Label(self, text='Ready')
        self.status.pack(fill='x')

    def on_analyze(self) -> None:
        url = self.url_entry.get().strip()
        if not url:
            messagebox.showwarning('No URL', 'Please enter article URL.')
            return
        self.status.config(text='Fetching...')
        self.update_idletasks()
        try:
            text = fetch_article(url)
            self.status.config(text='Analyzing...')
            self.update_idletasks()
            result = analyze_text(text, self.model_var.get(), self.fact_var.get())
            self.out_box.delete('1.0', tk.END)
            self.out_box.insert(tk.END, result)
            self.status.config(text='Done')
        except Exception as e:
            messagebox.showerror('Error', str(e))
            self.status.config(text='Error')


def main() -> None:
    App().mainloop()


if __name__ == '__main__':
    main()
