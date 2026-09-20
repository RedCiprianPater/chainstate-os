#!/usr/bin/env bash
set -Eeuo pipefail
 test -s hf-space/index.html
 test -s installer/install-chainstate.sh
 bash -n installer/install-chainstate.sh
 grep -q 'USD 666' hf-space/index.html
 echo 'Reference repository checks passed.'
