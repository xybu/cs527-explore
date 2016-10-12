#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <magic.h>

int main(int argc, char **argv) {
	struct magic_set *ms;
	const char *result;

	ms = magic_open(MAGIC_NONE);
	if (ms == NULL) {
		(void)fprintf(stderr, "ERROR opening MAGIC_NONE: out of memory\n");
		return 10;
	}

	if (magic_load(ms, NULL) == -1) {
		(void)fprintf(stderr, "ERROR loading with NULL file: %s\n", magic_error(ms));
		return 11;
	}

	if ((result = magic_file(ms, argv[1])) == NULL) {
		(void)fprintf(stderr, "ERROR loading file %s: %s\n", argv[1], magic_error(ms));
		return 12;
	}

	fprintf(stdout, "%s\n", result);

	magic_close(ms);
	return 0;
}
