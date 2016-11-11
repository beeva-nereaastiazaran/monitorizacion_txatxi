import statsd
import time
import psutil
import multiprocessing

host = '52.50.96.225'


def disk():
    c = statsd.StatsClient(host, 8125, prefix='txatxiGrupo.disco')
    while True:
        disk_usage = psutil.disk_usage('/')
        c.gauge('root.total', disk_usage.total)
        c.gauge('root.used', disk_usage.used)
        c.gauge('root.free', disk_usage.free)
        c.gauge('root.percent', disk_usage.percent)

        time.sleep(10)


def cpu_times():
    c = statsd.StatsClient(host, 8125, prefix='txatxiGrupo.cpu')
    while True:
        cpu_times = psutil.cpu_times()
        c.gauge('systemwide_times.user', cpu_times.user)
        c.gauge('systemwide_times.nice', cpu_times.nice)
        c.gauge('systemwide_times.system', cpu_times.system)
        c.gauge('systemwide_times.idle', cpu_times.idle)
        c.gauge('systemwide_times.iowait', cpu_times.iowait)
        c.gauge('systemwide_times.irq', cpu_times.irq)
        c.gauge('systemwide_times.softirq', cpu_times.softirq)
        c.gauge('systemwide_times.steal', cpu_times.steal)
        c.gauge('systemwide_times.guest', cpu_times.guest)
        c.gauge('systemwide_times.guest_nice', cpu_times.guest_nice)

        time.sleep(10)


def cpu_times_percent():
    c = statsd.StatsClient(host, 8125, prefix='txatxiGrupo.cpu')
    while True:
        value = psutil.cpu_percent(interval=1)
        c.gauge('systemwide_percent', value)

        cpu_times_percent = psutil.cpu_times_percent(interval=1)
        c.gauge('systemwide_times_percent.user', cpu_times_percent.user)
        c.gauge('systemwide_times_percent.nice', cpu_times_percent.nice)
        c.gauge('systemwide_times_percent.system', cpu_times_percent.system)
        c.gauge('systemwide_times_percent.idle', cpu_times_percent.idle)
        c.gauge('systemwide_times_percent.iowait', cpu_times_percent.iowait)
        c.gauge('systemwide_times_percent.irq', cpu_times_percent.irq)
        c.gauge('systemwide_times_percent.softirq', cpu_times_percent.softirq)
        c.gauge('systemwide_times_percent.steal', cpu_times_percent.steal)
        c.gauge('systemwide_times_percent.guest', cpu_times_percent.guest)
        c.gauge('systemwide_times_percent.guest_nice', cpu_times_percent.guest_nice)
        time.sleep(10)


def memory():
    c = statsd.StatsClient(host, 8125, prefix='txatxiGrupo.mem')
    while True:
        swap = psutil.swap_memory()
        c.gauge('swap.total', swap.total)
        c.gauge('swap.used', swap.used)
        c.gauge('swap.free', swap.free)
        c.gauge('swap.percent', swap.percent)

        virtual = psutil.virtual_memory()
        c.gauge('virtual.total', virtual.total)
        c.gauge('virtual.available', virtual.available)
        c.gauge('virtual.used', virtual.used)
        c.gauge('virtual.free', virtual.free)
        c.gauge('virtual.percent', virtual.percent)
        c.gauge('virtual.active', virtual.active)
        c.gauge('virtual.inactive', virtual.inactive)
        c.gauge('virtual.buffers', virtual.buffers)
        c.gauge('virtual.cached', virtual.cached)

        time.sleep(10)


if __name__ == '__main__':
    multiprocessing.Process(target=disk).start()
    multiprocessing.Process(target=cpu_times).start()
    multiprocessing.Process(target=cpu_times_percent).start()
    multiprocessing.Process(target=memory).start()

