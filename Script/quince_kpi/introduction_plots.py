###############################################################################
### Function for creating introduction plots                                ###
###############################################################################

### Description:
# ...


#------------------------------------------------------------------------------
### Import packages
import quince_kpi as kpi


#------------------------------------------------------------------------------
### Set variables


#------------------------------------------------------------------------------
### Functions


def intro_plots(intro_plot_config, render_dict, colnames, df, output_dir):

	for kpi_type, config in intro_plot_config.items():
		if config['include']:
			filename = 'kpi_' + kpi_type + '_filename'
			render_dict[filename] = eval('kpi.'+ kpi_type)(colnames=colnames,
				df=df, output_dir=output_dir, kwargs=config['function_input'])
	return render_dict