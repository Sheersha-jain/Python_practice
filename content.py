content = """ COMMAND> du -sh /var/lib/pgsql

635M    /var/lib/pgsql
22G     /var/lib/mongodb
6248    ./.git/objects
368     ./.git/logs/refs/remotes/origin
372     ./.git/logs/refs/remotes
16      ./.git/logs/refs/heads
392     ./.git/logs/refs
400     ./.git/logs
44      ./.git/hooks
368     ./.git/refs/remotes/origin
372     ./.git/refs/remotes
16      ./.git/refs/heads
32      ./.git/refs/tags
424     ./.git/refs
8       ./.git/info
4       ./.git/branches
7324    ./.git
8       ./__pycache__
8       ./.cache/v/cache
12      ./.cache/v
16      ./.cache

 """.strip()


for line in content:
    print line

