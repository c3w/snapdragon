#!/bin/sh
TRAP_DIR="/data/snapdragon/traps"
cd ${TRAP_DIR}

	for trap in *trap; do {
	mv -- ${trap} ${trap}.ack
	}; done

echo "Location: http://ipncore.com/snapdragon/"
echo
