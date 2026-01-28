from generate_analytic_snowflake_equilibria import *

if __name__ == "__main__":
    # Generate a SF15 equilibria
    generate_analytic_snowflake("./template_gfile", 
                                "./sf15_example/sf15_eq", 
                                i1 = 0.075, 
                                i2 = 0.02475, 
                                i3 = 0.0225,
                                plot=True
                                )
