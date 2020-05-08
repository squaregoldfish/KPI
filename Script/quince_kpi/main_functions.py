###############################################################################
### Functions running the kpi functions and producing kpi plots/tables etc. ###
###############################################################################

### Description:
# ...


#------------------------------------------------------------------------------
### Import packages
import quince_kpi as kpi


#------------------------------------------------------------------------------
### Functions

# This function creates the KPI plots for the report introduction, and store
# them in the output directory
def intro_plots(intro_config, parameters, df, output_dir):
	for kpi_name, config in intro_config.items():
		eval('kpi.'+ kpi_name)(parameters=parameters, df=df,
			output_dir=output_dir, kwargs=config['function_input'])


# This function creates the KPI plots for parameter sections, and store
# them in the output directory
def meas_param_plots(param_config, parameters, df, output_dir):
	for parameter, config in param_config.items():
		short_name = config['short_name']
		for kpi_name in config['kpis']:
			eval('kpi.' + kpi_name)(parameter=parameter, short_name=short_name,
				df=df, output_dir=output_dir)