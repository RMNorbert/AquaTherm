from flask import Flask, request, render_template, jsonify
from prometheus_flask_exporter import PrometheusMetrics
from prometheus.metrics import *
from sensor.arduino_multi_board_system_interface import *

app = Flask(__name__)
metrics = PrometheusMetrics(app)
metrics.info('app_info', 'Application info', version='1.0.0')

aquarium_type = 'cold'
state = 'OFF'
initial_value = '...'

@app.get('/')
def index():
    fan_status = 'turned off'
    tap_status = 'turned off'
    return render_template('index.html',
                           temperature=initial_value,
                           humidity=initial_value,
                           state=state,
                           status=initial_value,
                           aquariumType=aquarium_type,
                           fanStatus=fan_status,
                           tapStatus=tap_status,
                           highestTemperature=initial_value
                           )


@app.get('/data')
def get_data():
    return f'<p>{get_all_readings()}</p>'


@app.get('/warnings')
def warnings_get():
    return f'<p>{get_all_warnings()}</p>'


@app.route('/reading')
@graphs['e'].count_exceptions()
def update_data():
    if state == 'ON':
        start = time.time()  # start of the request
        graphs['c'].inc()    # increase request counter

        reading = read_sensor(aquarium_type)
        temperature = reading[0]
        humidity = reading[1]
        status = reading[2]

        fan_status = str(control_fan(status))
        tap_status = str(control_tap(status))

        graphs['ct'].set(temperature)
        graphs['ch'].set(humidity)

        end = time.time()  # end of the request
        graphs['h'].observe(end - start)  # duration of the request

        return jsonify(temperature=temperature,
                       humidity=humidity,
                       status=status,
                       fanStatus=fan_status,
                       tapStatus=tap_status
                       )
    else:
        return jsonify(temperature=initial_value,
                       humidity=initial_value,
                       status=initial_value,
                       fanStatus='Fan: ' + initial_value,
                       tapStatus='Tap: ' + initial_value
                       )


@app.route('/state', methods=['POST'])
def switch_state():
    global state
    highest_record = get_highest_readings()
    print(highest_record)
    graphs['hh'].set(highest_record.humidity)
    graphs['ht'].set(highest_record.temperature)
    highest_temperature = str(get_highest_readings().temperature)
    if state == 'OFF':
        state = 'ON'
    elif state == 'ON':
        state = 'OFF'
    return jsonify(state=state, highestTemperature=highest_temperature)


@app.route('/type', methods=['POST'])
def switch_aquarium_type():
    global aquarium_type
    new_aquarium_type = request.form.get('type')  # Get the new type from the request
    aquarium_type = new_aquarium_type
    return jsonify(aquariumType=aquarium_type)


if __name__ == '__main__':
    app.run("0.0.0.0", 5000, threaded=True)
