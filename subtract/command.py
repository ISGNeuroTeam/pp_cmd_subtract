import numpy as np
import pandas as pd
from otlang.sdk.syntax import Keyword, Positional, OTLType
from pp_exec_env.base_command import BaseCommand, Syntax


class SubtractCommand(BaseCommand):
    """
    Make subtraction of two columns of the dataframe
    a, b - columns or numbers must be subtracted
    | subtract a b - creates a new df

    | subtract a b as c - creates new column "c" in the old df
    """

    syntax = Syntax(
        [
            Positional("first_subtract", required=True, otl_type=OTLType.ALL),
            Positional("second_subtract", required=True, otl_type=OTLType.ALL),
        ],
    )
    use_timewindow = False  # Does not require time window arguments
    idempotent = True  # Does not invalidate cache

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        self.log_progress("Start subtract command")
        # that is how you get arguments
        first_subtract_argument = self.get_arg("first_subtract")
        if isinstance(first_subtract_argument.value, str):
            first_subtract = df[first_subtract_argument.value]
        else:
            first_subtract = first_subtract_argument.value

        second_subtract_argument = self.get_arg("second_subtract")
        if isinstance(second_subtract_argument.value, str):
            second_subtract = df[second_subtract_argument.value]
        else:
            second_subtract = second_subtract_argument.value
        result_column_name = second_subtract_argument.named_as

        if isinstance(first_subtract, (int, float)) and isinstance(second_subtract, (int, float)):
            if result_column_name != "" and not df.empty:
                first_subtract = np.array([first_subtract] * df.shape[0])
                second_subtract = np.array([second_subtract] * df.shape[0])
            else:
                first_subtract = np.array([first_subtract])
                second_subtract = np.array([second_subtract])

        self.logger.debug(f"Command add get first positional argument = {first_subtract_argument.value}")
        self.logger.debug(
            f"Command add get second positional argument = {second_subtract_argument.value}"
        )

        if result_column_name != "":
            if not df.empty:
                df[result_column_name] = first_subtract - second_subtract
            else:
                df = pd.DataFrame({result_column_name: first_subtract - second_subtract})
            self.logger.debug(f"New column name: {result_column_name}")

        else:
            df = pd.DataFrame(
                {
                    f"subtract_{first_subtract_argument.value}_{second_subtract_argument.value}": first_subtract - second_subtract
                }
            )
        self.log_progress("Subtraction is complete.", stage=1, total_stages=1)
        return df
