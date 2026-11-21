# Brain Blasters! 🦸‍♂️🤖

A comic-book-style practice site for the 2nd-grade CogAT (Level 8), starring Captain Waffle and Gizmo the robot.

It's a single self-contained page (`index.html`) with no build step and no server. Open it in a browser or host it with GitHub Pages.

> This is not an official CogAT practice test and doesn't predict a score. Its goal is to make the question formats feel familiar.

## Missions

There are 9 missions in 3 worlds, one for each CogAT Level 8 question type:

| World | Mission | CogAT type |
|---|---|---|
| 🌲 Word Woods (Verbal) | 🔗 Match Makers | Picture Analogies |
| | 💬 Riddle Room | Sentence Completion |
| | 🧺 Who Belongs? | Picture Classification |
| 🌋 Number Mountain (Quantitative) | ⚙️ Number Machines | Number Analogies |
| | ⚖️ Balance Bridge | Number Puzzles |
| | 🧮 Bead Patterns | Number Series |
| 🪐 Shape Space (Nonverbal) | 🔄 Shape Swap | Figure Matrices |
| | 🔷 Shape Squad | Figure Classification |
| | 📄 Hole Punch Hero | Paper Folding |

- Each mission is 5 puzzles, with no timer.
- A wrong answer grays out and he tries again. A hint appears after the second miss, and every answer shows a short "why."
- The first time he plays a mission, Gizmo shows a strategy tip.
- Number and shape puzzles are generated fresh every time. Word puzzles rotate through a hand-written set of about 70 puzzles.
- **🎲 Surprise Mission** mixes 5 random question types.
- Every finished mission ends with a movement **brain break**, a **new sticker** for the Sticker Vault, and a **bonus challenge** to invent his own puzzle (drawn or built with LEGO).
- His **rank** goes up with missions finished: Rookie → Sidekick → Hero → Super Hero → Puzzle Legend → Galactic Genius.

## ⚡ Challenge Mode

Switch between **Regular** and **Challenge** at the top of the mission map. Challenge Mode has harder versions of all 9 types, closer to 3rd-grade (Level 9) style:

| Mission | Challenge version |
|---|---|
| Match Makers | Written-word analogies ("hot → cold, up → ?") |
| Riddle Room | Fill-in-the-blank sentences and multi-clue riddles |
| Who Belongs? | Odd-one-out (pictures and words) and word groups |
| Number Machines | Two-step rules ("double it, then add 1") with numerals |
| Balance Bridge | Longer equations, "? + ? = 14," and picture-algebra (🍎 = 3) |
| Bead Patterns | Numeral sequences with growing, alternating or interleaved jumps |
| Shape Swap | 3×3 grids and two changes at once |
| Shape Squad | Count the sides, curvy vs. straight, and two-trait groups |
| Hole Punch Hero | Diagonal folds, folds from the right or bottom, and double folds with 2 holes |

The **Surprise Challenge** leans toward number and paper-folding puzzles.

## 🏅 Mission Checklist

The home screen has a checklist of all 9 missions:

- **✔** = aced a regular mission (all 5 right on the first try)
- **★** = aced a Challenge mission (gold)

Tapping a row's ✔ or ⚡ box starts that mission in Regular or Challenge mode. Aced missions are also marked on the mission map.

## 🕹️ Sticker Arcade

Challenge missions earn **Arcade tokens** 🎟️, which he spends on games that use his own stickers. He picks a **hero sticker** from his collection, and his other stickers become the enemies, bricks and cards.

**Earning tokens** (Challenge Mode only; regular missions don't earn tokens):

| Mission | Finished | Aced |
|---|---|---|
| Challenge mission | 1 | 2 |
| **🎟️×2 Bonus mission** | 2 | 4 |
| Surprise Challenge | 2 | 4 |

**Bonus missions** are the 4 types where his first-try rate is lowest across regular and Challenge play. They're marked 🎟️×2 on the Challenge map. The list updates automatically as he improves, so tokens keep pointing him toward his growth areas.

**Spending tokens:** each game costs **2 tokens** by default (adjustable to 1–3 in the Grown-Up Corner).

| Game | How it works | Game over |
|---|---|---|
| 🏓 **Sticker Pong** | His hero is the paddle; the ball is a waffle. The robot opponent starts easy and only gets tougher as he wins points. | 3 misses |
| 👾 **Sticker Invaders** | His stickers invade in waves; ❄️ freeze-rays stun him briefly. | Invaders reach him |
| 🏃 **Sticker Dash** | An endless runner like the offline dino game. He jumps over cactuses and low flyers and stays down for high flyers. It speeds up over time. | First crash |
| 🧱 **Sticker Smash** | A brick breaker with sticker bricks. Clearing the wall moves him up a level. | 3 missed balls |
| 🃏 **Sticker Match** | A memory game with 8 sticker pairs. Fewer flips scores higher (200 is perfect). | All pairs found |

Controls work with a mouse, keyboard or touch. Best scores are saved for each game.

The Pong ball physics and computer opponent come from the [Pong game in justin-harvey/test](https://github.com/justin-harvey/test).

## 🧺 Number Catcher (free)

A math game that **never costs tokens**, built to practice the quick addition behind Number Mountain.

- He catches two falling numbers that add up to the target. It starts with "make 10," and every 5 correct pairs the target changes (8, 9, 12, and eventually up to 20).
- On the first two targets, the matching partner glows to help him learn.
- A wrong pair is a strike. 3 strikes ends the game.
- It has a button on the home screen, a warm-up button on Number Mountain, and a FREE card in the Arcade.
- It stays available even when the Arcade is turned off.

## 🧑 Grown-Up Corner

- A guide to each mission, its CogAT question type, and how Challenge Mode and the Arcade work, plus the current bonus missions.
- Tips for short, low-pressure sessions.
- **Settings:**
  - 🔊 Auto-read questions aloud (the 2nd-grade CogAT is mostly read aloud)
  - 🕹️ Arcade on/off. When it's off, the Arcade is hidden and earned tokens are saved for later.
  - 🎟️ Tokens per Arcade game (1, 2 or 3)
  - 🧺 Number Catcher on/off
  - 🔔 Sound effects
- **Progress:** puzzles solved, first-try rate and aces for each type (regular and Challenge), missions, stickers, tokens, best game scores, and Number Catcher pairs.
- **Reset all progress.**

## Saving progress

Progress is saved in the browser's localStorage. There's no account and nothing is sent anywhere. Each browser and each site address (for example, GitHub Pages vs. the Claude link) keeps its own progress, and clearing browsing data erases it.

## Hosting on GitHub Pages

Settings → Pages → Source: "Deploy from a branch" → Branch: `main`, folder `/ (root)`.

The site will be at `https://justin-harvey.github.io/Hanks-GAT/`.
