import requests
# Steps
url = "https://v1.nocodeapi.com/zetaknight/fit/GpWLJGwidrAOkBVc/aggregatesDatasets?dataTypeName=steps_count&timePeriod=today"
params = {}
steps = requests.get(url = url, params = params)
steps_c = steps.json()
print(steps_c['steps_count'][0]['value'])

# Heart
