import sys
from packaging import version

is_version_gt_tag = version.parse(sys.argv[1]) > version.parse(sys.argv[2])

print(f"export VALID_VERSION={'1' if is_version_gt_tag else '0'!r}")