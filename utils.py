import pandas as pd

def rename_dataframe(df,
               n_core_name = "Processors",
               rmax_name = "RMax",
               rpeak_name = "RPeak",
               core_speed_name = "Proc. Frequency"):
    
    return df[[n_core_name,
                rmax_name,
                rpeak_name,
                core_speed_name]].rename(
                    columns={n_core_name: 'n_core',
                            rmax_name: 'rmax',
                            rpeak_name: 'rpeak',
                            core_speed_name: 'proc_speed'})

def clean_file(filename):
    # if filename[-3:] == 'xls' :
    try:
        top500_df = rename_dataframe(pd.read_excel(filename, header=1))
    except KeyError :
        try :
            top500_df = rename_dataframe(pd.read_excel(filename, header=0))
        except KeyError :
            try:
                top500_df = rename_dataframe(pd.read_excel(filename, header=0),
                                    n_core_name="Cores")
            except KeyError :
                try:
                    top500_df = rename_dataframe(pd.read_excel(filename, header=0),
                                        n_core_name="Total Cores",
                                        rmax_name = "Rmax",
                                        rpeak_name = "Rpeak",
                                        core_speed_name="Processor Speed (MHz)")
                except KeyError:
# else:
                    top500_df = rename_dataframe(pd.read_excel(filename, thousands=','),
                                                    n_core_name="Total Cores",
                                                    rmax_name = "Rmax [TFlop/s]",
                                                    rpeak_name = "Rpeak [TFlop/s]",
                                                    core_speed_name="Processor Speed (MHz)")
                    
                    top500_df["rmax"] *= 1000
                    top500_df["rpeak"] *= 1000

                    return top500_df

    # #We are not in Teraflops
    # if(top500_df.head(1)["rmax"].item() > 10e4):
    #     top500_df["rmax"] /= 1000
    #     top500_df["rpeak"] /= 1000

    return top500_df