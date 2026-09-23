/*
 * pin_verify - WPS PIN oracle for the "Cracking a WPS PIN" challenge.
 *
 * STATUS: DRAFT.  This is the verification logic only.  It is not wired
 * into a build yet - no .init compiles it, nobody has made it suid, and the
 * flag-reading path is untested outside that setup.  The compiled-binary
 * deployment pattern is being brought over from another dojo; once that
 * lands, this file just needs to be pointed at.
 *
 * Usage: pin_verify <8-digit-guess>
 *
 * The whole point of this challenge is that a real WPS-vulnerable access
 * point validates an 8-digit PIN in two independent stages (its M4 and M6
 * exchanges) and tells an attacker which stage failed - so the exit status
 * here mirrors that leak on purpose:
 *
 *   0   the whole 8-digit PIN is correct - the flag is printed to stdout
 *   1   the first four digits are wrong
 *   2   the first four digits are right, but the last four are wrong
 *   64  usage error: the argument was not exactly 8 digits
 *
 * That split is what shrinks the search space from a naive 10^8 (or 10^7,
 * accounting for the 8th digit being a checksum of the first seven - see
 * DESCRIPTION.md) down to 10^4 + 10^3 = 11,000 worst-case guesses: the
 * first half can be brute-forced on its own in at most 10,000 tries, and
 * once it is known, the checksum formula in DESCRIPTION.md removes the
 * need to guess the 8th digit at all, leaving only 1,000 tries for the
 * second half.
 */

#include <stdio.h>
#include <string.h>

/*
 * TODO(build): SECRET_PIN is a placeholder default so this compiles and
 * runs standalone for now.  A real deployment needs a fresh, random,
 * checksum-valid PIN per instance, injected however the compiled-binary
 * pattern ends up doing secrets (compile-time -DSECRET_PIN=... is the
 * obvious hook, hence the #ifndef guard below).
 *
 * 13372460 is a valid example: its checksum digit was computed with the
 * formula in DESCRIPTION.md from the 7-digit prefix 1337246.
 */
#ifndef SECRET_PIN
#define SECRET_PIN "13372460"
#endif

#define FLAG_PATH "/flag"
#define PIN_LEN 8

static int is_all_digits(const char *s)
{
    if (strlen(s) != PIN_LEN)
        return 0;

    for (size_t i = 0; i < PIN_LEN; i++)
        if (s[i] < '0' || s[i] > '9')
            return 0;

    return 1;
}

static void print_flag(void)
{
    FILE *f = fopen(FLAG_PATH, "r");
    char line[256];

    if (!f) {
        perror("fopen(" FLAG_PATH ")");
        return;
    }

    if (fgets(line, sizeof(line), f))
        fputs(line, stdout);

    fclose(f);
}

int main(int argc, char **argv)
{
    const char *secret = SECRET_PIN;
    const char *guess;

    if (argc != 2 || !is_all_digits(argv[1])) {
        fprintf(stderr, "usage: %s <8-digit-pin>\n", argv[0]);
        return 64;
    }

    guess = argv[1];

    if (strncmp(guess, secret, 4) != 0) {
        fprintf(stderr, "wrong\n");
        return 1;
    }

    if (strncmp(guess + 4, secret + 4, 4) != 0) {
        fprintf(stderr, "wrong\n");
        return 2;
    }

    print_flag();
    return 0;
}
