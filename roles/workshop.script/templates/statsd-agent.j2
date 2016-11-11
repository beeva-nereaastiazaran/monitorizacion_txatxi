import statsd
import time
import psutil
import multiprocessing

c = statsd.StatsClient('52.50.96.225', 8125)
#c.incr('bar')  # Will be 'foo.bar' in statsd/graphite.
while True:
    virtual = psutil.virtual_memory()
    c.gauge('mem_total_juanjo', virtual.total)
    print virtual.total
    c.gauge('mem_available_juanjo', virtual.available)
    c.gauge('mem_used_juanjo', virtual.used)
    print virtual.free
    c.gauge('mem_free_juanjo', virtual.free)

    time.sleep(10)