"""Draw the placeholder product illustrations for the Samples page.

Run: python3 tools/make_sample_art.py
Writes img/samples/<name>.svg. Replace any of them with a photo of our own
sample by uploading img/samples/<name>.jpg and changing the image line in
src/samples.md to the .jpg name.
"""
import math, os

INK = "#3D4240"
MID = "#6A6E6B"
ASH = "#AAB0AA"
LGRN = "#8DD783"
GRN = "#399A4B"
TINT = "#E4E7E4"
PAPER = "#FFFFFF"
W, H = 320, 200

os.makedirs("img/samples", exist_ok=True)


def svg(name, body, label):
    s = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{label}">'
         f'<rect width="{W}" height="{H}" rx="10" fill="{PAPER}"/>'
         f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="10" fill="none" stroke="{TINT}" stroke-width="2"/>'
         f'{body}</svg>\n')
    open(f"img/samples/{name}.svg", "w").write(s)


def hose(y=100, x0=40, x1=250, r=34, cover=MID, extra="", end_layers=(MID, LGRN, TINT)):
    """Side view of a hose with a cut end showing tube, reinforcement, cover."""
    b = f'<rect x="{x0}" y="{y-r}" width="{x1-x0}" height="{2*r}" rx="6" fill="{cover}"/>'
    b += extra
    rx = r * 0.42
    radii = [r, r * 0.78, r * 0.58]
    for rr, c in zip(radii, end_layers):
        b += f'<ellipse cx="{x1}" cy="{y}" rx="{rx*rr/r}" ry="{rr}" fill="{c}" stroke="{INK}" stroke-width="1.5"/>'
    b += f'<ellipse cx="{x1}" cy="{y}" rx="{rx*0.4}" ry="{r*0.4}" fill="{PAPER}" stroke="{INK}" stroke-width="1.5"/>'
    b += f'<rect x="{x0}" y="{y-r}" width="{x1-x0}" height="{2*r}" rx="6" fill="none" stroke="{INK}" stroke-width="2"/>'
    return b


def hexnut(cx, cy, w, h, fill=ASH):
    pts = f"{cx-w/2},{cy-h/2} {cx+w/2},{cy-h/2} {cx+w/2},{cy+h/2} {cx-w/2},{cy+h/2}"
    s = f'<polygon points="{pts}" fill="{fill}" stroke="{INK}" stroke-width="2"/>'
    s += f'<line x1="{cx-w/2}" y1="{cy-h/6}" x2="{cx+w/2}" y2="{cy-h/6}" stroke="{INK}" stroke-width="1"/>'
    s += f'<line x1="{cx-w/2}" y1="{cy+h/6}" x2="{cx+w/2}" y2="{cy+h/6}" stroke="{INK}" stroke-width="1"/>'
    return s


def threads(x0, x1, cy, h, step=7):
    s = f'<rect x="{x0}" y="{cy-h/2}" width="{x1-x0}" height="{h}" fill="{TINT}" stroke="{INK}" stroke-width="2"/>'
    x = x0 + 3
    while x < x1 - 2:
        s += f'<line x1="{x}" y1="{cy-h/2}" x2="{x+4}" y2="{cy+h/2}" stroke="{INK}" stroke-width="1.3"/>'
        x += step
    return s


# 1 Industrial air and water hose
svg("industrial-hose", hose(cover="#B03A2E" if False else MID) +
    f'<text x="70" y="106" font-family="Arial" font-size="13" fill="{PAPER}" font-weight="bold">AIR / WATER 300 PSI</text>',
    "Industrial air and water hose with a cut end showing tube, reinforcement, and cover")

# 2 Suction hose with helix
hel = "".join(f'<path d="M{x},66 q6,34 0,68" stroke="{LGRN}" stroke-width="4" fill="none"/>' for x in range(52, 246, 16))
svg("suction-hose", hose(extra=hel), "Suction hose with a rigid helix wire")

# 3 Steam hose
svg("steam-hose", hose(cover=INK) + f'<text x="62" y="106" font-family="Arial" font-size="13" fill="{LGRN}" font-weight="bold">STEAM 250 PSI EPDM</text>',
    "Steam hose")

# 4 Chemical hose
stripes = f'<rect x="40" y="94" width="210" height="12" fill="{GRN}"/>'
svg("chemical-hose", hose(extra=stripes, end_layers=(MID, ASH, PAPER)) +
    f'<text x="58" y="86" font-family="Arial" font-size="12" fill="{PAPER}" font-weight="bold">UHMWPE CHEMICAL</text>',
    "Chemical transfer hose with a smooth plastic tube")

# 5 Layflat discharge hose
lay = f'<path d="M30,120 C90,80 150,150 210,105 S290,95 300,100 L300,122 C280,118 250,124 210,128 C150,172 90,104 30,142 Z" fill="{GRN}" stroke="{INK}" stroke-width="2"/>'
lay += f'<path d="M30,131 C90,93 150,161 210,116 S280,108 300,111" stroke="{LGRN}" stroke-width="2" fill="none"/>'
svg("layflat-hose", lay, "Layflat discharge hose lying flat")

# 6 Hydraulic 2-wire braid hose
braid = ""
for x in range(48, 246, 12):
    braid += f'<line x1="{x}" y1="74" x2="{x+12}" y2="126" stroke="{ASH}" stroke-width="1.5"/>'
    braid += f'<line x1="{x+12}" y1="74" x2="{x}" y2="126" stroke="{ASH}" stroke-width="1.5"/>'
svg("hydraulic-braid", hose(r=26, cover=INK, extra=braid, end_layers=(INK, ASH, TINT)),
    "Two-wire braided hydraulic hose")

# 7 Hydraulic spiral hose
sp = "".join(f'<line x1="{x}" y1="70" x2="{x+22}" y2="130" stroke="{ASH}" stroke-width="2"/>' for x in range(40, 232, 7))
svg("hydraulic-spiral", hose(r=30, cover=INK, extra=sp, end_layers=(INK, ASH, TINT)),
    "Spiral-wire hydraulic hose")

# 8 Hydraulic crimp couplings
cp = f'<rect x="30" y="86" width="70" height="28" fill="{INK}"/>'
cp += f'<rect x="96" y="80" width="60" height="40" rx="3" fill="{ASH}" stroke="{INK}" stroke-width="2"/>'
cp += "".join(f'<line x1="{x}" y1="80" x2="{x}" y2="120" stroke="{INK}" stroke-width="1"/>' for x in range(104, 156, 8))
cp += hexnut(176, 100, 26, 44)
cp += threads(189, 226, 100, 24)
cp += f'<path d="M226,90 L240,96 L240,104 L226,110 Z" fill="{TINT}" stroke="{INK}" stroke-width="2"/>'
cp += f'<text x="110" y="150" font-family="Arial" font-size="12" fill="{INK}">ferrule</text><text x="160" y="150" font-family="Arial" font-size="12" fill="{INK}">swivel nut</text>'
svg("crimp-coupling", cp, "Hydraulic crimp coupling with ferrule and swivel nut on hose")

# 9 Adapters
ad = threads(50, 110, 100, 26) + hexnut(130, 100, 40, 48) + threads(150, 210, 100, 22)
ad += f'<path d="M210,92 L226,97 L226,103 L210,108 Z" fill="{TINT}" stroke="{INK}" stroke-width="2"/>'
ad += f'<circle cx="52" cy="100" r="0" /><text x="46" y="150" font-family="Arial" font-size="12" fill="{INK}">port end</text><text x="160" y="150" font-family="Arial" font-size="12" fill="{INK}">hose end</text>'
svg("adapter", ad, "Straight hydraulic adapter with two threaded ends and a hex")

# 10 Cam and groove couplings
cam = f'<rect x="40" y="76" width="90" height="48" rx="6" fill="{ASH}" stroke="{INK}" stroke-width="2"/>'
cam += f'<path d="M60,76 L52,44 L64,40 L76,76" fill="{MID}" stroke="{INK}" stroke-width="2"/>'
cam += f'<path d="M60,124 L52,156 L64,160 L76,124" fill="{MID}" stroke="{INK}" stroke-width="2"/>'
cam += f'<rect x="130" y="84" width="40" height="32" fill="{INK}"/>'
cam += f'<rect x="190" y="80" width="60" height="40" rx="4" fill="{ASH}" stroke="{INK}" stroke-width="2"/>'
cam += f'<rect x="200" y="80" width="10" height="40" fill="{MID}"/>'
cam += f'<rect x="250" y="86" width="40" height="28" fill="{INK}"/>'
cam += f'<text x="44" y="186" font-family="Arial" font-size="12" fill="{INK}">coupler (arms)</text><text x="186" y="186" font-family="Arial" font-size="12" fill="{INK}">adapter (groove)</text>'
svg("cam-groove", cam, "Cam and groove coupler with cam arms and an adapter with a groove")

# 11 Ground joint steam fitting
gj = f'<rect x="30" y="84" width="60" height="32" fill="{INK}"/>'
gj += f'<rect x="90" y="80" width="60" height="40" fill="{ASH}" stroke="{INK}" stroke-width="2"/>'
gj += f'<rect x="96" y="70" width="14" height="60" rx="3" fill="{MID}" stroke="{INK}" stroke-width="2"/>'
gj += f'<rect x="130" y="70" width="14" height="60" rx="3" fill="{MID}" stroke="{INK}" stroke-width="2"/>'
gj += f'<rect x="150" y="76" width="44" height="48" fill="{ASH}" stroke="{INK}" stroke-width="2"/>'
gj += f'<path d="M162,76 L156,40 L178,40 L182,76 Z" fill="{GRN}" stroke="{INK}" stroke-width="2"/>'
gj += f'<path d="M162,124 L156,160 L178,160 L182,124 Z" fill="{GRN}" stroke="{INK}" stroke-width="2"/>'
gj += threads(194, 250, 100, 26)
gj += f'<text x="80" y="186" font-family="Arial" font-size="12" fill="{INK}">interlocking clamp</text><text x="170" y="30" font-family="Arial" font-size="12" fill="{INK}">wing nut</text>'
svg("ground-joint", gj, "Ground joint steam fitting with wing nut and interlocking clamp")

# 12 Hose clamps and bands
cl = f'<circle cx="110" cy="100" r="52" fill="none" stroke="{ASH}" stroke-width="12"/>'
cl += f'<circle cx="110" cy="100" r="52" fill="none" stroke="{INK}" stroke-width="1.5"/>'
cl += f'<rect x="94" y="36" width="34" height="20" rx="3" fill="{MID}" stroke="{INK}" stroke-width="2"/>'
cl += f'<circle cx="230" cy="100" r="44" fill="none" stroke="{LGRN}" stroke-width="8"/>'
cl += f'<rect x="216" y="48" width="28" height="14" fill="{GRN}" stroke="{INK}" stroke-width="2"/>'
cl += f'<text x="70" y="186" font-family="Arial" font-size="12" fill="{INK}">worm gear clamp</text><text x="200" y="186" font-family="Arial" font-size="12" fill="{INK}">band</text>'
svg("clamps", cl, "Worm gear hose clamp and a preformed band")

# 13 Ring and full-face gaskets
g = f'<circle cx="90" cy="100" r="62" fill="{LGRN}" stroke="{INK}" stroke-width="2"/><circle cx="90" cy="100" r="40" fill="{PAPER}" stroke="{INK}" stroke-width="2"/>'
g += f'<circle cx="230" cy="100" r="70" fill="{ASH}" stroke="{INK}" stroke-width="2"/><circle cx="230" cy="100" r="34" fill="{PAPER}" stroke="{INK}" stroke-width="2"/>'
for k in range(8):
    a = k * math.pi / 4 + math.pi / 8
    g += f'<circle cx="{230+52*math.cos(a):.1f}" cy="{100+52*math.sin(a):.1f}" r="6" fill="{PAPER}" stroke="{INK}" stroke-width="1.5"/>'
g += f'<text x="60" y="190" font-family="Arial" font-size="12" fill="{INK}">ring (RF)</text><text x="196" y="190" font-family="Arial" font-size="12" fill="{INK}">full face (FF)</text>'
svg("gaskets", g, "Ring gasket and full-face gasket with bolt holes")

# 14 Gasket sheet
sh = f'<rect x="40" y="30" width="240" height="140" fill="{TINT}" stroke="{INK}" stroke-width="2"/>'
for cx in (90, 160, 230):
    for cy in (70, 130):
        sh += f'<circle cx="{cx}" cy="{cy}" r="26" fill="none" stroke="{GRN}" stroke-width="2" stroke-dasharray="5 3"/><circle cx="{cx}" cy="{cy}" r="14" fill="none" stroke="{GRN}" stroke-width="2" stroke-dasharray="5 3"/>'
svg("gasket-sheet", sh, "Gasket sheet with rings laid out for cutting")

# 15 O-rings and cord
o = "".join(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{INK}" stroke-width="{w}"/>' for cx, cy, r, w in ((70, 80, 34, 9), (140, 70, 22, 7), (120, 140, 16, 6)))
o += f'<path d="M190,150 C220,40 260,180 290,60" stroke="{INK}" stroke-width="14" fill="none" stroke-linecap="round"/>'
o += f'<text x="210" y="190" font-family="Arial" font-size="12" fill="{INK}">cord stock</text>'
svg("o-rings", o, "O-rings in three sizes and a length of O-ring cord")

# 16 Expansion joint / bellows
bl = f'<rect x="40" y="40" width="20" height="120" fill="{ASH}" stroke="{INK}" stroke-width="2"/><rect x="260" y="40" width="20" height="120" fill="{ASH}" stroke="{INK}" stroke-width="2"/>'
path = "M60,60 " + " ".join(f"Q{x+10},{48 if i%2==0 else 72} {x+20},60" for i, x in enumerate(range(60, 260, 20)))
bl += f'<path d="{path}" fill="none" stroke="{INK}" stroke-width="2"/>'
path2 = "M60,140 " + " ".join(f"Q{x+10},{152 if i%2==0 else 128} {x+20},140" for i, x in enumerate(range(60, 260, 20)))
bl += f'<path d="{path2}" fill="none" stroke="{INK}" stroke-width="2"/>'
bl += "".join(f'<line x1="{x}" y1="56" x2="{x}" y2="144" stroke="{MID}" stroke-width="1.5"/>' for x in range(70, 260, 20))
svg("bellows", bl, "Stainless steel bellows expansion joint between two flanges")

# 17 Stainless braided metal hose
mh = f'<rect x="30" y="50" width="16" height="100" fill="{ASH}" stroke="{INK}" stroke-width="2"/><rect x="274" y="50" width="16" height="100" fill="{ASH}" stroke="{INK}" stroke-width="2"/>'
mh += f'<rect x="46" y="74" width="228" height="52" fill="{TINT}" stroke="{INK}" stroke-width="2"/>'
for x in range(46, 274, 10):
    mh += f'<line x1="{x}" y1="74" x2="{x+10}" y2="126" stroke="{MID}" stroke-width="1.2"/><line x1="{x+10}" y1="74" x2="{x}" y2="126" stroke="{MID}" stroke-width="1.2"/>'
svg("metal-hose", mh, "Stainless steel braided metal hose with flanged ends")

# 18 Belting
bt = f'<circle cx="80" cy="100" r="40" fill="{ASH}" stroke="{INK}" stroke-width="2"/><circle cx="240" cy="100" r="30" fill="{ASH}" stroke="{INK}" stroke-width="2"/>'
bt += f'<path d="M80,54 L240,64 A36,36 0 0 1 240,136 L80,146 A46,46 0 0 1 80,54 Z" fill="none" stroke="{INK}" stroke-width="10"/>'
bt += f'<path d="M80,54 L240,64 A36,36 0 0 1 240,136 L80,146 A46,46 0 0 1 80,54 Z" fill="none" stroke="{GRN}" stroke-width="5"/>'
svg("belting", bt, "Conveyor belt running over two pulleys")

# 19 Compression packing
pk = ""
for i, r in enumerate((64, 50, 36, 22)):
    pk += f'<circle cx="110" cy="100" r="{r}" fill="none" stroke="{INK if i%2 else MID}" stroke-width="12"/>'
pk += f'<rect x="200" y="70" width="80" height="60" fill="none" stroke="{INK}" stroke-width="2"/>'
pk += "".join(f'<rect x="{200+i*20}" y="70" width="20" height="60" fill="{ASH if i%2 else MID}" stroke="{INK}" stroke-width="1"/>' for i in range(4))
pk += f'<text x="200" y="150" font-family="Arial" font-size="12" fill="{INK}">rings cut to fit</text>'
svg("packing", pk, "Coil of compression packing and cut packing rings")

# 20 Waterjet cutting
wj = f'<rect x="40" y="110" width="240" height="60" fill="{TINT}" stroke="{INK}" stroke-width="2"/>'
wj += f'<path d="M70,125 h40 v30 h-40 z M140,122 a14,14 0 1 0 0.1,0 M200,124 l30,0 l10,16 l-10,16 l-30,0 l-10,-16 z" fill="none" stroke="{GRN}" stroke-width="2" stroke-dasharray="5 3"/>'
wj += f'<rect x="146" y="30" width="28" height="44" rx="4" fill="{MID}" stroke="{INK}" stroke-width="2"/>'
wj += f'<path d="M154,74 L166,74 L162,90 L158,90 Z" fill="{INK}"/>'
wj += f'<line x1="160" y1="90" x2="160" y2="110" stroke="{GRN}" stroke-width="3"/>'
svg("waterjet", wj, "Waterjet nozzle cutting shapes from a sheet")

# 21 Hose assembly (built in our shop)
ha = f'<rect x="70" y="88" width="180" height="24" rx="4" fill="{INK}"/>'
ha += f'<rect x="40" y="82" width="34" height="36" rx="3" fill="{ASH}" stroke="{INK}" stroke-width="2"/>' + hexnut(30, 100, 18, 40)
ha += f'<rect x="246" y="82" width="34" height="36" rx="3" fill="{ASH}" stroke="{INK}" stroke-width="2"/>' + hexnut(290, 100, 18, 40)
ha += f'<rect x="130" y="118" width="60" height="22" rx="3" fill="{LGRN}" stroke="{INK}" stroke-width="1.5"/><text x="140" y="133" font-family="Arial" font-size="11" fill="{INK}">TAG</text>'
svg("hose-assembly", ha, "Finished hose assembly with fittings on both ends and an ID tag")

print("art written")
