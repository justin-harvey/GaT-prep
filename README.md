# Brain Blasters! 🦸‍♂️🤖

A comic-book-style practice site for the 2nd-grade CogAT (Level 8), starring Captain Waffle and Gizmo the robot.

It's a single self-contained page (`index.html`). Open it in a browser or host it with GitHub Pages.

## What's inside

There are 9 missions in 3 worlds, one for each CogAT Level 8 question type:

| World | Mission | CogAT type |
|---|---|---|
| 🌲 Word Woods (Verbal) | Match Makers | Picture Analogies |
| | Riddle Room | Sentence Completion |
| | Who Belongs? | Picture Classification |
| 🌋 Number Mountain (Quantitative) | Number Machines | Number Analogies |
| | Balance Bridge | Number Puzzles |
| | Bead Patterns | Number Series |
| 🪐 Shape Space (Nonverbal) | Shape Swap | Figure Matrices |
| | Shape Squad | Figure Classification |
| | Hole Punch Hero | Paper Folding |

- Each mission is 5 puzzles, with no timer. Wrong answers can be retried, and hints appear after a second miss.
- Number and shape puzzles are generated fresh every time. Word puzzles rotate through a hand-written set.
- Each mission ends with a brain break and a new sticker for the Sticker Vault.
- **⚡ Challenge Mode** (toggle on the mission map) has harder, 3rd-grade-style (Level 9) versions of all 9 types: written-word analogies, fill-in-the-blank sentences, odd-one-out, two-step number rules, numeral patterns, picture-algebra, 3×3 grids, side-counting, and slanted or reverse paper folds. Acing one earns a gold ★ on the checklist.
- **🧺 Number Catcher (free):** he catches two falling numbers that add up to a target, starting with "make 10" and working up to 20. It never costs a token, has a button on the home screen and on Number Mountain, and can be turned off in the Grown-Up Corner.
- **🕹️ Sticker Arcade:** each Challenge mission earns an Arcade token (2 if aced). **Bonus missions** (the 4 types with his lowest first-try rate, marked 🎟️×2) and Surprise Challenges earn double. Each game costs 2 tokens by default (adjustable to 1–3 in the Grown-Up Corner). The games are **Sticker Pong** (his hero sticker is the paddle; the game ends after 3 misses against the computer) **Sticker Invaders** (his stickers are the invaders; the game ends when they land on him), or **Sticker Dash** (an endless runner like the offline dino game; his hero jumps over cactuses and flying stickers, and one crash ends the game), **Sticker Smash** (a brick breaker with sticker bricks; 3 missed balls ends the game) or **Sticker Match** (a memory game with 8 sticker pairs; it ends when every pair is found, and fewer flips scores higher). The Pong physics come from the [Pong game in justin-harvey/test](https://github.com/justin-harvey/test).
- The Grown-Up Corner has a read-aloud option, sound settings and first-try stats for each question type. Stats are saved in the browser's localStorage.

## Hosting on GitHub Pages

Settings → Pages → Source: "Deploy from a branch" → Branch: `main`, folder `/ (root)`.

This is not an official CogAT practice test. Its only goal is to make the question formats feel familiar.
