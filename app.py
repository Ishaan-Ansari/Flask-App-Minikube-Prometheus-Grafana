from flask import Flask, jsonify, Response
import random
import time

app = Flask(__name__)

total_requests = 0

@app.route('/metrics')
def metrics():
    global total_requests
    total_requests += 1

    # Simulate some processing time
    request_processing_latency = round(random.uniform(0.1, 0.5), 2)
    model_prediction_success_rate = round(random.uniform(0.8, 1.0), 2)

    # Returns the metrics in Prometheus format
    prometheus_metrics = f"""
        f"# HELP total_api_requests_total Total number of API requests\n"
        f"# TYPE total_api_requests_total counter\n"
        f"total_api_requests_total {total_requests}\n"
        f"\n"
        f"# HELP request_processing_latency_seconds Latency for request processing\n"
        f"# TYPE request_processing_latency_seconds gauge\n"
        f"request_processing_latency_seconds {request_processing_latency}\n"
        f"\n"
        f"# HELP model_prediction_success_rate Model prediction success rate\n"
        f"# TYPE model_prediction_success_rate gauge\n"
        f"model_prediction_success_rate {model_prediction_success_rate}\n"
    """

    return Response(prometheus_metrics, status=200, mimetype='text/plain')

@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Welcome to the Flask Metrics API!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)