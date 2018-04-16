perf record -F 99 -a -g -- sleep 10
/usr/lib/jvm/FlameGraph/jmaps
chown root /tmp/perf-*.map
chown root perf.data
perf script | /usr/lib/jvm/FlameGraph/stackcollapse-perf.pl | grep -v cpu_idle | /usr/lib/jvm/FlameGraph/flamegraph.pl --color=java --hash > flamegraph.svg
