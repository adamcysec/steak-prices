from rocketry import Rocketry

app = Rocketry()

@app.task('every 1 day')
def do_daily():
    import importlib
    get_steak_prices = importlib.import_module("get-steakprices.py")
    get_steak_prices.main() # run script


if __name__ == "__main__":
    app.run()
