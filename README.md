# Brain Blasters

Brain Blasters is a free, comic-book-themed practice site that introduces young children to the question formats used on the Cognitive Abilities Test (CogAT), Level 8. Many school districts give this test in 2nd grade when screening for gifted and talented programs.

The site is a single self-contained HTML file. It needs no account, no server and no installation, and it works without an internet connection.

**Live site:** https://justin-harvey.github.io/Hanks-GAT/

## Recent updates

- **Team Up for siblings.** A new two-player co-op area lets an older child play alongside a younger sibling (around kindergarten age): turn-taking Team Puzzles, a Puzzle Maker where the older child builds puzzles for the younger one, and co-op versions of Number Catcher, Match and Invaders. See [Team Up](#team-up-two-player-co-op) below.
- **Works offline, with a Linux app installer.** The fonts are now built into the page, so it runs with no internet connection and makes no outside requests. A small script adds it to the Linux app menu (see below).
- **Original illustrations throughout.** Every picture in the word puzzles (more than 200 in total) and every counting object in the number puzzles is now an original drawing instead of an emoji. The drawings look the same on every device.
- **Picture names.** A short name appears under each puzzle picture to help with unfamiliar drawings. Parents can turn names off for test-style practice.
- **Easier counting.** Objects in the number puzzles are arranged in rows of five, so a group of seven shows as a row of five and a row of two.
- **Two-player Pong.** Sticker Pong can be played against the computer or as a two-player match on one keyboard or touchscreen. The second player chooses their own sticker.
- **New arcade games.** Sticker Smash (brick breaker) and Sticker Match (memory) joined Pong, Invaders and Dash.
- **Number Catcher.** A free addition game that never costs tokens.
- **Rewards tuned toward weaker areas.** Arcade games cost 2 tokens by default, and Challenge missions in the child's four weakest question types earn double.

## Purpose and limitations

The goal is familiarity, not test preparation in the drilling sense. A child who has seen these question formats before is less likely to be thrown by them on test day. The site is designed around short, low-pressure sessions.

Please keep in mind:

- This is not an official CogAT product, is not affiliated with the test's publisher, and does not predict a score.
- The CogAT compares children to others of the same age, so heavy practice is not recommended. A score inflated by drilling can lead to a placement whose pace doesn't fit the child.
- Districts use different tests and levels. Confirm with your school which assessment it uses.

## How it works

The site is organized into three "worlds," one for each CogAT battery. Each world has three missions, and each mission covers one question type:

| Battery | CogAT question type | Mission name in the site |
|---|---|---|
| Verbal | Picture Analogies | Match Makers |
| Verbal | Sentence Completion | Riddle Room |
| Verbal | Picture Classification | Who Belongs? |
| Quantitative | Number Analogies | Number Machines |
| Quantitative | Number Puzzles | Balance Bridge |
| Quantitative | Number Series | Bead Patterns |
| Nonverbal | Figure Matrices | Shape Swap |
| Nonverbal | Figure Classification | Shape Squad |
| Nonverbal | Paper Folding | Hole Punch Hero |

Each mission is five questions, with no timer and no failing:

- A wrong answer is grayed out, and the child tries again.
- A hint appears after a second miss, and every answer comes with a short explanation of why it's right.
- The first time a child plays a mission, a character gives a strategy tip, such as making a sentence to solve an analogy.
- Number and shape questions are generated fresh each time, so they don't repeat. Word questions come from a hand-written set of about 70, plus about 80 more in Challenge Mode.
- A "Surprise Mission" mixes five random question types.

Each completed mission ends with a short movement break (for example, "do five frog hops"), a collectible sticker, and an optional challenge to invent a similar puzzle for a parent to solve.

The format is designed with active, easily bored learners in mind: short tasks, frequent movement breaks, and the child's choice of what to work on.

## Illustrations

All puzzle pictures are original, hand-made SVG drawings in a consistent comic style: more than 200 pictures for the word puzzles, plus the counting objects used in the number puzzles. Unlike emoji, they look the same on every phone, tablet and computer, and each was checked for whether a young child can recognize it at puzzle size.

- A short name appears under each picture by default. Parents can turn names off in the Grown-Up Corner, since the real test uses unlabeled pictures.
- Counting objects are arranged in rows of five to make groups easier to count accurately.
- The shape puzzles (matrices, classification and paper folding) are drawn by the site itself and generated fresh each time.

## Challenge Mode

For children who find the standard questions easy, a Challenge Mode toggle on the mission map switches every question type to a harder version, closer to the style of the next level (CogAT Level 9):

| Question type | Challenge version |
|---|---|
| Picture Analogies | Analogies with written words |
| Sentence Completion | Fill-in-the-blank sentences and riddles with several clues |
| Picture Classification | "Which one doesn't belong," with pictures and with words |
| Number Analogies | Two-step rules, such as "double it, then add 1" |
| Number Puzzles | Longer equations, and puzzles where pictures stand for numbers |
| Number Series | Number patterns with growing, alternating or interleaved steps |
| Figure Matrices | 3x3 grids, and shapes that change in two ways at once |
| Figure Classification | Grouping by number of sides, curved vs. straight edges, or two shared traits |
| Paper Folding | Diagonal folds, folds from different sides, and double folds |

## Progress and rewards

**Mission checklist.** The home screen lists all nine missions. A mission is checked off when the child gets all five questions right on the first try, with a separate gold mark for doing the same in Challenge Mode.

**Arcade.** Challenge missions earn tokens that can be spent on short arcade games. The games use the stickers the child has collected, so the collection carries over into play.

Tokens are earned only in Challenge Mode:

| Challenge mission | Completed | All correct on first try |
|---|---|---|
| Standard | 1 token | 2 tokens |
| Bonus mission | 2 tokens | 4 tokens |
| Surprise Challenge | 2 tokens | 4 tokens |

Bonus missions are the four question types with the child's lowest first-try accuracy. They're marked on the mission map, and the list updates automatically as the child improves. This steers rewards toward the areas where practice helps most.

Each game costs 2 tokens by default. Parents can set this to 1, 2 or 3. Every game has a natural end, so a session doesn't turn into open-ended screen time:

| Game | Description | Ends when |
|---|---|---|
| Sticker Pong | Pong against a computer opponent that starts easy and adapts to the child's skill, or a 2-player match on one keyboard (W/S vs. ↑/↓) or touchscreen | 1 player: the child misses 3 times. 2 players: first to 5 points |
| Sticker Invaders | A Space Invaders-style shooter with waves that speed up | The invaders reach the player |
| Sticker Dash | An endless runner similar to the offline dinosaur game in Chrome | The first collision |
| Sticker Smash | A brick breaker with levels | The child misses 3 balls |
| Sticker Match | A memory game with 8 pairs; fewer flips scores higher | All pairs are found |

All games work with a mouse, keyboard or touchscreen.

**Two-player Pong.** On the Pong start screen, players choose one player (against the computer) or two players. In a two-player match, the left player uses W and S and the right player uses the up and down arrow keys. On a touchscreen, each player drags on their own half of the screen. The second player picks their own sticker, both paddles are the same size, and the first to 5 points wins. Two-player results don't affect the one-player best score.

## Team Up (two-player co-op)

Team Up is for an older child and a younger sibling to play together on one device. It is reached from the "Team Up" button on the home screen (and from the arcade). Everything in it is cooperative: the two players share a score and win together.

On the Team Up screen, parents can enter each player's name. The older player's sticker is their arcade hero, and the younger player picks their own sticker from a separate set.

**Team Puzzles.** A round is six puzzles, and the players take turns, younger player first. A "your turn" screen between puzzles makes it easy to pass the device back and forth.

- The younger player gets kindergarten-level puzzles: same color, same shape, counting to 10, which group has more, simple patterns (AB, AAB, ABB, ABC), which one doesn't belong, and what goes together. These are always read aloud, use three large answer buttons, and don't depend on reading.
- The older player gets his usual question types (the Challenge versions if Challenge Mode is on).
- On the younger player's turn, a Help button lets the older player remove one wrong answer.
- After each correct answer, the screen prompts the older player to give a high-five or to explain how he solved his puzzle. Explaining reasoning to someone younger is good practice in itself.
- A finished round earns a team sticker for a shared Team Sticker Book and, if the arcade is on, 1 arcade token. Team turns are not counted in the older child's progress report.

**Puzzle Maker.** The older player builds a puzzle and the younger player solves it. There are four kinds:

| Puzzle | What the older player builds |
|---|---|
| Who Doesn't Belong? | Picks 3 pictures that go together and 1 that doesn't |
| Goes Together | Picks a picture, its partner, and 2 wrong answers |
| How Many? | Picks a picture and a number from 1 to 10 |
| What Comes Next? | Builds a shape pattern of 4 to 8 shapes and picks the next shape |

He can add an optional sentence about why the answer is right, which is shown and read aloud after the younger player solves it. Saved puzzles go into a Puzzle Book (up to 24) so they can be replayed or deleted. Building a puzzle requires the same reasoning the CogAT asks for, from the other side.

**Team games.**

| Game | How it works | Cost | Ends when |
|---|---|---|---|
| Team Catcher | The screen is split in two. The younger player catches any number from 1 to 5 (shown with dots for counting), then the older player catches its partner to make the target (10, then 8, 9 and so on) | Free | 3 wrong pairs, or after 4 minutes |
| Team Match | 6 pairs. Players take turns flipping two cards. A match means another turn; a miss passes the turn. Each found pair is marked with the finder's sticker | Usual token cost | All pairs are found |
| Team Invaders | Two blasters and slower invaders. A freeze-ray freezes one blaster, and the other player thaws it by flying over for a "high-five" | Usual token cost | The invaders land |

Team Catcher, Team Match and Team Invaders can also be started from the arcade by choosing "Team, 2 players" on the game's start screen. Team scores are kept separately from the older child's own best scores.

Controls on one keyboard: the left player uses A and D (and W to fire in Invaders); the right player uses the arrow keys (and the up arrow or space to fire). On a touchscreen, each player uses their own side of the screen.

## Number Catcher (free math game)

Number Catcher is a math game that never costs tokens. It's meant to encourage extra practice with addition facts, which support the quantitative section.

- Numbers fall from the top of the screen, and the child catches two that add up to a target.
- The target starts at 10 and changes after every five correct pairs, eventually reaching 20.
- In the first two rounds, the correct partner number is highlighted to support learning.
- Three incorrect pairs end the game.

It has a button on the home screen and stays available even when the arcade is turned off.

## Parent settings

A "Grown-Up Corner" (linked from the home screen) explains each question type and contains:

- **Read-aloud.** Questions are read aloud by the device's text-to-speech. This matches the 2nd-grade CogAT, where directions are typically read aloud.
- **Arcade on/off.** When off, the arcade is hidden. Tokens earned in the meantime are kept.
- **Tokens per game** (1, 2 or 3).
- **Number Catcher on/off.**
- **Picture names on/off.** A short name appears under each puzzle picture by default. The real test uses unlabeled pictures, so this can be turned off for test-style practice.
- **Sound effects on/off.**
- **Progress report.** For each question type, the report shows questions answered, first-try accuracy, and missions completed without errors, for both standard and Challenge Mode. It also shows arcade scores and Number Catcher results.
- **Reset all progress.**

## Suggested use

- Keep sessions to one or two missions, about 5 to 10 minutes, and stop while it's still enjoyable.
- Let the child choose which mission to play.
- Ask "How did you figure that out?" Explaining reasoning out loud builds the underlying skills more than getting answers right.
- Use the progress report to see which formats feel unfamiliar, not as a grade. Low first-try accuracy on a new format is normal.
- A few short sessions a week over a couple of weeks is plenty.

## Privacy

All progress is stored in the browser's local storage on the device being used. There are no accounts, no analytics, and no data is sent anywhere. The page doesn't load anything from the internet: the fonts and all artwork are built into the file.

Progress doesn't sync between devices or browsers, and clearing the browser's data will erase it.

## Running it offline on Linux

The whole site is one file, `index.html`, and it runs without an internet connection.

**Quickest:** download `index.html` and open it in any browser.

**As an app in the menu** (no sudo needed):

1. On the GitHub page, click **Code → Download ZIP** and unzip it.
2. Open a terminal in the unzipped folder and run:
   ```
   bash linux/install.sh
   ```
3. "Brain Blasters" now appears in the app menu with its own icon. It opens in its own app window in Brave, Chrome, Chromium, Edge or Vivaldi, or in a new window in Firefox.

The installer copies the game to `~/BrainBlasters/` and adds a launcher at `~/.local/bin/brain-blasters`. To update, download the new ZIP and run the installer again; saved progress is kept. To remove it, run `bash linux/install.sh --uninstall`.

Notes:

- **Progress is separate from the online site.** The installed copy keeps its own stickers, checkmarks and tokens in the browser.
- **Read-aloud** uses the computer's built-in voices, and voices that need the internet won't work offline. On Ubuntu or Debian, `sudo apt install speech-dispatcher espeak-ng` adds offline voices.
- **Sandboxed browsers:** the game is installed in a visible folder in your home directory so that snap-packaged browsers can open it. A Flatpak browser may need permission to read your home folder.

## Using or hosting your own copy

Download `index.html` and open it in any modern browser, or fork this repository and turn on GitHub Pages:

**Settings → Pages → Source: "Deploy from a branch" → Branch: `main`, folder `/ (root)`**

The characters, artwork and questions are original. The puzzle drawings are generated by the scripts in `tools/` (`art.py` builds all of them). Everything, including the fonts, is contained in the single HTML file.

## Credits

- The Pong game's physics and computer opponent are adapted from [justin-harvey/test](https://github.com/justin-harvey/test).
- Fonts: [Bangers](https://github.com/googlefonts/bangers) and [Comic Neue](https://github.com/crozynski/comicneue), both under the SIL Open Font License 1.1. The licenses are in `fonts/`.
