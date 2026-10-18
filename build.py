# Собирает deploy/index.html из исходника артефакта: полный HTML-документ + отступы под Telegram.
src = open('src/app.html', encoding='utf-8').read()
src = src.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', '')
head_end = src.index('</style>') + len('</style>')
head, body = src[:head_end], src[head_end:]
extra_css = """
/* Отступы под вырез, «домой»-полоску и панели Telegram */
/* В полноэкранном режиме Telegram сверху свои кнопки «Закрыть» и «⋯» — отступаем на их высоту */
:root{--sat:calc(var(--tg-safe-area-inset-top,0px) + var(--tg-content-safe-area-inset-top,0px));
  --sab:max(env(safe-area-inset-bottom,0px),calc(var(--tg-safe-area-inset-bottom,0px) + var(--tg-content-safe-area-inset-bottom,0px)))}
html{padding-top:max(env(safe-area-inset-top,0px),var(--sat))}
.sheet{max-height:calc(100% - 24px - max(env(safe-area-inset-top,0px),var(--sat)))}
[hidden]{display:none!important}
img{max-width:100%}
.view{padding-bottom:calc(104px + var(--sab))}
.view.is-day{padding-bottom:calc(96px + var(--sab))}
.dock{padding-bottom:calc(var(--sab) + 12px)}
.sheet{padding-bottom:var(--sab)}
.toast{bottom:calc(var(--sab) + 96px)}
</style>"""
head = head[:-len('</style>')] + extra_css
doc = ('<!doctype html>\n<html lang="ru">\n<head>\n<meta charset="utf-8">\n'
       '<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, viewport-fit=cover">\n'
       '<meta name="theme-color" content="#2A2161">\n'
       + head + '\n</head>\n<body>' + body + '\n</body>\n</html>\n')
open('index.html', 'w', encoding='utf-8').write(doc)
print('index.html', len(doc), 'chars')
