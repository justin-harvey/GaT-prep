# Batch 2 drawings. Imported by art.py after batch 1 (uses its helpers and dict A).

def outlined(d, w, color):
    """A thick stroked path with an ink outline (tentacles, necks, trunks)."""
    return line(d, w + 6, K) + line(d, w, color)

B2 = {}
B2['⌚'] = ('wristwatch', rect(39, 4, 22, 92, '#8B5A2B', 6) + line('M44 14 L56 14 M44 86 L56 86', 2.5, '#5A3418') +
            rect(69, 45, 6, 10, '#C9D3DD', 2, 2.5) + circ(50, 50, 22, '#FFD93D') + circ(50, 50, 17, '#fff', 2.5) +
            line('M50 50 L50 39 M50 50 L58 55', 3.5) + circ(50, 50, 2.5, K, 0))
B2['⏰'] = ('alarm clock', line('M30 82 L24 92 M70 82 L76 92', 5) + circ(25, 22, 11, '#FFD93D') + circ(75, 22, 11, '#FFD93D') +
            line('M50 22 L50 14', 4) + circ(50, 12, 4, '#FFD93D', 2.5) + circ(50, 55, 33, '#E63946') + circ(50, 55, 25, '#fff', 2.5) +
            line('M50 33 L50 37 M72 55 L68 55 M50 77 L50 73 M28 55 L32 55', 3) + line('M50 55 L50 41 M50 55 L62 61', 4) + circ(50, 55, 3, K, 0))
B2['☁️'] = ('cloud', blob([(30, 58, 17), (50, 46, 23), (72, 58, 17), (52, 64, 15)], '#F2F6FA'))
B2['☕'] = ('hot drink', line('M36 28 Q31 20 36 12 M50 26 Q45 17 50 7 M64 28 Q59 20 64 12', 3, '#9aa3ad') +
            line('M72 50 Q90 50 88 64 Q86 76 70 74', 10, K) + line('M72 50 Q90 50 88 64 Q86 76 70 74', 4, '#fff') +
            path('M20 38 H72 V72 Q72 88 58 88 H34 Q20 88 20 72 Z', '#fff') + ell(46, 38, 26, 5, '#6B3E1F', 0, 3) +
            line('M30 56 L30 74', 3, '#e1e6ec'))
B2['⛺'] = ('tent', line('M4 86 L96 86', 3) + line('M50 16 L50 4', 3) + path('M50 4 L64 8 L50 13 Z', '#E63946', 2.5) +
            path('M10 86 L50 16 L90 86 Z', '#2BB673') + path('M38 86 L50 52 L62 86 Z', '#1F7A4C', 3) + line('M50 16 L50 52', 2.5, '#1F7A4C'))
B2['🌈'] = ('rainbow', ''.join(f'<path d="M{50-r} 74 A{r} {r} 0 0 1 {50+r} 74" fill="none" stroke="{c}" stroke-width="7.5"/>' for r, c in
             [(40, '#E63946'), (32.5, '#FF8C42'), (25, '#FFD93D'), (17.5, '#2BB673'), (10, '#2F80ED')]) +
            '<path d="M6.2 74 A43.8 43.8 0 0 1 93.8 74" fill="none" stroke="#1d1d1d" stroke-width="2.5"/>' +
            '<path d="M43.8 74 A6.2 6.2 0 0 1 56.2 74" fill="none" stroke="#1d1d1d" stroke-width="2.5"/>' +
            blob([(10, 76, 9), (20, 78, 8), (4, 80, 6)], '#fff', 3) + blob([(90, 76, 9), (80, 78, 8), (96, 80, 6)], '#fff', 3))
B2['🍇'] = ('grapes', line('M50 22 Q52 12 58 8', 4, '#6B3E1F') + path('M54 16 Q68 6 80 14 Q68 26 54 16 Z', '#2BB673', 3) +
            ''.join(circ(x, y, 10, '#8E44AD', 3) for x, y in [(32,32),(50,30),(68,32),(40,48),(58,48),(76,46),(30,50),(48,64),(66,62),(56,80),(40,78)]) +
            ''.join(circ(x - 3, y - 3, 2.5, '#C39BD3', 0, 'none') for x, y in [(32,32),(50,30),(68,32),(40,48),(58,48),(48,64),(66,62),(56,80)]))
B2['🍉'] = ('watermelon', path('M8 38 A42 42 0 0 0 92 38 Z', '#2BB673') + path('M14 38 A36 36 0 0 0 86 38 Z', '#F4FFE9', 0, 'none') +
            path('M18 38 A32 32 0 0 0 82 38 Z', '#FF5A6E', 0, 'none') + path('M8 38 A42 42 0 0 0 92 38 Z', 'none') + line('M8 38 L92 38', 3.5) +
            ''.join(ell(x, y, 2, 3.4, '#2b2b2b', r, 0, 'none') for x, y, r in [(34,48,-20),(50,52,0),(66,48,20),(42,62,-10),(58,62,10),(50,72,0)]))
B2['🍕'] = ('pizza slice', path('M14 22 Q50 8 86 22 L50 93 Z', '#FFD27A') +
            path('M12 21 Q50 6 88 21 Q90 30 82 32 Q50 20 18 32 Q10 30 12 21 Z', '#C98A44') +
            circ(38, 40, 7, '#E63946', 2.5) + circ(62, 42, 7, '#E63946', 2.5) + circ(50, 62, 6, '#E63946', 2.5) + circ(44, 52, 2, '#2BB673', 0) + circ(58, 76, 2, '#2BB673', 0))
B2['🍞'] = ('bread', path('M14 46 Q14 22 50 22 Q86 22 86 46 Q86 54 80 56 L80 84 Q80 88 76 88 L24 88 Q20 88 20 84 L20 56 Q14 54 14 46 Z', '#E2AE6C') +
            path('M26 56 L74 56 L74 82 L26 82 Z', '#F6DDB0', 0, 'none') + line('M36 30 L42 40 M50 28 L56 38 M64 30 L70 40', 3, '#B9773A'))
B2['🍦'] = ('ice cream cone', path('M30 50 L50 93 L70 50 Z', '#E2AE6C') + line('M36 58 L60 70 M40 70 L56 78 M64 58 L40 70 M60 70 L44 78', 2, '#B9773A') +
            blob([(50, 34, 20), (34, 46, 10), (50, 50, 10), (66, 46, 10)], '#FFB7D5') + circ(50, 13, 5, '#E63946', 2.5) + hi(42, 28, 3, 7))
B2['🍯'] = ('honey pot', line('M62 30 L80 6', 5, '#8B5A2B') + path('M24 40 Q16 70 30 88 H70 Q84 70 76 40 Z', '#FFB800') +
            rect(20, 30, 60, 12, '#D98C00', 6) + path('M28 42 Q30 52 34 48 Q36 56 40 50 L44 42 Z', '#FFB800', 0, 'none') +
            rect(32, 56, 36, 16, '#fff', 4, 2.5) +
            '<text x="50" y="69" font-family="Bangers, Impact, sans-serif" font-size="10.5" text-anchor="middle" fill="#D98C00" stroke="none">HONEY</text>')
B2['🍿'] = ('popcorn', blob([(32, 34, 10), (44, 26, 11), (58, 26, 11), (70, 34, 10), (50, 38, 10)], '#FFF3C4') +
            '<clipPath id="popclip"><path d="M24 40 L76 40 L67 93 L33 93 Z"/></clipPath>' + path('M24 40 L76 40 L67 93 L33 93 Z', '#fff') +
            '<g clip-path="url(#popclip)">' + rect(34, 38, 8, 60, '#E63946', 0, 0, 'none') + rect(58, 38, 8, 60, '#E63946', 0, 0, 'none') + '</g>' +
            path('M24 40 L76 40 L67 93 L33 93 Z', 'none'))
def _vball():
    """Classic swirl volleyball: three curved seams from the center, parallel stripes in each section."""
    O, RB, RS = (50.0, 50.0), 40.0, 44.0
    def seam(th):
        u = math.radians(th + 90); C = (O[0] + RS * math.cos(u), O[1] + RS * math.sin(u))
        phi0 = math.atan2(O[1] - C[1], O[0] - C[0]); best = None
        for sgn in (1, -1):
            pts = []
            for k in range(0, 400):
                ph = phi0 + sgn * k * 0.01; p = (C[0] + RS * math.cos(ph), C[1] + RS * math.sin(ph))
                if math.hypot(p[0] - O[0], p[1] - O[1]) > RB + 0.5: break
                pts.append(p)
            if len(pts) > 2:
                d = (pts[3][0] - O[0], pts[3][1] - O[1]); score = d[0] * math.cos(math.radians(th)) + d[1] * math.sin(math.radians(th))
                if best is None or score > best[0]: best = (score, pts, C, sgn, phi0)
        return best[1], best[2], best[3], best[4]
    seams = [seam(-90 + 120 * i) for i in range(3)]
    ang = lambda p: math.atan2(p[1] - O[1], p[0] - O[0])
    P = lambda pts: ' '.join(f'{f(x)},{f(y)}' for x, y in pts)
    s = circ(50, 50, RB, '#fff')
    cols = ['#2F80ED', '#FFD93D', '#fff']
    for i in range(3):
        a_pts, C, sgn, phi0 = seams[i]; b_pts = seams[(i + 1) % 3][0]
        a0, a1 = ang(a_pts[-1]), ang(b_pts[-1])
        while a1 <= a0: a1 += 2 * math.pi
        rim = [(O[0] + RB * math.cos(a0 + (a1 - a0) * t / 30), O[1] + RB * math.sin(a0 + (a1 - a0) * t / 30)) for t in range(31)]
        sector = a_pts + rim + b_pts[::-1]
        cid = f'vbs{i}'
        s += f'<clipPath id="{cid}"><polygon points="{P(sector)}"/></clipPath><g clip-path="url(#{cid})">'
        for sg in (1, -1):
            s += f'<circle cx="{f(C[0])}" cy="{f(C[1])}" r="{f(RS + sg * 5)}" fill="none" stroke="{cols[i]}" stroke-width="10"/>'
            s += circ(C[0], C[1], RS + sg * 10, 'none', 2.2) + circ(C[0], C[1], RS + sg * 20, 'none', 2.2)
        s += '</g>'
    for pts, *_ in seams:
        s += f'<polyline points="{P(pts)}" fill="none" stroke="{K}" stroke-width="2.6" stroke-linecap="round"/>'
    return s + circ(50, 50, RB, 'none')
B2['🏐'] = ('volleyball', _vball())
B2['🏠'] = ('house', rect(64, 18, 11, 22, '#8B5A2B', 1) + path('M10 52 L50 14 L90 52 Z', '#E63946') + rect(20, 48, 60, 42, '#FFE9B0') +
            rect(43, 64, 15, 26, '#8B5A2B', 2) + circ(54, 78, 1.8, '#FFD93D', 0) + rect(25, 56, 13, 13, '#CDEFFF', 1, 3) + rect(63, 56, 13, 13, '#CDEFFF', 1, 3) +
            line('M31.5 56 V69 M25 62.5 H38 M69.5 56 V69 M63 62.5 H76', 2))
B2['🐇'] = ('rabbit', A['🐰'][1])
B2['🐍'] = ('snake', outlined('M12 82 Q28 60 44 76 Q60 92 74 68 Q84 48 64 40', 11, '#2BB673') +
            ''.join(circ(x, y, 2.2, '#FFD93D', 0, 'none') for x, y in [(22,70),(44,76),(62,80),(74,62)]) +
            ell(58, 38, 14, 10, '#2BB673', -10) + eye(54, 34, 3) + line('M45 40 L36 41 M36 41 L32 37 M36 41 L32 45', 2.5, '#E63946'))
B2['🐘'] = ('elephant', ''.join(rect(x, 68, 11, 22, '#A7B4C2', 3) for x in (36, 52, 66, 78)) + line('M86 56 Q94 60 92 70', 3) +
            ell(60, 56, 30, 22, '#A7B4C2') + outlined('M18 52 Q8 70 16 84 Q20 88 24 84', 8, '#A7B4C2') + circ(28, 44, 19, '#A7B4C2') +
            ell(40, 46, 13, 17, '#C3CDD8', 10) + path('M20 56 Q14 60 18 64', '#fff', 2.5) + eye(22, 40, 3))
B2['🐙'] = ('octopus', ''.join(outlined(d, 8, '#B06AD8') for d in ['M28 52 Q14 66 22 82', 'M38 56 Q32 74 40 88', 'M50 58 Q50 76 56 90', 'M62 56 Q70 74 64 88', 'M72 52 Q88 64 80 82']) +
            path('M22 54 Q20 12 50 12 Q80 12 78 54 Q50 62 22 54 Z', '#B06AD8') + circ(40, 38, 7, '#fff', 2.5) + circ(60, 38, 7, '#fff', 2.5) +
            circ(41, 39, 3.5, K, 0) + circ(61, 39, 3.5, K, 0) + line('M44 50 Q50 54 56 50', 2.5) + hi(34, 24, 4, 8))
B2['🐜'] = ('ant', line('M44 54 L30 70 L24 84 M48 56 L48 74 L44 88 M52 54 L66 70 L74 84', 3) + line('M20 44 L14 30 L8 26 M26 42 L26 28 L32 22', 2.5) +
            circ(24, 50, 10, '#5A3418') + circ(45, 52, 9, '#5A3418') + ell(72, 54, 17, 13, '#5A3418') + circ(21, 47, 2.4, '#fff', 0))
B2['🐠'] = ('tropical fish', path('M70 50 L92 30 L86 50 L92 70 Z', '#2F80ED') +
            '<clipPath id="tfclip"><path d="M10 50 Q36 18 74 50 Q36 82 10 50 Z"/></clipPath>' + path('M10 50 Q36 18 74 50 Q36 82 10 50 Z', '#FFD93D') +
            '<g clip-path="url(#tfclip)">' + rect(30, 10, 8, 80, '#2F80ED', 0, 0, 'none') + rect(50, 10, 8, 80, '#2F80ED', 0, 0, 'none') + '</g>' +
            path('M10 50 Q36 18 74 50 Q36 82 10 50 Z', 'none') + path('M34 32 Q44 14 56 34 Z', '#2F80ED', 3) + circ(21, 47, 4.5, '#fff', 2.5) + circ(20, 47, 2.2, K, 0))
B2['🐢'] = ('turtle', ell(28, 70, 8, 6, '#9ED36A') + ell(76, 70, 8, 6, '#9ED36A') + path('M88 62 L96 66 L88 68 Z', '#9ED36A', 2.5) +
            circ(14, 56, 10, '#9ED36A') + eye(11, 53, 2.5) + rect(18, 60, 72, 8, '#1F7A4C', 4) +
            path('M20 62 Q22 26 54 26 Q86 26 88 62 Z', '#2BB673') +
            line('M54 26 L54 62 M36 34 L40 62 M72 34 L68 62 M24 48 H84', 2.5, '#1F7A4C'))
B2['🐣'] = ('hatching chick', circ(50, 44, 21, '#FFD93D') + path('M46 46 L38 50 L46 54 Z', '#FF8C42', 2.5) + eye(44, 38, 3) + eye(58, 38, 3) +
            line('M50 20 Q48 14 52 12', 2.5) +
            path('M18 58 L27 50 L36 58 L45 50 L54 58 L63 50 L72 58 L82 50 Q90 92 50 92 Q12 92 18 58 Z', '#FFF6E0') + hi(32, 70, 3, 7))
B2['🐧'] = ('penguin', ell(36, 90, 9, 5, '#FF8C42') + ell(64, 90, 9, 5, '#FF8C42') + ell(22, 58, 7, 18, '#2b2b2b', 20) + ell(78, 58, 7, 18, '#2b2b2b', -20) +
            ell(50, 56, 27, 35, '#2b2b2b') + ell(50, 62, 18, 26, '#fff', 0, 2.5) + circ(41, 34, 5, '#fff', 0) + circ(59, 34, 5, '#fff', 0) +
            circ(42, 35, 2.5, K, 0) + circ(58, 35, 2.5, K, 0) + path('M44 42 L56 42 L50 50 Z', '#FF8C42', 2.5))
B2['🐭'] = ('mouse', circ(25, 28, 16, '#B8C4D6') + circ(75, 28, 16, '#B8C4D6') + circ(25, 28, 9, '#F7B6C2', 0) + circ(75, 28, 9, '#F7B6C2', 0) +
            path('M50 84 Q24 74 24 52 Q24 32 50 32 Q76 32 76 52 Q76 74 50 84 Z', '#B8C4D6') + eye(40, 54, 3.5) + eye(60, 54, 3.5) +
            circ(50, 74, 5, '#FF7E9B', 2.5) + line('M42 72 L22 68 M42 76 L23 80 M58 72 L78 68 M58 76 L77 80', 2))
B2['🐳'] = ('whale', line('M34 22 Q34 14 28 8 M34 22 Q34 14 40 8 M34 22 L34 12', 3, '#5CC8FF') +
            path('M8 56 Q10 30 44 30 Q76 30 82 50 L94 38 L92 62 L82 58 Q70 78 40 78 Q10 78 8 56 Z', '#2F80ED') +
            path('M14 62 Q30 74 50 72 Q66 70 76 62 Q66 76 40 76 Q20 74 14 62 Z', '#BFE3FF', 0) + eye(26, 50, 3) + line('M14 60 Q22 64 32 62', 2.5))
B2['👓'] = ('glasses', line('M12 46 L4 40 M88 46 L96 40', 3.5) + circ(29, 52, 17, '#E3F4FF') + circ(71, 52, 17, '#E3F4FF') +
            line('M46 50 Q50 44 54 50', 3.5) + line('M22 46 L28 40 M64 46 L70 40', 2.5, '#fff'))
B2['👖'] = ('jeans', path('M24 10 H76 L82 90 H58 L50 40 L42 90 H18 Z', '#2F80ED') + rect(24, 10, 52, 10, '#1E5FB8', 0, 3) +
            line('M50 20 L50 40 M30 26 Q36 34 44 28 M70 26 Q64 34 56 28', 2.5, '#9CC4F5') + circ(50, 15, 2, '#FFD93D', 0))
B2['👟'] = ('sneaker', rect(6, 70, 90, 12, '#fff', 5) + path('M8 70 L8 50 Q8 42 18 42 L38 42 Q46 32 56 34 L64 38 Q72 54 90 58 Q96 62 94 70 Z', '#E63946') +
            line('M40 44 L50 50 M46 40 L56 46 M52 37 L60 42', 3, '#fff') + line('M14 62 Q40 56 70 64', 3, '#fff') + line('M8 76 H94', 2, '#ccc'))
B2['💧'] = ('water drop', path('M50 8 Q80 46 80 64 Q80 92 50 92 Q20 92 20 64 Q20 46 50 8 Z', '#5CC8FF') + hi(38, 62, 4, 10, 0))
B2['📏'] = ('ruler', f'<g transform="rotate(-25 50 50)">' + rect(8, 38, 84, 24, '#FFD93D', 3) +
            ''.join(line(f'M{x} 38 L{x} {46 if i % 2 else 50}', 2.5) for i, x in enumerate(range(16, 90, 8))) + '</g>')
B2['📖'] = ('open book', path('M8 28 Q30 22 50 32 Q70 22 92 28 L92 84 Q70 78 50 88 Q30 78 8 84 Z', '#2F80ED') +
            path('M50 30 Q32 18 12 22 L12 78 Q32 74 50 84 Z', '#fff') + path('M50 30 Q68 18 88 22 L88 78 Q68 74 50 84 Z', '#fff') +
            line('M20 34 Q32 32 42 38 M20 44 Q32 42 42 48 M20 54 Q32 52 42 58 M58 38 Q68 32 80 34 M58 48 Q68 42 80 44 M58 58 Q68 52 80 54', 2, '#b9c3cf'))
B2['📚'] = ('stack of books', rect(14, 66, 72, 18, '#2F80ED', 3) + rect(20, 46, 64, 18, '#E63946', 3) + rect(12, 26, 68, 18, '#2BB673', 3) +
            line('M22 70 V80 M28 50 V60 M20 30 V40', 3, '#fff') + line('M86 69 H80 M86 80 H80', 2, '#fff'))
B2['🔧'] = ('wrench', rect(44, 40, 12, 52, '#9AA5B1', 6) + path('M36 10 L42 24 L58 24 L64 10 Q76 18 72 32 Q68 44 56 44 L44 44 Q32 44 28 32 Q24 18 36 10 Z', '#9AA5B1') +
            line('M50 52 L50 84', 2.5, '#c8d0d8'))
B2['🕷️'] = ('spider', ''.join(line(d, 3) for d in ['M42 50 L26 38 L18 48', 'M42 54 L22 52 L12 62', 'M42 58 L24 66 L18 80', 'M44 62 L32 76 L30 90',
                                                    'M58 50 L74 38 L82 48', 'M58 54 L78 52 L88 62', 'M58 58 L76 66 L82 80', 'M56 62 L68 76 L70 90']) +
            circ(50, 60, 16, '#2b2b2b') + circ(50, 38, 10, '#2b2b2b') + circ(46, 36, 2.5, '#fff', 0) + circ(54, 36, 2.5, '#fff', 0))
B2['🖍️'] = ('crayon', '<g transform="rotate(-35 50 50)">' + path('M72 41 L90 50 L72 59 Z', '#E63946') + path('M84 47 L90 50 L84 53 Z', '#A61E2A', 0) +
            rect(14, 41, 60, 18, '#E63946', 3) + rect(28, 41, 32, 18, '#F59AA2', 0) + line('M34 46 H54 M34 54 H54', 2.5, '#fff') + '</g>')
B2['🚁'] = ('helicopter', line('M12 26 H88', 5) + line('M50 26 V36', 4) + rect(64, 50, 28, 8, '#E63946', 4) + line('M90 44 V64 M84 54 H96', 3) +
            ell(42, 54, 28, 19, '#E63946') + path('M20 50 Q22 38 38 38 L38 56 L18 56 Q18 52 20 50 Z', '#CDEFFF', 3) +
            line('M24 84 H66 M34 72 L32 84 M56 72 L58 84', 4))
B2['🚢'] = ('ship', line('M4 90 Q14 86 24 90 Q34 94 44 90 Q54 86 64 90 Q74 94 84 90 Q90 88 96 90', 3, '#2F80ED') +
            rect(38, 18, 10, 26, '#E63946', 1) + rect(56, 18, 10, 26, '#E63946', 1) + rect(38, 18, 10, 6, '#2b2b2b', 0, 2) + rect(56, 18, 10, 6, '#2b2b2b', 0, 2) +
            rect(24, 40, 52, 20, '#fff') + ''.join(circ(x, 50, 3.5, '#5CC8FF', 2) for x in (34, 46, 58, 70)) +
            path('M6 60 H94 L80 84 H20 Z', '#2F80ED') + path('M14 74 H86 L80 84 H20 Z', '#E63946', 0))
B2['🥁'] = ('drum', line('M28 6 L52 34 M72 6 L48 34', 4, '#8B5A2B') + circ(28, 6, 3.5, '#FFE9B0', 2) + circ(72, 6, 3.5, '#FFE9B0', 2) +
            path('M18 42 V78 Q18 88 50 88 Q82 88 82 78 V42 Z', '#E63946') +
            line('M18 48 L30 80 L42 48 L54 80 L66 48 L78 80', 2.5, '#FFD93D') + ell(50, 42, 32, 10, '#F4F4F4'))
B2['🥄'] = ('spoon', rect(46, 44, 8, 50, '#C9D3DD', 4) + ell(50, 26, 16, 21, '#C9D3DD') + hi(45, 20, 3, 8, 0))
B2['🥾'] = ('boot', rect(22, 80, 72, 10, '#333', 4) + path('M28 12 H58 V52 Q84 56 90 70 V82 H24 V60 Q24 40 28 12 Z', '#8B5A2B') +
            rect(26, 12, 34, 8, '#5A3418', 2, 3) + line('M34 26 L52 32 M34 36 L52 42 M52 26 L34 32 M52 36 L34 42', 2.5, '#FFD93D') + line('M60 56 Q74 60 82 70', 2.5, '#5A3418'))
B2['🦀'] = ('crab', ''.join(line(d, 3.5) for d in ['M30 64 L14 70 L10 80', 'M32 70 L18 80 L16 90', 'M70 64 L86 70 L90 80', 'M68 70 L82 80 L84 90',
                                                  'M34 52 L22 42', 'M66 52 L78 42', 'M42 46 L40 32', 'M58 46 L60 32']) +
            path('M20 40 A13 13 0 1 1 30 26 L20 33 Z', '#E63946') + path('M80 40 A13 13 0 1 0 70 26 L80 33 Z', '#E63946') +
            ell(50, 60, 27, 18, '#E63946') + circ(40, 30, 5, '#fff', 2.5) + circ(60, 30, 5, '#fff', 2.5) + circ(40, 30, 2.4, K, 0) + circ(60, 30, 2.4, K, 0) +
            line('M44 64 Q50 68 56 64', 2.5))
B2['🦁'] = ('lion', blob([(50 + 32 * math.cos(math.radians(a)), 52 + 32 * math.sin(math.radians(a)), 13) for a in range(0, 360, 36)], '#C9702A') +
            circ(30, 32, 7, '#FFC15A') + circ(70, 32, 7, '#FFC15A') + circ(50, 54, 24, '#FFC15A') + ell(50, 64, 12, 9, '#FFE3A8', 0, 0) +
            path('M45 58 L55 58 L50 64 Z', '#5A3418', 2) + line('M50 64 V68 M44 70 Q50 74 56 70', 2.5) + eye(41, 48, 3.5) + eye(59, 48, 3.5))
B2['🦅'] = ('eagle', line('M52 80 L50 90 M62 80 L64 90', 4, '#FFB800') + path('M70 70 L92 84 L86 66 Z', '#fff') +
            path('M30 44 Q40 34 60 40 Q82 48 78 72 Q60 84 42 72 Q30 62 30 44 Z', '#7A4A24') + path('M46 50 Q66 48 76 66 Q60 70 48 60 Z', '#5A3418', 2.5) +
            circ(32, 32, 15, '#fff') + path('M18 30 L4 34 Q6 44 14 40 L19 37 Z', '#FFB800', 3) + eye(30, 28, 3))
B2['🦇'] = ('bat', path('M44 46 Q30 30 6 36 Q14 44 12 54 Q20 50 24 58 Q30 52 36 60 Q40 54 46 58 Z', '#4A3B5C') +
            path('M56 46 Q70 30 94 36 Q86 44 88 54 Q80 50 76 58 Q70 52 64 60 Q60 54 54 58 Z', '#4A3B5C') +
            ell(50, 54, 9, 15, '#4A3B5C') + path('M42 34 L42 20 L48 28 Z', '#4A3B5C', 3) + path('M58 34 L58 20 L52 28 Z', '#4A3B5C', 3) +
            circ(50, 36, 10, '#4A3B5C') + circ(46, 35, 2.5, '#fff', 0) + circ(54, 35, 2.5, '#fff', 0) + path('M47 42 L49 46 L50 42 Z', '#fff', 1.5) + path('M50 42 L51 46 L53 42 Z', '#fff', 1.5))
B2['🦒'] = ('giraffe', path('M40 96 L46 40 L58 34 L58 96 Z', '#FFC15A') +
            ''.join(path(d, '#C9702A', 0, 'none') for d in ['M48 54 L54 50 L56 58 L50 60 Z', 'M47 70 L53 66 L56 74 L50 78 Z', 'M50 86 L56 84 L57 92 L50 94 Z', 'M52 42 L56 40 L57 46 L53 47 Z']) +
            path('M40 96 L46 40 L58 34 L58 96', 'none') + line('M58 24 L56 12 M66 22 L68 10', 3) + circ(56, 11, 3, '#C9702A', 2) + circ(68, 9, 3, '#C9702A', 2) +
            path('M74 22 L84 16 L80 26 Z', '#FFC15A', 2.5) + ell(66, 30, 17, 10, '#FFC15A', 15) + ell(78, 35, 6, 5, '#FFE3A8', 15, 2) + eye(63, 26, 2.6))
B2['🦢'] = ('swan', line('M8 84 Q18 80 28 84 Q38 88 48 84 Q58 80 68 84 Q78 88 92 84', 3, '#2F80ED') +
            path('M30 66 Q30 50 56 50 Q86 50 92 62 Q86 78 56 80 Q32 80 30 66 Z', '#fff') + line('M50 60 Q64 56 80 64', 2.5, '#c9d3dd') +
            outlined('M40 58 Q26 42 34 28 Q40 18 31 15', 6, '#fff') + circ(30, 16, 7, '#fff') + path('M24 15 L13 19 L24 21 Z', '#FF8C42', 2.5) + eye(30, 14, 2.2))
B2['🧀'] = ('cheese', path('M10 50 L58 26 L92 50 Z', '#FFE680') + path('M10 50 L92 50 L92 80 L10 80 Z', '#FFC93D') +
            ''.join(ell(x, y, rx, ry, '#E6A800', 0, 0, 'none') for x, y, rx, ry in [(26,62,6,5),(48,70,4,3.5),(70,60,7,6),(82,72,3.5,3),(40,42,5,2.5),(66,40,4,2)]))
B2['🧢'] = ('baseball cap', path('M50 62 H94 Q98 72 86 74 H50 Z', '#1E5FB8') + path('M14 64 Q14 26 50 24 Q82 26 82 64 Z', '#2F80ED') +
            circ(48, 24, 4, '#1E5FB8', 2.5) + line('M48 26 Q36 40 34 64 M48 26 Q62 40 64 64', 2.5, '#1E5FB8'))
B2['🧱'] = ('bricks', ''.join(rect(x, y, w, 19, '#C9573A', 2, 3) for x, y, w in
                              [(6,12,42),(50,12,44),(6,33,20),(28,33,42),(72,33,22),(6,54,42),(50,54,44),(6,75,20),(28,75,42),(72,75,22)]))
B2['🪚'] = ('saw', path('M8 34 L66 28 L66 66 L8 60 Z', '#C9D3DD') +
            line('M8 60 ' + ' '.join(f'L{f(8 + 4.8 * i)} {64 if i % 2 else 60}' for i in range(1, 13)), 2.5) +
            path('M62 24 H86 Q96 24 96 36 V66 Q96 76 86 76 H62 Z', '#C68642') + ell(81, 50, 6, 13, '#fff', 0, 3))
B2['🪛'] = ('screwdriver', path('M47 84 L53 84 L51 95 L49 95 Z', '#7D8893', 2.5) + rect(46.5, 46, 7, 40, '#9AA5B1', 2, 3) +
            rect(38, 6, 24, 42, '#E63946', 10) + line('M44 14 V40 M50 14 V40 M56 14 V40', 2.5, '#A61E2A'))

B2['🌞'] = ('smiling sun', A['☀️'][1] + eye(43, 46, 2.6) + eye(57, 46, 2.6) + line('M42 55 Q50 62 58 55', 2.8) +
            circ(38, 54, 3, '#FF8C42', 0, 'none', 'opacity="0.6"') + circ(62, 54, 3, '#FF8C42', 0, 'none', 'opacity="0.6"'))

B2['🐬'] = ('dolphin', path('M20 66 L5 54 Q8 63 12 66 Q5 72 7 82 Z', '#6E9FD6') +
            path('M58 35 Q55 19 43 16 Q48 26 46 36 Z', '#6E9FD6') +
            path('M10 60 C20 42 44 31 66 34 C77 35 85 40 88 44 L97 46 Q98 51 92 52 L84 52 C78 58 68 62 56 62 C40 62 28 64 19 70 Z', '#6E9FD6') +
            path('M26 63 C40 58 56 58 68 57 C76 56 82 54 85 52 C78 58 68 62 56 62 C42 62 32 63 26 63 Z', '#DCEBFA', 0) +
            path('M60 58 Q58 70 49 73 Q51 64 53 58 Z', '#5786BD', 2.5) + eye(79, 44, 2.8) + line('M84 51 Q88 53 92 51', 2.2))
B2['🧽'] = ('sponge', circ(76, 16, 7, '#E3F4FF', 2, '#5CC8FF') + circ(89, 24, 5, '#E3F4FF', 2, '#5CC8FF') + circ(64, 12, 4, '#E3F4FF', 2, '#5CC8FF') +
            circ(74, 14, 1.8, '#fff', 0, 'none') + circ(88, 22, 1.3, '#fff', 0, 'none') +
            path('M80 42 L88 30 L88 72 L80 86 Z', '#E8B800') + path('M18 42 L28 30 L88 30 L80 42 Z', '#FFE680') +
            path('M14 48 Q14 42 20 42 L74 42 Q80 42 80 48 L80 80 Q80 86 74 86 L20 86 Q14 86 14 80 Z', '#FFD93D') +
            ''.join(ell(x, y, rx, ry, '#E0A800', 0, 0, 'none') for x, y, rx, ry in
                    [(24,54,4,3),(38,50,2.5,2),(52,56,5,4),(68,50,3,2.5),(30,68,3,2.5),(46,72,4,3),(62,68,3,2.5),(72,78,2.5,2),(22,78,2.5,2),(56,80,2,1.6)]) +
            ''.join(ell(x, y, 2.2, 1.2, '#E6C200', 0, 0, 'none') for x, y in [(36,36),(52,34),(68,36),(80,34)]))
