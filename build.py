"""Genera index.html desde la política de la app (fuente: biottux_porotos).
Uso: python3 -I build.py   (lee ../biottux_porotos/assets/store/listing/privacy-policy-es.md)
"""
import os, re, markdown
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, '..', 'biottux_porotos', 'assets', 'store', 'listing', 'privacy-policy-es.md')
body = markdown.markdown(open(SRC, encoding='utf-8').read(), extensions=['sane_lists'])
# enlaces: URLs y correos sueltos
body = re.sub(r'(?<![":/@\w])(https?://[^\s<]+[^\s<.,;)])(?!</a>)', r'<a href="\1" rel="noopener">\1</a>', body)
body = re.sub(r'(?<![":\w/])([\w.+-]+@[\w-]+\.[\w.-]+\w)(?!</a>)', r'<a href="mailto:\1">\1</a>', body)

html = '''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Porotos — Política de privacidad</title>
<meta name="description" content="Política de privacidad de la app Porotos, anotador de truco.">
<style>
  :root { --wood:#7b4b28; --ink:#2a1d12; --muted:#6b5a4a; --bg:#faf5ec; }
  * { box-sizing: border-box; }
  body { margin:0; font:16px/1.65 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif; color:var(--ink); background:var(--bg); }
  header { background:linear-gradient(180deg,#8d5a30,#5e3519); color:#f5e9d3; padding:28px 20px 22px; }
  header .wrap { max-width:760px; margin:0 auto; }
  header h1 { margin:0 0 4px; font-size:1.7rem; }
  header p { margin:0; opacity:.92; }
  main { max-width:760px; margin:0 auto; padding:8px 20px 56px; }
  h1,h2,h3 { line-height:1.25; }
  main h1 { font-size:1.6rem; margin-top:28px; }
  main h2 { font-size:1.25rem; margin-top:28px; color:var(--wood); }
  main h3 { font-size:1.05rem; margin-top:20px; }
  a { color:var(--wood); overflow-wrap:anywhere; }
  ul { padding-left:22px; }
  li { margin:4px 0; }
  footer { max-width:760px; margin:0 auto; padding:0 20px 40px; color:var(--muted); font-size:.9rem; }
</style>
</head>
<body>
<header><div class="wrap">
  <h1>Porotos</h1>
  <p>Política de privacidad</p>
</div></header>
<main>
''' + body + '''
</main>
</body>
</html>
'''
open(os.path.join(HERE, 'index.html'), 'w', encoding='utf-8').write(html)
print('index.html', len(html), 'bytes')
