/* Signed trampoline: Sikarugir execs bin/wine; we exec the real loader as bin/macxg
   so Dock/Cmd-Tab and Wine's WINELOADER (built from argv[0] basename) say "macxg". */
#include <mach-o/dyld.h>
#include <limits.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

extern char **environ;

int main(int argc, char **argv)
{
    char exe[PATH_MAX], resolved[PATH_MAX], dest[PATH_MAX];
    uint32_t size = sizeof(exe);
    char *slash;
    char *argvz[argc + 1];
    int i;

    if (_NSGetExecutablePath(exe, &size) != 0) {
        fprintf(stderr, "macxg: cannot resolve trampoline path\n");
        return 127;
    }
    if (realpath(exe, resolved))
        snprintf(exe, sizeof(exe), "%s", resolved);
    slash = strrchr(exe, '/');
    if (!slash) return 127;
    *slash = '\0';
    if (snprintf(dest, sizeof(dest), "%s/macxg", exe) >= (int)sizeof(dest))
        return 127;
    if (access(dest, X_OK) != 0) {
        fprintf(stderr, "macxg: missing Wine loader at %s\n", dest);
        return 127;
    }
    setenv("WINELOADER", dest, 1);
    argvz[0] = dest;
    for (i = 1; i < argc; i++) argvz[i] = argv[i];
    argvz[argc] = NULL;
    execve(dest, argvz, environ);
    perror("macxg: execve");
    return 127;
}
