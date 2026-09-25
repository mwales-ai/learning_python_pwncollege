<!--
STATUS: DRAFT / WORK IN PROGRESS.

This challenge is not deployed yet - it has no .init, no run script, no
.eval_data, and it is deliberately left out of module.yml until the ROM,
the real Game Genie codes, and the judge all exist.  See CLAUDE.md's note
about not adding incomplete challenges to the pwn.college module list.

Sections marked PLACEHOLDER below are drafted with filler content on
purpose and need real content before this ships:
  * the Game Genie discussion (how the 6-letter code encodes address+value)
  * decode_game_genie_code(), which currently does not actually decode
  * the ROM file itself (a small homebrew UNROM/mapper-2 ROM) and the real
    codes it ships with
-->

# Game Genie ROM Patcher

# Background Information

I like old 8-bit and 16-bit video games. One of my favorite systems was the
Nintendo Entertainment System (NES).  If you have ever heard a video game
called "Nintendo Hard", it means the game is very difficult, much like NES
games were in the 1980s and 1990s.  The games were hard because memory was
very expensive, so devs were limited on how large of a game they could make,
so they made the games hard so players wouldn't complete them too fast.

The NES games were often brutally hard. Some game companies would help out
gamers by having cheat codes (this is where the Konami code got invented).
But if a game didn't have any cheat codes, there was still a way to get
help.  We had a device we could stick on the end of our cartridges called
a Game Genie.

![Picture of game genie attached to NES game](url of image)

The Game Genie came with a [100+ page booklet](https://archive.org/details/game-genie-1992-nes/NES-Game-Genie-codes/page/n19/mode/2up)
of secret codes for games, and a description of what each code would do.
We could pick up to 3 codes to use for the game, so we had to choose
our effects wisely.

# How does a Game Genie actually work?

We will focus on the 6 character codes for this discussion (there were 8
character codes, but we will ignore for now).  The code was essentially a two
byte address, and a 1-byte value. The program instructions for each game
were stored in ROM chips inside of the cartridge.  The Game Genie would watch
which addresses were being fetched by the NES, and if the address for your
cheat code was seen, instead of the memory from the ROM being returned, the
value in your cheat code would be returned.

One of ways we would typically use it it to change the op-code for an NES CPU
instruction.  For instance, for the following instruction:

```
dec $052d        ; decrements the memory at address 0x052d
lda #$01         ; loads reg A with (immediate) value 0x01
```

The decrement instruction (mnemonic dec) is going to decrement the value stored
in a memory location of the NES which happens to be the number of hit points
our character has.  If we can change that op-code to something benign, then
our character won't lose any HP when he gets hit by an enemy.  Since the next
instruction is trying to load register A with the value 0x01, we can change the
decrement instruction opcode to an LDA instruction as well, and it will be
benign because the very next instruction will overwrites register A anyways.

If you are a little bit more advanced, you might be wondering why we don't use
a NOP (no operation) instruction instead.  Because that is what we do a lot of
times when trying to patch our unwanted code in other binaries.  For this
case, the instruction we are trying to invalidate is 3 bytes.  The NES CPU (MOS
6502) has a 1-byte NOP instruction, and we could NOP all 3 bytes, but then that
would need 3 Game Genie codes to be entered by the user. The game genie code we
will be using will instead change 1 byte, the instructions will become:

```
lda $052d        ; loads reg A with value in memory at address 0x052d
lda #$01         ; loads reg A with (immediate) value 0x01
```

The game we are going to be hacking is called
[Cat Mercs](https://team-disposable.itch.io/catmercs-1). It looks really fun,
but it is extremely challenging.  I have a couple of Game Genie codes that
we can use to make it easier.

```
SZYONU            No damage from enemies walking into Miaya
SZYPKK            No damage from bullets hitting Miaya
```

You can try this out using the FCEUX emulator in our pwn.college VM.  You must
use the Desktop mode.  Try the game first without any cheats to see how
difficult it is. Starts FCEUX and then load the ROM from
/challenge/cat_mercs_1.1.nes

Keyboard Controls by default with FCEUX:

| NES    | Emulator    |
|--------|-------------|
| Up     | Up arrow    |
| Down   | Down Arrow  |
| Left   | Left Arrow  |
| Right  | Right Arrow |
| Start  | Return      |
| Select | S           |
| A      | F           |
| B      | D           |


Now try it with our cheat codes!  You must load the Game Genie rom file by
clicking Emulation->Load Game Genie Rom and then navigating to the game genie
rom:

```
/challenge/gg.rom 
```

![Loading Game Genie ROM](https://raw.githubusercontent.com/mwales-ai/learning_python_pwncollege/refs/heads/main/files/game-genie-patcher/.images/loading_gg_rom.jpg)

In that same drop down menu, click the check box that enables Game Genie.

![Enabling Game Genie](https://raw.githubusercontent.com/mwales-ai/learning_python_pwncollege/refs/heads/main/files/game-genie-patcher/.images/enabled_option.jpg)

Once you do that, hard reset the emulator, and you will be presented with the Game Genie code entry
screen.  Enter our two cheat codes

```
SZYONU
SZYPKK
```

![Entering game genie code](https://raw.githubusercontent.com/mwales-ai/learning_python_pwncollege/refs/heads/main/files/game-genie-patcher/.images/code_entered.jpg)

# The challenge

For this challenge we will patch the NES ROM files with game genie codes.
By patching the ROM file, we don't have any limit to how many codes we
can apply to a NES game, and we don't ever have to enter in the codes
ever again!

The program you are about to write will load the original Cat Mercs game
ROM, and then change the instruction bytes, and save a new copy of the game
with a different filename.  You can even play this game (if you are OK with
cheating!)

Every ROM hacking tool you have used so far - the sprite editor, BlastEm's
capture tools - works by reading and writing raw bytes in a file that was
never meant to be read as text.  

## Binary files are not text files

This challenge is your introduction to reading and writing files that are
not just text.  We will be opening the file in binary mode, and editing it
byte by byte.

Every file you have opened so far in this dojo has been a text file, opened
with `"r"`, `"w"`, or `"a"`.  A ROM is not text - it is machine code and raw
data, and most of its bytes are not valid characters at all.  Open it in
**binary mode** instead, by adding a `b`:

```python
with open("game.nes", "rb") as f:
    rom_data = f.read()
```

`rom_data` is a `bytes` object, not a `str`.  The biggest difference that
trips people up: indexing into it gives you a **number**, not a
one-character string.

```
>>> data = b"\x00\x01\xFF"
>>> data[0]
0
>>> data[2]
255
```

That number is one byte's value, `0` to `255`. Text files could also be
opened up as binary too, their values would range from `0` to `127` (with
most printable characters above `32`), because that is the range that
ASCII characters use of a byte of data.

## bytes vs. bytearray

`bytes` objects are **immutable** - you cannot change a byte in place, the
same way you cannot do `my_string[0] = "x"`. To edit bytes, convert to a
`bytearray` first:

```python
patched = bytearray(rom_data)
patched[100] = 0xFF
```

Now `patched[100]` really has been changed. When you are done editing, write
it back out the same way you read it in, in binary mode:

```python
with open("patched.nes", "wb") as f:
    f.write(patched)
```

## The iNES header

NES ROM files normally use the **iNES** format: a 16-byte header in front of
the actual game data, followed by the PRG-ROM (program code) and then the
CHR-ROM (graphics tiles). All you need to know for this challenge:

* The header is exactly **16 bytes** (offsets `0x00` through `0x0F`).
* PRG-ROM - the actual 6502 program - starts immediately after it, at file
  offset `0x10`.

Skip the header wherever you read the file:

```python
prg_rom = rom_data[0x10:]
```

## From file offset to NES address

The NES's CPU does not see the file the way you do. Its addresses start
counting from `0x8000`, and the very first byte of PRG-ROM data (file offset
`0x10`) is what the CPU sees as address `0x8000`. The mapping is a constant
offset:

```
nes_address = file_offset - 0x10 + 0x8000
file_offset = nes_address - 0x8000 + 0x10
```

That second formula is the one you need: a patch tells you the NES address
it wants to change, and you have to turn that into the right position in
the file.

**Note: Only about 32KB of NES games can fit into program memory at a time.
There are games with more program code than this, but they have to include
some special mapper logic on the cartridge to work for a NES (we call . We
don't need to worry about any of that for this challenge **

## Game Genie Codes

How does the game genie code convert all the letters into an address and a
value?  Well, we have 16 different possible letters that a game genie code
can use, so that means the codes are kinda like 3 hexadecimal bytes, which
is perfect for 1-byte value and a 2-byte address.

Unfortunately, the developers of the game genie didn't make the codes a
simple address and value pair.  They deliberately scrambed many of the bits
of the game genie codes up to make it mysterious or magical.

Since it's kinda complicated what they did, and it's a mess to explain, the
code for converting the game genie code to an address and valeu pair will
be provided for you.  In the challenge folder their will be a decoder.py
script you can copy and modify.

That program will give you the NES address location, but you will have to
remember how to convert that NES address into the offset of the byte in
the file (see the section above).

**Note: You may have noticed that Game Genie codes can be 8 letters long too.
Those codes are a little bit different because they are designed to work on
those larger NES games that don't fit within 32KB.  We don't have to worry
about that for this challenge.**

## Further Reading

* [PLACEHOLDER: link to an iNES format reference and a Game Genie encoding
  reference once this challenge is finalized]

# Instructions

Write a program that patches a ROM using one or more Game Genie codes.

The overall shape of the task, once the ROM and codes exist:

1. Read the original ROM file, in binary mode.
2. For each Game Genie code you are given, call `decode_game_genie_code()`
   to get the `(address, value)` it wants to patch, convert that NES
   address to a file offset, and change that byte.
3. Write the patched bytes to a new ROM file.

The 2 game genie codes you need to patch your ROM with are:

```
SZYONU
SZYPKK
```

You will be able to load the patched ROM straight into the emulator
included in this pwn.college environment and see your change take effect in
the running game.

To get the pwn.college flag just the the judge program the name of your new
patched ROM file.  This judge program is just going to read the contents of
your file and verify that it's the same as the original except for the two
bytes you patch. There is not a challenge where we are reading input and
checking the output of your program.

```
/challenge/judge.py /home/hacker/cat_mercs_patched.nes
```

Learning to cheat at video games is great practice and training for a career
in cybersecurity!
