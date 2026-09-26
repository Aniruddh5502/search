import re
import sys
import click
import httpx                                    # To fetch the href links
from search.animation          import ThinkingAnimation
from ddgs               import DDGS             # Searching the web with query
from bs4                import BeautifulSoup    # Parse te HTML to make it reasable
from rich.markdown      import Markdown
from rich.console       import Console

# Force UTF-8 encoding for Windows terminals to prevent UnicodeEncodeError
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

anim    = ThinkingAnimation()
console = Console()

theme_char      =   "*"
book_cloth      =   "#CC785C"
error           =   "#BF4D43"
focus           =   "#61AAF2"
white           =   "#FFFFFF"
black           =   "#000000"
cloud_light     =   "#BFBFBA"


@click.command()
@click.argument("query", type=str)
@click.argument("num", type=int, default=5)
def search(query:str, num:int):
    anim.start()
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query=query, max_results=num))
        
        anim.stop()
        
        for item in range(len(results)):
            console.print("")
            console.print(f"[bold]Number: {item}[/bold]")
            console.print(f"[bold]Title: {results[item]['title']}[/bold]")
            console.print(f"[cyan]Content: [/cyan]", Markdown(results[item]['body']))
            console.print(f"[dim]Link: {results[item]['href']}[/dim]")
            console.print(f"\n")
        return results
    except Exception as e:
        anim.stop()
        console.print(f"{theme_char} [bold red]Search Failed:[/bold red] {e}")
        return None


@click.command()
@click.argument("link", type=str)
@click.option("--store", is_flag=True, help="Save fetched page as .md file")
@click.option("--timeout", type=int, default=10, help="Timeout in seconds")
def fetch(link:str, store, timeout):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    anim.start()
    try:
        response = httpx.get(link, timeout=timeout, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        for tag in soup(["script", "style", "nav", "header", "footer"]):
            tag.decompose()
        
        text = " ".join(soup.get_text(separator=" ").split())
        anim.stop()
        
        console.print(f"[{focus}]Content: [/]", Markdown(text))
    except Exception as e:
        anim.stop()
        console.print(f"{theme_char} [{error}] Fetching Failed. ERROR[/] \n{e}")
        return None
    
    console.print("\n")
    if store:
        try:
            safe_name = response.url.path.rstrip("/").split("/")[-1] or "index"
            safe_name = re.sub(r'[<>:\"/\\\\|?*]', '_', safe_name)
            if not safe_name.endswith(".md"):
                safe_name += ".md"
                
            with open(f"{safe_name}", 'w', encoding='utf-8') as file:
                file.write(text)
            console.print(f"{theme_char} [dim]Written successfully as {safe_name}[/]")
            console.print("\n")
        except Exception as e:
            console.print(f"{theme_char} [{error}] Storage Error:[/] {e}")
            console.print("\n")

if __name__ == "__main__":
    pass
