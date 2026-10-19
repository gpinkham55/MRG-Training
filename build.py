"""Build the MR&G Training site from src/*.md.

Requires pandoc. Run: python3 build.py
Pages are written to the repo root. trainer.html is hand-built and not touched.
"""
import html, re, subprocess

PAGES = [
    ("index", "Home", None, ""),
    ("schedule", "Schedule", "src/schedule.md", "Three-week plan, daily blocks, and mentor hours."),
    ("guides", "P21 Guides", "src/guides.md", "Step-by-step P21 workflows with fields and common mistakes."),
    ("reference", "Product Reference", "src/reference.md", "Hose, hydraulics, crimping, threads, gaskets, flanges, and torque."),
    ("exercises", "Exercises", "src/exercises.md", "Daily practice tasks and simulations to work in P21PLAY."),
    ("assessments", "Assessments", "src/assessments.md", "Week 1 and Week 2 quizzes, final exam, and sign-off record."),
    ("trainer", "Call Desk Trainer", None, "Practice customer calls: ask the right questions, build the ticket, pick the P21PLAY action."),
]

CSS = """
:root{--bg:#F8F8FA;--panel:#FFFFFF;--ink:#0E1D35;--muted:#2B3D5B;--line:#C3C3C3;--steel:#2B3D5B;--steel-ink:#FFFFFF;--tag:#DDDEE5;--tag-ink:#0E1D35;--code:#DDDEE5;--head:#0E1D35;--head-ink:#DDDEE5;--head-hover:#2B3D5B;--focus:#7C8594;
--display:"Barlow Condensed","Arial Narrow",Arial,sans-serif;--body:"Source Sans 3","Segoe UI",Arial,sans-serif;--mono:"IBM Plex Mono",Consolas,monospace}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#0E1D35;--panel:#15253F;--ink:#DDDEE5;--muted:#C3C3C3;--line:#2B3D5B;--steel:#C3C3C3;--steel-ink:#0E1D35;--tag:#DDDEE5;--tag-ink:#0E1D35;--code:#2B3D5B;--head:#15253F;--head-ink:#DDDEE5;--head-hover:#2B3D5B;--focus:#7C8594;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#0E1D35;--panel:#15253F;--ink:#DDDEE5;--muted:#C3C3C3;--line:#2B3D5B;--steel:#C3C3C3;--steel-ink:#0E1D35;--tag:#DDDEE5;--tag-ink:#0E1D35;--code:#2B3D5B;--head:#15253F;--head-ink:#DDDEE5;--head-hover:#2B3D5B;--focus:#7C8594;color-scheme:dark}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.55 var(--body)}
.top{background:var(--head);border-bottom:1px solid var(--head-hover);position:sticky;top:0;z-index:5}
.top-in{max-width:1180px;margin:0 auto;padding:10px max(16px,env(safe-area-inset-left,0px));display:flex;flex-wrap:wrap;align-items:center;gap:8px 18px}
.brand{font:700 1.3rem var(--display);color:var(--head-ink);text-decoration:none;letter-spacing:.01em}
.brand span{background:var(--tag);color:var(--tag-ink);padding:0 .25em;border-radius:3px}
.nav{display:flex;flex-wrap:wrap;gap:4px}
.nav a{font-weight:600;font-size:.92rem;color:var(--head-ink);text-decoration:none;padding:6px 10px;border-radius:5px}
.nav a:hover{background:var(--head-hover)}
.nav a[aria-current="page"]{background:var(--head-ink);color:var(--head)}
.wrap{max-width:1180px;margin:0 auto;padding:24px max(16px,env(safe-area-inset-left,0px)) 48px;display:grid;grid-template-columns:240px minmax(0,1fr);gap:32px;align-items:start}
@media (max-width:860px){.wrap{grid-template-columns:minmax(0,1fr)}.toc{position:static!important;max-height:none!important}}
.toc{position:sticky;top:70px;max-height:calc(100vh - 90px);overflow:auto;font-size:.88rem;border-left:2px solid var(--line);padding-left:12px}
.toc b{display:block;font:600 .72rem var(--body);letter-spacing:.1em;text-transform:uppercase;color:var(--muted);margin-bottom:6px}
.toc a{display:block;color:var(--ink);text-decoration:none;padding:3px 0}
.toc a.l3{padding-left:12px;color:var(--muted)}
.toc a:hover{color:var(--steel)}
main{min-width:0;max-width:78ch}
main h1{font:700 2.2rem/1.05 var(--display);margin:0 0 16px;text-wrap:balance}
main h2{font:600 1.6rem/1.15 var(--display);margin:36px 0 10px;padding-bottom:4px;border-bottom:2px solid var(--steel);text-transform:uppercase;letter-spacing:.02em}
main h3{font:600 1.25rem var(--display);margin:26px 0 8px;letter-spacing:.02em}
main a{color:var(--steel)}
main table{border-collapse:collapse;font-size:.9rem;width:100%;font-variant-numeric:tabular-nums}
.tw{overflow-x:auto;margin:12px 0}
main th,main td{border:1px solid var(--line);padding:6px 9px;text-align:left;vertical-align:top}
main th{background:var(--code);font-weight:600}
main code{font-family:var(--mono);background:var(--code);padding:1px 4px;border-radius:3px}
main hr{border:0;border-top:1px dashed var(--line);margin:28px 0}
main li{margin:3px 0}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:14px;margin-top:20px}
.card{display:flex;flex-direction:column;gap:4px;background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:16px;text-decoration:none;color:var(--ink)}
.card:hover{border-color:var(--steel)}
.card b{font:600 1.3rem var(--display);letter-spacing:.02em}
.card span{color:var(--muted);font-size:.92rem}
.card.hi{border-top:4px solid var(--steel)}
.home{grid-template-columns:minmax(0,1fr)}
.home main{max-width:none}
a:focus-visible{outline:3px solid var(--focus);outline-offset:2px}
"""

HEAD = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700&family=Source+Sans+3:wght@400;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>{css}</style></head><body>
<header class="top"><div class="top-in"><a class="brand" href="index.html"><span>MR&amp;G</span> Training</a><nav class="nav">{nav}</nav></div></header>
"""


def nav(cur):
    cur_attr = ' aria-current="page"'
    return "".join(
        f'<a href="{k}.html"{cur_attr if k == cur else ""}>{html.escape(t)}</a>'
        for k, t, _, _ in PAGES
    )


def slug(t):
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")


def render(src):
    body = subprocess.run(["pandoc", src, "-f", "gfm", "-t", "html5"], capture_output=True, text=True, check=True).stdout
    toc, seen = [], {}

    def hd(m):
        lvl, text = m.group(1), m.group(3)
        plain = re.sub(r"<[^>]+>", "", text)
        s = slug(plain) or "s"
        seen[s] = seen.get(s, 0) + 1
        if seen[s] > 1:
            s += f"-{seen[s]}"
        if lvl in ("1", "2", "3"):
            toc.append((int(lvl), plain, s))
        return f'<h{lvl} id="{s}">{text}</h{lvl}>'

    body = re.sub(r"<h([1-6])( [^>]*)?>(.*?)</h\1>", hd, body, flags=re.S)
    body = body.replace("<table>", '<div class="tw"><table>').replace("</table>", "</table></div>")
    return body, toc


def page(key, title, src, blurb):
    body, toc = render(src)
    t = "".join(
        f'<a class="l{max(2, l)}" href="#{s}">{html.escape(p)}</a>' for l, p, s in toc if l <= 3
    )
    out = HEAD.format(title=f"{title} | MR&amp;G Training", css=CSS, nav=nav(key))
    out += f'<div class="wrap"><aside class="toc"><b>On this page</b>{t}</aside><main>{body}</main></div></body></html>\n'
    open(f"{key}.html", "w").write(out)


def home():
    cards = "".join(
        f'<a class="card{" hi" if k == "trainer" else ""}" href="{k}.html"><b>{html.escape(t)}</b><span>{html.escape(b)}</span></a>'
        for k, t, _, b in PAGES if k != "index"
    )
    out = HEAD.format(title="MR&amp;G Training", css=CSS, nav=nav("index"))
    out += f"""<div class="wrap home"><main>
<h1>New Hire Onboarding</h1>
<p>Montgomery Rubber &amp; Gasket's three-week program for inside sales, counter sales, and customer service. The first half of each day is self-taught in P21PLAY and the product reference. The second half is with your mentor.</p>
<p>Start with the <a href="schedule.html">Schedule</a> to see what's on today, then work the matching guide and reference sheet. Practice calls anytime in the <a href="trainer.html">Call Desk Trainer</a>.</p>
<div class="cards">{cards}</div>
<p style="color:var(--muted);font-size:.85rem;margin-top:28px">All practice entries go in P21PLAY, never live P21. Wear safety glasses when cutting or operating shop equipment.</p>
</main></div></body></html>
"""
    open("index.html", "w").write(out)


for k, t, src, b in PAGES:
    if src:
        page(k, t, src, b)
home()
print("built")
