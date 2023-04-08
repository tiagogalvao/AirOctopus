#!/usr/bin/env python3
import click
from main import AppData


class AirOctopus:
    def __init__(self, params: AppData):
        self.params = params

    def start(self):
        # Mock the use of the parameters to process something
        print(f"Processing {self.params.required_param_1} with {self.params.required_param_2} and optional param 1 = {self.params.optional_param_1} and optional param 2 = {self.params.optional_param_2}")


@click.command()
@click.argument('required_param_1', type=str)
@click.argument('required_param_2', type=int)
@click.option('--optional_param_1', type=float, help='An optional parameter of type float')
@click.option('--optional_param_2', type=bool, help='An optional parameter of type bool')
def run_app(required_param_1, required_param_2, optional_param_1=None, optional_param_2=None):
    # Create an instance of the AppParams dataclass
    params = AppData.AppData(required_param_1, required_param_2, optional_param_1, optional_param_2)

    # Create an instance of the MyApp class with the AppParams dataclass instance as a parameter
    my_app = AirOctopus(params)

    # Run the application by calling the process method of the MyApp instance
    my_app.start()


if __name__ == '__main__':
    run_app()