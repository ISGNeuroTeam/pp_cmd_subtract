# pp_cmd_subtract
Postprocessing command "subtract"

Make subtraction of two columns of the dataframe

a, b - columns or numbers must be subtracted

| subtract a b - creates a new df

Usage example:
`... | subtract a b as c`

## Getting started
###  Prerequisites
1. [Miniconda](https://docs.conda.io/en/latest/miniconda.html)

### Installing
1. Create virtual environment with post-processing sdk 
```bash
make dev
```
That command  
- creates python virtual environment with [postprocessing_sdk](https://github.com/ISGNeuroTeam/postprocessing_sdk)
- creates `pp_cmd` directory with links to available post-processing commands
- creates `otl_v1_config.ini` with otl platform address configuration

2. Configure connection to platform in `otl_v1_config.ini`

### Test subtract
Use `pp` to test subtract command:  
```bash
pp
Storage directory is /tmp/pp_cmd_test/storage
Commmands directory is /tmp/pp_cmd_test/pp_cmd
query: | otl_v1 <# makeresults count=100 | eval a = 10 | eval b = 9#> |  subtract a b as c
```
