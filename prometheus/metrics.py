from prometheus_client import Counter, Gauge, Histogram

_INF = float('inf')


graphs = {}
graphs['c'] = Counter('request_operations_total', 'The total number of request')
graphs['e'] = Counter('total_exceptions', 'The total number of exceptions occurred')
graphs['ht'] = Gauge('highest_temperature', 'The highest temperature recorded')
graphs['hh'] = Gauge('highest_humidity', 'The highest humidity recorded')
graphs['ct'] = Gauge('current_temperature', 'The current temperature recorded')
graphs['ch'] = Gauge('current_humidity', 'The current humidity recorded')
graphs['h'] = Histogram('request_duration_seconds', 'Histogram for the duration in seconds', buckets=(1, 2, 5, 6, 10, _INF))
