"""Original comic-style SVG drawings for Brain Blasters puzzles.
Each drawing is an SVG fragment in a 100x100 viewBox. Outputs art.js."""
import math, json

K = '#1d1d1d'          # outline ink
SW = 3.5               # default outline width

def f(v): return ('%.1f' % v).rstrip('0').rstrip('.')

def circ(cx, cy, r, fill, sw=SW, stroke=K, extra=''):
    return f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r)}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" {extra}/>'
def ell(cx, cy, rx, ry, fill, rot=0, sw=SW, stroke=K, extra=''):
    t = f' transform="rotate({rot} {f(cx)} {f(cy)})"' if rot else ''
    return f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(rx)}" ry="{f(ry)}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{t} {extra}/>'
def path(d, fill, sw=SW, stroke=K, extra=''):
    return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" {extra}/>'
def line(d, sw=SW, stroke=K):
    return f'<path d="{d}" fill="none" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/>'
def rect(x, y, w, h, fill, rx=0, sw=SW, stroke=K, rot=None):
    t = f' transform="rotate({rot[0]} {rot[1]} {rot[2]})"' if rot else ''
    return f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" rx="{f(rx)}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{t}/>'
def poly(pts, fill, sw=SW, stroke=K):
    return f'<polygon points="{" ".join(f(x)+","+f(y) for x,y in pts)}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
def blob(circles, fill, sw=SW):
    """Union of circles: outlines first, then fills on top, so inner overlaps vanish."""
    return ''.join(circ(x, y, r, fill, sw) for x, y, r in circles) + ''.join(circ(x, y, r - sw/2, fill, 0, 'none') for x, y, r in circles)
def hi(cx, cy, rx, ry, rot=-25, op=0.55):
    return ell(cx, cy, rx, ry, '#fff', rot, 0, 'none', f'opacity="{op}"')
def star_pts(cx, cy, R, r, n=5, start=-90):
    return [(cx + (R if i % 2 == 0 else r) * math.cos(math.radians(start + i * 180 / n)),
             cy + (R if i % 2 == 0 else r) * math.sin(math.radians(start + i * 180 / n))) for i in range(2 * n)]
def eye(cx, cy, r=4): return circ(cx, cy, r, K, 0, 'none') + circ(cx + r*0.35, cy - r*0.35, r*0.35, '#fff', 0, 'none')

A = {}   # emoji -> (name, svg fragment)

# ---------------- counting objects ----------------
A['🍎'] = ('apple', line('M50 31 Q49 18 55 9', 5, '#6B3E1F') +
          path('M50 31 C36 18 12 25 14 52 C16 78 34 93 50 86 C66 93 84 78 86 52 C88 25 64 18 50 31 Z', '#E63946') +
          path('M53 21 Q66 7 78 14 Q67 27 53 21 Z', '#2BB673') + hi(30, 46, 5, 10))
A['⭐'] = ('star', poly(star_pts(50, 53, 45, 19), '#FFD93D') + hi(38, 42, 4, 8))
A['🐞'] = ('ladybug', line('M44 20 Q38 8 30 8', 3) + line('M56 20 Q62 8 70 8', 3) + circ(30, 8, 3, K, 0) + circ(70, 8, 3, K, 0) +
          circ(50, 28, 15, '#2b2b2b') + circ(50, 58, 32, '#E63946') + line('M50 27 L50 90', 3.5) +
          circ(37, 49, 6, K, 0) + circ(63, 49, 6, K, 0) + circ(35, 71, 6, K, 0) + circ(65, 71, 6, K, 0) +
          circ(44, 24, 3, '#fff', 0) + circ(56, 24, 3, '#fff', 0) + hi(30, 44, 4, 8))
A['🍪'] = ('cookie', circ(50, 50, 40, '#D9A15B') + circ(50, 50, 33, '#E2AE6C', 0, 'none') +
          ''.join(circ(x, y, r, '#5A3418', 0) for x, y, r in [(36,34,5),(60,30,4.5),(70,52,5),(46,54,5),(30,62,4),(56,72,5),(40,78,3.5),(66,68,3),(52,40,3)]))
A['🚀'] = ('rocket', path('M33 54 L18 78 L34 73 Z', '#E63946') + path('M67 54 L82 78 L66 73 Z', '#E63946') +
          path('M42 78 Q50 100 58 78 Z', '#FF8C42') + path('M46 78 Q50 91 54 78 Z', '#FFD93D', 0, 'none') +
          rect(38, 70, 24, 8, '#8A96A3', 2) +
          path('M50 7 C67 21 70 45 67 71 L33 71 C30 45 33 21 50 7 Z', '#EEF1F6') +
          path('M50 7 C57 13 61 19 63 26 L37 26 C39 19 43 13 50 7 Z', '#E63946') +
          circ(50, 43, 9, '#5CC8FF') + hi(47, 40, 2.5, 4) + line('M50 71 L50 60', 3, '#c6ccd4'))
A['🐟'] = ('fish', path('M74 50 L94 31 L89 50 L94 69 Z', '#FF8C42') +
          path('M46 30 Q56 16 66 33 Z', '#FF8C42') +
          path('M14 50 C26 27 62 22 78 50 C62 78 26 73 14 50 Z', '#FFA94D') +
          line('M54 34 Q60 50 54 66', 3) + circ(29, 46, 6, '#fff', 3) + circ(28, 46, 3, K, 0) + line('M15 53 Q19 55 22 53', 2.5) + hi(42, 40, 3, 7, 70))
A['🍩'] = ('donut', circ(50, 52, 40, '#E2AE6C') +
          path('M50 16 C66 14 80 26 84 42 C86 52 80 56 78 62 C74 74 62 82 50 82 C38 84 24 74 20 60 C16 48 20 34 30 24 C36 18 44 16 50 16 Z', '#FF7EB6') +
          circ(50, 50, 12, '#fff') +
          ''.join(rect(x, y, 9, 3.5, c, 1.5, 0, 'none', (a, x+4.5, y+1.75)) for x, y, c, a in
                  [(30,32,'#2F80ED',30),(58,26,'#FFD93D',-20),(70,44,'#2BB673',60),(34,62,'#FFD93D',-40),(60,66,'#2F80ED',20),(40,22,'#2BB673',80),(24,46,'#fff',10),(66,58,'#fff',-60)]))
A['⚽'] = ('soccer ball', '<clipPath id="bbclip"><circle cx="50" cy="50" r="39"/></clipPath>' + circ(50, 50, 40, '#fff') +
          '<g clip-path="url(#bbclip)">' +
          poly([(50 + 13*math.cos(math.radians(-90+72*i)), 50 + 13*math.sin(math.radians(-90+72*i))) for i in range(5)], '#222', 2) +
          ''.join(line(f'M{f(50+13*math.cos(math.radians(-90+72*i)))} {f(50+13*math.sin(math.radians(-90+72*i)))} L{f(50+30*math.cos(math.radians(-90+72*i)))} {f(50+30*math.sin(math.radians(-90+72*i)))}', 2.5) for i in range(5)) +
          ''.join(poly([(50+42*math.cos(math.radians(-90+72*i)) + 12*math.cos(math.radians(-90+72*i+72*j)), 50+42*math.sin(math.radians(-90+72*i)) + 12*math.sin(math.radians(-90+72*i+72*j))) for j in range(5)], '#222', 2) for i in range(5)) +
          '</g>' + circ(50, 50, 40, 'none'))
A['🎈'] = ('balloon', line('M50 78 Q41 87 52 97', 2.5) + path('M45 79 L55 79 L50 72 Z', '#E63946', 2.5) +
          ell(50, 42, 28, 33, '#E63946') + hi(38, 30, 5, 10))
A['🍓'] = ('strawberry', path('M50 91 C30 82 15 58 19 41 C23 28 40 26 50 31 C60 26 77 28 81 41 C85 58 70 82 50 91 Z', '#E63946') +
          ''.join(ell(x, y, 1.8, 2.8, '#FFE066', 0, 0, 'none') for x, y in [(34,44),(50,42),(66,44),(28,58),(42,56),(58,56),(72,58),(36,70),(50,70),(64,70),(44,82),(56,82)]) +
          path('M28 31 L41 27 L36 15 L50 22 L64 15 L59 27 L72 31 L57 35 L50 30 L43 35 Z', '#2BB673', 3) + line('M50 22 L52 10', 4, '#2E7D32'))

# ---------------- word-puzzle batch 1 ----------------
def handshape(skin, cuff=None):
    s = ''
    for x, top in [(30, 18), (40.5, 11), (51, 13), (61.5, 21)]:
        s += rect(x, top, 10, 50 - top, skin, 5)
    s += line('M33 68 L15 46', 16, K) + line('M33 68 L15 46', 9, skin)
    s += rect(28, 40, 44, 40, skin, 14)
    s += rect(30.5, 42, 39, 18, skin, 0, 0, 'none')
    if cuff: s += rect(28, 74, 44, 18, cuff, 5)
    return s
A['🧤'] = ('glove', handshape('#7E57C2', '#5E35B1') + line('M32 80 H68 M32 86 H68', 2.5, '#B39DDB'))
A['✋'] = ('hand', handshape('#F5C9A0') + line('M38 66 Q50 72 62 66', 2.5, '#C98F5E'))
A['🥕'] = ('carrot', path('M70 30 Q66 12 74 4 Q80 18 76 31 Z', '#2BB673', 3) + path('M74 33 Q86 14 96 18 Q88 32 78 38 Z', '#2BB673', 3) +
          path('M76 36 Q92 34 96 44 Q84 46 76 42 Z', '#2BB673', 3) +
          path('M58 24 Q78 30 82 46 Q60 76 16 92 Q32 52 58 24 Z', '#FF8C42') +
          line('M46 46 L54 50 M38 60 L46 64 M30 74 L37 77 M58 38 L66 42', 2.5, '#C4621A'))
A['🐄'] = ('cow', path('M31 27 Q22 13 30 8 Q33 18 39 24 Z', '#F3E3B5', 3) + path('M69 27 Q78 13 70 8 Q67 18 61 24 Z', '#F3E3B5', 3) +
          ell(22, 38, 13, 7, '#fff', -20) + ell(78, 38, 13, 7, '#fff', 20) + ell(23, 38, 7, 3.5, '#F7B6C2', -20, 0) + ell(77, 38, 7, 3.5, '#F7B6C2', 20, 0) +
          ell(50, 48, 27, 30, '#fff') + path('M30 30 Q40 22 48 30 Q46 44 34 44 Q26 40 30 30 Z', '#2b2b2b', 0) + path('M64 50 Q76 48 76 60 Q68 64 62 58 Z', '#2b2b2b', 0) +
          ell(50, 70, 22, 15, '#F7B6C2') + ell(43, 70, 3.5, 4.5, '#8a4a5a', 0, 0) + ell(57, 70, 3.5, 4.5, '#8a4a5a', 0, 0) +
          eye(40, 47) + eye(60, 47))
A['🌳'] = ('tree', rect(43, 56, 14, 36, '#8B5A2B', 3) + line('M50 92 L50 80', 0) +
          blob([(50, 32, 24), (30, 46, 17), (70, 46, 17), (50, 54, 16)], '#2BB673') +
          circ(40, 30, 5, '#5ccf88', 0, 'none') + circ(60, 42, 4, '#5ccf88', 0, 'none'))
A['🐝'] = ('bee', ell(40, 33, 12, 17, '#DDF3FF', -25) + ell(58, 31, 12, 17, '#DDF3FF', 20) +
          '<clipPath id="beeclip"><ellipse cx="54" cy="58" rx="27" ry="20"/></clipPath>' +
          ell(54, 58, 28, 21, '#FFD93D') + f'<g clip-path="url(#beeclip)">{rect(45,30,8,60,"#2b2b2b",0,0,"none")}{rect(60,30,8,60,"#2b2b2b",0,0,"none")}</g>' +
          ell(54, 58, 28, 21, 'none') + path('M81 56 L92 58 L81 62 Z', '#2b2b2b', 2) +
          circ(25, 56, 13, '#2b2b2b') + line('M22 45 Q18 34 12 32', 2.5) + line('M28 44 Q30 32 26 26', 2.5) +
          circ(20, 54, 3.5, '#fff', 0) + circ(19.5, 54.5, 1.8, K, 0))
A['🐶'] = ('dog', path('M30 26 Q10 30 14 62 Q24 68 32 52 Z', '#8B5A2B') + path('M70 26 Q90 30 86 62 Q76 68 68 52 Z', '#8B5A2B') +
          ell(50, 50, 26, 29, '#D9A15B') + ell(50, 66, 15, 11, '#F3D9B1') + ell(50, 59, 6.5, 4.5, K, 0, 0) +
          line('M50 63 L50 68 M43 70 Q50 75 57 70', 3) + eye(41, 46) + eye(59, 46) + path('M48 72 Q50 80 53 72 Z', '#FF7E9B', 2))
A['🥚'] = ('egg', path('M50 11 C70 11 83 44 83 62 C83 81 68 92 50 92 C32 92 17 81 17 62 C17 44 30 11 50 11 Z', '#FFF6E0') + hi(36, 38, 5, 11, -20))
A['🚗'] = ('car', path('M10 67 L10 53 Q12 46 22 45 L31 45 L40 31 Q42 28 46 28 L68 28 Q72 28 74 32 L82 45 Q92 47 92 55 L92 67 Z', '#E63946') +
          path('M41 43 L47 33 L57 33 L57 43 Z', '#CDEFFF', 3) + path('M61 33 L70 33 L76 43 L61 43 Z', '#CDEFFF', 3) +
          circ(28, 68, 10, '#333') + circ(28, 68, 4, '#ccc', 2) + circ(74, 68, 10, '#333') + circ(74, 68, 4, '#ccc', 2) +
          ell(88, 53, 3, 3, '#FFE066', 0, 2) + line('M58 48 L62 48', 3))
A['🦋'] = ('butterfly', ell(31, 35, 21, 16, '#FF8C42', -30) + ell(69, 35, 21, 16, '#FF8C42', 30) +
          ell(35, 65, 14, 12, '#FFD93D', 25) + ell(65, 65, 14, 12, '#FFD93D', -25) +
          circ(27, 32, 4.5, '#fff', 2) + circ(73, 32, 4.5, '#fff', 2) + circ(34, 66, 3.5, '#E63946', 0) + circ(66, 66, 3.5, '#E63946', 0) +
          line('M48 30 Q42 15 35 12', 2.5) + line('M52 30 Q58 15 65 12', 2.5) + circ(35, 12, 2.5, K, 0) + circ(65, 12, 2.5, K, 0) +
          ell(50, 52, 5, 25, '#3a3a3a'))
A['🥛'] = ('milk carton', poly([(62, 36), (80, 30), (80, 86), (62, 92)], '#D6EBFA') + poly([(62, 36), (44, 18), (62, 12), (80, 30)], '#1E5FB8') +
          rect(22, 36, 40, 56, '#fff') + path('M22 36 L44 18 L62 36 Z', '#2F80ED') + rect(38, 8, 12, 8, '#E63946', 2, 2.5) +
          '<text x="42" y="66" font-family="Bangers, Impact, sans-serif" font-size="16" text-anchor="middle" fill="#2F80ED" stroke="none">MILK</text>' +
          path('M28 76 Q34 70 40 76 Q36 84 30 82 Z', '#2b2b2b', 0) + path('M46 74 Q54 72 56 80 Q50 86 46 80 Z', '#2b2b2b', 0))
A['🐱'] = ('cat', path('M24 46 L26 14 L46 32 Z', '#FF9F43') + path('M76 46 L74 14 L54 32 Z', '#FF9F43') +
          path('M29 36 L30 22 L39 31 Z', '#F7B6C2', 0) + path('M71 36 L70 22 L61 31 Z', '#F7B6C2', 0) +
          ell(50, 57, 29, 25, '#FF9F43') + line('M44 36 L44 44 M50 34 L50 43 M56 36 L56 44', 3, '#D9731F') +
          ell(40, 53, 3.5, 5.5, K, 0, 0) + ell(60, 53, 3.5, 5.5, K, 0, 0) + path('M46 61 L54 61 L50 65 Z', '#FF7E9B', 2) +
          line('M50 65 Q46 71 41 68 M50 65 Q54 71 59 68', 2.5) +
          line('M36 63 L14 59 M36 67 L15 70 M64 63 L86 59 M64 67 L85 70', 2))
A['🍌'] = ('banana', path('M23 21 C20 60 50 87 88 77 C60 73 36 55 35 23 Z', '#FFD93D') +
          path('M23 21 L23 12 L33 13 L35 23 Z', '#8B5A2B', 3) + path('M84 76 L90 77 L88 80 Z', '#5A3418', 2) +
          line('M30 30 C30 56 50 74 76 77', 2.5, '#E0A800'))
A['🐔'] = ('chicken', line('M46 80 L44 93 M38 94 L50 94 M60 80 L62 93 M56 94 L68 94', 3.5, '#E07A16') +
          path('M76 50 Q93 34 92 56 Q88 68 76 66 Z', '#fff') + ell(54, 60, 28, 23, '#fff') +
          path('M44 58 Q56 74 70 60', 'none') + circ(31, 37, 13, '#fff') +
          path('M22 27 Q23 16 30 22 Q32 12 38 22 Q43 18 42 28 Z', '#E63946', 2.5) +
          path('M18 36 L7 40 L18 43 Z', '#FF8C42', 2.5) + path('M19 44 Q16 52 21 54 Q25 50 23 44 Z', '#E63946', 2) + eye(29, 34, 2.8))
A['🐛'] = ('caterpillar', ''.join(line(f'M{x} 66 L{x-2} 74', 3) for x in (22, 36, 50, 64)) +
          ''.join(circ(x, y, 12.5, '#8BD17C') for x, y in [(20,58),(34,54),(48,58),(62,54)]) +
          circ(78, 46, 15, '#2BB673') + line('M72 33 Q68 22 62 20 M84 33 Q88 22 94 20', 2.5) + circ(62, 20, 2.5, K, 0) + circ(94, 20, 2.5, K, 0) +
          eye(73, 44, 3) + eye(84, 44, 3) + line('M73 52 Q79 57 85 52', 2.5))
A['🧊'] = ('ice cube', poly([(50,14),(84,30),(50,46),(16,30)], '#EAF8FF') + poly([(16,30),(50,46),(50,86),(16,70)], '#BFE8FF') +
          poly([(50,46),(84,30),(84,70),(50,86)], '#94D3F7') + line('M24 40 L24 56 M60 36 L74 30', 3, '#fff'))
A['🔨'] = ('hammer', rect(43, 34, 14, 58, '#C68642', 5) + line('M50 44 L50 84', 2.5, '#A86A2F') +
          path('M24 18 L64 18 L80 9 L86 16 L72 27 L86 38 L80 45 L64 36 L24 36 Z', '#9AA5B1') +
          rect(12, 14, 14, 26, '#7D8893', 3) + line('M30 22 L60 22', 3, '#c8d0d8'))
A['🧦'] = ('sock', '<clipPath id="sockclip"><path d="M36 10 H64 V58 L82 70 Q94 78 86 88 Q80 95 70 90 L42 76 Q34 70 36 60 Z"/></clipPath>' +
          path('M36 10 H64 V58 L82 70 Q94 78 86 88 Q80 95 70 90 L42 76 Q34 70 36 60 Z', '#2F80ED') +
          f'<g clip-path="url(#sockclip)">{rect(30,8,40,14,"#fff",0,0,"none")}{line("M30 15 L70 15",3,"#E63946")}{circ(86,86,14,"#E63946",0,"none")}{circ(36,72,12,"#E63946",0,"none")}</g>' +
          path('M36 10 H64 V58 L82 70 Q94 78 86 88 Q80 95 70 90 L42 76 Q34 70 36 60 Z', 'none') + line('M36 22 L64 22', 3))
A['✈️'] = ('airplane', path('M42 46 L53 46 L41 13 L32 13 Z', '#5CC8FF') + path('M42 54 L53 54 L41 87 L32 87 Z', '#5CC8FF') +
          path('M16 46 L25 46 L19 31 L12 31 Z', '#5CC8FF') + path('M16 54 L25 54 L19 69 L12 69 Z', '#5CC8FF') +
          path('M9 50 Q9 44 18 44 L79 44 Q93 46 93 50 Q93 54 79 56 L18 56 Q9 56 9 50 Z', '#F2F4F7') + path('M82 46 Q90 48 90 50 Q90 52 82 54 Z', '#2F80ED', 0))
A['✂️'] = ('scissors', path('M56 52 L28 9 L35 5 L50 56 Z', '#C9D3DD') + path('M44 52 L72 9 L65 5 L50 56 Z', '#DCE3EA') +
          line('M50 54 L39 67 M50 54 L61 67', 6, '#E63946') + circ(35, 77, 11, 'none', 6, '#E63946') + circ(65, 77, 11, 'none', 6, '#E63946') +
          circ(50, 52, 4, '#555', 2))
A['🌽'] = ('corn', '<clipPath id="cornclip"><path d="M50 9 C66 13 68 60 59 86 L41 86 C32 60 34 13 50 9 Z"/></clipPath>' +
          path('M50 9 C66 13 68 60 59 86 L41 86 C32 60 34 13 50 9 Z', '#FFD93D') +
          '<g clip-path="url(#cornclip)">' + ''.join(line(f'M30 {y} L70 {y}', 2, '#E0A800') for y in range(20, 86, 9)) +
          ''.join(line(f'M{x} 5 L{x} 90', 2, '#E0A800') for x in (43, 50, 57)) + '</g>' +
          path('M43 92 Q20 62 29 30 Q38 58 51 88 Z', '#2BB673') + path('M57 92 Q80 62 71 30 Q62 58 49 88 Z', '#3CC47F'))
A['🔥'] = ('fire', path('M50 8 C60 26 80 36 78 62 C76 82 62 92 50 92 C38 92 24 82 22 62 C20 46 32 38 36 24 C42 34 44 40 48 44 C50 30 46 20 50 8 Z', '#FF8C42') +
          path('M50 46 C58 55 66 61 64 75 C62 86 56 90 50 90 C44 90 38 86 36 75 C34 63 44 58 50 46 Z', '#FFD93D', 2.5))
A['🦆'] = ('duck', line('M8 84 Q16 80 24 84 Q32 88 40 84 Q48 80 56 84 Q64 88 72 84 Q80 80 92 84', 3, '#2F80ED') +
          path('M24 60 Q26 44 50 46 Q74 44 86 52 L95 45 Q93 62 82 70 Q62 82 40 78 Q22 74 24 60 Z', '#B98B5E') +
          path('M44 56 Q64 50 78 60 Q64 70 46 64 Z', '#8B6340', 3) + line('M24 49 Q31 53 38 49', 4, '#fff') +
          circ(31, 36, 13, '#2E8B57') + path('M19 37 L5 40 Q5 46 19 44 Z', '#FF8C42', 3) + eye(28, 33, 2.8))
A['🐰'] = ('rabbit', ell(38, 25, 8.5, 22, '#F4F4F4', -8) + ell(62, 25, 8.5, 22, '#F4F4F4', 8) +
          ell(38, 26, 4, 15, '#F7B6C2', -8, 0) + ell(62, 26, 4, 15, '#F7B6C2', 8, 0) +
          circ(50, 62, 27, '#F4F4F4') + eye(40, 57, 3.8) + eye(60, 57, 3.8) +
          path('M46 66 L54 66 L50 70 Z', '#FF7E9B', 2) + line('M50 70 L50 74 M44 77 Q50 80 56 77', 2.5) +
          rect(46, 74, 8, 7, '#fff', 1.5, 2) + line('M36 69 L18 66 M36 73 L19 76 M64 69 L82 66 M64 73 L81 76', 2))
A['☀️'] = ('sun', ''.join(line(f'M{f(50+28*math.cos(math.radians(a)))} {f(50+28*math.sin(math.radians(a)))} L{f(50+43*math.cos(math.radians(a)))} {f(50+43*math.sin(math.radians(a)))}', 7, '#FFB800') for a in range(0, 360, 45)) +
          circ(50, 50, 21, '#FFD93D') + hi(43, 43, 4, 7))
A['🕶️'] = ('sunglasses', line('M12 43 L4 36 M88 43 L96 36', 3.5) +
          path('M11 40 H44 Q47 40 45 54 Q41 67 28 67 Q15 67 12 54 Q10 40 11 40 Z', '#262626') +
          path('M56 40 H89 Q90 40 88 54 Q85 67 72 67 Q59 67 55 54 Q53 40 56 40 Z', '#262626') +
          line('M44 44 Q50 38 56 44', 3.5) + line('M20 47 L28 55 M65 47 L73 55', 3, '#888'))
A['🔦'] = ('flashlight', poly([(72, 30), (97, 14), (97, 86), (72, 70)], '#FFF6A0', 0, 'none') +
          rect(8, 40, 46, 20, '#2F80ED', 4) + rect(26, 36, 10, 5, '#E63946', 2, 2.5) + path('M54 34 L70 28 L70 72 L54 66 Z', '#9AA5B1') +
          ell(70, 50, 4, 22, '#FFF6A0', 0, 3))
A['🌊'] = ('ocean waves', path('M6 52 Q20 34 34 52 Q48 70 62 52 Q76 34 94 52 L94 92 L6 92 Z', '#2F80ED') +
          path('M6 70 Q20 58 34 70 Q48 82 62 70 Q76 58 94 70 L94 92 L6 92 Z', '#5CC8FF') +
          line('M14 44 Q20 40 26 44 M70 44 Q76 40 82 44', 3, '#fff'))
A['🧸'] = ('teddy bear', circ(33, 19, 8, '#C68642') + circ(67, 19, 8, '#C68642') + circ(33, 19, 3.5, '#E8B98A', 0) + circ(67, 19, 3.5, '#E8B98A', 0) +
          ell(50, 72, 23, 21, '#C68642') + ell(50, 74, 12, 11, '#E8B98A', 0, 0) +
          ell(27, 66, 8, 11, '#C68642', 30) + ell(73, 66, 8, 11, '#C68642', -30) + ell(37, 91, 9, 6, '#C68642') + ell(63, 91, 9, 6, '#C68642') +
          circ(50, 36, 21, '#C68642') + ell(50, 43, 10, 7.5, '#E8B98A') + ell(50, 40, 4, 3, K, 0, 0) + line('M50 43 L50 47', 2.5) + eye(42, 32, 3) + eye(58, 32, 3))
A['🚲'] = ('bicycle', circ(26, 64, 18, 'none', 4.5, '#333') + circ(74, 64, 18, 'none', 4.5, '#333') + circ(26, 64, 3, '#333', 0) + circ(74, 64, 3, '#333', 0) +
          line('M26 64 L48 64 L40 38 Z M40 38 L66 38 M48 64 L66 38 L74 64', 5, '#E63946') +
          line('M66 38 L63 28 L73 27', 4, '#333') + rect(33, 33, 14, 5, '#333', 2, 0) + circ(48, 64, 5, '#555', 2))
A['🐦'] = ('bird', line('M48 74 L46 84 M58 74 L60 84', 3, '#E07A16') + path('M74 52 L94 44 L89 61 Z', '#2F80ED') +
          ell(52, 56, 26, 20, '#2F80ED') + ell(50, 63, 16, 10, '#BFE3FF', 0, 0) +
          circ(30, 42, 14, '#2F80ED') + path('M17 42 L5 46 L17 49 Z', '#FF8C42', 2.5) +
          path('M44 50 Q60 44 72 54 Q60 64 46 58 Z', '#1E5FB8', 2.5) + eye(27, 39, 3))
A['🐒'] = ('monkey', circ(20, 50, 11, '#8B5A2B') + circ(80, 50, 11, '#8B5A2B') + circ(20, 50, 6, '#F3D9B1', 0) + circ(80, 50, 6, '#F3D9B1', 0) +
          circ(50, 50, 29, '#8B5A2B') +
          ell(41, 45, 12, 12, '#F3D9B1', 0, 0) + ell(59, 45, 12, 12, '#F3D9B1', 0, 0) + ell(50, 63, 19, 14, '#F3D9B1', 0, 0) +
          eye(42, 45) + eye(58, 45) + ell(46, 59, 1.8, 2.5, K, 0, 0) + ell(54, 59, 1.8, 2.5, K, 0, 0) + line('M41 67 Q50 75 59 67', 3))
A['🌻'] = ('sunflower', line('M50 60 L50 96', 6, '#2E8B57') + path('M50 82 Q32 70 24 80 Q36 90 50 86 Z', '#2BB673', 3) +
          ''.join(ell(50 + 23*math.cos(math.radians(a)), 38 + 23*math.sin(math.radians(a)), 6.5, 13, '#FFD93D', a + 90, 3) for a in range(0, 360, 30)) +
          circ(50, 38, 15, '#8B5A2B') + ''.join(circ(50 + dx, 38 + dy, 1.8, '#5A3418', 0) for dx, dy in [(-6,-5),(0,-7),(6,-5),(-7,1),(0,0),(7,1),(-4,7),(4,7)]))
A['🌙'] = ('moon', path('M60 14 A36 36 0 1 0 60 86 A44 44 0 0 1 60 14 Z', '#FFE066') + circ(36, 40, 4, '#F5CF3D', 0) + circ(34, 62, 3, '#F5CF3D', 0))
A['🦉'] = ('owl', path('M26 28 L28 8 L42 20 Z', '#8B5A2B') + path('M74 28 L72 8 L58 20 Z', '#8B5A2B') +
          path('M50 14 C74 14 84 40 82 62 C80 84 66 92 50 92 C34 92 20 84 18 62 C16 40 26 14 50 14 Z', '#8B5A2B') +
          ell(50, 68, 20, 20, '#D9A15B', 0, 0) + line('M42 62 L45 66 L48 62 M52 62 L55 66 L58 62 M45 74 L48 78 L51 74 M53 74 L56 78 L59 74', 2, '#8B5A2B') +
          circ(37, 40, 12, '#fff') + circ(63, 40, 12, '#fff') + circ(38, 41, 6, K, 0) + circ(62, 41, 6, K, 0) + circ(40, 39, 2, '#fff', 0) + circ(64, 39, 2, '#fff', 0) +
          path('M45 50 L55 50 L50 58 Z', '#FF8C42', 2.5) + line('M40 92 L40 96 M46 92 L46 96 M54 92 L54 96 M60 92 L60 96', 3, '#E07A16'))
A['🥦'] = ('broccoli', path('M42 93 L46 56 L54 56 L58 93 Z', '#A8D672') + line('M50 70 L42 60 M50 66 L58 58', 3, '#7FB24C') +
          blob([(32, 44, 16), (50, 33, 18), (68, 44, 16), (50, 52, 13)], '#2E8B57') +
          ''.join(circ(x, y, 3, '#25744a', 0) for x, y in [(30,40),(44,30),(56,28),(66,40),(48,46),(38,52),(62,52),(54,38)]))
A['🦈'] = ('shark', path('M18 52 L4 34 L10 52 L4 70 Z', '#8FA3B5') +
          path('M14 52 Q30 36 60 38 L66 20 L77 40 Q90 44 96 54 Q90 62 74 64 L62 66 L56 77 L50 66 Q30 68 14 52 Z', '#8FA3B5') +
          path('M30 58 Q50 66 74 64 Q88 62 94 56 Q86 62 70 60 Q50 60 30 58 Z', '#E8EEF3', 0) +
          eye(84, 48, 2.8) + line('M66 46 Q68 52 66 58 M71 46 Q73 52 71 58', 2.5) + line('M82 59 Q88 60 93 56', 2.5))
A['🏀'] = ('basketball', circ(50, 50, 40, '#FF8C42') + line('M50 10 V90 M10 50 H90 M23 21 Q40 50 23 79 M77 21 Q60 50 77 79', 3) + hi(34, 30, 4, 8))
A['🌸'] = ('flower', blob([(50 + 19*math.cos(math.radians(a)), 50 + 19*math.sin(math.radians(a)), 15) for a in range(-90, 270, 72)], '#FFB7D5') +
          ''.join(line(f'M50 50 L{f(50+14*math.cos(math.radians(a)))} {f(50+14*math.sin(math.radians(a)))}', 2, '#F38BB8') for a in range(-90, 270, 72)) +
          circ(50, 50, 8, '#FFD93D', 3))
A['🦶'] = ('foot', path('M40 90 C24 88 22 66 28 52 C34 38 30 30 40 27 C56 23 66 33 64 50 C62 64 66 74 62 84 C58 92 50 92 40 90 Z', '#F5C9A0') +
          ell(36, 17, 7.5, 8.5, '#F5C9A0') + circ(49, 12, 5.5, '#F5C9A0') + circ(58.5, 14, 4.8, '#F5C9A0') + circ(65.5, 19.5, 4.2, '#F5C9A0') + circ(70.5, 26.5, 3.6, '#F5C9A0'))
A['🌧️'] = ('rain cloud', ''.join(path(f'M{x} {y-9} Q{x+6} {y} {x} {y+6} Q{x-6} {y} {x} {y-9} Z', '#2F80ED', 2.5) for x, y in [(32,74),(50,84),(68,74)]) +
          blob([(32, 42, 15), (52, 34, 20), (70, 44, 14), (48, 50, 12)], '#B8C4D6'))
A['☂️'] = ('umbrella', line('M50 50 V83 Q50 93 41 91 Q35 89 37 83', 5, '#333') + line('M50 13 L50 6', 4, '#333') +
          path('M10 50 Q14 14 50 12 Q86 14 90 50 Q80 42 70 50 Q60 42 50 50 Q40 42 30 50 Q20 42 10 50 Z', '#E63946') +
          line('M50 13 Q40 26 30 50 M50 13 Q60 26 70 50 M50 13 L50 50', 2.5, '#A61E2A'))
A['🧣'] = ('scarf', path('M58 46 L76 88 L60 94 L46 50 Z', '#E63946') +
          line('M52 62 L66 56 M57 74 L71 68', 4, '#fff') + line('M62 94 L63 99 M66 93 L68 98 M70 91 L72 96 M74 89 L76 94', 2.5) +
          path('M18 30 Q50 46 82 30 L82 45 Q50 60 18 45 Z', '#E63946') + line('M30 40 L30 52 M70 40 L70 52', 4, '#fff'))
A['🐷'] = ('pig', path('M26 32 L22 12 L42 24 Z', '#F48FA6') + path('M74 32 L78 12 L58 24 Z', '#F48FA6') +
          circ(50, 54, 31, '#F7A8B8') + ell(50, 63, 15, 11, '#F48FA6') + ell(45, 63, 2.8, 4, '#a0485e', 0, 0) + ell(55, 63, 2.8, 4, '#a0485e', 0, 0) +
          eye(38, 47, 3.5) + eye(62, 47, 3.5) + line('M44 79 Q50 82 56 79', 2.5))
A['🚂'] = ('train', circ(24, 16, 6, '#d6d6d6', 2.5) + circ(34, 9, 5, '#e4e4e4', 2.5) +
          rect(21, 24, 12, 22, '#333', 2) + rect(18, 22, 18, 5, '#333', 2) +
          rect(52, 28, 32, 42, '#E63946', 3) + rect(58, 34, 20, 14, '#CDEFFF', 2, 3) + rect(48, 24, 40, 6, '#333', 2) +
          rect(14, 44, 42, 26, '#2F80ED', 7) + path('M14 66 L4 80 L14 80 Z', '#9AA5B1', 3) + rect(10, 66, 76, 8, '#555', 2) +
          circ(26, 80, 9, '#333') + circ(46, 80, 9, '#333') + circ(70, 78, 11, '#333') + circ(26, 80, 3, '#ccc', 0) + circ(46, 80, 3, '#ccc', 0) + circ(70, 78, 4, '#ccc', 0))

exec(open(__import__('os').path.join(__import__('os').path.dirname(__file__), 'art2.py')).read())
A.update(B2)
BATCH2 = list(B2.keys())
exec(open(__import__('os').path.join(__import__('os').path.dirname(__file__), 'art3.py')).read())
A.update(B3)
BATCH3 = list(B3.keys())

COUNT = ['🍎', '⭐', '🐞', '🍪', '🚀', '🐟', '🍩', '⚽', '🎈', '🍓']
BATCH1 = [e for e in A if e not in ('⭐', '🍪', '🚀', '🍩', '🍓') and e not in B2 and e not in B3]

if __name__ == '__main__':
    import sys
    art = {e: A[e][1] for e in A}
    names = {e: A[e][0] for e in A}
    js = ('/* Original SVG drawings (100x100). LIVE = drawings switched on in the puzzles; others fall back to emoji. */\n'
          f'const ART={json.dumps(art, ensure_ascii=False)};\n'
          f'const ARTNAME={json.dumps(names, ensure_ascii=False)};\n')
    open(sys.argv[1], 'w').write(js)
    json.dump({'count': COUNT, 'batch1': BATCH1, 'batch2': BATCH2, 'batch3': BATCH3, 'names': names, 'art': art}, open(sys.argv[2], 'w'), ensure_ascii=False)
    print(len(A), 'drawings;', len(BATCH1), 'in batch 1;', len(js), 'bytes')
