from prometheus_client import start_http_server, Gauge

gpu_utilization = Gauge('gpu_utilization', 'GPU Utilization Percentage')
queue_length = Gauge('queue_length', 'Number of tasks in the queue')

def update_metrics():
    while True:
        gpu_util = get_gpu_utilization()  # Logic to get GPU utilization
        queue_len = get_queue_length()  # Logic to get queue length
        gpu_utilization.set(gpu_util)
        queue_length.set(queue_len)
        time.sleep(15)

if __name__ == '__main__':
    start_http_server(8000)  # Expose metrics on port 8000
    update_metrics()
