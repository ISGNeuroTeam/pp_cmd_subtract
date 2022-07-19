import pandas as pd
from otlang.sdk.syntax import Keyword, Positional, OTLType
from pp_exec_env.base_command import BaseCommand, Syntax


class SubtractCommand(BaseCommand):
    """
    Make subtraction of two columns of the dataframe
    a, b - columns must be subtracted
    | subtract a b - creates a new df

    | subtract a b as c - creates new column "c" in the old df
    """

    syntax = Syntax(
        [
            Positional("first_column", required=True, otl_type=OTLType.TEXT),
            Positional("second_column", required=True, otl_type=OTLType.TEXT),
        ],
    )
    use_timewindow = False  # Does not require time window arguments
    idempotent = True  # Does not invalidate cache

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        self.log_progress("Start subtract command")
        # that is how you get arguments
        first_column = self.get_arg("first_column").value
        second_column_argument = self.get_arg("second_column")
        second_column = second_column_argument.value
        result_column_name = second_column_argument.named_as

        self.logger.debug(f"Command add get first positional argument = {first_column}")
        self.logger.debug(
            f"Command add get second positional argument = {second_column}"
        )

        if result_column_name != "":
            df[result_column_name] = df[first_column] - df[second_column]
            self.logger.debug(f"New column name: {result_column_name}")

        else:
            df = pd.DataFrame(
                {
                    f"subtract_{first_column}_{second_column}": df[first_column].values
                    - df[second_column].values
                }
            )
        self.log_progress("Subtraction is complete.", stage=1, total_stages=2)
        return df
